---
title: "Agent Skills in Visual Studio: Teach Copilot How Your Team Actually Works"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio now supports Agent Skills — reusable instruction sets that teach Copilot your team's specific workflows, coding standards, and conventions. Define once, apply automatically."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

One of the persistent frustrations with AI coding assistants: they know general programming well but don't know *your* team's specific conventions, your internal APIs, or your preferred patterns. Every session, you're re-explaining context. Agent Skills in Visual Studio is designed to fix this.

## What Agent Skills Are

Reusable instruction sets — defined in `SKILL.md` files — that teach Copilot agents how to handle specific tasks. Define a skill for "how to run our build pipeline," "how to generate boilerplate for our service layer," or "our code review checklist." The agent applies the skill automatically when it's relevant.

This isn't new as a concept (`.github/copilot-instructions.md` has existed for a while), but the Visual Studio integration makes them first-class objects with discovery UI.

## Creating Skills in Visual Studio

The integrated UI flow: click the tools icon in Copilot Chat, open the skills panel, click `+`. You choose global (personal) or solution-level scope, pick a name, and Visual Studio generates a template. Copilot Agent mode can then help you fill in the template — use the agent to write the skill for the agent.

Currently in Insiders channel, coming to Release soon.

You can also create skills manually:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Discovery Locations

Skills are auto-discovered from standard paths:

**Solution-level (shared via repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/personal (your user profile, available everywhere):** `~/.copilot/skills/`, `~/.agents/skills/`

The multi-location support means the same convention works with GitHub Copilot, Claude Code, and other agent frameworks — define your skills once, use them everywhere.

## The Format

Skills follow the [agentskills.io/specification](https://agentskills.io/specification) format — a Markdown-based spec that's both human-readable and machine-parseable. You can include scripts, templates, and examples alongside the `SKILL.md`.

## Practical Value

The real power isn't the individual features — it's the combination of team-shared skills (via `.github/skills/`) and personal skills (via `~/.agents/skills/`). Team skills encode how your organization does things. Personal skills encode how you specifically work. The agent gets both contexts automatically.

For organizations already using Copilot heavily, this is a meaningful step toward making the tool actually aware of your specific codebase conventions rather than giving generic advice.

Original post: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
