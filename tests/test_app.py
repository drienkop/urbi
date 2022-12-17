from pathlib import Path

import pytest

from app.dynamic_modules import import_modules


@pytest.fixture
def mappings_path():
    return Path("./fixtures/mappings")


def test_import_modules(mappings_path):
    modules = import_modules(mappings_path)
    module_a = next(modules)
    module_b = next(modules)

    assert module_a.foo is True
    assert module_b.bar is False


def test_import_modules_with_non_existing_path():
    with pytest.raises(StopIteration):
        modules = import_modules("non_existing_path")
        next(modules)
