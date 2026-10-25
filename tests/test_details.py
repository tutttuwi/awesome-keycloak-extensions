import build_site
import common
import validate
from conftest import make_project


def make_details(**overrides) -> dict:
    d = {
        "repo": "owner/keycloak-foo",
        "researched_at": "2026-10-25",
        "sources": ["https://github.com/owner/keycloak-foo#readme"],
        "can": [{"en": "Does foo.", "ja": "fooができる"}],
        "cannot": [{"en": "No bar.", "ja": "barはできない"}],
        "requires": [{"en": "Keycloak 26+", "ja": "Keycloak 26以上"}],
    }
    d.update(overrides)
    return d


# ---- validate

def test_valid_details_have_no_errors():
    assert validate.check_details(make_details(), "owner/keycloak-foo.yml", {"owner/keycloak-foo"}) == []


def test_details_for_unknown_project_are_reported():
    errs = validate.check_details(make_details(), "owner/keycloak-foo.yml", set())

    assert any("no project" in e for e in errs)


def test_details_filename_must_match_repo():
    errs = validate.check_details(make_details(), "x.yml", {"owner/keycloak-foo"})

    assert any("file name" in e for e in errs)


def test_details_need_at_least_one_can_item():
    errs = validate.check_details(make_details(can=[]), "owner/keycloak-foo.yml", {"owner/keycloak-foo"})

    assert any("can" in e for e in errs)


def test_details_items_need_both_languages():
    errs = validate.check_details(
        make_details(cannot=[{"en": "only english"}]), "owner/keycloak-foo.yml", {"owner/keycloak-foo"}
    )

    assert any("cannot[0]" in e and "ja" in e for e in errs)


def test_details_sources_must_be_https_urls():
    errs = validate.check_details(
        make_details(sources=["javascript:alert(1)"]), "owner/keycloak-foo.yml", {"owner/keycloak-foo"}
    )

    assert any("sources" in e for e in errs)


# ---- render

def test_render_detail_escapes_html_in_untrusted_text():
    p = make_project(summary="<script>x</script>", _activity="Active")
    d = make_details(can=[{"en": "<img src=x onerror=1>", "ja": "a&b"}])

    html = build_site.render_detail(p, d)

    assert "<script>x</script>" not in html
    assert "&lt;img src=x onerror=1&gt;" in html
    assert "a&amp;b" in html


def test_render_detail_shows_placeholder_when_no_documented_limits():
    html = build_site.render_detail(make_project(_activity="Active"), make_details(cannot=[]))

    assert "No limitations are stated in the documentation" in html


def test_render_detail_links_sources_and_repo():
    html = build_site.render_detail(make_project(_activity="Active"), make_details())

    assert 'href="https://github.com/owner/keycloak-foo#readme"' in html
    assert 'href="https://github.com/owner/keycloak-foo"' in html


def test_write_detail_pages_creates_one_page_per_detailed_project(tmp_path):
    p = make_project(_activity="Active")
    out = tmp_path / "p"

    written = build_site.write_detail_pages([p], {"owner/keycloak-foo": make_details()}, out)

    assert written == 1
    assert (out / "owner" / "keycloak-foo.html").exists()


def test_write_detail_pages_removes_stale_pages(tmp_path):
    out = tmp_path / "p"
    (out / "gone").mkdir(parents=True)
    (out / "gone" / "repo.html").write_text("old")

    build_site.write_detail_pages([], {}, out)

    assert not (out / "gone").exists()


def test_details_path_is_owner_dir_and_repo_file():
    assert common.details_path("Owner/Repo").relative_to(common.DETAILS).as_posix() == "Owner/Repo.yml"


def test_load_details_keys_by_lower_repo(tmp_path, monkeypatch):
    d = tmp_path / "details"
    (d / "Owner").mkdir(parents=True)
    (d / "Owner" / "Foo.yml").write_text("repo: Owner/Foo\ncan: []\n")
    monkeypatch.setattr(common, "DETAILS", d)

    assert list(common.load_details()) == ["owner/foo"]


def test_render_detail_turns_backticks_into_code_after_escaping():
    d = make_details(can=[{"en": "Set `a<b>` here", "ja": "`x`を設定"}])

    html = build_site.render_detail(make_project(_activity="Active"), d)

    assert "<code>a&lt;b&gt;</code>" in html
    assert "<code>x</code>を設定" in html
