# Setup (GitHub Pages)

1. Create a GitHub repo (e.g. `awesome-keycloak-spi`) and push this directory to `main`.
2. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
3. Actions → "Update data & deploy Pages" → **Run workflow** (first run fills stars/forks/contributors/last commit and discovers the full official list).
4. Site: `https://<owner>.github.io/<repo>/`. After that it refreshes every Monday.

Local: `pip install pyyaml && GITHUB_TOKEN=... python scripts/discover.py && python scripts/fetch_github.py && python scripts/build_site.py && cd site && python -m http.server`
Env: `MIN_STARS` (default 50) = threshold for community entries found via GitHub topics.
