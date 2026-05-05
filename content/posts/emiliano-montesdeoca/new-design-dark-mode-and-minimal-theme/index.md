---
title: "New Design: Dark Mode and a Minimal Theme"
date: 2025-06-20
author: "Emiliano Montesdeoca"
description: "The .NET Blog got a full visual refresh — a custom minimal dark theme built from scratch. Here's what changed and why."
tags:
  - meta
  - blog
  - design
---

The blog has a new look.

I spent a few weeks redesigning The .NET Blog from the ground up with a custom Hugo theme I'm calling `dotnet-minimal`. It's dark by default, fast to load, and designed to keep the focus on the writing.

## What changed

**Dark mode as the default.** Not as an option, not as a toggle you have to find — dark by default, with a light mode toggle in the header for those who prefer it. Most developers I know have their editor in dark mode, their terminal in dark mode, their OS in dark mode. The blog should match.

**Typography first.** The previous design had too much visual noise. The new one strips everything back to the content: a clear reading width, generous line height, and a font stack that respects the system.

**Code blocks.** Syntax highlighting uses the Nord theme, which pairs well with the dark background. Line numbers are off by default — they add visual weight without much value for most posts.

**Performance.** No JavaScript frameworks, no CSS-in-JS, no npm install required to edit the theme. The entire CSS is a single file. Page load times are in the sub-100ms range on the CDN.

## What stayed the same

The content structure didn't change. Posts still live in Markdown files organised by author. The Hugo build pipeline is identical. If you were a contributor before, nothing in your workflow changed.

## The typewriter effect

The one bit of JavaScript on the home page is a small typewriter animation in the hero. It cycles through phrases like "share what they build." and "build cloud-native apps." It's purely cosmetic and degrades gracefully if JS is disabled.

## Open source

The theme is part of the [blog repository](https://github.com/thedotnetblog/blog) and is available under the MIT license. If you want to use it as a base for your own Hugo blog, go ahead.
