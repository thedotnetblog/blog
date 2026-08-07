---
title: "AI Meets Remote Development: Context-Aware Agents in Any Environment"
description: "VS Code integrates AI seamlessly across remote SSH, dev containers, WSL, tunnels, and Codespaces. Custom instructions, chat participants, and auto-approvals transform how you work from anywhere."
date: 2026-08-11
author: Emiliano Montesdeoca
tags: [remote-development, AI, dev-containers, context, agent-mode, productivity]
slug: ai-and-remote-development-unified
---

Original source: [Enhance productivity with AI + Remote Dev](https://code.visualstudio.com/blogs/2025/05/27/ai-and-remote)

# AI Meets Remote Development: Context-Aware Agents in Any Environment

Remote development was already powerful in VS Code—SSH into a VM, work in a dev container, develop in WSL, tunnel to a remote machine, or use GitHub Codespaces. But those workflows were isolated from AI. You had to switch contexts mentally: AI in the editor, but your actual code living somewhere else.

That split is gone. VS Code's latest integration brings agent mode, chat, and AI completions to every remote environment. More importantly, it lets agents understand which environment they're in and tailor their behavior accordingly.

That's not just convenience. That's a fundamentally different approach to distributed development.

## The Five Remote Flavors, Now AI-Enabled

VS Code's remote development comes in five flavors:

- **Remote SSH** — Connect to any VM or machine via SSH
- **Dev Containers** — Work inside a containerized environment with preconfigured dependencies
- **WSL** — Linux-powered development on Windows
- **Remote Tunnels** — Access a machine via secure tunnel, no SSH config needed
- **GitHub Codespaces** — Managed cloud environments

Before this update, AI worked in all of them. But now, it works *with context*. GitHub Copilot automatically installs when you connect remotely. Better: custom instructions and chat participants now understand your remote setup.

## Custom Instructions: Teaching AI About Your Environment

Imagine you connect to a dev container for Python development. The container has Python 3, pip, and the Python language extensions installed. But the agent doesn't know that automatically.

With custom instructions, you can tell it:

```
This is a dev container that includes `python3` and `pip3` pre-installed
and available on the `PATH`, along with the Python language extensions
for Python development.
```

That one instruction changes everything. Now when you ask the agent to write Python code, it won't suggest installation steps you've already done. It won't guess at your project structure. It understands the environment.

Better yet: VS Code's dev container templates now include custom instructions by default. The Python template, the Node.js template—they all ship with environment context built in. Clone a repo with a dev container, open it in VS Code, and the agent knows exactly what toolchain is available.

From the blog: "We've made it so that custom instructions can merge successfully across images and Templates." That means custom instructions compose. Your base Python image has one set of instructions. Your project adds another. The agent gets the union of both.

## Chat Participants: Domain-Specific Helpers

Chat participants are AI helpers specialized in particular domains. Type `@` in the chat field and you see the available options—`@workspace`, `@vscode`, `@terminal`. Extensions can add their own.

The Remote SSH extension includes `@remote-ssh`. Ask it how to troubleshoot SSH connection failures. Ask how to configure key-based authentication. It's like having someone who knows your remote setup sitting next to you.

If an SSH connection fails, there's a **Diagnose with Copilot** button. The agent investigates and surfaces actionable insights right in the editor. No context switching. No searching the web. The agent is already in the right context.

## Auto-Approvals: Agent Autonomy, Safely

Agents are powerful because they can run terminal commands and tools—install dependencies, run tests, modify local configuration. But some commands are destructive. You might not want an agent deleting files on your local machine.

VS Code now supports `chat.tools.autoApprove`. When enabled, the agent doesn't pause for confirmation on tool calls. It just runs them.

Here's the key: you can scope this to dev containers or remote machines only. This gives you a security model where:

- **Local dev machine**: tools require explicit approval
- **Dev container**: tools auto-approve (it's ephemeral, less risk)
- **Remote VM**: depends on your risk tolerance

You get autonomy without exposing your local dev machine to potentially destructive commands.

```json
{
  "chat.tools.autoApprove": true
}
```

Treat that setting as an environment policy, not a productivity switch. A remote VM with production credentials is not automatically safe just because it is remote.

## Practical Pattern: Dev Container + Custom Instructions

Here's how it comes together:

1. Create a dev container from the **Dev Containers: Add Dev Container Configuration** command.
2. Select Python (or your language of choice).
3. Reopen the folder in the container.
4. Open chat and ask the agent to build something.
5. Check that the agent uses the installed toolchain and your repository instructions.

What used to require manual setup—"I'm working in a container, let me tell the agent about it"—now becomes part of the environment definition.

## The Caveat: Context Bleed Risk

Here's the edge case: the more context an agent has, the more it can hallucinate connections that don't exist.

An agent in your Python dev container might think there is a database available because a `.env` file contains a connection string. That database may not be running. The agent tries to use it and fails.

Custom instructions help—you can explicitly say "this container does NOT have access to the production database"—but they're not foolproof. Agents still need human review for risky operations.

## My Perspective: This Unlocks Asynchronous Teamwork

Remote development is already about working asynchronously across machines. AI makes it better because agents now understand the context of *where* they're working.

Pair this with GitHub's Copilot Coding Agent, which runs in the cloud, and you have a powerful model:

- **Local agents** handle quick tasks and understand your local dev container.
- **Remote agents** tackle complex features across your codebase.
- **Both speak the same language** because they can share workspace context and coding standards.

## What To Do Next

1. **Add custom instructions to your dev container templates.** If you maintain dev containers for your team, include environment-aware guidance.
2. **Test auto-approvals in an ephemeral container.** Do not begin with a remote machine that holds production credentials.
3. **Experiment with `@remote-ssh`.** Use it to troubleshoot your own setup, then consider what domain-specific participants would help your team.

Remote development plus AI is no longer AI in a desktop editor. It is a distributed workflow where context follows you everywhere you work.

That's the future. It's here.

Happy coding.