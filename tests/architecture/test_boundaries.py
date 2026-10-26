"""Éprouve le vrai linter sans inventer de modules métier dans l'application.

Les contrats de chaque module réel seront ajoutés lors de son introduction.
Ces fixtures vérifient les garde-fous, pas un découpage métier encore absent.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def boundary_probe(tmp_path: Path) -> Path:
    files = {
        "boundary_probe/__init__.py": "",
        "boundary_probe/alpha/__init__.py": "",
        "boundary_probe/alpha/internal.py": "VALUE = 1\n",
        "boundary_probe/alpha/api.py": "from boundary_probe.alpha.internal import VALUE\n",
        "boundary_probe/beta/__init__.py": "",
        "boundary_probe/beta/api.py": "from boundary_probe.alpha.api import VALUE\n",
        "pyproject.toml": """
[tool.importlinter]
root_package = "boundary_probe"
exclude_type_checking_imports = false

[[tool.importlinter.contracts]]
name = "Alpha internals are private"
type = "protected"
protected_modules = ["boundary_probe.alpha.internal"]
allowed_importers = ["boundary_probe.alpha"]

[[tool.importlinter.contracts]]
name = "Modules have no cycles"
type = "acyclic_siblings"
ancestors = ["boundary_probe"]
depth = 0
""",
    }
    for relative_path, content in files.items():
        target = tmp_path / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    return tmp_path


def lint_probe(probe: Path) -> subprocess.CompletedProcess[str]:
    # Le PYTHONPATH ne concerne que ce package synthétique dans le sous-processus.
    # Le package applicatif reste installé normalement depuis src/.
    return subprocess.run(
        [str(Path(sys.executable).with_name("lint-imports")), "--no-cache", "--no-logo"],
        cwd=probe,
        env={**os.environ, "PYTHONPATH": str(probe), "NO_COLOR": "1"},
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )


def test_public_facade_is_allowed(boundary_probe: Path) -> None:
    result = lint_probe(boundary_probe)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Alpha internals are private KEPT" in result.stdout
    assert "Modules have no cycles KEPT" in result.stdout


def test_direct_private_import_is_rejected(boundary_probe: Path) -> None:
    (boundary_probe / "boundary_probe/beta/api.py").write_text(
        "from boundary_probe.alpha.internal import VALUE\n"
    )
    result = lint_probe(boundary_probe)
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Alpha internals are private BROKEN" in result.stdout
    assert "Modules have no cycles KEPT" in result.stdout


def test_cycle_between_descendants_is_rejected(boundary_probe: Path) -> None:
    (boundary_probe / "boundary_probe/alpha/internal.py").write_text(
        "from boundary_probe.beta import api\nVALUE = 1\n"
    )
    result = lint_probe(boundary_probe)
    assert result.returncode == 1, result.stdout + result.stderr
    assert "Modules have no cycles BROKEN" in result.stdout
    assert "Alpha internals are private KEPT" in result.stdout
