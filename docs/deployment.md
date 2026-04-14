# Deployment

The `hugo --gc --minify` command generates a static site in `public/`. Deploy that directory to any static host.

---

## Static branch deploy (current setup)

The repository includes a workflow at `.github/workflows/github-pages.yml` that builds Hugo on every push to `main` and force-pushes the static output to the `public` branch. This makes it easy to serve from any platform that can pull a branch (e.g. Dokploy, Coolify, or a plain Nginx container).

```yaml
# .github/workflows/github-pages.yml (summary)
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-and-deploy:
    steps:
      - uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: "0.159.0"
          extended: true
      - run: hugo --gc --minify
      - uses: peaceiris/actions-gh-pages@v4
        with:
          publish_dir: ./public
          publish_branch: public
          force_orphan: true
```

### Dokploy

1. Create a new **Application** and connect the GitHub repository
2. Set the **Branch** to `public`
3. Set **Build Type** to **Static** (Nixpacks will detect it automatically)
4. Set the **Publish Directory** to `/` (the branch root already contains the built site)
5. Add your domain and deploy

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
