import glob
import importlib.util
from pathlib import Path
from typing import Generator


def import_modules(folder_path: str) -> Generator:
    return (_import_module(file_path) for file_path in _list_files(folder_path))


def _list_files(path: str, extension: str = "py") -> list:
    return glob.glob(f"{path}/*.{extension}")


def _import_module(file_path: str) -> object:
    module_name = Path(file_path).stem
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
