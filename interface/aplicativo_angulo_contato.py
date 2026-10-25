import cv2
import csv
import io
import numpy as np
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

from processamento_imagem import contorno
from linha_base import linha_base
from Cal_angulo import angulo_contato
from visualizacao import desenho
try:
    from processamento_imagem.preprocessamento import save_debug_imgs
except ImportError:
    def save_debug_imgs(debug_dict, out_dir, prefix='dbg'):
        return None


def _make_comparison_images(
    raw_image,
    bin_image,
    contour_points,
    baseline_y,
    baseline_line_params,
    left_contact,
    right_contact,
    left_tangent,
    right_tangent,
    left_angle,
    right_angle,
    smoothing_applied,
):
    gray = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.GaussianBlur(gray, (5, 5), 0) if smoothing_applied else gray

    mask_rgb = cv2.cvtColor(bin_image, cv2.COLOR_GRAY2RGB)
    raw_rgb = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    contour_view = mask_rgb.copy()
    result_view = raw_rgb.copy()

    if contour_points is not None and len(contour_points) >= 2:
        points = np.asarray(contour_points, dtype=np.int32).reshape(-1, 1, 2)
        cv2.polylines(contour_view, [points], True, (0, 255, 255), 2)
        cv2.polylines(result_view, [points], True, (60, 190, 150), 2)

    height, width = raw_image.shape[:2]
    if baseline_line_params is not None:
        vx, vy, x0, y0 = baseline_line_params
        if abs(float(vx)) > 1e-9:
            y_left = int(round(float(y0) + (0 - float(x0)) * float(vy) / float(vx)))
            y_right = int(round(float(y0) + (width - 1 - float(x0)) * float(vy) / float(vx)))
            cv2.line(contour_view, (0, y_left), (width - 1, y_right), (255, 40, 40), 2)
            cv2.line(result_view, (0, y_left), (width - 1, y_right), (255, 165, 0), 2)
        else:
            y = int(round(float(y0)))
            cv2.line(contour_view, (0, y), (width - 1, y), (255, 40, 40), 2)
            cv2.line(result_view, (0, y), (width - 1, y), (255, 165, 0), 2)
    elif baseline_y is not None:
        y = int(round(float(baseline_y)))
        cv2.line(contour_view, (0, y), (width - 1, y), (0, 0, 255), 2)
        cv2.line(result_view, (0, y), (width - 1, y), (0, 165, 255), 2)

    for contact in (left_contact, right_contact):
        if contact is not None:
            point = tuple(np.round(contact).astype(int))
            cv2.circle(contour_view, point, 5, (255, 255, 0), -1)
            cv2.circle(result_view, point, 5, (255, 0, 0), -1)

    for contact, tangent, color in (
        (left_contact, left_tangent, (0, 100, 255)),
        (right_contact, right_tangent, (0, 100, 255)),
    ):
        if contact is not None and tangent is not None:
            vector = np.asarray(tangent, dtype=float).reshape(-1)
            if vector.size == 2 and np.all(np.isfinite(vector)):
                start = np.round(np.asarray(contact) - vector * 50).astype(int)
                end = np.round(np.asarray(contact) + vector * 50).astype(int)
                cv2.line(result_view, tuple(start), tuple(end), color, 2)

    for x, angle, label in (
        (10, left_angle, "L"),
        (max(10, width - 120), right_angle, "R"),
    ):
        if angle is not None:
            cv2.putText(
                result_view,
                f"{label}: {float(angle):.2f} deg",
                (x, max(24, height - 12)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

    return {
        "Imagem original (ROI)": raw_rgb,
        (
            "Suavização (cinza, Gaussian 5x5)"
            if smoothing_applied else "Tons de cinza (fallback sem suavização)"
        ): smoothed,
        "Máscara + contorno + linha de base": contour_view,
        "Resultado final (contatos, tangentes e ângulos)": result_view,
    }


class ContactAngleApp(ctk.CTkToplevel):


    def __init__(
        self,
        img_bgr,
        img_bin,
        master=None,
        debug=False,
        debug_imgs=None,
        measurement_metadata=None,
        measurement_history=None,
    ):
        super().__init__(master=master)
        self.title("Ângulo de Contato")
        self.geometry("1100x700")
        # iniciar maximizada (mant�m o bot�o X vis�vel)
        try:
            self.state("zoomed")
        except Exception:
            pass


        # garantir fechamento limpo: quando a janela de an�lise fechar,
        # fecha tamb�m a janela principal (se ainda existir)
        self.protocol("WM_DELETE_WINDOW", self._on_close)


        # img_bgr: imagem para visualiza��o (BGR uint8)
        # img_bin: m�scara bin�ria para processamento (2D uint8, 0/255)
        self.raw_image = img_bgr
        self.bin_image = img_bin
        self.measurement_metadata = dict(measurement_metadata or {})
        self.measurement_history = measurement_history if measurement_history is not None else []
        self.measurement_timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        self.measurement_record = None
        self.manual_adjustments = set()


        # checagens de sanidade
        try:
            assert self.raw_image is not None
            assert self.bin_image is not None
            assert self.raw_image.ndim == 3 and self.raw_image.shape[2] == 3
            assert self.bin_image.ndim == 2
            assert self.raw_image.shape[:2] == self.bin_image.shape[:2]
            assert self.bin_image.dtype == np.uint8
        except AssertionError:
            messagebox.showerror("Erro", "Imagens inválidas passadas para análise (verifique formatos e dimensões).")
            self.destroy()
            return


        # salvar debug images se solicitado
        if debug and debug_imgs is not None:
            try:
                out_dir = os.path.join(os.path.expanduser("~"), "Pictures", "capturas_Angle", "debug")
                os.makedirs(out_dir, exist_ok=True)
                save_debug_imgs(debug_imgs, out_dir)
            except Exception:
                logger.warning("Falha ao salvar imagens de debug", exc_info=True)
        self.gota_pts = None
        self.perfil_liquido_ar = None
        self.validacao_perfil = None


        self.baseline_y = 0
        self.baseline_line_params = None
        self.baseline_method = None
        self.p_esq = None
        self.p_dir = None
        self.contact_method = None
        self.indice_contato_esq = None
        self.indice_contato_dir = None
        self.fit_quality = {"score": 0.0, "rmse_px": 999.0, "n_pts": 2.0}
        self.ae = None
        self.ad = None
        self.ae_interna = None
        self.ad_interna = None
        self.ae_externa = None
        self.ad_externa = None


        self.zoom_scale = 1.0
        self.pan_offset_x = 0
        self.pan_offset_y = 0


        self.ratio = 1.0


        self.setup_ui()
        self.initial_analysis()


    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.sidebar = ctk.CTkScrollableFrame(self, width=300)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)


        self.res_e = self.res_box("Ângulo Esq.")
        self.res_d = self.res_box("Ângulo Dir.")
        self.res_m = self.res_box("Média", True)

        ctk.CTkLabel(self.sidebar, text="Identificação da medição").pack(pady=(8, 2))
        self.sample_entry = ctk.CTkEntry(self.sidebar, placeholder_text="Amostra / identificação")
        self.sample_entry.pack(fill="x", padx=20, pady=3)
        self.notes_entry = ctk.CTkEntry(self.sidebar, placeholder_text="Observações (opcional)")
        self.notes_entry.pack(fill="x", padx=20, pady=3)
        self.sample_entry.bind("<KeyRelease>", self._measurement_fields_changed)
        self.notes_entry.bind("<KeyRelease>", self._measurement_fields_changed)

        ctk.CTkLabel(self.sidebar, text="Resumo da medição").pack(pady=(8, 2))
        self.measurement_summary = ctk.CTkTextbox(self.sidebar, height=150, wrap="word")
        self.measurement_summary.pack(fill="x", padx=12, pady=(0, 4))
        self.measurement_summary.configure(state="disabled")
        ctk.CTkButton(
            self.sidebar, text="Copiar resumo", command=self.copy_measurement_summary
        ).pack(fill="x", padx=20, pady=3)
        ctk.CTkButton(
            self.sidebar, text="Copiar linha para planilha", command=self.copy_measurement_row
        ).pack(fill="x", padx=20, pady=3)
        self.history_button = ctk.CTkButton(
            self.sidebar, text="Histórico da sessão (0)", command=self.show_measurement_history
        )
        self.history_button.pack(fill="x", padx=20, pady=3)
        ctk.CTkButton(
            self.sidebar,
            text="Comparar etapas da imagem",
            command=self.show_image_comparison,
        ).pack(fill="x", padx=20, pady=3)

        # Bot�o para iniciar novo teste (voltar � sele��o)
        ctk.CTkButton(self.sidebar, text="Novo Teste", fg_color="#a52a2a", command=self._novo_teste).pack(fill="x", padx=20, pady=(10,0))


        self.canvas = ctk.CTkCanvas(self, bg="#121212")
        self.canvas.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)
        self.canvas.bind("<Button-3>", self.on_pan_start)
        self.canvas.bind("<B3-Motion>", self.on_pan_drag)
        self.canvas.bind("<ButtonRelease-3>", self.on_pan_release)
        self.bind("<Configure>", lambda e: self.render())


        # Estado para arrastar pontos
        self.dragging_point = None  # 'esq', 'dir', ou None
        # Estado para pan (arrastar imagem)
        self.pan_start_pos = None
        # Estado de feedback visual quando um ponto � corrigido para o contorno
        self._contorno_destacado = False
        self._contorno_highlight_after_id = None


    def _measurement_fields_changed(self, _event=None):
        if self.measurement_record is not None:
            self._refresh_measurement_record()


    def _current_measurement_data(self):
        def point(value):
            return [round(float(value[0]), 2), round(float(value[1]), 2)] if value is not None else None

        return {
            "timestamp": self.measurement_timestamp,
            "sample": self.sample_entry.get().strip(),
            "notes": self.notes_entry.get().strip(),
            "source_path": self.measurement_metadata.get("source_path", ""),
            "source_name": self.measurement_metadata.get("source_name", ""),
            "acquisition_mode": self.measurement_metadata.get("acquisition_mode", "Não informado"),
            "image_size": self.measurement_metadata.get("image_size", ""),
            "analysis_size": f"{self.raw_image.shape[1]}x{self.raw_image.shape[0]} px",
            "roi": self.measurement_metadata.get("roi", ""),
            "filter_mode": self.measurement_metadata.get("filter_mode", "Auto"),
            "mask_source": self.measurement_metadata.get("mask_source", "Não informado"),
            "mask_quality": self.measurement_metadata.get("mask_quality"),
            "risk_flags": list(self.measurement_metadata.get("risk_flags", [])),
            "baseline_method": self.baseline_method or "Não informado",
            "contact_method": self.contact_method or "Não informado",
            "baseline_y_px": round(float(self.baseline_y), 2) if self.baseline_y is not None else None,
            "left_contact_px": point(self.p_esq),
            "right_contact_px": point(self.p_dir),
            "left_internal_deg": round(float(self.ae_interna), 2) if self.ae_interna is not None else None,
            "left_external_deg": round(float(self.ae_externa), 2) if self.ae_externa is not None else None,
            "right_internal_deg": round(float(self.ad_interna), 2) if self.ad_interna is not None else None,
            "right_external_deg": round(float(self.ad_externa), 2) if self.ad_externa is not None else None,
            "mean_internal_deg": (
                round((float(self.ae_interna) + float(self.ad_interna)) / 2, 2)
                if self.ae_interna is not None and self.ad_interna is not None else None
            ),
            "fit_score": round(float(self.fit_quality.get("score", 0.0)) * 100, 2),
            "fit_rmse_px": round(float(self.fit_quality.get("rmse_px", 0.0)), 3),
            "fit_points": int(self.fit_quality.get("n_pts", 0)),
            "manual_adjustments": sorted(self.manual_adjustments),
            "calculation_parameters": dict(self.measurement_metadata.get("calculation_parameters", {})),
        }


    @staticmethod
    def _format_measurement_value(value, suffix=""):
        return f"{value}{suffix}" if value is not None and value != "" else "Não informado"


    def _measurement_summary_text(self, record):
        roi = record["roi"]
        if isinstance(roi, (list, tuple)) and len(roi) == 4:
            roi = f"x={roi[0]}, y={roi[1]}, largura={roi[2] - roi[0]}, altura={roi[3] - roi[1]} px"
        risk_flags = ", ".join(record["risk_flags"]) if record["risk_flags"] else "Nenhum sinalizado"
        adjustments = ", ".join(record["manual_adjustments"]) if record["manual_adjustments"] else "Nenhum"
        params = "\n".join(f"  {key}: {value}" for key, value in record["calculation_parameters"].items())
        return (
            f"Data/hora: {record['timestamp']}\n"
            f"Amostra: {record['sample'] or 'Não informada'}\n"
            f"Observações: {record['notes'] or 'Nenhuma'}\n"
            f"Imagem: {record['source_name'] or 'Não informada'}\n"
            f"Origem: {record['acquisition_mode']}\n"
            f"Caminho: {record['source_path'] or 'Não informado'}\n"
            f"Dimensão original: {record['image_size'] or 'Não informada'}\n"
            f"Dimensão analisada: {record['analysis_size']}\n"
            f"ROI: {roi or 'Não informada'}\n"
            f"Modo/filtro: {record['filter_mode']} / máscara {record['mask_source']}\n"
            f"Qualidade da máscara: {self._format_measurement_value(record['mask_quality'], '%')}\n"
            f"Riscos do contorno: {risk_flags}\n"
            f"Ângulo interno esquerdo: {self._format_measurement_value(record['left_internal_deg'], '°')}\n"
            f"Ângulo externo esquerdo: {self._format_measurement_value(record['left_external_deg'], '°')}\n"
            f"Ângulo interno direito: {self._format_measurement_value(record['right_internal_deg'], '°')}\n"
            f"Ângulo externo direito: {self._format_measurement_value(record['right_external_deg'], '°')}\n"
            f"Média interna: {self._format_measurement_value(record['mean_internal_deg'], '°')}\n"
            f"Linha de base: método={record['baseline_method']}, y={self._format_measurement_value(record['baseline_y_px'], ' px')}\n"
            f"Contato: {record['contact_method']}\n"
            f"Ponto esquerdo (x, y): {record['left_contact_px'] or 'Não detectado'}\n"
            f"Ponto direito (x, y): {record['right_contact_px'] or 'Não detectado'}\n"
            f"Ajuste do contorno: score={record['fit_score']}%, RMSE={record['fit_rmse_px']} px, "
            f"pontos={record['fit_points']}\n"
            f"Ajustes do pesquisador: {adjustments}\n"
            f"Parâmetros do cálculo:\n{params or '  Padrões internos do algoritmo'}"
        )


    @staticmethod
    def _measurement_csv_row(record):
        return [
            record["timestamp"], record["sample"], record["notes"], record["source_name"],
            record["source_path"], record["acquisition_mode"], record["image_size"],
            record["analysis_size"], str(record["roi"]), record["filter_mode"],
            record["mask_source"], record["mask_quality"], "; ".join(record["risk_flags"]),
            record["left_internal_deg"], record["left_external_deg"],
            record["right_internal_deg"], record["right_external_deg"],
            record["mean_internal_deg"], record["baseline_method"], record["baseline_y_px"],
            str(record["left_contact_px"]), str(record["right_contact_px"]),
            record["contact_method"], record["fit_score"], record["fit_rmse_px"],
            record["fit_points"], "; ".join(record["manual_adjustments"]),
        ]


    @staticmethod
    def _measurement_csv_text(records):
        headers = [
            "data_hora", "amostra", "observacoes", "imagem", "caminho_imagem",
            "origem", "dimensao_original", "dimensao_analisada", "roi_px", "filtro",
            "mascara", "qualidade_mascara_pct", "riscos_contorno",
            "angulo_interno_esq_deg", "angulo_externo_esq_deg",
            "angulo_interno_dir_deg", "angulo_externo_dir_deg", "media_interna_deg",
            "metodo_linha_base", "linha_base_y_px", "contato_esq_xy_px", "contato_dir_xy_px",
            "metodo_contato", "qualidade_ajuste_pct", "rmse_px", "pontos_ajuste",
            "ajustes_pesquisador",
        ]
        output = io.StringIO()
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(ContactAngleApp._measurement_csv_row(record) for record in records)
        return output.getvalue()


    def _refresh_measurement_record(self):
        record = self._current_measurement_data()
        if self.measurement_record is None:
            self.measurement_record = record
            self.measurement_history.append(record)
        else:
            self.measurement_record.update(record)

        self.measurement_summary.configure(state="normal")
        self.measurement_summary.delete("1.0", "end")
        self.measurement_summary.insert("1.0", self._measurement_summary_text(self.measurement_record))
        self.measurement_summary.configure(state="disabled")
        self.history_button.configure(text=f"Histórico da sessão ({len(self.measurement_history)})")


    def _copy_to_clipboard(self, text):
        try:
            self.clipboard_clear()
            self.clipboard_append(text)
            self.update()
        except Exception as exc:
            logger.warning("Não foi possível copiar os dados da medição", exc_info=True)
            messagebox.showerror("Erro ao copiar", f"Não foi possível copiar para a área de transferência:\n{exc}")


    def copy_measurement_summary(self):
        if self.measurement_record is not None:
            self._copy_to_clipboard(self._measurement_summary_text(self.measurement_record))


    def copy_measurement_row(self):
        if self.measurement_record is not None:
            self._copy_to_clipboard(self._measurement_csv_text([self.measurement_record]))


    def show_measurement_history(self):
        window = ctk.CTkToplevel(self)
        window.title("Histórico de medições da sessão")
        window.geometry("900x600")
        window.transient(self)
        window.grid_columnconfigure(1, weight=1)
        window.grid_rowconfigure(0, weight=1)

        records_frame = ctk.CTkScrollableFrame(window, width=230)
        records_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        details = ctk.CTkTextbox(window, wrap="word")
        details.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)

        def show_record(record):
            details.configure(state="normal")
            details.delete("1.0", "end")
            details.insert("1.0", self._measurement_summary_text(record))
            details.configure(state="disabled")

        for index, record in reversed(list(enumerate(self.measurement_history, start=1))):
            title = record["sample"] or record["source_name"] or f"Medição {index}"
            ctk.CTkButton(
                records_frame,
                text=f"{index}. {title}\n{record['timestamp']}",
                anchor="w",
                command=lambda item=record: show_record(item),
            ).pack(fill="x", padx=4, pady=3)

        actions = ctk.CTkFrame(window)
        actions.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ctk.CTkButton(
            actions,
            text="Copiar histórico para planilha",
            command=lambda: self._copy_to_clipboard(self._measurement_csv_text(self.measurement_history)),
        ).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(actions, text="Fechar", command=window.destroy).pack(side="right", padx=5, pady=5)

        if self.measurement_history:
            show_record(self.measurement_history[-1])
        else:
            details.insert("1.0", "Nenhuma medição foi registrada nesta sessão.")
            details.configure(state="disabled")


    def show_image_comparison(self):
        if self.raw_image is None or self.bin_image is None:
            messagebox.showerror("Comparação indisponível", "A imagem original ou a máscara não está disponível.")
            return

        smoothing_applied = self.measurement_metadata.get("mask_source") != "FALLBACK_OTSU"
        panels = _make_comparison_images(
            self.raw_image,
            self.bin_image,
            self.gota_pts,
            self.baseline_y,
            self.baseline_line_params,
            self.p_esq,
            self.p_dir,
            getattr(self, "tangent_left", None),
            getattr(self, "tangent_right", None),
            self.ae_interna,
            self.ad_interna,
            smoothing_applied,
        )

        window = ctk.CTkToplevel(self)
        window.title("Comparação das etapas do processamento")
        window.geometry("1200x850")
        try:
            window.state("zoomed")
        except Exception:
            pass
        window.transient(self)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        for row in range(2):
            window.grid_rowconfigure(row, weight=1)

        image_refs = []
        for index, (title, pixels) in enumerate(panels.items()):
            row, column = divmod(index, 2)
            frame = ctk.CTkFrame(window)
            frame.grid(row=row, column=column, sticky="nsew", padx=8, pady=8)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(1, weight=1)
            ctk.CTkLabel(frame, text=title, font=("Arial", 14, "bold")).grid(
                row=0, column=0, sticky="w", padx=8, pady=(6, 2)
            )

            image = Image.fromarray(pixels)
            image.thumbnail((540, 300), Image.Resampling.LANCZOS)
            display_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=image.size,
            )
            image_refs.append(display_image)
            ctk.CTkLabel(frame, text="", image=display_image).grid(
                row=1, column=0, sticky="nsew", padx=8, pady=(0, 8)
            )

        window._comparison_images = image_refs
        ctk.CTkButton(window, text="Fechar", command=window.destroy).grid(
            row=3, column=0, columnspan=2, pady=(0, 10)
        )


    def res_box(self, label, highlight=False):
        f = ctk.CTkFrame(
            self.sidebar,
            fg_color="#1f6aa5" if highlight else "#2b2b2b"
        )
        f.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(f, text=label).pack()
        v = ctk.CTkLabel(f, text="0.00°", font=("Arial", 26, "bold"))
        v.pack()
        return v
    # ---------------- AN�LISE ----------------
    def initial_analysis(self):
        """
        Realiza a an�lise inicial seguindo a hierarquia cient�fica:
        Prioridade 1: Transi��o F�sica (Joelhos da gota)
        Prioridade 2: Fallback Estat�stico (apenas se a f�sica falhar)
        """
        # 1. Obt�m o contorno da gota atrav�s do m�dulo especializado
        self.gota_pts = contorno.encontrar_contorno_gota(self.bin_image)
        if self.gota_pts is None:
            self.gota_pts = contorno.encontrar_contorno_gota_robusto(self.bin_image)
        if self.gota_pts is None:
            messagebox.showerror("Erro", "Não foi possível detectar a silhueta da gota.")
            return


        # Qualidade calculada internamente mas n�o exibida na UI


        # 2. Executa o pipeline h�brido para detectar baseline e contatos.
        # Note: `detectar_baseline_hibrida` aceita apenas `gota_pts` e `debug`.
        res = linha_base.detectar_baseline_hibrida(self.gota_pts, debug=False)

        # 3. Extrai os par�metros fundamentais da baseline
        self.baseline_y = res['baseline_y']
        self.baseline_line_params = res.get('line_params')
        self.baseline_method = res.get('method')

        # 4. Define os pontos de contato (Prioriza o que veio da Transi��o)
        self.p_esq = res.get('p_esq')
        self.p_dir = res.get('p_dir')
        self.contact_method = res.get('contact_method')


        try:
            baseline_ok = self.baseline_y is not None and np.isfinite(self.baseline_y)
        except Exception:
            baseline_ok = False

        if not baseline_ok:
            self.baseline_y = float(np.max(self.gota_pts[:, 1]))

        if self.p_esq is None or self.p_dir is None:
            self.contact_method = 'contact_not_reliable'

        # Assegura tipos corretos
        if self.p_esq is not None:
            self.p_esq = [float(self.p_esq[0]), float(self.p_esq[1])]
        if self.p_dir is not None:
            self.p_dir = [float(self.p_dir[0]), float(self.p_dir[1])]

        baseline_imagem, params_imagem, info_imagem = linha_base.detectar_baseline_superficie(
            self.raw_image,
            self.gota_pts,
            fallback_y=self.baseline_y,
        )
        if info_imagem.get("valida") and baseline_imagem is not None:
            self.baseline_y = float(baseline_imagem)
            self.baseline_line_params = params_imagem
            self.p_esq, self.p_dir = linha_base.find_contact_points_by_extrapolation(
                self.gota_pts,
                self.baseline_y,
            )

        # Garante que a primeira an�lise j� use contatos aderidos ao contorno.
        self._validar_corrigir_pontos_contato(origem="inicial")


        # DEBUG: ajuda a identificar se os pontos foram detectados corretamente
        logger.debug("DEBUG AN�LISE INICIAL:")
        logger.debug("  Contorno: %s pontos", len(self.gota_pts))
        logger.debug("  Y_min=%.1f, Y_max=%.1f", np.min(self.gota_pts[:, 1]), np.max(self.gota_pts[:, 1]))
        logger.debug("  Baseline Y: %.2f", self.baseline_y)
        logger.debug("  Ponto Esq: %s", self.p_esq)
        logger.debug("  Ponto Dir: %s", self.p_dir)
        if self.p_esq and self.p_dir:
            dist = abs(self.p_dir[0] - self.p_esq[0])
            y_diff = abs(self.p_dir[1] - self.p_esq[1])
            logger.debug("  Dist�ncia X entre pontos: %.2f px", dist)
            logger.debug("  Diferen�a Y entre pontos: %.2f px", y_diff)
        logger.debug("  M�todo contato: %s", self.contact_method)


        # --- TRAVA ABSOLUTA NO CH�O ---
        if self.gota_pts is not None:
            baseline_detectada = float(self.baseline_y)
            gray_raw = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2GRAY)
            _, thresh_bg = cv2.threshold(gray_raw, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            x_esq = max(0, int(np.min(self.gota_pts[:, 0])) - 5)
            x_dir = min(gray_raw.shape[1] - 1, int(np.max(self.gota_pts[:, 0])) + 5)

            meio_y = gray_raw.shape[0] // 2

            transicoes_esq = np.where(thresh_bg[meio_y:, x_esq] == 0)[0]
            transicoes_dir = np.where(thresh_bg[meio_y:, x_dir] == 0)[0]

            y_esq = (transicoes_esq[0] + meio_y) if len(transicoes_esq) > 0 else self.baseline_y
            y_dir = (transicoes_dir[0] + meio_y) if len(transicoes_dir) > 0 else self.baseline_y

            chao_real = float(max(y_esq, y_dir))

            # S� substitui a baseline quando a transi��o da imagem diverge
            # claramente do piso detectado no contorno. Pequenas diferen�as
            # s�o espessura/ru�do da linha e devem preservar o comportamento-base.
            if abs(chao_real - baseline_detectada) > 10.0:
                self.baseline_y = chao_real
                p_esq, p_dir = linha_base.find_contact_points_by_extrapolation(
                    self.gota_pts, self.baseline_y
                )
                if p_esq is not None and p_dir is not None:
                    self.p_esq = p_esq
                    self.p_dir = p_dir
                    # A trava sobrescreveu os contatos; revalida pela mesma ancora usada antes.
                    self._validar_corrigir_pontos_contato(origem="trava_chao")

        self._atualizar_indices_contato()

        if self.baseline_line_params is not None:
            vx, vy, x0, _ = self.baseline_line_params
            self.baseline_line_params = (vx, vy, x0, self.baseline_y)

        self.perfil_liquido_ar, self.validacao_perfil = contorno.extrair_perfil_liquido_ar(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y,
            indice_esq=self.indice_contato_esq, indice_dir=self.indice_contato_dir
        )
        if not self.validacao_perfil["valida"]:
            messagebox.showerror("Geometria inválida", "O perfil líquido-ar não pôde ser separado do fechamento Binary.")
            return

        logger.info("An�lise conclu�da via: %s", self.contact_method)

        fit_q = angulo_contato.calcular_qualidade_dinamica(
            self.perfil_liquido_ar, self.p_esq, self.p_dir, self.baseline_y
        )
        self.fit_quality = fit_q
        q_pct = int(100 * float(fit_q.get("score", 0.0)))
        rmse = float(fit_q.get("rmse_px", 0.0))
        logger.info("[QUALIDADE AJUSTE] Score=%s%% | RMSE=%.3fpx", q_pct, rmse)

        self.calculate()

    def update_contact_points(self):
        # Mant�m os pontos de contato apenas quando o fluxo atual os produziu com confian�a.
        if self.p_esq is None or self.p_dir is None:
            self.contact_method = 'contact_not_reliable'
            self.calculate()
            return

        # Recompute baseline line_params to keep rendering consistent
        if self.p_esq is not None and self.p_dir is not None:
            dx = self.p_dir[0] - self.p_esq[0]
            dy = self.p_dir[1] - self.p_esq[1]
            vx, vy = linha_base.safe_normalize(dx, dy)

            # Use center horizontal of the droplet for x0 to avoid lateral offset
            try:
                x0 = float(np.mean(self.gota_pts[:, 0]))
            except Exception:
                x0 = (self.p_esq[0] + self.p_dir[0]) / 2.0

            y0 = self.baseline_y  # Usa o Y original

            self.baseline_line_params = (
                float(vx),
                float(vy),
                float(x0),
                float(y0)
            )

            self.baseline_method = 'fallback_estatistico'

        self.calculate()

    def update_baseline(self, new_y: float):
        """
        Atualiza a posi��o da baseline e recalcula os contatos.
        """
        if float(new_y) != float(self.baseline_y):
            self.manual_adjustments.add("Linha de base ajustada pelo pesquisador")
        self.baseline_y = float(new_y)

        if self.baseline_line_params is not None:
            vx, vy, x0, _ = self.baseline_line_params
            self.baseline_line_params = (
                vx,
                vy,
                x0,
                float(new_y)
            )

        self._validar_corrigir_pontos_contato(
            origem="ajuste_baseline"
        )
        self._atualizar_indices_contato()

        self.perfil_liquido_ar, self.validacao_perfil = contorno.extrair_perfil_liquido_ar(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y,
            indice_esq=self.indice_contato_esq, indice_dir=self.indice_contato_dir
        )

        self.calculate()
        self.render()


    def _validar_corrigir_pontos_contato(self, origem: str = "manual"):
        """
        Corrige contatos fora do contorno.
        """
        if self.gota_pts is None:
            return

        houve_correcao = False

        if self.p_esq is not None:
            p_esq_final, corrigido_esq = contorno.projetar_ponto_no_contorno(
                self.p_esq,
                self.gota_pts,
                self.baseline_y,
                tolerancia_px=2.0
            )

            self.p_esq = p_esq_final

            if corrigido_esq:
                houve_correcao = True
                logger.info("[CONTORNO] p_esq corrigido (%s)", origem)

        if self.p_dir is not None:
            p_dir_final, corrigido_dir = contorno.projetar_ponto_no_contorno(
                self.p_dir,
                self.gota_pts,
                self.baseline_y,
                tolerancia_px=2.0
            )

            self.p_dir = p_dir_final

            if corrigido_dir:
                houve_correcao = True
                logger.info("[CONTORNO] p_dir corrigido (%s)", origem)

        if houve_correcao:
            self._ativar_destaque_contorno(400)


    def _atualizar_indices_contato(self):
        """Resolve o indice em gota_pts do contato ja validado (ancora unica por lado)."""
        self.indice_contato_esq = None
        self.indice_contato_dir = None
        if self.gota_pts is None:
            return
        if self.p_esq is not None:
            self.indice_contato_esq = int(np.argmin(np.linalg.norm(self.gota_pts - np.asarray(self.p_esq), axis=1)))
        if self.p_dir is not None:
            self.indice_contato_dir = int(np.argmin(np.linalg.norm(self.gota_pts - np.asarray(self.p_dir), axis=1)))


    def _ativar_destaque_contorno(self, duracao_ms: int = 400):
        self._contorno_destacado = True

        if self._contorno_highlight_after_id is not None:
            try:
                self.after_cancel(self._contorno_highlight_after_id)
            except Exception:
                pass

        self.render()

        self._contorno_highlight_after_id = self.after(
            duracao_ms,
            self._desativar_destaque_contorno
        )


    def _desativar_destaque_contorno(self):
        self._contorno_destacado = False
        self._contorno_highlight_after_id = None
        self.render()

    def calculate(self):
        if self.p_esq is None or self.p_dir is None:
            # N�o � poss�vel calcular sem ambos os pontos de contato
            self.ae = None
            self.ad = None
            self.res_e.configure(text="---")
            self.res_d.configure(text="---")
            self.res_m.configure(text="---")
            self.ae_interna = self.ad_interna = None
            self.ae_externa = self.ad_externa = None
            self._refresh_measurement_record()
            return

        perfil = self.perfil_liquido_ar
        if perfil is None or len(perfil) < 3:
            self.ae = None
            self.ad = None
            self.res_e.configure(text="---")
            self.res_d.configure(text="---")
            self.res_m.configure(text="---")
            self.ae_interna = self.ad_interna = None
            self.ae_externa = self.ad_externa = None
            self._refresh_measurement_record()
            return

        ae = angulo_contato.calcular_angulo_circular(
            perfil, self.p_esq, self.p_dir, self.baseline_y, "esq"
        )
        ad = angulo_contato.calcular_angulo_circular(
            perfil, self.p_esq, self.p_dir, self.baseline_y, "dir"
        )

        self.tangent_left = angulo_contato.calcular_vetor_tangente(
            perfil, self.p_esq, self.p_dir, self.baseline_y, "esq"
        )
        self.tangent_right = angulo_contato.calcular_vetor_tangente(
            perfil, self.p_esq, self.p_dir, self.baseline_y, "dir"
        )

        # Mant�m None se c�lculo falhar (melhor sinaliza��o ao usu�rio)
        self.ae = float(ae) if ae is not None else None
        self.ad = float(ad) if ad is not None else None

        self.ae_interna = float(self.ae) if self.ae is not None else None
        self.ad_interna = float(self.ad) if self.ad is not None else None
        self.ae_externa = float(180.0 - self.ae) if self.ae is not None else None
        self.ad_externa = float(180.0 - self.ad) if self.ad is not None else None

        def fmt_duplo(valor_interno, valor_externo):
            if valor_interno is None or valor_externo is None:
                return "---"
            return f"Int {valor_interno:.2f}°\nExt {valor_externo:.2f}°"

        ae_txt = fmt_duplo(self.ae_interna, self.ae_externa)
        ad_txt = fmt_duplo(self.ad_interna, self.ad_externa)
        media = (self.ae_interna + self.ad_interna) / 2 if (self.ae_interna is not None and self.ad_interna is not None) else None
        med_txt = f"{media:.2f}°" if media is not None else "---"

        self.res_e.configure(text=ae_txt)
        self.res_d.configure(text=ad_txt)
        self.res_m.configure(text=med_txt)

        self._refresh_measurement_record()

        self.render()


    # ---------------- RENDER ----------------
    def zoom(self, e):
        self.zoom_scale *= 1.1 if e.delta > 0 else 0.9
        self.render()


    def get_offsets(self):
        cw, ch = self.canvas.winfo_width(), self.canvas.winfo_height()
        ih, iw = self.raw_image.shape[:2]
        self.ratio = min(cw / iw, ch / ih) * self.zoom_scale
        nw, nh = int(iw * self.ratio), int(ih * self.ratio)
        return (cw - nw) // 2 + self.pan_offset_x, (ch - nh) // 2 + self.pan_offset_y


    def render(self):
        # Guarda re-entr�ncia: evita recurs�o causada por update_idletasks / Configure
        if getattr(self, '_rendering', False):
            return
        self._rendering = True
        try:
            self._render_internal()
        finally:
            self._rendering = False


    def _render_internal(self):
        self.canvas.delete("all")


        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw <= 1 or ch <= 1:
            return


        ih, iw = self.raw_image.shape[:2]
        # inclui zoom_scale no c�lculo do ratio
        self.ratio = min(cw / iw, ch / ih) * self.zoom_scale


        nw = int(iw * self.ratio)
        nh = int(ih * self.ratio)
        if nw <= 0 or nh <= 0:
            return


        img_pil = Image.fromarray(
            cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2RGB)
        ).resize((nw, nh), Image.NEAREST)
        self.tk_img = ImageTk.PhotoImage(img_pil)


        ox = (cw - nw) // 2 + self.pan_offset_x
        oy = (ch - nh) // 2 + self.pan_offset_y


        self.canvas.create_image(
            ox, oy,
            image=self.tk_img,
            anchor="nw"
        )


        def to_scr(x, y):
            return x * self.ratio + ox, y * self.ratio + oy


        perfil = self.perfil_liquido_ar
        if perfil is not None and len(perfil) >= 2 and self.validacao_perfil and self.validacao_perfil.get("valida", False):
            if self._contorno_destacado:
                desenho.desenhar_contorno_destaque(self.canvas, perfil, to_scr)
            else:
                desenho.desenhar_contorno(self.canvas, perfil, to_scr)


        if self.baseline_y is not None:
            # passar par�metros de linha base inclinada se dispon�veis
            line_params = getattr(self, 'baseline_line_params', None)
            desenho.desenhar_baseline(
                self.canvas,
                self.baseline_y,
                self.ratio,
                ox,  # offset_x (novo par�metro)
                oy,  # offset_y
                image_width=iw,  # largura da imagem (coordenadas de imagem)
                line_params=line_params  # par�metros de regress�o (se houver)
            )


        if self.p_esq and self.p_dir:
            desenho.desenhar_pontos_contato(
                self.canvas, self.p_esq, self.p_dir, to_scr
            )
            # Desenha tangentes somente quando pelo menos um �ngulo for v�lido
            ae_val = getattr(self, 'ae', None)
            ad_val = getattr(self, 'ad', None)
            if ae_val is not None or ad_val is not None:
                try:
                    if hasattr(self, 'tangent_left') and self.tangent_left is not None:
                        desenho.desenhar_tangente_vetor(
                            self.canvas,
                            self.p_esq,
                            self.tangent_left,
                            self.zoom_scale,
                            to_scr,
                        )
                    if hasattr(self, 'tangent_right') and self.tangent_right is not None:
                        desenho.desenhar_tangente_vetor(
                            self.canvas,
                            self.p_dir,
                            self.tangent_right,
                            self.zoom_scale,
                            to_scr,
                        )
                except Exception:
                    logger.warning("Falha ao desenhar as tangentes", exc_info=True)


    # ============ M�TODOS PARA ARRASTAR PONTOS MANUALMENTE ============

    def on_canvas_click(self, e):
        """Detecta clique nos pontos de contato amarelos."""
        if self.p_esq is None or self.p_dir is None:
            return
    
        # Calcular offsets da tela para imagem
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        ih, iw = self.raw_image.shape[:2]
        ratio_local = min(cw / iw, ch / ih) * self.zoom_scale
        nw = int(iw * ratio_local)
        nh = int(ih * ratio_local)
        ox = (cw - nw) // 2 + self.pan_offset_x
        oy = (ch - nh) // 2 + self.pan_offset_y
    
        # Converter coordenadas da tela para imagem
        img_x = (e.x - ox) / ratio_local
        img_y = (e.y - oy) / ratio_local

        # Verificar se clicou perto dos pontos (raio: 15 pixels na tela)
        screen_radius = 15
        img_radius = screen_radius / ratio_local if ratio_local > 0 else 15

        dist_esq = np.hypot(img_x - self.p_esq[0], img_y - self.p_esq[1])
        dist_dir = np.hypot(img_x - self.p_dir[0], img_y - self.p_dir[1])

        if dist_esq < img_radius:
            self.dragging_point = 'esq'
        elif dist_dir < img_radius:
            self.dragging_point = 'dir'


    def on_canvas_drag(self, e):
        """Arrasta o ponto com intera��o de Snap Magn�tico."""
        if self.dragging_point is None:
            return

        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        ih, iw = self.raw_image.shape[:2]
        ratio_local = min(cw / iw, ch / ih) * self.zoom_scale

        nw = int(iw * ratio_local)
        nh = int(ih * ratio_local)

        ox = (cw - nw) // 2 + self.pan_offset_x
        oy = (ch - nh) // 2 + self.pan_offset_y

        img_x = (e.x - ox) / ratio_local
        img_y = (e.y - oy) / ratio_local

        img_x = np.clip(img_x, 0, iw - 1)

        # �MAN DE CONTORNO
        if self.gota_pts is not None:
            meio_x = np.mean(self.gota_pts[:, 0])
            
            if self.dragging_point == 'esq':
                pts_lado = self.gota_pts[self.gota_pts[:, 0] < meio_x]
            else:
                pts_lado = self.gota_pts[self.gota_pts[:, 0] >= meio_x]
                
            if len(pts_lado) > 0:
                distancias = np.hypot(pts_lado[:, 0] - img_x, pts_lado[:, 1] - img_y)
                idx_min = np.argmin(distancias)
                
                # FOR�A O PONTO A GRUDAR NO CONTORNO CIANO SEMPRE
                novo_ponto = [float(pts_lado[idx_min, 0]), float(pts_lado[idx_min, 1])]
                self._ativar_destaque_contorno(300)
            else:
                novo_ponto = [float(img_x), float(img_y)]
        else:
            novo_ponto = [float(img_x), float(img_y)]

        # Atualiza a posi��o em tempo real
        if self.dragging_point == 'esq':
            self.p_esq = novo_ponto
            self.manual_adjustments.add("Ponto de contato esquerdo ajustado pelo pesquisador")
        elif self.dragging_point == 'dir':
            self.p_dir = novo_ponto
            self.manual_adjustments.add("Ponto de contato direito ajustado pelo pesquisador")

        self._atualizar_indices_contato()

        self.perfil_liquido_ar, self.validacao_perfil = contorno.extrair_perfil_liquido_ar(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y,
            indice_esq=self.indice_contato_esq, indice_dir=self.indice_contato_dir
        )
        self.calculate()


    def on_canvas_release(self, e):
        """Solta o ponto quando mouse � liberado."""
        self.dragging_point = None


    def on_pan_start(self, e):
        """Inicia pan (arrastar imagem) com bot�o direito."""
        self.pan_start_pos = (e.x, e.y)


    def on_pan_drag(self, e):
        """Arrasta a imagem enquanto bot�o direito est� pressionado."""
        if self.pan_start_pos is None:
            return
    
        dx = e.x - self.pan_start_pos[0]
        dy = e.y - self.pan_start_pos[1]
    
        self.pan_offset_x += dx
        self.pan_offset_y += dy
    
        self.pan_start_pos = (e.x, e.y)
    
        self.render()


    def on_pan_release(self, e):
        """Libera o pan quando bot�o direito � solto."""
        self.pan_start_pos = None


    def _on_close(self):
        if self._contorno_highlight_after_id is not None:
            try:
                self.after_cancel(self._contorno_highlight_after_id)
            except Exception:
                pass
            self._contorno_highlight_after_id = None
        try:
            if self.master is not None:
                self.master.destroy()
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass


    def _novo_teste(self):
        # Reseta SelectionWindow e volta a ela
        try:
            if self.master is not None:
                self.master.reset_for_new_test()
                self.master.deiconify()
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass




# ====================================================
