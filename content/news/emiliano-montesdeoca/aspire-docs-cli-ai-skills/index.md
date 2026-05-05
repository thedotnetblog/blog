---
title: "Aspire 13.2 Ships a Docs CLI — and Your AI Agent Can Use It Too"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 adds aspire docs — a CLI for searching, browsing, and reading official documentation without leaving your terminal. It also works as a tool for AI agents. Here's why this matters."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

You know that moment when you're deep in an Aspire AppHost, wiring up integrations, and you need to check exactly which parameters the Redis integration expects? You alt-tab to your browser, hunt through aspire.dev, squint at the API docs, then come back to your editor. Context lost. Flow broken.

Aspire 13.2 just [shipped a fix for that](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). The `aspire docs` CLI lets you search, browse, and read official Aspire documentation directly from your terminal. And because it's backed by reusable services, AI agents and skills can use the same commands to look up docs instead of hallucinating APIs that don't exist.

## The problem this actually solves

David Pine nails it in the original post: AI agents were *terrible* at helping developers build Aspire apps. They'd recommend `dotnet run` instead of `aspire run`, reference learn.microsoft.com for docs that live on aspire.dev, suggest outdated NuGet packages, and — my personal favorite — hallucinate APIs that don't exist.

Why? Because Aspire was .NET-specific far longer than it's been polyglot, and LLMs are working off training data that predates the latest features. When you give an AI agent the ability to actually look up the current docs, it stops guessing and starts being useful.

## Three commands, zero browser tabs

The CLI is refreshingly simple:

### List all docs

```bash
aspire docs list
```

Returns every documentation page available on aspire.dev. Need machine-readable output? Add `--format Json`.

### Search for a topic

```bash
aspire docs search "redis"
```

Searches both titles and content with weighted relevance scoring. Same search engine that powers the documentation tooling internally. You get ranked results with titles, slugs, and relevance scores.

### Read a full page (or just one section)

```bash
aspire docs get redis-integration
```

Streams the full page as markdown to your terminal. Need just one section?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Surgical precision. No scrolling through 500 lines. Just the part you need.

## The AI agent angle

Here's where it gets interesting for us developers building with AI tooling. The same `aspire docs` commands work as tools for AI agents — through skills, MCP servers, or simple CLI wrappers.

Instead of your AI assistant making up Aspire APIs based on stale training data, it can call `aspire docs search "postgres"`, find the official integration docs, read the right page, and give you the documented approach. Real-time, current documentation — not what the model memorized six months ago.

The architecture behind this is intentional. The Aspire team built reusable services (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) rather than a one-off integration. That means the same search engine works for humans in the terminal, AI agents in your editor, and automation in your CI pipeline.

## Real-world scenarios

**Quick terminal lookups:** You're three files deep and need Redis config parameters. Two commands, ninety seconds, back to work:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**AI-assisted development:** Your VS Code skill wraps the CLI commands. You ask "Add a PostgreSQL database to my AppHost" and the agent looks up the real docs before answering. No hallucinations.

**CI/CD validation:** Your pipeline validates AppHost configurations against official documentation programmatically. `--format Json` output pipes cleanly to `jq` and other tools.

**Custom knowledge bases:** Building your own AI tooling? Pipe structured JSON output directly into your knowledge base:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

No web scraping. No API keys. Same structured data the docs tooling uses internally.

## The documentation is always live

This is the part I appreciate most. The CLI doesn't download a snapshot — it queries aspire.dev with ETag-based caching. The moment the docs update, your CLI and any skill built on top of it reflects that. No stale copies, no "but the wiki said..." moments.

## Wrapping up

`aspire docs` is one of those small features that solves a real problem cleanly. Humans get terminal-native documentation access. AI agents get a way to stop guessing and start referencing actual docs. And it's all backed by the same source of truth.

If you're building with .NET Aspire and haven't tried the CLI yet, run `aspire docs search "your-topic-here"` and see how it feels. Then consider wrapping those commands into whatever AI skill or automation setup you're using — your agents will thank you.

Check out [David Pine's deep dive](https://davidpine.dev/posts/aspire-docs-mcp-tools/) on how the docs tooling came together, and the [official CLI reference](https://aspire.dev/reference/cli/commands/aspire-docs/) for all the details.
