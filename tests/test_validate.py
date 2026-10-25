import validate
from conftest import make_project


def errors_for(p: dict, filename: str = "owner__keycloak-foo.yml") -> list[str]:
    return validate.check_project(p, filename)


def test_valid_project_has_no_errors():
    assert errors_for(make_project()) == []


def test_missing_required_field_is_reported():
    p = make_project()
    del p["summary"]

    assert any("summary" in e for e in errors_for(p))


def test_unknown_genre_and_kind_are_reported():
    errs = errors_for(make_project(genre="Nope", kind="plugin"))

    assert any("genre" in e for e in errs)
    assert any("kind" in e for e in errs)


def test_filename_must_match_repo():
    assert any("file name" in e for e in errors_for(make_project(), "wrong.yml"))


def test_url_must_match_repo():
    assert any("url" in e for e in errors_for(make_project(url="https://github.com/evil/x")))


def test_malformed_repo_is_reported():
    assert any("repo" in e for e in errors_for(make_project(repo="not-a-repo"), "not-a-repo.yml"))


def test_reviewed_entry_cannot_be_uncategorized():
    assert any("Uncategorized" in e for e in errors_for(make_project(genre="Uncategorized", reviewed=True)))


def test_unreviewed_entry_may_be_uncategorized():
    assert errors_for(make_project(genre="Uncategorized", reviewed=False)) == []


def test_numeric_fields_must_be_non_negative_ints_or_null():
    errs = errors_for(make_project(stars="many", forks=-1))

    assert any("stars" in e for e in errs)
    assert any("forks" in e for e in errs)


def test_last_commit_must_be_iso_date():
    assert any("last_commit" in e for e in errors_for(make_project(last_commit="yesterday")))


def test_duplicate_repos_and_aliases_are_reported():
    a = make_project(repo="owner/a", aliases=["old/a"])
    b = make_project(repo="old/a")

    errs = validate.check_duplicates([a, b])

    assert any("old/a" in e for e in errs)
