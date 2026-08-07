---
title: "Long-Distance Next Edit Suggestions Understand Refactoring Patterns"
description: "VS Code's next-edit suggestions can look farther across a file to predict related changes. Here is where the feature helps .NET refactors and where it stops."
date: 2026-08-22
author: "Emiliano Montesdeoca"
tags: [copilot, vscode, productivity]
slug: vscode-long-distance-next-edit-suggestions
---

Original source: [Building Long-Distance Next Edit Suggestions](https://code.visualstudio.com/blogs/2026/02/26/long-distance-nes)

## Refactoring Does Not Stay Near the Cursor

Next edit suggestions are useful when the next change is close to the current one. A field initialization, a related assignment, or a small follow-up edit can appear where the developer is already working.

Real refactoring is often less local. Rename a method and a call site farther down the same file needs attention. Change a parameter and a validation branch later in the file may no longer make sense. The developer has to scroll, find the related code, and wait for a new suggestion.

Long-distance next edit suggestions aim at that gap. The feature predicts where the next meaningful edit may occur within the file, rather than limiting the search to the immediate neighborhood. For .NET developers doing API renames, signature changes, or validation refactors, that can remove some tedious navigation.

## Separate Models for Location and Content

The engineering approach is notable because it separates two decisions. A location model predicts where the next edit belongs, while the existing next-edit model generates the edit itself.

That division reflects the actual problem. Finding the right location is a different skill from proposing a syntactically plausible change. A model trained to recognize the spatial pattern of a refactor can look for a distant caller, while the edit model can focus on the local code around that caller.

The training data also follows editing trajectories instead of treating every edit as an isolated event. That matters because developers usually make related changes in a sequence: rename a declaration, update a use, adjust a test, and then fix documentation or diagnostics. The sequence contains information about intent.

The system also needs to know when not to jump. A false distant suggestion is more disruptive than a missed one. The source describes evaluation that measures both jump and no-jump behavior, along with tuning to reduce unnecessary jumps.

## Why This Is Useful in .NET

The feature is most promising for edits with a clear ripple pattern.

**Mass renames** are the obvious example. If a private helper or a method local is renamed, a distant use in the same file can be surfaced without a manual search.

**Signature changes** are another. When a method gains a parameter, related calls or validation logic may need a corresponding edit. A suggestion that points to the next affected location can shorten the loop between compiler feedback and code change.

**In-file structural refactors** also benefit. Moving a block, adjusting a type, or changing a repeated pattern often creates follow-up work below the current cursor.

The feature is not a replacement for the compiler, analyzers, or a deliberate search. Those tools remain authoritative for finding every reference, especially across a multi-project solution.

## The Trust Tradeoff

The source reports a lift in code written through next-edit suggestions, but it also notes that distant suggestions are rejected more often than standard suggestions. That is understandable. A distant suggestion asks the developer to trust a model's interpretation of a broader editing pattern.

A compact preview near the cursor is a sensible interaction. It gives enough context to decide whether the proposed jump is relevant without taking over the screen. For .NET refactors, inspect the surrounding method and run the compiler or tests before treating the suggestion as complete.

There are important boundaries. The feature works within a single file, so it does not solve a public type rename across a solution. It is also more reliable for straightforward patterns than for changes involving subtle validation, error handling, or cross-cutting behavior. A codebase with unusual conventions may not resemble the trajectories used for training.

## How to Use It Responsibly

Enable the extended-range setting for a refactor-heavy session and start with a change that is easy to verify. Rename a method in a test file, update a signature in one class, or revise a repeated validation pattern. Compare the suggestions with compiler errors, Find All References, and tests.

Do not accept a distant edit merely because it appears in a polished widget. Treat it as a proposed navigation shortcut. The quality bar is the same as for any generated code: the change must match the intended behavior and pass the repository's checks.

Long-distance next-edit suggestions are a focused improvement rather than a new programming model. For .NET teams that do frequent in-file refactoring, the saved scrolling and context recovery can compound. The feature earns trust when it helps developers reach the next correct edit while keeping the compiler and human review in charge.