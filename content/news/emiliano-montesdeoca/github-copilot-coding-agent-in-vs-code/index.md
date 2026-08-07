---
title: "Autonomous Development Within VS Code: GitHub Copilot Coding Agent Arrives"
description: "Assign GitHub issues to an autonomous agent. Track progress in VS Code. Review PRs, iterate, and close issues without leaving your editor. Multi-agent workflows are now practical."
date: 2026-08-14
author: Emiliano Montesdeoca
tags: [GitHub Copilot, coding-agent, automation, agent-mode, GitHub, productivity]
slug: github-copilot-coding-agent-in-vs-code
---

Original source: [Command GitHub's Coding Agent from VS Code](https://code.visualstudio.com/blogs/2025/07/17/copilot-coding-agent)

# Autonomous Development Within VS Code: GitHub Copilot Coding Agent Arrives

There's a difference between an AI that suggests code and an AI that completes tasks.

VS Code's agent mode was the former: chat with an AI, ask it to modify files, and approve tool calls. Powerful, but synchronous. You're still in the loop, making decisions.

GitHub's Copilot Coding Agent is different. You assign it an issue. It spins up a temporary development environment. It explores your codebase, makes changes, runs tests, and opens a pull request. Then it waits for your feedback.

And now, you can do all of that—assign, track, review, and iterate—without switching to GitHub.com. It's all in VS Code.

That's not just convenience. That's a different workflow.

## How Copilot Coding Agent Works

The flow is simple:

1. **Enable** the agent in GitHub settings.
2. **Assign an issue** to Copilot Coding Agent.
3. **Let it work** in a temporary, isolated development environment.
4. **Review the pull request** it opens.
5. **Ask for changes** or approve the result.
6. **Let the agent iterate** until the issue is resolved.

The key difference from local agent mode is that the agent runs remotely, in a temporary environment isolated from your machine. It can explore your codebase, install dependencies, build, run tests, and make changes without touching your local filesystem.

From the blog: "The agent runs within a temporary isolated dev environment that gets spun up where the agent can explore the codebase, make changes, build the code, run tests, etc. - a complete dev environment just for the agent."

That isolation is crucial for safety. The agent can be as destructive as it needs to be because the environment is disposable.

## VS Code Integration: Track and Control Everything

Copilot Coding Agent lived on GitHub.com. You assigned an issue, then switched to a browser to watch progress.

Now, the pull requests extension brings it into VS Code:

**Assign from the sidebar.** Select an issue in the pull request view and assign it to Copilot Coding Agent without leaving the editor.

**Track progress.** A new **Copilot on My Behalf** query shows agent sessions. Open a session to watch the play-by-play: commands, decisions, and progress.

**Terminate when needed.** If the agent goes off course, terminate the session from VS Code.

**Review and iterate.** When the agent opens a pull request, leave comments and request changes. The agent reads the feedback, updates the pull request, and tries again.

The workflow is familiar—review, request changes, iterate—but with an agent as the implementer.

## A Pull Request Is Still the Boundary

The example in the source article is useful because it shows where autonomy stops. The agent implements a Trending section, including UI and database changes, and opens a pull request. A reviewer notices that the database migration is not enough and the agent needs access to an external account.

That is the right place to pause. The pull request is the review boundary. Additional access should be granted deliberately through an MCP server, not by quietly adding credentials to the agent's environment.

For a .NET team, the same pattern might look like this:

```text
Issue: Add a paginated orders endpoint

Acceptance criteria:
- Use the existing application service pattern.
- Return ProblemDetails for validation errors.
- Add integration tests for page boundaries.
- Do not change the public database schema.
- Report the dotnet test command and result in the pull request.
```

Clear acceptance criteria give the agent a shape it can follow and give the reviewer something concrete to verify.

## MCP Expands the Agent's Reach

VS Code lets you configure MCP servers for the Copilot Coding Agent. That is powerful, but the security trade-off is direct: more tools mean more autonomy and more risk.

A conceptual configuration might look like this:

```yaml
# Example only: grant a narrowly scoped external capability
github:
  codingAgent:
    mcpServers:
      - supabase
        credentials: ${SUPABASE_API_KEY}
```

Use the smallest useful permission set. An agent that can inspect a deployment is not the same as one that can change production. Keep credentials scoped, short-lived, and observable.

## The Caveat: Agent Behavior Is Still Unpredictable

LLMs are stochastic. Sometimes the agent nails a complex feature. Sometimes it misses context and opens a pull request that needs significant rework.

For critical infrastructure changes, add another review layer. The agent is well suited to bounded work that follows existing patterns. Architectural decisions, security-sensitive changes, and changes that cross several systems deserve human ownership.

Good tests matter too. The agent runs tests and uses their results as feedback. Bad or missing tests mean more back-and-forth and weaker confidence.

## My Take: Issue Quality Becomes an Engineering Input

This workflow works best when the issue is clear. "Fix the dashboard" is a conversation starter, not an implementation specification. "Add a dark mode toggle to the settings panel, persist the preference, and cover it with a browser test" gives an agent something verifiable.

Teams adopting coding agents will improve when they invest in:

1. Clear issue acceptance criteria.
2. Test coverage that describes expected behavior.
3. Deliberate MCP access policies.
4. Review rules for agent-generated changes.
5. Metrics for rework and successful first passes.

This is not replacing developers. It is moving developer attention toward architecture, design, and review while an agent handles routine implementation.

## What To Do Next

1. Install or update the GitHub Pull Requests extension.
2. Enable Copilot Coding Agent in GitHub settings.
3. Create a small test issue with explicit acceptance criteria.
4. Assign it from VS Code and watch the session.
5. Review the pull request as carefully as any human-authored change.

For .NET teams, start with a bounded endpoint, a test addition, or a small refactoring that fits existing patterns. The autonomous developer is not here to replace your judgment. It is here to multiply the amount of work your judgment can supervise.

Use it deliberately.

Happy coding.