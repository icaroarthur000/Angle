"""Ponto de entrada da interface do Angle."""

import customtkinter as ctk

from interface.aplicativo_angulo_contato import ContactAngleApp
from interface.janela_selecao import SelectionWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

__all__ = ["SelectionWindow", "ContactAngleApp"]


if __name__ == "__main__":
    SelectionWindow().mainloop()
