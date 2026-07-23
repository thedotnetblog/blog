---
title: "VS Code 1.128 Makes a Clear Bet: The Agents Window Is Becoming the New Work Surface"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 turns agent workflows from novelty into daily ergonomics with multi-chat sessions, GA vision support, and deeper host/session controls."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 is a meaningful release not because of one killer feature, but because several changes align around a single direction: agent-first development inside the editor is becoming structured, parallel, and operationally manageable.

Original source: https://code.visualstudio.com/updates/v1_128

The standout is **richer multi-chat behavior** in agent host sessions, including peer chats, forks, and concurrent turns under one parent session. This is exactly what experienced developers need when exploring alternative implementations or splitting tasks across verification paths. It mirrors real engineering work, which is rarely linear.

My take: this is the first VS Code release where the Agents window feels less like a chat panel and more like a workspace orchestration surface.

Quick chats without a selected workspace also matter more than they appear. They lower friction for conceptual or architectural questions while keeping project-bound sessions distinct. That separation can reduce clutter and preserve context integrity for code-modifying workflows.

**Copilot Vision reaching GA** is another inflection point. Once images and PDFs are normal inputs to chat, documentation-heavy and UI-heavy tasks become significantly more fluid. Teams should now think of multimodal context as default capability, not an advanced add-on.

There are practical platform implications too. **BYOK support** in agent host scenarios, configurable model sampling parameters, and utility model defaults indicate growing maturity for enterprise model governance. Organizations with strict provider requirements can now shape behavior with finer control instead of one-size-fits-all defaults.

### Recommendations for teams adopting 1.128

- **Define conventions for chat branching and naming** in multi-chat sessions so parallel exploration does not become conversational noise.
- **Encourage developers to keep one chat for implementation** and one for tests or failure analysis.
- **Use quick chats intentionally** for non-repo questions.
- **If you run BYOK endpoints**, establish baseline temperature/top_p profiles per workload class and document exceptions.
- **Decide whether utility flows** should run on Copilot-provided or BYOK models to avoid accidental silent behavior gaps.
- **Consider OS-level shortcuts strategically.** Being able to trigger VS Code commands system-wide can improve flow for power users, but unmanaged keybinding sprawl can hurt consistency across teams.

## The bottom line

VS Code 1.128 does not just add features. It tightens the mechanics of agent collaboration in real development loops. The editors that win in the next cycle will be the ones that treat agent interactions as **first-class workflow primitives**, not sidebar experiments. This release shows VS Code understands that race.
