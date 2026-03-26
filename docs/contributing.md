# Contributing

Contributions are welcome — new posts, author profiles, event entries, bug fixes, or theme improvements.

---

## Adding Content

1. **Fork** the repository and clone your fork
2. **Create a branch:**
   ```bash
   git checkout -b my-new-post
   ```
3. **Create your content** using Hugo's archetypes (see [Content Guide](content-guide.md)):
   ```bash
   hugo new posts/my-post.md
   ```
4. **Preview locally:**
   ```bash
   hugo server -D -F
   ```
5. **Commit and push:**
   ```bash
   git add .
   git commit -m "feat(posts): add my post title"
   git push origin my-new-post
   ```
6. **Open a Pull Request** against `main`

---

## Content Guidelines

- Write in clear, accessible English
- Use fenced code blocks with a language identifier (e.g., ` ```csharp `)
- Keep `description` under 200 characters
- Tag posts with relevant terms — check existing tags at `/tags`
- Test locally before submitting (`hugo --gc --minify` must succeed with no errors)

---

## Theme Changes

If you're modifying the theme:

- CSS lives in `themes/dotnet-minimal/static/css/style.css`
- Templates live in `themes/dotnet-minimal/layouts/`
- Test on both desktop and mobile viewport sizes
- Confirm the site builds cleanly: `hugo --gc --minify`
