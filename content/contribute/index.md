---
title: "Write for The .NET Blog"
description: "Share your knowledge with the .NET community. Learn how to join as an author and submit your first post."
---

The .NET Blog is a community-driven publication where developers share insights, tutorials, and stories about .NET, Azure, AI, and cloud-native development. **We welcome contributions from developers of all levels** — whether you're writing your first technical post or you're a seasoned speaker.

The blog has three content sections:

| Section | URL | What belongs here |
|---------|-----|-------------------|
| **News** | `/news/` | Tech news, community updates, release summaries |
| **Tutorials** | `/tutorials/` | Step-by-step how-to guides with code examples |
| **Posts** | `/posts/` | Meta-blog: about this publication and its history |

## How to Join

Everything lives on GitHub and follows a pull-request workflow. Here's how to get started:

### 1. Fork the Repository

Head to [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) and fork it to your GitHub account.

### 2. Create Your Author Profile

If this is your first contribution, add yourself as an author by creating a folder at `content/authors/your-username/` with an `index.md` file:

```yaml
---
title: "Your Name"
id: "your-username"
role: "Your role or title"
bio: "A short bio about yourself."
avatar: "/img/authors/your-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/your-username"
  - platform: "Twitter"
    url: "https://x.com/your-username"
---
```

Add your avatar image (square, at least 200×200px) to `static/img/authors/`.

### 3. Write Your Content

Pick the right section and create a leaf bundle under your author folder:

**News post** — use for tech news, release summaries, community updates:
```bash
mkdir -p content/news/your-username/your-post-slug
```

**Tutorial** — use for step-by-step guides with code examples:
```bash
mkdir -p content/tutorials/your-username/your-tutorial-slug
```

Add an `index.md` inside the folder:

```yaml
---
title: "Your Post Title"
date: 2025-01-01
author: "Your Name"
description: "A one-sentence description of your post."
tags: ["dotnet", "azure"]
---

Your post content in Markdown...
```

### 4. Open a Pull Request

Push your changes to your fork and open a pull request against the `main` branch. Our team will review it and provide feedback within a few days.

## What We're Looking For

- **News** — timely summaries of .NET ecosystem news and releases
- **Tutorials** — step-by-step guides on .NET, Azure, AI, Blazor, Aspire, and more
- **Deep dives** — in-depth explorations of a technology, pattern, or architecture
- **Community stories** — your experience building with .NET in production

## Guidelines

- Content should be technical and relevant to the .NET ecosystem
- Code examples must be accurate and tested against a real project
- Include a meaningful description and at least one relevant tag
- Posts are automatically translated into all supported languages

## Get in Touch

Open an issue on [GitHub](https://github.com/thedotnetblog/blog/issues) or reach out on [X / Twitter](https://x.com/thedotnetblog). We'd love to have you as part of the community!
