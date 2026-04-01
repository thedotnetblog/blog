---
title: "Bookmark Studio Brings Slot-Based Navigation and Sharing to Visual Studio Bookmarks"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Mads Kristensen's new Bookmark Studio extension adds keyboard-driven slot navigation, a bookmark manager, colors, labels, and export/share capabilities to Visual Studio bookmarks."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

Bookmarks in Visual Studio have always been... fine. You set one, you navigate to the next, you forget which bookmark is which. They work, but they've never been the kind of feature you'd call powerful.

Mads Kristensen just [released Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), an experimental extension that fills in exactly the gaps you've probably run into if you use bookmarks regularly.

## Slot-based navigation

The core addition: bookmarks can now be assigned to slots 1–9 and jumped to directly with `Alt+Shift+1` through `Alt+Shift+9`. New bookmarks automatically get the next available slot, so in most cases, fast navigation works without any setup.

This sounds simple, but it changes bookmarks from "I have some bookmarks somewhere" to "Slot 3 is my API controller, Slot 5 is the service layer, Slot 7 is the test." That kind of spatial memory makes navigation nearly instant during focused work sessions.

## The Bookmark Manager

A new tool window shows all your bookmarks in one place with filtering by name, file, location, color, or slot. Double-click or keyboard-navigate to jump to any bookmark.

If you've ever had more than five or six bookmarks and lost track of which was which, this alone is worth installing the extension.

## Organization with labels, colors, and folders

Bookmarks can optionally have labels, colors, and be grouped into folders. None of it is required — your current bookmark workflow keeps working. But when you're debugging a complex issue or exploring an unfamiliar codebase, being able to color-code and label your bookmarks adds useful context.

All metadata is stored per solution, so your bookmark organization persists across sessions.

## Export and share

This is the feature I didn't know I wanted. Bookmark Studio lets you export bookmarks as plain text, Markdown, or CSV. That means you can:

- Include bookmark paths in pull request descriptions
- Share investigation breadcrumbs with teammates
- Move bookmark sets between repos or branches

Bookmarks stop being a solo navigation tool and start being a way to communicate "here's the path through this code."

## Bookmarks that track code movement

Bookmark Studio tracks bookmarks relative to the text they're anchored to, so they don't drift to wrong lines as you edit. If you've ever set bookmarks during a debugging session and had them all point to the wrong lines after a refactor — this fixes that.

## Wrapping up

Bookmark Studio doesn't reinvent anything. It takes a feature that's been "good enough" for years and makes it genuinely useful for focused development. Slot navigation, the Bookmark Manager, and export capabilities are the highlights.

Grab it from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio) and give it a try.
