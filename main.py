import cv2
import numpy as np  
import math
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os
from datetime import datetime
# tenta importar módulo de pré-processamento robusto; fallback para filtros se faltar
try:
    from processamento_imagem.preprocess import preprocess_image_for_contact_angle, save_debug_imgs
    HAVE_PREPROCESS = True
except Exception: 
    HAVE_PREPROCESS = False
    def preprocess_image_for_contact_angle(img_bgr):
        # fallback: usa filtros.aplicar_pre_processamento que retorna (vis, bin)
        try: 
            res = filtros.aplicar_pre_processamento(img_bgr)
            if isinstance(res, dict):
                # suporta dicionário retornado
                bin_img = res.get('binary') or res.get('bin')
                enhanced = res.get('enhanced_gray') or res.get('gray')
                if enhanced is not None and enhanced.ndim == 2:
                    vis = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
                else:
                    vis = img_bgr
            else:
                # espera tuple (gray, bin) ou (vis, bin)
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
            # última alternativa: converte para gray e faz threshold simples
            gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            _, bin_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            vis = img_bgr
        # garante tipos e formatos
        if bin_img is None:
            _, bin_img = cv2.threshold(enhanced, 128, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        if bin_img.dtype != np.uint8:
            bin_img = (bin_img.astype(np.uint8))
        return {"binary": bin_img, "corrected_bgr": vis, "enhanced_gray": enhanced, "debug_imgs": {}}
    def save_debug_imgs(debug_dict, out_dir, prefix="dbg"):
        return None

# Modifique o método toggle_camera para chamar select_camera
def toggle_camera(self):
    if not self.camera_running:
        self.select_camera()  # Chama a nova função para selecionar a câmera
    else:
        self.stop_camera()
# ================= IMPORTS MODULARES =================
from processamento_imagem import filtros, contorno
from linha_base import linha_base
from Cal_angulo import angulo_contato
from visualizacao import desenho

# ================= CONFIGURAÇÃO CTK =================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ====================================================
# JANELA 1 — SELEÇÃO / RECORTE
# ====================================================
class SelectionWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Preparação - Seleção da Gota")
        self.geometry("1100x700")
        # iniciar maximizada (mantém o botão X visível)
        try:
            self.state("zoomed")
        except Exception:
            pass

        self.raw_image = None
        self.cap = None
        self.camera_running = False

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

        top = ctk.CTkFrame(self)
        top.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        ctk.CTkButton(top, text="Abrir Arquivo",
                      command=self.load_from_file).pack(side="left", padx=10)

        ctk.CTkButton(top, text="Câmera ON/OFF",
                      command=self.toggle_camera).pack(side="left", padx=10)

        # Botão de Capturar (aparece apenas quando câmera está ligada)
        self.btn_capture = ctk.CTkButton(
            top, text="Capturar",
            fg_color="#4CAF50",
            command=self.capture_image
        )
        # Não adiciona ao layout inicialmente (será feito quando câmera ligar)
        self.btn_capture_visible = False

        # ===== BOTÕES DE FILTRO =====
        sep = ctk.CTkLabel(top, text="|", text_color="#555555", font=("Arial", 18))
        sep.pack(side="left", padx=8)

        self.btn_filter_otsu = ctk.CTkButton(
            top, text="⬛ Binary",
            width=110,
            fg_color="#2b2b2b",
            hover_color="#404040",
            border_width=2,
            border_color="#555555",
            command=lambda: self.toggle_filter("OTSU")
        )
        self.btn_filter_otsu.pack(side="left", padx=4)

        self.btn_filter_canny = ctk.CTkButton(
            top, text="🔲 Edges",
            width=110,
            fg_color="#2b2b2b",
            hover_color="#404040",
            border_width=2,
            border_color="#555555",
            command=lambda: self.toggle_filter("CANNY")
        )
        self.btn_filter_canny.pack(side="left", padx=4)

        # Label que mostra o modo atual (Auto / Binary / Edges / Ambos)
        self.lbl_filter_mode = ctk.CTkLabel(
            top, text=" Auto",
            text_color="#aaaaaa",
            font=("Arial", 11)
        )
        self.lbl_filter_mode.pack(side="left", padx=6)

        sep2 = ctk.CTkLabel(top, text="|", text_color="#555555", font=("Arial", 18))
        sep2.pack(side="left", padx=8)

        self.btn_next = ctk.CTkButton(
            top, text="Analisar Seleção →",
            fg_color="green",
            command=self.confirm_and_analyze,
            state="disabled"
        )
        self.btn_next.pack(side="right", padx=10)

        self.display_frame = ctk.CTkFrame(self, fg_color="#121212")
        self.display_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self.canvas = ctk.CTkCanvas(
            self.display_frame, bg="#121212", highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.start_roi)
        self.canvas.bind("<B1-Motion>", self.draw_roi)
        self.canvas.bind("<ButtonRelease-1>", self.end_roi)

        # handler de fechamento
        self.protocol("WM_DELETE_WINDOW", self._on_close)

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
        """Gera máscara de análise robusta e escolhe o melhor contorno disponível."""
        try:
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            bin_mask, metodo = filtros.aplicar_multi_threshold(roi)
            mask_gota, pts = contorno.extrair_mascara_gota(bin_mask, img_gray=gray)
            q = contorno.avaliar_qualidade_contorno(pts, bin_mask.shape)
            return mask_gota, {
                "mask_source": metodo,
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
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
                bin_canny_filled = cv2.morphologyEx(bin_canny, cv2.MORPH_CLOSE, kernel, iterations=2)
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
                pts_canny = contorno.encontrar_contorno_gota_robusto(bin_canny)
                if pts_canny is None:
                    pts_canny = contorno.encontrar_contorno_gota(bin_canny)
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
            print(f"Erro ao aplicar filtro(s) {self.active_filters}: {e}")
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
                pass
            self.roi_rect = None
        try:
            self.btn_next.configure(state="disabled")
        except Exception:
            pass

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
        self.camera_running = True
        # Mostra o botão de capturar
        if not self.btn_capture_visible:
            self.btn_capture.pack(side="left", padx=10, after=self.master.winfo_children()[0] if self.master else None)
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
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"captura_{timestamp}.jpg"
            filepath = os.path.join(capture_folder, filename)
            
            # Salvar a imagem
            cv2.imwrite(filepath, self.raw_image)
            
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
        cropped = self.raw_image[r[1]:r[3], r[0]:r[2]]
        if cropped.size == 0:
            return

        # === Usar filtro selecionado (já pré-visualizado) ou auto ===
        modo = "Auto" if not self.active_filters else "/".join(sorted(self.active_filters))
        print(f"[ANÁLISE] Modo: {modo}")
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
            print(f"[ANÁLISE] Mascara: {src} | Qualidade estimada: {q}%")

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
        new_win = ContactAngleApp(bgr_vis, bin_img, master=self, debug_imgs=debug_imgs)
        new_win.lift()

    def reset_for_new_test(self):
        """Reseta estado completo para permitir nova medição."""
        self.raw_image = None
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

    def _on_close(self):
        # parar camera e sair
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
class ContactAngleApp(ctk.CTkToplevel):

    def __init__(self, img_bgr, img_bin, master=None, debug=False, debug_imgs=None):
        super().__init__(master=master)
        self.title("Ângulo de Contato")
        self.geometry("1100x700")
        # iniciar maximizada (mantém o botão X visível)
        try:
            self.state("zoomed")
        except Exception:
            pass

        # garantir fechamento limpo: quando a janela de análise fechar,
        # fecha também a janela principal (se ainda existir)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        # img_bgr: imagem para visualização (BGR uint8)
        # img_bin: máscara binária para processamento (2D uint8, 0/255)
        self.raw_image = img_bgr
        self.bin_image = img_bin

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
                pass
        self.gota_pts = None

        self.baseline_y = 0
        self.baseline_line_params = None
        self.baseline_method = None
        self.p_esq = None
        self.p_dir = None
        self.contact_method = None
        self.fit_quality = {"score": 0.0, "rmse_px": 999.0, "n_pts": 0.0}

        self.zoom_scale = 1.0
        self.pan_offset_x = 0
        self.pan_offset_y = 0

        self.ratio = 1.0

        self.setup_ui()
        self.initial_analysis()

    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=300)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        self.res_e = self.res_box("Ângulo Esq.")
        self.res_d = self.res_box("Ângulo Dir.")
        self.res_m = self.res_box("Média", True)

        # Botão para iniciar novo teste (voltar à seleção)
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
        # Estado de feedback visual quando um ponto é corrigido para o contorno
        self._contorno_destacado = False
        self._contorno_highlight_after_id = None

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
    # ---------------- ANÁLISE ----------------
    def initial_analysis(self):
        """
        Realiza a análise inicial seguindo a hierarquia científica:
        Prioridade 1: Transição Física (Joelhos da gota)
        Prioridade 2: Fallback Estatístico (apenas se a física falhar)
        """
        # 1. Obtém o contorno da gota através do módulo especializado
        self.gota_pts = contorno.encontrar_contorno_gota_robusto(self.bin_image)
        if self.gota_pts is None:
            self.gota_pts = contorno.encontrar_contorno_gota(self.bin_image)
        if self.gota_pts is None:
            messagebox.showerror("Erro", "Não foi possível detectar a silhueta da gota.")
            return

        # Qualidade calculada internamente mas não exibida na UI

        # 2. Cria máscara limpa (somente gota, sem substrato) a partir do contorno
        # para que detect_baseline_tls use análise por coluna em vez de percentil.
        _h, _w = self.bin_image.shape[:2]
        _mask_clean = np.zeros((_h, _w), dtype=np.uint8)
        cv2.fillPoly(_mask_clean, [self.gota_pts.astype(np.int32)], 255)

        # 3. Executa o pipeline híbrido passando a máscara limpa
        res = linha_base.detectar_baseline_hibrida(self.gota_pts, mascara=_mask_clean)
        
        # 3. Extrai os parâmetros fundamentais da baseline
        self.baseline_y = res['baseline_y']
        self.baseline_line_params = res.get('line_params')
        self.baseline_method = res.get('method')
        
        # 4. Define os pontos de contato (Prioriza o que veio da Transição)
        self.p_esq = res.get('p_esq')
        self.p_dir = res.get('p_dir')
        self.contact_method = res.get('contact_method')

        # Garantia de segurança: se baseline/contatos vierem inválidos, usa a base do contorno
        try:
            baseline_ok = self.baseline_y is not None and np.isfinite(self.baseline_y)
        except Exception:
            baseline_ok = False
        if not baseline_ok or self.p_esq is None or self.p_dir is None:
            base_y, base_p_esq, base_p_dir = linha_base.encontrar_pontos_contato_base(self.gota_pts)
            if baseline_ok is False:
                self.baseline_y = base_y
            if self.p_esq is None and base_p_esq is not None:
                self.p_esq = base_p_esq
            if self.p_dir is None and base_p_dir is not None:
                self.p_dir = base_p_dir

        # DEBUG: ajuda a identificar se os pontos foram detectados corretamente
        print(f"\n{'='*70}")
        print(f"DEBUG ANÁLISE INICIAL:")
        print(f"  Contorno: {len(self.gota_pts)} pontos")
        print(f"  Y_min={np.min(self.gota_pts[:, 1]):.1f}, Y_max={np.max(self.gota_pts[:, 1]):.1f}")
        print(f"  Baseline Y: {self.baseline_y:.2f}")
        print(f"  Ponto Esq: {self.p_esq}")
        print(f"  Ponto Dir: {self.p_dir}")
        if self.p_esq and self.p_dir:
            dist = abs(self.p_dir[0] - self.p_esq[0])
            y_diff = abs(self.p_dir[1] - self.p_esq[1])
            print(f"  Distância X entre pontos: {dist:.2f} px")
            print(f"  Diferença Y entre pontos: {y_diff:.2f} px")
        print(f"  Método contato: {self.contact_method}")
        print(f"{'='*70}\n")

        # 5. Fallback explícito: Segurança científica caso o contorno esteja muito ruidoso
        if self.p_esq is None or self.p_dir is None:
            print("[AVISO]: Transição física falhou. Aplicando Fallback de Geometria Fixa.")
            self.p_esq, self.p_dir = linha_base.encontrar_pontos_contato(
                self.gota_pts, self.baseline_y
            )
            self.contact_method = "fallback_estatistico"
            # Recompute line parameters from fallback contacts so drawing matches points
            if self.p_esq is not None and self.p_dir is not None:
                dx = self.p_dir[0] - self.p_esq[0]
                dy = self.p_dir[1] - self.p_esq[1]
                vx, vy = linha_base.safe_normalize(dx, dy)
                # Use center horizontal of the droplet for x0 to avoid lateral offset
                try:
                    x0 = float(np.mean(self.gota_pts[:, 0]))
                except Exception:
                    x0 = (self.p_esq[0] + self.p_dir[0]) / 2.0
                y0 = (self.p_esq[1] + self.p_dir[1]) / 2.0
                self.baseline_line_params = (float(vx), float(vy), float(x0), float(y0))
                self.baseline_y = y0
                self.baseline_method = 'fallback_estatistico'        

        # Garantia física: pontos de contato devem permanecer na borda da gota.
        self._validar_corrigir_pontos_contato(origem="auto")

        # 6. Registra no console para fins de auditoria científica
        print(f"Análise Concluída via: {self.contact_method}")

        # 6.1 Calcula qualidade dinâmica baseada no resíduo do ajuste geométrico
        fit_q = angulo_contato.calcular_qualidade_dinamica(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y
        )
        self.fit_quality = fit_q
        q_pct = int(100 * float(fit_q.get("score", 0.0)))
        rmse = float(fit_q.get("rmse_px", 0.0))
        print(f"[QUALIDADE AJUSTE] Score={q_pct}% | RMSE={rmse:.3f}px")
        
        # 7. Dispara os cálculos matemáticos finais e a renderização
        self.calculate()

    def update_contact_points(self):
        # usa pontos de contato já computados ou refallback
        if self.p_esq is None or self.p_dir is None:
            self.p_esq, self.p_dir = linha_base.encontrar_pontos_contato(
                self.gota_pts, self.baseline_y
            )
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
                y0 = (self.p_esq[1] + self.p_dir[1]) / 2.0
                self.baseline_line_params = (float(vx), float(vy), float(x0), float(y0))
                self.baseline_y = y0
                self.baseline_method = 'fallback_estatistico'

        self._validar_corrigir_pontos_contato(origem="update")
        self.calculate()

    def _validar_corrigir_pontos_contato(self, origem: str = "manual"):
        """Corrige contatos fora do contorno, restringindo à faixa inferior."""
        if self.gota_pts is None:
            return

        houve_correcao = False

        if self.p_esq is not None:
            p_esq_final, corrigido_esq = contorno.projetar_ponto_no_contorno(
                self.p_esq, self.gota_pts, self.baseline_y, tolerancia_px=2.0
            )
            self.p_esq = p_esq_final
            houve_correcao = houve_correcao or corrigido_esq
            if corrigido_esq:
                print(f"[CONTORNO] p_esq corrigido ({origem})")

        if self.p_dir is not None:
            p_dir_final, corrigido_dir = contorno.projetar_ponto_no_contorno(
                self.p_dir, self.gota_pts, self.baseline_y, tolerancia_px=2.0
            )
            self.p_dir = p_dir_final
            houve_correcao = houve_correcao or corrigido_dir
            if corrigido_dir:
                print(f"[CONTORNO] p_dir corrigido ({origem})")

        if houve_correcao:
            self._ativar_destaque_contorno(400)

    def _ativar_destaque_contorno(self, duracao_ms: int = 400):
        """Destaca o contorno temporariamente quando houver correção."""
        self._contorno_destacado = True
        if self._contorno_highlight_after_id is not None:
            try:
                self.after_cancel(self._contorno_highlight_after_id)
            except Exception:
                pass
            self._contorno_highlight_after_id = None

        self.render()
        self._contorno_highlight_after_id = self.after(duracao_ms, self._desativar_destaque_contorno)

    def _desativar_destaque_contorno(self):
        self._contorno_destacado = False
        self._contorno_highlight_after_id = None
        self.render()

    def calculate(self):
        if self.p_esq is None:
            return

        ae = angulo_contato.calcular_angulo_circular(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y, "esq"
        )
        ad = angulo_contato.calcular_angulo_circular(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y, "dir"
        )

        self.res_e.configure(text=f"{ae:.2f}°")
        self.res_d.configure(text=f"{ad:.2f}°")
        self.res_m.configure(text=f"{(ae+ad)/2:.2f}°")

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
        # Guarda re-entrância: evita recursão causada por update_idletasks / Configure
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
        # inclui zoom_scale no cálculo do ratio
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

        if self.gota_pts is not None:
            if self._contorno_destacado:
                desenho.desenhar_contorno_destaque(self.canvas, self.gota_pts, to_scr)
            else:
                desenho.desenhar_contorno(self.canvas, self.gota_pts, to_scr)

        if self.baseline_y is not None:
            # passar parâmetros de linha base inclinada se disponíveis
            line_params = getattr(self, 'baseline_line_params', None)
            desenho.desenhar_baseline(
                self.canvas,
                self.baseline_y,
                self.ratio,
                ox,  # offset_x (novo parâmetro)
                oy,  # offset_y
                image_width=iw,  # largura da imagem (coordenadas de imagem)
                line_params=line_params  # parâmetros de regressão (se houver)
            )

        if self.p_esq and self.p_dir:
            desenho.desenhar_pontos_contato(
                self.canvas, self.p_esq, self.p_dir, to_scr
            )

    # ============ MÉTODOS PARA ARRASTAR PONTOS MANUALMENTE ============
    
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
        """Arrasta o ponto enquanto o mouse se move."""
        if self.dragging_point is None:
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
        
        # Limitar ao contorno da imagem
        img_x = np.clip(img_x, 0, iw - 1)
        img_y = np.clip(img_y, 0, ih - 1)

        novo_ponto = [float(img_x), float(img_y)]

        # Restrição física: manter o contato na borda da gota, próximo à baseline.
        if self.gota_pts is not None:
            novo_ponto, foi_corrigido = contorno.projetar_ponto_no_contorno(
                novo_ponto,
                self.gota_pts,
                self.baseline_y,
                tolerancia_px=2.0,
            )
            if foi_corrigido:
                self._ativar_destaque_contorno(400)
        
        # Atualizar o ponto sendo arrastado
        if self.dragging_point == 'esq':
            self.p_esq = novo_ponto
        elif self.dragging_point == 'dir':
            self.p_dir = novo_ponto
        
        # Atualizar baseline_y como a média entre os dois pontos
        self.baseline_y = (self.p_esq[1] + self.p_dir[1]) / 2.0
        
        # Recalcular ângulos e renderizar em tempo real
        self.calculate()

    def on_canvas_release(self, e):
        """Solta o ponto quando mouse é liberado."""
        self.dragging_point = None

    def on_pan_start(self, e):
        """Inicia pan (arrastar imagem) com botão direito."""
        self.pan_start_pos = (e.x, e.y)

    def on_pan_drag(self, e):
        """Arrasta a imagem enquanto botão direito está pressionado."""
        if self.pan_start_pos is None:
            return
        
        dx = e.x - self.pan_start_pos[0]
        dy = e.y - self.pan_start_pos[1]
        
        self.pan_offset_x += dx
        self.pan_offset_y += dy
        
        self.pan_start_pos = (e.x, e.y)
        
        self.render()

    def on_pan_release(self, e):
        """Libera o pan quando botão direito é solto."""
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
if __name__ == "__main__":
    SelectionWindow().mainloop()
