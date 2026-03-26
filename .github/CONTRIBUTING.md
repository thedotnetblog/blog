# Contributing to The .NET Blog

Thanks for your interest in contributing.

## Getting Started

1. Fork the repository.
2. Create a branch from `main`.
3. Run the site locally:

```bash
hugo server
```

4. Make your changes.
5. Verify the production build:

```bash
hugo --gc --minify
```

6. Open a pull request.

## Content Guidelines

- Keep posts practical and useful for .NET developers.
- Add clear titles, descriptions, and relevant tags.
- Use code blocks with language hints (for example: `csharp`, `bash`, `json`).
- Link to official sources when referencing announcements or docs.

## Post Front Matter

Use this minimum front matter for posts in `content/posts/`:

```yaml
---
title: "Your title"
date: YYYY-MM-DD
author: "Your Name"
description: "Short summary"
tags:
  - dotnet
---
```

## Pull Request Checklist

- I ran `hugo --gc --minify` locally.
- I verified formatting and links.
- I kept changes focused and minimal.
- I updated docs if needed.

## Reporting Issues

Use the issue templates for bugs and feature requests.

Be respectful and constructive in all interactions.
