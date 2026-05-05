---
title: "We Added Multi-Language Support"
date: 2025-02-14
author: "Emiliano Montesdeoca"
description: "The .NET Blog now publishes every post in 17 languages using automated translation — and here's how we built it into the Hugo workflow."
tags:
  - meta
  - blog
  - i18n
---

As of today, every new post on The .NET Blog is automatically translated into 16 additional languages.

We support: English, Spanish, Catalan, German, French, Portuguese, Italian, Japanese, Chinese, Korean, Russian, Hindi, Polish, Turkish, Arabic, Indonesian, and Dutch.

## Why bother?

The .NET ecosystem is global. A large chunk of our readers are not native English speakers, and while most developers *can* read technical English, reading in your first language is faster and less fatiguing. If we want the blog to actually be useful to the wider .NET community, we had to solve this.

## How it works

Each post lives in a **leaf bundle** — a folder with an `index.md` and language-specific variants like `index.es.md`, `index.ja.md`, etc. Hugo's multilingual mode handles routing: `/posts/my-post/` serves English, `/es/posts/my-post/` serves Spanish, and so on.

Translation is handled as part of the content pipeline. When a new post is merged, a workflow generates the translated variants and commits them alongside the original.

## What we didn't want

We specifically didn't want a "translated version" to feel like a second-class page. Every translated page has the same layout, the same code examples, and the same SEO treatment as the English original.

The language switcher in the header lets readers jump between languages on any page — it links to the same content, not the home page.

## What's next?

Right-to-left layout support for Arabic is on the list. The CSS foundation is in place (`dir="rtl"` on the `<html>` element), but there are a few edge cases in the post layout to sort out first.
