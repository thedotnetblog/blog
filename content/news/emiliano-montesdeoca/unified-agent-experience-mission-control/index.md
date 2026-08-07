---
title: "Mission Control for Coding Agents: A Unified Experience in VS Code"
description: "VS Code brings local, cloud, CLI, and third-party coding agents into Agent Sessions so developers can track, interrupt, and coordinate autonomous work."
date: 2026-08-17
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

Original source: [A Unified Experience for all Coding Agents](https://code.visualstudio.com/blogs/2025/11/03/unified-agent-experience)

# Mission Control for Coding Agents: A Unified Experience in VS Code

A single coding assistant is easy to understand. Several agents working in different places are not.

One agent runs locally in VS Code. Another works on a GitHub issue in the cloud. A CLI agent lives in the terminal. A third-party coding agent may have a different session model and different limits. Without a shared view, developers spend more time tracking work than supervising it.

VS Code's unified agent experience addresses that coordination problem with Agent Sessions: one place to launch agents, see their status, open their conversations, and intervene when the plan changes.

This is less about adding another agent and more about making multiple agents manageable.

## One View for Different Kinds of Work

The source article describes four distinct participants: local GitHub Copilot, Copilot Coding Agent in the cloud, GitHub Copilot CLI, and OpenAI Codex for eligible Copilot subscribers.

They have different strengths:

- A local agent can inspect the current workspace and make quick changes.
- A cloud coding agent can work asynchronously on an issue and open a pull request.
- A CLI agent fits terminal-heavy workflows and operational commands.
- Another provider can offer a different model or reasoning style.

Agent Sessions gives those tasks a common home. You can see what is running, what it is doing, and where to pick up the conversation.

That visibility is important because autonomous work does not remove coordination. It makes coordination a first-class engineering task.

## Interruptions Are Part of the Workflow

The source makes a simple observation: "It's common to send a prompt and realize you forgot something important." Previously, the choice was often to wait or cancel. With chat editors, you can open an active session and add information while the agent is working.

That is closer to real collaboration. Requirements change. A test reveals an assumption. A reviewer notices that an API must remain backward compatible. The useful agent is not the one that never needs correction; it is the one that can absorb correction without losing the whole task.

For .NET work, an interruption might be as simple as:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

The instruction is short because the repository already carries the larger context. The session is the place to correct direction, not to restate the entire system.

## Custom Agents Turn Team Habits Into Roles

VS Code also introduces specialized agents such as Plan. Instead of implementing immediately, a planning agent asks questions about scope, components, libraries, and constraints before producing an implementation specification.

That pattern is useful beyond a built-in agent. A team can define focused roles:

- **Research** gathers evidence and writes a short decision record.
- **Review** checks a change against repository conventions.
- **Testing** identifies missing cases and proposes a test plan.
- **Architecture** compares options without modifying files.

A small custom agent definition might look like this:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

The useful part is not the YAML. It is the explicit separation of responsibilities. A planning agent should not quietly edit production code. A review agent should not rewrite the design it is supposed to evaluate.

## Subagents Reduce Context Collisions

Long conversations accumulate unrelated context. Subagents provide an isolated workspace for a bounded research task, then return the result to the main session.

That is a good fit for questions such as:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

The main agent stays focused on implementation while the research agent handles a narrower question. The same principle applies to teams: clear delegation produces better results than launching several agents with overlapping authority.

## The Caveat: More Agents Mean More Coordination

Agent Sessions can show activity, but it cannot solve conflicting ownership. Two agents editing the same area can still create a merge problem. A cloud agent and a local agent can make incompatible assumptions. A custom agent can produce a recommendation that another agent ignores.

Set boundaries:

1. One agent owns implementation for a given branch.
2. Research agents return artifacts, not untracked edits.
3. Pull requests remain the review boundary.
4. Agent names and prompts state what they may change.
5. Session output is retained when it explains an important decision.

## My Take

The multi-agent future is not a queue of chat windows. It is a small team with roles, handoffs, and accountability.

Agent Sessions is valuable because it acknowledges that reality. It gives developers a control surface for work that is already happening across the editor, terminal, and cloud. The next productivity gain will come less from having more agents and more from making their boundaries legible.

For a .NET team, I would start with one planning agent and one implementation agent. Use the planning output as the issue or pull request specification, then let the implementation agent work inside that boundary. Measure rework before adding more roles.

The best mission control is still the one that makes ownership obvious.