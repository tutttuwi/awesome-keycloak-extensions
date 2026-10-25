# Setup (GitHub Pages)

1. Create a GitHub repo (`tutttuwi/awesome-keycloak-extensions`) and push to `main`.
2. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
3. Actions → "Update data & deploy Pages" → **Run workflow** (first run fills stars/forks/contributors/last commit and discovers the full official list).
4. Site: https://noccalabs.com/awesome-keycloak-extensions/ (the owner's Pages custom domain; `https://<owner>.github.io/<repo>/` redirects there). After that it refreshes every Monday.

Local:

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
export GITHUB_TOKEN=$(gh auth token)      # optional; without it numbers are not refreshed
.venv/bin/python scripts/discover.py      # add stubs for new extensions (reviewed: false)
.venv/bin/python scripts/fetch_github.py  # refresh stars / forks / last commit, merge renamed repos
.venv/bin/python scripts/validate.py      # schema check (also runs in CI)
.venv/bin/python -m pytest -q
.venv/bin/python scripts/build_site.py && (cd site && python3 -m http.server)
```

CI: `.github/workflows/ci.yml` runs validate + tests + build on every PR.

Env: `MIN_STARS` (default 50) = threshold for community entries found via GitHub topics.
