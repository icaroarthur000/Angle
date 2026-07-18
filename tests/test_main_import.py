import importlib.util
from pathlib import Path


def test_main_module_imports_without_syntax_errors():
    root = Path(__file__).resolve().parents[1]
    module_path = root / "main.py"

    spec = importlib.util.spec_from_file_location("angle_main", module_path)
    module = importlib.util.module_from_spec(spec)

    assert spec.loader is not None
    spec.loader.exec_module(module)
    assert hasattr(module, "SelectionWindow")
