import pathlib
import sys

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    """Point common.DATA at an empty temp directory."""
    d = tmp_path / "projects"
    d.mkdir()
    monkeypatch.setattr(common, "DATA", d)
    return d


def make_project(**overrides) -> dict:
    p = {
        "name": "keycloak-foo",
        "repo": "owner/keycloak-foo",
        "url": "https://github.com/owner/keycloak-foo",
        "summary": "Does foo.",
        "summary_ja": None,
        "kind": "core",
        "genre": "Authentication",
        "spi_types": [],
        "stars": 10,
        "forks": 1,
        "contributors": None,
        "last_commit": "2026-01-01",
        "official": False,
        "reviewed": True,
    }
    p.update(overrides)
    return p
