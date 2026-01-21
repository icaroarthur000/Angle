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

    # ---------------- IMAGEM ----------------
    def load_from_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
        )
        if path:
            self.stop_camera()
            self.raw_image = cv2.imread(path)
            self.current_roi = None
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
            
            # Liberar o botão "Analisar Seleção"
            self.current_roi = None
            self.btn_next.configure(state="normal")
            
            messagebox.showinfo("Sucesso", f"Imagem capturada e salva!\nCaminho: {filepath}\n\nVocê pode fazer a seleção agora.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar a imagem: {str(e)}")

    def render_frame(self):
        if self.raw_image is None:
            return

        cw, ch = self.canvas.winfo_width(), self.canvas.winfo_height()
        if cw < 10:
            cw, ch = 800, 600

        ih, iw = self.raw_image.shape[:2]
        self.ratio = min(cw / iw, ch / ih)
        nw, nh = int(iw * self.ratio), int(ih * self.ratio)
        self.offset_x, self.offset_y = (cw - nw) // 2, (ch - nh) // 2

        img = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img).resize((nw, nh), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)

        self.canvas.delete("all")
        self.canvas.create_image(
            cw // 2, ch // 2, image=self.tk_img
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

        # === PRÉ-PROCESSAMENTO: PRIORIZAR FILTROS.PY (OTSU SIMPLES E RÁPIDO) ===
        try:
            # Tenta usar filtros.py primeiro (método simples, robusto e rápido)
            gray_vis, bin_img = filtros.aplicar_pre_processamento(cropped)
            bgr_vis = cropped  # Usa imagem original para visualização
            debug_imgs = None
        except Exception as e:
            # Fallback para preprocess.py se disponível
            if HAVE_PREPROCESS:
                try:
                    pre = preprocess_image_for_contact_angle(cropped)
                    bin_img = pre.get("binary")
                    bgr_vis = pre.get("corrected_bgr", cropped)
                    debug_imgs = pre.get("debug_imgs")
                except Exception:
                    # Última alternativa: grayscale + Otsu manual
                    gray_vis = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                    blur = cv2.GaussianBlur(gray_vis, (5, 5), 0)
                    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                    bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=1)
                    bgr_vis = cropped
                    debug_imgs = None
            else:
                # Última alternativa: grayscale + Otsu manual
                gray_vis = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray_vis, (5, 5), 0)
                _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=1)
                bgr_vis = cropped
                debug_imgs = None

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
        self.p_esq = None
        self.p_dir = None

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
        self.bind("<Configure>", lambda e: self.render())

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
        # 1. Encontra o contorno (agora mais preciso)
        self.gota_pts = contorno.encontrar_contorno_gota(self.bin_image)
        if self.gota_pts is None:
            return

        # 2. Chama o novo pipeline híbrido
        baseline_result = linha_base.detectar_baseline_hibrida(self.gota_pts)
        
        # 3. Extrai os dados (O segredo está em usar o que vem do dicionário)
        self.baseline_y = baseline_result['baseline_y']
        self.baseline_line_params = baseline_result.get('line_params')
        self.baseline_method = baseline_result['method']
        
        # Aqui garantimos a prioridade científica
        self.p_esq = baseline_result.get('p_esq')
        self.p_dir = baseline_result.get('p_dir')
        self.contact_method = baseline_result.get('contact_method')

        # Fallback explícito: se a transição falhar, usa a geometria fixa
        if self.p_esq is None or self.p_dir is None:
            self.p_esq, self.p_dir = linha_base.encontrar_pontos_contato(
                self.gota_pts, self.baseline_y
            )
            self.contact_method = "fallback_estatistico"
        
        self.calculate()

    def update_contact_points(self):
        # usa pontos de contato já computados ou refallback
        if self.p_esq is None or self.p_dir is None:
            self.p_esq, self.p_dir = linha_base.encontrar_pontos_contato(
                self.gota_pts, self.baseline_y
            )
        self.calculate()

    def calculate(self):
        if self.p_esq is None:
            return

        ae = angulo_contato.calcular_angulo_polinomial(
            self.gota_pts, self.p_esq, self.p_dir, self.baseline_y, "esq"
        )
        ad = angulo_contato.calcular_angulo_polinomial(
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
        self.canvas.delete("all")
        self.canvas.update_idletasks()

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
                image_width=nw,  # largura da imagem escalada
                line_params=line_params  # parâmetros de regressão (se houver)
            )

        if self.p_esq and self.p_dir:
            desenho.desenhar_pontos_contato(
                self.canvas, self.p_esq, self.p_dir, to_scr
            )

            try:
                ae = float(self.res_e.cget("text")[:-1])
                ad = float(self.res_d.cget("text")[:-1])
                desenho.desenhar_tangentes(
                    self.canvas,
                    self.p_esq, self.p_dir,
                    ae, ad,
                    self.zoom_scale,
                    to_scr
                )
            except:
                pass

    def _on_close(self):
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
        # Volta para a janela de seleção (se existir)
        try:
            if self.master is not None:
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
