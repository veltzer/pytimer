"""
Sanity tests: the package and every module in it import cleanly.

A failed import here means a missing declared dependency, a syntax
error, or a broken import-time side effect — the failure classes a
placeholder test never catches.
"""

import importlib
import pkgutil

import pytimer


def _raise_on_package_error(name: str) -> None:
    """Surface subpackages that fail to import during the walk."""
    raise ImportError(f"failed to import package {name}")


def test_package_imports() -> None:
    """The top-level package imports and knows its own name."""
    assert pytimer.__name__ == "pytimer"


def test_all_modules_import() -> None:
    """Every module in the package imports without errors."""
    for info in pkgutil.walk_packages(pytimer.__path__, prefix="pytimer.", onerror=_raise_on_package_error):
        importlib.import_module(info.name)
