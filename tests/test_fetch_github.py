import urllib.error

import common
import fetch_github
from conftest import make_project


def fake_gh(full_name: str):
    def gh(path: str, want_headers: bool = False):
        if path.startswith("/repos/") and path.count("/") == 3:
            return {
                "full_name": full_name, "stargazers_count": 7, "forks_count": 2, "archived": False,
                "language": "Java", "license": {"spdx_id": "MIT"}, "description": "desc",
                "default_branch": "main", "pushed_at": "2026-01-02T00:00:00Z",
            }
        if "/commits" in path:
            return [{"commit": {"committer": {"date": "2026-01-01T00:00:00Z"}}}]
        raise urllib.error.HTTPError(path, 404, "nf", {}, None)
    return gh


def test_refresh_fills_numbers_from_api(monkeypatch):
    monkeypatch.setattr(fetch_github, "gh", fake_gh("owner/keycloak-foo"))
    p = make_project(stars=None, last_commit=None)

    assert fetch_github.refresh(p) is True
    assert (p["stars"], p["forks"], p["license"], p["last_commit"]) == (7, 2, "MIT", "2026-01-01")
    assert "_moved_to" not in p


def test_refresh_records_redirect_target(monkeypatch):
    monkeypatch.setattr(fetch_github, "gh", fake_gh("new-owner/keycloak-foo"))
    p = make_project()

    fetch_github.refresh(p)

    assert p["_moved_to"] == "new-owner/keycloak-foo"


def test_refresh_does_not_duplicate_not_found_note(monkeypatch):
    def gh(path, want_headers=False):
        raise urllib.error.HTTPError(path, 404, "nf", {}, None)
    monkeypatch.setattr(fetch_github, "gh", gh)
    p = make_project(note=None)

    fetch_github.refresh(p)
    fetch_github.refresh(p)

    assert p["note"].count(fetch_github.NOT_FOUND_NOTE) == 1


def test_merge_moved_into_existing_canonical_drops_alias_file(data_dir):
    canonical = make_project(repo="new/foo", url="https://github.com/new/foo")
    alias = make_project(repo="old/foo", url="https://github.com/old/foo")
    common.save(canonical)
    common.save(alias)
    projects = common.load_all()
    alias_loaded = next(p for p in projects if p["repo"] == "old/foo")
    alias_loaded["_moved_to"] = "new/foo"

    fetch_github.merge_moved(projects)

    remaining = common.load_all()
    assert [p["repo"] for p in remaining] == ["new/foo"]
    assert remaining[0]["aliases"] == ["old/foo"]


def test_merge_moved_without_canonical_renames_file(data_dir):
    alias = make_project(repo="old/foo", url="https://github.com/old/foo", name="foo")
    common.save(alias)
    projects = common.load_all()
    projects[0]["_moved_to"] = "new/foo"

    fetch_github.merge_moved(projects)

    remaining = common.load_all()
    assert len(remaining) == 1
    assert remaining[0]["repo"] == "new/foo"
    assert remaining[0]["url"] == "https://github.com/new/foo"
    assert remaining[0]["aliases"] == ["old/foo"]
    assert remaining[0]["_path"].name == "new__foo.yml"


def test_parse_kc_version_reads_property():
    assert fetch_github.parse_kc_version("<keycloak.version>26.8.0</keycloak.version>") == "26.8.0"


def test_parse_kc_version_reports_nightly_snapshot():
    assert fetch_github.parse_kc_version("<keycloak.version>999.0.0-SNAPSHOT</keycloak.version>") == "nightly"


def test_parse_kc_version_returns_none_when_absent():
    assert fetch_github.parse_kc_version("<project></project>") is None
