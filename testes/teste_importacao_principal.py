import importlib.util
import sys
from pathlib import Path


def test_main_module_imports_without_syntax_errors():
    root = Path(__file__).resolve().parents[1]
    module_path = root / "principal.py"

    spec = importlib.util.spec_from_file_location("angle_main", module_path)
    module = importlib.util.module_from_spec(spec)

    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    assert hasattr(module, "SelectionWindow")
    assert hasattr(module, "ContactAngleApp")


def test_ui_modules_expose_public_window_classes():
    from interface.aplicativo_angulo_contato import ContactAngleApp
    from interface.janela_selecao import SelectionWindow

    assert ContactAngleApp.__name__ == "ContactAngleApp"
    assert SelectionWindow.__name__ == "SelectionWindow"
