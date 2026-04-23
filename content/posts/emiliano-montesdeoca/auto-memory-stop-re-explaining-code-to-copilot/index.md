---
title: "68 Minutes a Day Re-Explaining Code to Copilot? There's a Fix for That"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot is real — your AI agent drifts after 30 turns, and you're paying the compaction tax every hour. auto-memory gives GitHub Copilot CLI surgical recall without burning thousands of tokens."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

You know that moment when your Copilot session hits `/compact` and the agent completely forgets what you were doing? You spend the next five minutes re-explaining the file structure, the failing test, the three approaches you already tried. Then it happens again. And again.

Desi Villanueva timed it: **68 minutes per day** — just on re-orientation. Not writing code. Not reviewing PRs. Just catching the AI up on things it already knew.

Turns out there's a concrete reason this happens, and a concrete fix.

## The Context Window Lie

Your agent ships with a big number on the box. 200K tokens. Sounds massive. In practice it's a ceiling, not a guarantee.

Here's the actual math:

- 200K total context
- Minus ~65K for MCP tools loaded at startup (~33%)
- Minus ~10K for instruction files like `AGENTS.md` or `copilot-instructions.md`

That leaves you with roughly **125K before you type a word**. And it gets worse — LLMs don't degrade gracefully as context fills up. They hit a wall at around 60% capacity. The model starts losing things mentioned 30 turns ago, contradicts earlier responses, hallucinates file names it stated confidently 10 minutes prior. The industry calls this the "lost in the middle" problem.

Effective limit: **45K tokens** before quality degrades. That's maybe 20-30 turns of active conversation before the agent starts drifting. Which is why you're hitting `/compact` every 45 minutes — not because you've filled 200K tokens, but because the model is already rotting at 120K.

## The Compaction Tax

Every `/compact` costs you flow state. You're deep in a debugging session. Shared context built up over 30 minutes. The agent knows the file structure, the failing test, the hypothesis. Then the warning hits.

- Ignore it → agent gets progressively dumber, hallucinates old state
- Run `/compact` → agent has a 2-paragraph summary of a 30-minute investigation

Either way you lose. Either way you're narrating your own project back to it like a new hire on day one.

The cruel part? **The memory already exists.** Copilot CLI writes every session to a local SQLite database at `~/.copilot/session-store.db` — every file touched, every turn, every checkpoint. It's all sitting on disk. The agent just can't read it.

## auto-memory: A Recall Layer, Not a Memory System

That's the key insight behind [auto-memory](https://github.com/dezgit2025/auto-memory): don't build a new memory system — build a read-only query layer over the one that already exists.

```bash
pip install auto-memory
```

~1,900 lines of Python. Zero dependencies. Installs in 30 seconds.

Instead of flooding the context with grep results, you give the agent surgical access to what actually matters:

| Operation | Tokens | What you get |
|-----------|--------|--------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 results, most irrelevant |
| `find . -name "*.py"` | ~2,000 | Every Python file, no context |
| Agent re-orientation | ~2,000 | You explaining what it should know |
| **`auto-memory files --json --limit 10`** | **~50** | **The 10 files you touched yesterday** |

That's a 200x improvement. The agent skips the archaeological dig and goes straight to what matters.

The recommended flow: when you're approaching 50-70% context usage, run `/clear` and then prompt with "review last sessions we discussed topic X". Instead of burning 12K tokens on blind searches, auto-memory pulls the relevant context in 50.

## Why This Matters for .NET Developers

If you're using GitHub Copilot CLI for .NET work — scaffolding services, debugging EF Core queries, iterating on Blazor components — the context rot problem hits just as hard. Complex solutions with multiple projects, shared libraries, and deep call chains are exactly the kind of codebase where the agent loses track fastest.

The [install guide](https://github.com/dezgit2025/auto-memory/blob/main/deploy/install.md) walks through pointing Copilot CLI at it. It's a one-time setup.

Honestly? 68 minutes a day back in your pocket is not a minor quality-of-life tweak. That's almost 6 hours a week.

## Wrapping up

Context rot is a real architectural constraint, not a bug that will get patched. auto-memory works around it by giving your agent a cheap, precise recall mechanism instead of expensive, noisy re-exploration. If you're doing serious AI-assisted development with GitHub Copilot CLI, it's worth the 30-second install.

Check it out: [auto-memory on GitHub](https://github.com/dezgit2025/auto-memory). Original post by Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).
