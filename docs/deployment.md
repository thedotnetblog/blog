# Deployment

The `hugo --gc --minify` command generates a static site in `public/`. The site is built by GitHub Actions and published to the `public` branch.

---

## How it works

A workflow at `.github/workflows/deploy.yml` runs on every push to `main`. It builds Hugo and force-pushes the static output to the `public` branch (orphan branch containing only the built site).

```yaml
# .github/workflows/deploy.yml (summary)
on:
  push:
    branches: [main]
  workflow_dispatch:

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

---

## Dokploy setup

1. Create a new **Application** and connect the GitHub repository
2. Set the **Branch** to `public`
3. Set **Build Type** to **Nixpacks** (it will detect static HTML automatically)
4. Set the **Publish Directory** to `/` (the branch root already contains the built site)
5. Add your domain and deploy
