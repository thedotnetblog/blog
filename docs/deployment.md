# Deployment

The `hugo --gc --minify` command generates a static site in `public/`. Deploy that directory to any static host.

---

## GitHub Pages (current setup)

The repository includes a ready-made workflow at `.github/workflows/github-pages.yml` that builds and deploys the site automatically on every push to `main`.

**One-time setup in your GitHub repository:**

1. Go to **Settings → Pages**
2. Under **Source**, select **GitHub Actions**
3. Push to `main` — the workflow handles the rest

The workflow uses Hugo `0.159.0` extended and uploads the built `public/` directory as a Pages artifact.

```yaml
# .github/workflows/github-pages.yml (summary)
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    steps:
      - uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: "0.159.0"
          extended: true
      - run: hugo --gc --minify --baseURL "${{ steps.pages.outputs.base_url }}/"
      - uses: actions/upload-pages-artifact@v3

  deploy:
    needs: build
    steps:
      - uses: actions/deploy-pages@v4
```

---

## Netlify

Create `netlify.toml` in the project root:

```toml
[build]
  command = "hugo --gc --minify"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.159.0"
```

---

## Azure Static Web Apps

```yaml
- task: HugoTask@1
  inputs:
    hugoVersion: "0.159.0"
    extendedVersion: true
    args: "--gc --minify"
```

---

## Vercel

Create `vercel.json`:

```json
{
  "build": {
    "env": {
      "HUGO_VERSION": "0.159.0"
    }
  }
}
```

Set the framework preset to **Hugo** in Vercel's project settings.

---

## Manual / Any Static Host

```bash
hugo --gc --minify
# Upload the contents of public/ to your web server
```
