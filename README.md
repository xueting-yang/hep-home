# Xueting's HEP HOME

A personal academic homepage and knowledge base, focused on High Energy Physics research and web development learning.

## Features

- **HEP-EX Daily Pick** — Automatically fetches and displays a random recent paper from [arXiv hep-ex](https://arxiv.org/list/hep-ex/recent) via the free arXiv API
- **Projects & Assignments** — Dynamically loaded from `data/projects.json`
- **Offline fallback** — Papers served from local cache when API is unavailable
- **Responsive** — Works on mobile and desktop
- **Zero backend** — Pure static site, deploys to GitHub Pages for free

## Tech Stack

Plain HTML + CSS + JavaScript (vanilla). No framework, no build step, no dependencies.

## Project Structure

```
/
├── index.html          # Main page
├── style.css           # Styles
├── app.js              # Logic (arXiv fetcher, dynamic content)
├── data/
│   ├── projects.json   # Projects/assignments data
│   └── papers.json    # Fallback paper data
├── .nojekyll           # Required for GitHub Pages
└── README.md
```

## Local Development

Since the site fetches data via `fetch()`, you need to serve it over HTTP (not `file://`).

```bash
# Python 3
python3 -m http.server 8000

# Then open http://localhost:8000
```

## Deploying to GitHub Pages

1. Push this repo to GitHub
2. Go to **Settings → Pages → Source → Deploy from a branch → main**
3. Your site will be live at `https://yourusername.github.io/repo-name/`

## Adding Content

### Projects

Edit `data/projects.json`:

```json
{
  "title": "New Project",
  "status": "done",
  "description": "...",
  "date": "2026年4月",
  "url": "https://...",
  "tags": ["Tag1", "Tag2"]
}
```

### Fallback Papers

Edit `data/papers.json` to update the offline paper cache. Fields: `title`, `authors`, `summary`, `published`, `arxivId`.

## License

MIT
