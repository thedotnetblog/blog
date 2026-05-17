# Deployment

The `hugo --gc --minify` command generates a static site in `public/`. The site is built by GitHub Actions and published to the `public` branch.

---

## How it works

A workflow at `.github/workflows/deploy.yml` runs on every pull request targeting `main`, on every push to `main`, on a daily schedule (`0 2 * * *` UTC), and when manually dispatched. It always builds Hugo, and only deploys to `public` for non-PR runs.

```yaml
# .github/workflows/deploy.yml (summary)
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
  schedule:
    - cron: "0 2 * * *"
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
        if: github.event_name != 'pull_request'
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
