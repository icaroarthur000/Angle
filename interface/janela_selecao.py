import cv2
import hashlib
import numpy as np
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

from Cal_angulo import angulo_contato
from parametros import carregar_parametros
from processamento_imagem import filtros, contorno
from interface.aplicativo_angulo_contato import ContactAngleApp

try:
    from processamento_imagem.preprocessamento import preprocess_image_for_contact_angle, save_debug_imgs
    HAVE_PREPROCESS = True
except ImportError:
    HAVE_PREPROCESS = False
    def preprocess_image_for_contact_angle(img_bgr):
        try:
            res = filtros.aplicar_pre_processamento(img_bgr)
            if isinstance(res, dict):
                bin_img = res.get('binary') or res.get('bin')
                enhanced = res.get('enhanced_gray') or res.get('gray')
                if enhanced is not None and enhanced.ndim == 2:
                    vis = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
                else:
                    vis = img_bgr
            else:
                first, bin_img = res[0], res[1]
                if first is None:
                    vis = img_bgr
                    enhanced = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                elif first.ndim == 2:
                    enhanced = first
                    vis = cv2.cvtColor(first, cv2.COLOR_GRAY2BGR)
                else:
                    vis = first
                    enhanced = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
        except Exception:
            gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            _, bin_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            vis = img_bgr
        if bin_img is None:
            _, bin_img = cv2.threshold(enhanced, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        if bin_img.dtype != np.uint8:
            bin_img = bin_img.astype(np.uint8)
        return {'binary': bin_img, 'corrected_bgr': vis, 'enhanced_gray': enhanced, 'debug_imgs': {}}

    def save_debug_imgs(debug_dict, out_dir, prefix='dbg'):
        return None
class SelectionWindow(ctk.CTk):


    def __init__(self):
        super().__init__()
        self.title(" Seleção da Gota")
        self.geometry("1100x700")
        self.minsize(800, 540)
        # iniciar maximizada (mantém o botão X visível)
        try:
            self.state("zoomed")
        except Exception:
            pass


        self.raw_image = None
        self.cap = None
        self.camera_running = False
        self.image_source_path = ""
        self.acquisition_mode = "Não informado"
        self.measurement_history = ContactAngleApp.load_measurement_history()
        self._history_save_after_id = None


        self.roi_start = None
        self.roi_rect = None
        self.current_roi = None


        self.ratio = 1.0
        self.offset_x = 0
        self.offset_y = 0
       
        # ===== Seleção de Filtro =====
        self.active_filters = set()   # vazio = Automático; pode ter "OTSU", "CANNY", ou ambos
        self.binary_image = None      # Imagem binarizada com filtro principal
        self.binary_preview = None    # Preview com contorno(s) desenhado(s)
        self.analysis_meta = {}


        self.setup_ui()


    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


        top = ctk.CTkFrame(self, corner_radius=12)
        top.grid(row=0, column=0, sticky="ew", padx=20, pady=(14, 10))
        top.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            top,
            text="1. Imagem e região  ›  2. Processamento  ›  3. Análise",
            font=("Arial", 16, "bold"),
            anchor="w",
        ).grid(row=0, column=0, sticky="ew", padx=16, pady=(12, 8))

        ctk.CTkLabel(
            top,
            text="Abra uma imagem ou use a câmera; depois arraste sobre a gota para selecionar a região.",
            text_color="#aeb8c4",
            anchor="w",
        ).grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 8))

        toolbar = ctk.CTkFrame(top, fg_color="transparent")
        toolbar.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
        self._toolbar = toolbar
        toolbar.grid_columnconfigure(1, weight=1)
        source_actions = ctk.CTkFrame(toolbar, fg_color="transparent")
        source_actions.grid(row=0, column=0, sticky="w")
        self._source_actions = source_actions
        filter_actions = ctk.CTkFrame(toolbar, fg_color="transparent")
        filter_actions.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self._filter_actions = filter_actions
        filter_actions.grid_columnconfigure(2, weight=1)

        ctk.CTkButton(
            source_actions,
            text="Abrir imagem",
            width=125,
            command=self.load_from_file,
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            source_actions,
            text="Câmera",
            width=100,
            command=self.toggle_camera,
        ).pack(side="left", padx=4)


        # Botão de Capturar (aparece apenas quando câmera está ligada)
        self.btn_capture = ctk.CTkButton(
            source_actions,
            text="Capturar",
            width=100,
            fg_color="#4CAF50",
            hover_color="#388e3c",
            command=self.capture_image
        )
        # Não adiciona ao layout inicialmente (será feito quando câmera ligar)
        self.btn_capture_visible = False


        # ===== BOTÕES DE FILTRO =====
        self.btn_filter_otsu = ctk.CTkButton(
            filter_actions, text="Binária",
            width=95,
            fg_color="#2b2b2b",
            hover_color="#404040",
            border_width=2,
            border_color="#555555",
            command=lambda: self.toggle_filter("OTSU")
        )
        self.btn_filter_otsu.grid(row=0, column=0, padx=3)


        self.btn_filter_canny = ctk.CTkButton(
            filter_actions, text="Contornos",
            width=100,
            fg_color="#2b2b2b",
            hover_color="#404040",
            border_width=2,
            border_color="#555555",
            command=lambda: self.toggle_filter("CANNY")
        )
        self.btn_filter_canny.grid(row=0, column=1, padx=3)


        # Label que mostra o modo atual (Auto / Binary / Edges / Ambos)
        self.lbl_filter_mode = ctk.CTkLabel(
            filter_actions, text="Auto",
            text_color="#aaaaaa",
            font=("Arial", 11)
        )
        self.lbl_filter_mode.grid(row=0, column=2, sticky="w", padx=8)

        self.btn_next = ctk.CTkButton(
            toolbar, text="Analisar seleção  →",
            width=175,
            height=38,
            fg_color="#18794e",
            hover_color="#146640",
            command=self.confirm_and_analyze,
            state="disabled"
        )
        self.btn_next.grid(row=0, column=2, sticky="e", padx=(8, 4))


        self.display_frame = ctk.CTkFrame(self, fg_color="#121212")
        self.display_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self._toolbar_compact = None
        toolbar.bind("<Configure>", self._adapt_toolbar)

        self.canvas = ctk.CTkCanvas(
            self.display_frame, bg="#121212", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda _event: self.render_frame())


        self.canvas.bind("<Button-1>", self.start_roi)
        self.canvas.bind("<B1-Motion>", self.draw_roi)
        self.canvas.bind("<ButtonRelease-1>", self.end_roi)


        # handler de fechamento
        self.protocol("WM_DELETE_WINDOW", self._on_close)


    def _adapt_toolbar(self, event):
        if event.widget is not self._toolbar:
            return
        compact = event.width < 820
        if compact == self._toolbar_compact:
            return
        self._toolbar_compact = compact

        if compact:
            self._toolbar.grid_rowconfigure(0, weight=0)
            self._toolbar.grid_rowconfigure(1, weight=0)
            self._source_actions.grid(row=0, column=0, columnspan=3, sticky="w")
            self._filter_actions.grid(row=1, column=0, columnspan=2, sticky="w", padx=(0, 8))
            self.btn_next.grid(row=1, column=2, sticky="e", padx=(8, 4))
        else:
            self._toolbar.grid_rowconfigure(1, weight=0)
            self._source_actions.grid(row=0, column=0, sticky="w")
            self._filter_actions.grid(row=0, column=1, sticky="w", padx=(8, 0))
            self.btn_next.grid(row=0, column=2, sticky="e", padx=(8, 4))


    # ===== Gerenciamento de Filtro =====
    def toggle_filter(self, filtro: str):
        """Ativa/desativa um filtro (toggle). Ambos podem estar ativos ao mesmo tempo.
        Se clicar em um já ativo → desativa (volta para Auto se ambos desligados)."""
        if filtro in self.active_filters:
            self.active_filters.discard(filtro)
        else:
            self.active_filters.add(filtro)
        self._update_filter_buttons()
        if self.current_roi is not None:
            self.apply_and_preview_filter()


    def _update_filter_buttons(self):
        """Atualiza visual dos botões e label de modo conforme active_filters."""
        active_fg     = "#1e4d8c"
        active_border = "#4a9eff"
        inactive_fg     = "#2b2b2b"
        inactive_border = "#555555"


        if "OTSU" in self.active_filters:
            self.btn_filter_otsu.configure(fg_color=active_fg, border_color=active_border)
        else:
            self.btn_filter_otsu.configure(fg_color=inactive_fg, border_color=inactive_border)


        if "CANNY" in self.active_filters:
            self.btn_filter_canny.configure(fg_color=active_fg, border_color=active_border)
        else:
            self.btn_filter_canny.configure(fg_color=inactive_fg, border_color=inactive_border)


        # Atualiza label do modo
        if not self.active_filters:
            self.lbl_filter_mode.configure(text="🤖 Auto",    text_color="#aaaaaa")
        elif self.active_filters == {"OTSU"}:
            self.lbl_filter_mode.configure(text="⬛ Binary",  text_color="#4a9eff")
        elif self.active_filters == {"CANNY"}:
            self.lbl_filter_mode.configure(text="🔲 Edges",   text_color="#4a9eff")
        else:
            self.lbl_filter_mode.configure(text="⬛🔲 Ambos", text_color="#ffcc00")


    def _gerar_binario_analise(self, roi):
        """Gera a máscara padrão compatível com o pipeline geométrico de referência."""
        try:
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, bin_mask = filtros.aplicar_filtro_binary_otsu(roi)
            mask_gota, pts = contorno.extrair_mascara_gota(bin_mask, img_gray=gray)
            q = contorno.avaliar_qualidade_contorno(pts, bin_mask.shape)
            return mask_gota, {
                "mask_source": "OTSU_BASE",
                "quality_score": float(q.get("score", 0.0)),
                "risk_flags": q.get("risk_flags", [])
            }
        except Exception:
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, bin_fallback = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            return bin_fallback, {"mask_source": "FALLBACK_OTSU", "quality_score": 0.0, "risk_flags": ["fallback"]}


    def apply_and_preview_filter(self):
        """Aplica filtro(s) escolhido(s) à ROI e mostra contorno(s) detectado(s).
        - Nenhum filtro ativo → modo Auto (usa pipeline padrão, mostra apenas contorno)
        - 1 filtro ativo     → mostra o resultado desse filtro
        - Ambos ativos       → mostra os 2 contornos sobrepostos (verde=Binary, ciano=Edges)
        """
        if self.raw_image is None or self.current_roi is None:
            return


        x1, y1, x2, y2 = self.current_roi
        roi = self.raw_image[y1:y2, x1:x2].copy()
        if roi.size == 0:
            return


        try:
            use_otsu  = "OTSU"  in self.active_filters
            use_canny = "CANNY" in self.active_filters
            auto_mode = not use_otsu and not use_canny


            # Imagem cinza da ROI para alimentar Sobel Y do pipeline de separação
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)


            # Máscaras para preview
            _, bin_otsu = filtros.aplicar_filtro_binary_otsu(roi)
            bin_otsu, _ = contorno.remover_substrato_abaixo_superficie(bin_otsu, img_gray=roi_gray)
            bin_canny = None
            if use_canny:
                _, bin_canny = filtros.aplicar_filtro_edges_canny(roi)
                bin_canny, _ = contorno.remover_substrato_abaixo_superficie(bin_canny, img_gray=roi_gray)


            # Binário de análise respeita o filtro escolhido pelo usuário
            if use_otsu and not use_canny:
                self.binary_image, pts = contorno.extrair_mascara_gota(bin_otsu, img_gray=roi_gray)
                q = contorno.avaliar_qualidade_contorno(pts, self.binary_image.shape)
                self.analysis_meta = {
                    "mask_source": "OTSU",
                    "quality_score": float(q.get("score", 0.0)),
                    "risk_flags": q.get("risk_flags", []),
                }
            elif use_canny and not use_otsu:
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, filtros.CANNY_CLOSE_KERNEL)
                bin_canny_filled = cv2.morphologyEx(
                    bin_canny,
                    cv2.MORPH_CLOSE,
                    kernel,
                    iterations=filtros.CANNY_CLOSE_ITERATIONS,
                )
                self.binary_image, pts = contorno.extrair_mascara_gota(bin_canny_filled, img_gray=roi_gray)
                q = contorno.avaliar_qualidade_contorno(pts, self.binary_image.shape)
                self.analysis_meta = {
                    "mask_source": "CANNY",
                    "quality_score": float(q.get("score", 0.0)),
                    "risk_flags": q.get("risk_flags", []),
                }
            else:
                # Auto (nenhum ativo ou ambos) — pipeline inteligente escolhe o melhor
                self.binary_image, self.analysis_meta = self._gerar_binario_analise(roi)


            # --- Monta o preview SEM recortar visualmente a imagem inteira ---
            preview = self.raw_image.copy()


            # Contorno OTSU (verde) — mostra se OTSU ativo ou auto
            if use_otsu or auto_mode:
                pts_otsu = contorno.encontrar_contorno_gota_robusto(bin_otsu)
                if pts_otsu is None:
                    pts_otsu = contorno.encontrar_contorno_gota(bin_otsu)
                if pts_otsu is not None and len(pts_otsu) > 0:
                    pts_int = pts_otsu.astype(np.int32)
                    pts_int[:, 0] += x1
                    pts_int[:, 1] += y1
                    cv2.polylines(preview, [pts_int], True, (0, 220, 80), 2)
                    for pt in pts_int:
                        cv2.circle(preview, tuple(pt), 2, (0, 255, 180), -1)


            # Contorno Canny (ciano) — mostra se CANNY ativo
            if use_canny and bin_canny is not None:
                pts_canny = contorno.encontrar_contorno_gota_robusto(bin_canny_filled)
                if pts_canny is None:
                    pts_canny = contorno.encontrar_contorno_gota(bin_canny_filled)
                if pts_canny is not None and len(pts_canny) > 0:
                    pts_int = pts_canny.astype(np.int32)
                    pts_int[:, 0] += x1
                    pts_int[:, 1] += y1
                    cv2.polylines(preview, [pts_int], True, (255, 200, 0), 2)
                    for pt in pts_int:
                        cv2.circle(preview, tuple(pt), 2, (255, 220, 80), -1)


            # Destaca a ROI atual sem recortar a tela
            cv2.rectangle(preview, (x1, y1), (x2, y2), (0, 255, 255), 2)


            # Legenda no canto
            legends = []
            if use_otsu or auto_mode:
                legends.append(("Binary", (0, 220, 80)))
            if use_canny:
                legends.append(("Edges",  (255, 200, 0)))
            for i, (lbl, color) in enumerate(legends):
                cv2.putText(preview, lbl, (6, 18 + i * 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 1, cv2.LINE_AA)


            # Sem texto de análise/qualidade — só mostra o que é necessário


         


            self.binary_preview = preview
            self.render_frame()


        except Exception as e:
            logger.exception("Erro ao aplicar filtro(s) %s", self.active_filters)
            self.binary_image  = None
            self.binary_preview = None


    # ===== FIM: Gerenciamento de Filtro =====


    # ---------------- IMAGEM ----------------
    def _reset_selection_state(self):
        """Limpa ROI e previews para permitir nova seleção sem resíduos do estado anterior."""
        self.current_roi = None
        self.roi_start = None
        self.binary_image = None
        self.binary_preview = None
        self.analysis_meta = {}
        if self.roi_rect is not None:
            try:
                self.canvas.delete(self.roi_rect)
            except Exception:
                logger.debug("Falha ao remover o retângulo de ROI", exc_info=True)
            self.roi_rect = None
        try:
            self.btn_next.configure(state="disabled")
        except Exception:
            logger.debug("Falha ao preparar a janela de análise", exc_info=True)


    def load_from_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
        )
        if path:
            self.stop_camera()
            img = cv2.imread(path)
            if img is None:
                messagebox.showerror("Erro", "Não foi possível abrir a imagem selecionada.")
                return
            self.raw_image = img
            self.image_source_path = path
            self.acquisition_mode = "Arquivo"
            self._reset_selection_state()
            self.render_frame()


    def detect_cameras(self):
        """Detecta todas as câmeras disponíveis no sistema"""
        cameras = []
        for i in range(10):  # Testa até 10 câmeras
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                cameras.append(i)
                cap.release()
        return cameras


    def select_camera(self):
        """Abre diálogo para selecionar qual câmera usar"""
        cameras = self.detect_cameras()
       
        if not cameras:
            messagebox.showerror("Erro", "Nenhuma câmera disponível")
            return
       
        if len(cameras) == 1:
            # Se há apenas uma câmera, usa direto
            self.open_camera(cameras[0])
            return
       
        # Se há múltiplas câmeras, abre diálogo de seleção
        selection_window = ctk.CTkToplevel(self)
        selection_window.title("Selecionar Câmera")
        selection_window.geometry("400x300")
        selection_window.grab_set()
       
        ctk.CTkLabel(
            selection_window,
            text="Selecione a câmera:",
            font=("Arial", 14, "bold")
        ).pack(pady=20)
       
        # Criar botões para cada câmera
        frame = ctk.CTkFrame(selection_window)
        frame.pack(padx=20, pady=10, fill="both", expand=True)
       
        for cam_id in cameras:
            btn_text = f"Câmera {cam_id}" if cam_id > 0 else "Câmera 0 (Padrão)"
            ctk.CTkButton(
                frame,
                text=btn_text,
                command=lambda cid=cam_id: [self.open_camera(cid), selection_window.destroy()]
            ).pack(pady=10, fill="x")
       
        # Botão Cancelar
        ctk.CTkButton(
            selection_window,
            text="Cancelar",
            fg_color="#a52a2a",
            command=selection_window.destroy
        ).pack(pady=10, padx=20, fill="x")


    def open_camera(self, camera_id):
        """Abre a câmera com o ID especificado"""
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            messagebox.showerror("Erro", f"Não foi possível abrir câmera {camera_id}")
            return
        self.image_source_path = ""
        self.acquisition_mode = f"Câmera {camera_id}"
        self.camera_running = True
        # Mostra o botão de capturar
        if not self.btn_capture_visible:
            self.btn_capture.pack(side="left", padx=4)
            self.btn_capture_visible = True
        self.update_camera()


    def toggle_camera(self):
        if not self.camera_running:
            self.select_camera()  # Abre diálogo para selecionar câmera
        else:
            # Se câmera está ligada, abre diálogo para trocar
            self.select_camera_replace()


    def select_camera_replace(self):
        """Abre diálogo para trocar câmera ou desligar"""
        cameras = self.detect_cameras()
       
        if not cameras:
            messagebox.showerror("Erro", "Nenhuma câmera disponível")
            return
       
        # Se há múltiplas câmeras, abre diálogo de seleção
        selection_window = ctk.CTkToplevel(self)
        selection_window.title("Trocar Câmera ou Desligar")
        selection_window.geometry("400x300")
        selection_window.grab_set()
       
        ctk.CTkLabel(
            selection_window,
            text="Selecione a câmera ou deslige:",
            font=("Arial", 14, "bold")
        ).pack(pady=20)
       
        # Criar botões para cada câmera
        frame = ctk.CTkFrame(selection_window)
        frame.pack(padx=20, pady=10, fill="both", expand=True)
       
        for cam_id in cameras:
            btn_text = f"Câmera {cam_id}" if cam_id > 0 else "Câmera 0 (Padrão)"
            ctk.CTkButton(
                frame,
                text=btn_text,
                command=lambda cid=cam_id: [self.stop_camera(), self.open_camera(cid), selection_window.destroy()]
            ).pack(pady=10, fill="x")
       
        # Botão Desligar
        ctk.CTkButton(
            selection_window,
            text="Desligar Câmera",
            fg_color="#a52a2a",
            command=lambda: [self.stop_camera(), selection_window.destroy()]
        ).pack(pady=10, padx=20, fill="x")


    def stop_camera(self):
        self.camera_running = False
        if self.cap:
            self.cap.release()
            self.cap = None
        # Oculta o botão de capturar
        if self.btn_capture_visible:
            self.btn_capture.pack_forget()
            self.btn_capture_visible = False


    def update_camera(self):
        if self.camera_running:
            ret, frame = self.cap.read()
            if ret:
                self.raw_image = frame
                self.render_frame()
            self.after(15, self.update_camera)


    def capture_image(self):
        """Captura a imagem atual da câmera e salva em pasta"""
        if self.raw_image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem disponível para capturar.")
            return
       
        try:
            # Criar pasta "capturas_Angle" se não existir
            capture_folder = os.path.join(os.path.expanduser("~"), "Pictures", "capturas_Angle")
            os.makedirs(capture_folder, exist_ok=True)
           
            # Gerar nome do arquivo com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"captura_{timestamp}.jpg"
            filepath = os.path.join(capture_folder, filename)
           
            # Salvar a imagem
            if not cv2.imwrite(filepath, self.raw_image):
                messagebox.showerror("Erro", "Não foi possível salvar a imagem capturada.")
                return
            self.image_source_path = filepath
            self.acquisition_mode = "Captura de câmera"
           
            # Parar a câmera para congelar a imagem
            self.stop_camera()
           
            # Limpa seleção antiga para o usuário recortar novamente
            self._reset_selection_state()
           
            messagebox.showinfo("Sucesso", f"Imagem capturada e salva!\nCaminho: {filepath}\n\nVocê pode fazer a seleção agora.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar a imagem: {str(e)}")


    def render_frame(self):
        if self.raw_image is None:
            return


        cw, ch = self.canvas.winfo_width(), self.canvas.winfo_height()
        if cw < 10:
            cw, ch = 800, 600


        # Sempre mantém a escala da imagem completa para permitir reseleção contínua.
        if self.binary_preview is not None:
            display_img = self.binary_preview
        else:
            display_img = self.raw_image


        ih, iw = self.raw_image.shape[:2]


        self.ratio = min(cw / iw, ch / ih)
        nw, nh = int(iw * self.ratio), int(ih * self.ratio)
        self.offset_x, self.offset_y = (cw - nw) // 2, (ch - nh) // 2


        if display_img is self.raw_image:
            img = cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)
        else:
            # binary_preview já está em BGR
            img = cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)
       
        img = Image.fromarray(img).resize((nw, nh), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)


        self.canvas.delete("all")
        self.canvas.create_image(
            cw // 2, ch // 2, image=self.tk_img
        )


        # Redesenha ROI atual para facilitar ajustes sem reabrir imagem
        if self.current_roi is not None:
            x1, y1, x2, y2 = self.current_roi
            sx1 = int(x1 * self.ratio + self.offset_x)
            sy1 = int(y1 * self.ratio + self.offset_y)
            sx2 = int(x2 * self.ratio + self.offset_x)
            sy2 = int(y2 * self.ratio + self.offset_y)
            self.roi_rect = self.canvas.create_rectangle(
                sx1, sy1, sx2, sy2, outline="yellow", width=2
            )


    # ---------------- ROI ----------------
    def start_roi(self, e):
        self.roi_start = (e.x, e.y)
        if self.roi_rect:
            self.canvas.delete(self.roi_rect)
        self.roi_rect = self.canvas.create_rectangle(
            e.x, e.y, e.x, e.y, outline="yellow", width=2
        )


    def draw_roi(self, e):
        self.canvas.coords(
            self.roi_rect,
            self.roi_start[0], self.roi_start[1], e.x, e.y
        )


    def end_roi(self, e):
        x1, y1 = self.roi_start
        x2, y2 = e.x, e.y


        ix1, iy1 = self.canvas_to_img(x1, y1)
        ix2, iy2 = self.canvas_to_img(x2, y2)


        self.current_roi = [
            min(ix1, ix2), min(iy1, iy2),
            max(ix1, ix2), max(iy1, iy2)
        ]
        self.btn_next.configure(state="normal")
       
        # ===== NOVO: Aplica filtro e mostra pré-visualização =====
        self.apply_and_preview_filter()


    def canvas_to_img(self, x, y):
        ix = (x - self.offset_x) / self.ratio
        iy = (y - self.offset_y) / self.ratio
        h, w = self.raw_image.shape[:2]
        return int(np.clip(ix, 0, w - 1)), int(np.clip(iy, 0, h - 1))


    def confirm_and_analyze(self):
        r = self.current_roi
        if self.raw_image is None or r is None:
            return
        if self.acquisition_mode.startswith("Câmera") and not self.image_source_path:
            try:
                capture_folder = os.path.join(os.path.expanduser("~"), "Pictures", "capturas_Angle")
                os.makedirs(capture_folder, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filepath = os.path.join(capture_folder, f"captura_{timestamp}.jpg")
                saved = cv2.imwrite(filepath, self.raw_image)
            except (OSError, cv2.error) as exc:
                messagebox.showerror(
                    "Erro",
                    f"Não foi possível arquivar a imagem da câmera. A análise foi cancelada:\n{exc}",
                )
                return
            if not saved:
                messagebox.showerror(
                    "Erro",
                    "Não foi possível salvar a imagem da câmera. A análise foi cancelada para não perder a origem da medição.",
                )
                return
            self.image_source_path = filepath
            self.acquisition_mode = "Captura automática de câmera"

        cropped = self.raw_image[r[1]:r[3], r[0]:r[2]]
        if cropped.size == 0:
            return


        # === Usar filtro selecionado (já pré-visualizado) ou auto ===
        modo = "Auto" if not self.active_filters else " + ".join(sorted(self.active_filters))
        if self.active_filters == {"OTSU", "CANNY"}:
            modo += " (pipeline automático)"
        logger.info("[ANÁLISE] Modo: %s", modo)
        if self.binary_image is not None:
            # Usa máscara sólida preparada para análise.
            bin_img = self.binary_image.copy()
            bgr_vis = cropped
            debug_imgs = None
        else:
            # Gera máscara robusta caso não exista preview anterior.
            bin_img, self.analysis_meta = self._gerar_binario_analise(cropped)
            bgr_vis = cropped
            debug_imgs = None


        if self.analysis_meta:
            src = self.analysis_meta.get("mask_source", "?")
            q = int(100 * float(self.analysis_meta.get("quality_score", 0.0)))
            logger.info("[ANÁLISE] Mascara: %s | Qualidade estimada: %s%%", src, q)

        height, width = self.raw_image.shape[:2]
        roi = tuple(int(value) for value in r)
        measurement_metadata = {
            "source_path": self.image_source_path,
            "source_name": os.path.basename(self.image_source_path) if self.image_source_path else "",
            "acquisition_mode": self.acquisition_mode,
            "image_size": f"{width}x{height} px",
            "image_sha256": hashlib.sha256(self.raw_image.tobytes()).hexdigest(),
            "roi": roi,
            "filter_mode": modo,
            "mask_source": self.analysis_meta.get("mask_source", "Não informado"),
            "mask_quality": round(100 * float(self.analysis_meta.get("quality_score", 0.0)), 2),
            "risk_flags": list(self.analysis_meta.get("risk_flags", [])),
            "calculation_parameters": {
                **carregar_parametros(),
                "offset_baseline_fator": angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR,
                "offset_baseline_min_px": angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
                "offset_baseline_max_px": angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
                "janela_ajuste_fator": angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR,
                "janela_ajuste_min_px": angulo_contato.ANGLE_WINDOW_HEIGHT_MIN,
                "janela_ajuste_max_px": angulo_contato.ANGLE_WINDOW_HEIGHT_MAX,
                "distancia_maxima_contato_px": angulo_contato.ANGLE_CONTACT_CANDIDATE_MAX_DIST,
                "distancia_vertical_maxima_contato_px": angulo_contato.ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL,
                "janelas_locais_contato_px": angulo_contato.ANGLE_CONTACT_LOCAL_WINDOW_SIZES,
                "minimo_pontos_janela_contato": angulo_contato.ANGLE_CONTACT_MIN_WINDOW_POINTS,
                "r2_minimo_ajuste_tangente": angulo_contato.ANGLE_CONTACT_MIN_R2,
                "rmse_maximo_ajuste_tangente_px": angulo_contato.ANGLE_CONTACT_MAX_RMSE,
                "condicionamento_maximo_ajuste_tangente": angulo_contato.ANGLE_CONTACT_MAX_COND,
                "escala_sigma_outliers": angulo_contato.ANGLE_OUTLIER_SIGMA_SCALE,
                "rmse_referencia_px": angulo_contato.QUALITY_RMSE_REF_PX,
                "correcao_baseline_minima_px": ContactAngleApp.SURFACE_BASELINE_CORRECTION_MIN_DIFF_PX,
                "suavizacao_otsu_kernel_px": filtros.OTSU_BLUR_KERNEL,
                "morfologia_otsu_kernel_px": filtros.OTSU_MORPH_KERNEL,
                "morfologia_otsu_iteracoes": filtros.OTSU_MORPH_ITERATIONS,
                "suavizacao_canny_kernel_px": filtros.CANNY_BLUR_KERNEL,
                "canny_threshold_inferior": filtros.CANNY_THRESHOLD_LOW,
                "canny_threshold_superior": filtros.CANNY_THRESHOLD_HIGH,
                "fechamento_canny_kernel_px": filtros.CANNY_CLOSE_KERNEL,
                "fechamento_canny_iteracoes": filtros.CANNY_CLOSE_ITERATIONS,
            },
            "smoothing_kernel": (
                filtros.CANNY_BLUR_KERNEL
                if self.analysis_meta.get("mask_source") == "CANNY"
                else filtros.OTSU_BLUR_KERNEL
            ),
        }

        # sanity checks
        if bin_img is None:
            messagebox.showerror("Erro", "Pré-processamento não retornou imagem binária.")
            return
        if bgr_vis.shape[:2] != bin_img.shape[:2]:
            messagebox.showerror("Erro", "Dimensões da imagem visível e da binária não coincidem.")
            return


        # garante que a câmera/parsers foram parados e oculta a janela de seleção
        try:
            self.stop_camera()
        except Exception:
            pass
        self.withdraw()


        # Abrir janela de análise passando imagem BGR (vis) e BIN (processamento)
        new_win = ContactAngleApp(
            bgr_vis,
            bin_img,
            master=self,
            debug_imgs=debug_imgs,
            measurement_metadata=measurement_metadata,
            measurement_history=self.measurement_history,
        )
        new_win.lift()


    def reset_for_new_test(self):
        """Reseta estado completo para permitir nova medição."""
        self._flush_measurement_history()
        self.raw_image = None
        self.image_source_path = ""
        self.acquisition_mode = "Não informado"
        self.current_roi = None
        self.binary_image = None
        self.binary_preview = None
        self.roi_start = None
        self.roi_rect = None
        self.active_filters = set()
        try:
            self.canvas.delete("all")
        except Exception:
            pass
        try:
            self._update_filter_buttons()
        except Exception:
            pass
        try:
            self.btn_next.configure(state="disabled")
        except Exception:
            pass


    def _schedule_history_save(self):
        if self._history_save_after_id is not None:
            self.after_cancel(self._history_save_after_id)
        self._history_save_after_id = self.after(700, self._save_measurement_history)


    def _save_measurement_history(self):
        self._history_save_after_id = None
        try:
            ContactAngleApp.save_measurement_history(self.measurement_history)
        except OSError as exc:
            messagebox.showerror(
                "Erro ao salvar histórico",
                f"Não foi possível salvar o histórico de medições:\n{exc}",
            )


    def _flush_measurement_history(self):
        if self._history_save_after_id is not None:
            self.after_cancel(self._history_save_after_id)
            self._history_save_after_id = None
        self._save_measurement_history()


    def _on_close(self):
        # parar camera e sair
        self._flush_measurement_history()
        try:
            self.stop_camera()
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass




# ====================================================
# JANELA 2 — ANÁLISE
# ====================================================
