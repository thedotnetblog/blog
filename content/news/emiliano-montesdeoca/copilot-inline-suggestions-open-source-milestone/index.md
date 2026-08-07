---
title: "Inline Suggestions Go Open Source: Consolidating VS Code's AI Foundation"
description: "GitHub Copilot inline suggestions become open source as VS Code moves toward a unified extension. The interesting story is the performance work behind ghost text."
date: 2026-08-18
author: Emiliano Montesdeoca
tags: [open-source, VS Code, inline-suggestions, ghost-text, consolidation]
slug: copilot-inline-suggestions-open-source-milestone
---

Original source: [Open Source AI Editor: Second Milestone](https://code.visualstudio.com/blogs/2025/11/04/openSourceAIEditorSecondMilestone)

# Inline Suggestions Go Open Source: Consolidating VS Code's AI Foundation

GitHub Copilot Chat going open source was a major transparency milestone. The next step is more immediate for anyone who codes in VS Code: the inline suggestion pipeline is now open source too.

That ghost text appearing as you type is not a single model call. It is a carefully optimized loop involving reuse, caching, prompt construction, post-processing, and decisions about how much code to show. Making that implementation visible is useful for both developers and extension authors.

At the same time, VS Code is moving toward a unified Copilot Chat extension that handles chat, agents, and inline suggestions together.

## One Extension, One Coordination Point

The old split was familiar:

- The GitHub Copilot extension provided ghost text.
- The GitHub Copilot Chat extension provided chat, agent mode, and next-edit suggestions.

The source says the team is "working towards providing all Copilot functionality in a single VS Code extension: Copilot Chat."

That consolidation should reduce duplicated work and make it easier for chat and inline suggestions to share context. It also simplifies deployment for organizations managing editor extensions.

There is a trade-off, though. Separate extensions offered a clear switch: keep chat and disable inline suggestions, or the other way around. A unified extension moves that control to feature settings instead of extension installation.

## Ghost Text Is a Latency Problem

The newly open implementation makes the performance strategy easier to understand. A suggestion request starts with reuse, not inference:

1. Check whether the developer is accepting an existing suggestion.
2. Look for a relevant cached suggestion.
3. Reuse an in-flight request from a nearby keystroke.
4. Construct a new prompt only when the earlier work is no longer useful.
5. Post-process the model output and decide how much to display.

That order matters. A request on every keystroke would be expensive and slow. The editor has to treat typing as a stream of related events, not thousands of isolated prompts.

The conceptual loop looks like this:

```text
keystroke
  -> accepting existing suggestion? reuse it
  -> relevant cache? show it
  -> request still running? reuse it
  -> otherwise build context and call the model
  -> normalize indentation and syntax
  -> choose single-line or multi-line output
```

For .NET developers, the language-specific context is only one part of the problem. The extension also has to decide which open files, workspace details, and surrounding code are relevant enough to send.

## Open Source Makes the Heuristics Observable

The real value is not that everyone needs to modify ghost text. It is that the behavior can be inspected.

Researchers can study typing-as-suggested detection. Extension authors can understand how context is assembled. Security reviewers can investigate what data leaves the editor. Teams can reason about why a suggestion was fast in one situation and slow in another.

That visibility also improves conversations about AI quality. "The suggestions feel slow" becomes a question about cache hits, request reuse, model latency, or post-processing instead of a vague complaint about the model.

## The Caveat: Consolidation Reduces a Control Boundary

A single extension is simpler to install and maintain, but it can be harder to customize. If your organization wants chat while disabling inline suggestions, check the feature-level settings and policies rather than assuming the old extension split still applies.

Also remember that an open implementation does not make model output deterministic. The pipeline can be transparent while the model remains probabilistic. Tests and review still matter.

## Why This Matters to .NET Teams

Most .NET teams already manage an editor baseline, analyzers, SDK versions, and repository instructions. A unified AI extension fits that model better than a collection of loosely coordinated add-ons.

It also makes a useful operational question possible: where should AI suggestions help, and where should they stay quiet? A team can keep inline suggestions enabled for routine boilerplate while using chat or an agent for deliberate changes that require tests and review.

Open source helps the platform team understand the defaults before writing that policy.

## My Take

The headline is open source, but the engineering story is consolidation and latency management. Good AI assistance is not just a bigger model. It is a fast, stateful client that knows when not to call the model.

That is a lesson worth carrying into our own .NET tools. Cache what is safe to reuse. Keep context bounded. Make the expensive path observable. Treat the model call as one stage in a workflow, not the whole workflow.

For now, update the unified extension in a test group, watch for regressions in latency and suggestion quality, and read the implementation when you need to understand what the editor is doing. Transparency is most useful when it changes how we operate the tool.