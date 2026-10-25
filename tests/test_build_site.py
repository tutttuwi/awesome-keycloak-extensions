import build_site
from conftest import make_project


def test_sort_key_orders_by_stars_desc_with_unknown_last():
    items = [make_project(repo="a/a", stars=5), make_project(repo="b/b", stars=None), make_project(repo="c/c", stars=50)]

    ordered = sorted(items, key=build_site.sort_key)

    assert [p["repo"] for p in ordered] == ["c/c", "a/a", "b/b"]


def test_sort_key_breaks_star_ties_by_newer_commit():
    old = make_project(repo="old/x", stars=10, last_commit="2024-01-01")
    new = make_project(repo="new/x", stars=10, last_commit="2026-01-01")

    assert sorted([old, new], key=build_site.sort_key)[0]["repo"] == "new/x"


def test_fmt_stars_marks_approximate_and_unknown():
    assert build_site.fmt_stars(make_project(stars=1200, stars_approx=True)) == "~1,200"
    assert build_site.fmt_stars(make_project(stars=None)) == "unknown"
    assert build_site.fmt_stars(make_project(stars=42)) == "42"


def test_row_escapes_pipes_in_summaries():
    p = make_project(summary="a | b", summary_ja="c | d", _activity="Active")

    r = build_site.row(1, p)

    assert "a \\| b<br>c \\| d" in r


def test_table_shows_placeholder_when_empty():
    assert build_site.table([]) == "_None yet._\n"
