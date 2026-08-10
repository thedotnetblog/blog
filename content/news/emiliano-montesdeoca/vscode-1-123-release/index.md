---
title: "Visual Studio Code 1.123: Smoother Handoffs for Agent-Assisted Development"
description: "VS Code 1.123 improves agent handoffs, browser context, prompt commands, terminal batching, and session feedback across the development loop."
date: 2026-10-16
author: "Emiliano Montesdeoca"
tags: ["Visual Studio Code", "Copilot", "Agents", "Release", ".NET Development"]
slug: vscode-1-123-release
---

Original source: [Visual Studio Code 1.123](https://code.visualstudio.com/updates/v1_123)

The May 2026 updates in VS Code 1.123 are mostly refinements, which is exactly why they are worth noticing. Once agent-assisted development becomes part of a daily workflow, small interruptions accumulate: a conversation needs a different surface, a browser bug is hard to describe, parallel commands produce too many turns, and feedback gets buried in one long session.

This release smooths those transitions. It does not reinvent the .NET development loop, but it makes the agent's context and the developer's interventions easier to carry from one step to the next.

## Hand Off a Conversation Without Starting Again

You can now hand off a chat session from VS Code to the standalone Agents window and continue the same conversation there. That is a small feature with a useful implication: the right surface can change as the task changes without throwing away the context already gathered.

A .NET developer might begin with a quick question beside an open controller or project file, then move to the Agents window when the task becomes a longer debugging or refactoring session. The handoff avoids copying the prompt, re-explaining the repository, or pretending that the first session did not happen.

The handoff is not a substitute for a durable task description. For work that spans days, keep acceptance criteria and architectural decisions in the repository. The session should carry working context; source control should carry the decisions the team must be able to review.

## Browser Screenshots Add Precise Visual Context

In the integrated browser, you can select a region of a page and add that area screenshot as chat context. This is useful when the problem is visible but difficult to explain: a layout shift, a missing control, a validation message, or a rendered component that does not match the intended design.

For ASP.NET Core and Blazor developers, the feature shortens the path from observation to diagnosis. Capture the relevant region, attach it to the request, and describe the behavior you expected. The assistant receives the same visual evidence you are looking at instead of a long description assembled from memory.

A screenshot still represents one state. It does not prove that the page is accessible, that the underlying API is authorized correctly, or that the issue reproduces across viewports. Use it alongside browser tests and normal application diagnostics. Do not include customer data or secrets in the captured region.

## Fewer Command Turns, Less Agent Noise

When agent mode runs multiple terminal commands in parallel, completion notifications are now batched into one message instead of creating a separate agent turn for every command. That is a quality-of-life improvement for workflows that run tests, builds, or infrastructure checks concurrently.

The benefit is not merely a cleaner transcript. A single batch summary makes it easier to compare successes and failures and reduces the chance that an important error is lost between repetitive status messages. For a .NET solution, this could make parallel project tests or a Bicep validation-and-build sequence easier to supervise.

The trade-off is that a batch summary can hide detail if the agent does not report each command clearly. Keep commands independently reproducible, and ask for the failing command and its output when a batch is not green. Less noise should not mean less evidence.

## Small Command and Session Improvements

Prompt file subcommands can now use a space instead of a colon, such as `/chronicle tips` instead of `/chronicle:tips`. The change is small, but consistent command syntax matters when a team creates custom prompts or teaches a workflow to new developers.

The Agents window now uses a grid layout for sessions, agent feedback supports threaded replies, and steering messages appear as their own user turn instead of being folded into the in-flight turn. These details make a busy agent workspace easier to scan and make interventions more explicit.

The explicit steering turn is particularly useful when reviewing a session after the fact. You can distinguish what the agent planned from what the developer asked it to do next. That improves debugging and makes a correction part of the visible history rather than an invisible change in direction.

The release also updates Electron to 42, including Chromium 148 and Node.js 22.x, gives browser settings their own Settings section, and puts the AI Customization management editor in a compact header mode. These are infrastructure and UI changes, but they may matter to teams that package VS Code in a controlled developer environment.

## Fixes That Matter in Real Repositories

The release fixes BYOK reasoning models from OpenRouter, DeepSeek, and similar providers failing with HTTP 400 errors after tool calls. It also fixes `/doc` placing Python docstrings before decorators instead of inside function bodies, and resolves Windows CLI flag failures involving `--folder-uri` and `--file-uri` when combined with other arguments or `--wait`.

These are the kind of fixes that only become visible when the editor is used as a platform. A .NET team using a non-default model provider, automating VS Code startup, or generating documentation across mixed-language repositories should include these paths in its smoke checks.

## What .NET Developers Should Try

1. Start a focused chat in the editor and hand it off when the work becomes a longer agent session.
2. Use area screenshots for local UI diagnosis, with sanitized test data.
3. Run parallel builds or tests and inspect the batched result for the first failure.
4. Update custom prompt documentation to use the space-based command syntax where appropriate.
5. Verify the Windows CLI flags and BYOK provider paths that your developer tooling depends on.

VS Code 1.123 is a polish release, but polish is infrastructure when developers spend hours inside the same loop. Better handoffs, better context, and less status noise make the agent easier to supervise without making the developer's workflow feel like a collection of disconnected tools.