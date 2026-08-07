---
title: "Run and Test AI Agents Locally with Azure Developer CLI"
description: "New azd AI agent commands shorten the inner loop by starting agents locally and invoking local or remote sessions from the terminal."
date: 2026-08-28
author: "Emiliano Montesdeoca"
tags: [azure, azd, ai-agents, local-development]
slug: azd-run-test-ai-agents-locally
---

# Run and Test AI Agents Locally with Azure Developer CLI

Original source: [Azure Developer CLI (azd): Run and test AI agents locally with azd](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-run-invoke/)

Agent development often has an unnecessarily slow inner loop: edit locally, deploy to a cloud endpoint, open a portal or client, send a message, then return to the editor to fix the next issue. The Azure Developer CLI's AI agent extension adds commands that bring more of that loop into the terminal.

`azd ai agent run` starts an agent locally, while `azd ai agent invoke` sends a message to a running agent. The result is not a replacement for deployed testing, but it is a better place to catch obvious behavior and integration problems before spending a deployment cycle.

## Run and Invoke Are Separate Responsibilities

The distinction between the commands is useful. `run` starts the local process and can detect the project setup described by the extension. `invoke` sends a message to an agent that is already running. By default, invocation can target a remote Foundry endpoint; the `--local` option selects the local process.

That explicit local/remote choice matters when both versions are available. A developer can run the local agent in one terminal, invoke it with test messages, and then deliberately compare the result with the deployed endpoint. Avoid relying on an implicit target when the behavior or data boundary matters.

The extension also supports selecting a named agent when a project contains more than one. Keep those names meaningful and make the expected entry point clear in project documentation.

## A Better Local Inner Loop

A practical loop looks like this:

1. Modify the agent implementation in the editor.
2. Start it with `azd ai agent run`.
3. Send a focused message with `azd ai agent invoke --local`.
4. Inspect logs and the response.
5. Change the implementation and repeat.

The source describes session and conversation identifiers that persist across invocations, which makes multi-turn checks possible. That is valuable when an agent must remember a previous turn, call a tool, and then explain the result.

For a .NET team, the surrounding application can run locally with `dotnet run` while the agent process is started separately. Use test data and an explicit local configuration. The goal is to exercise the code path, not accidentally connect a development session to a production resource.

## What This Means for .NET Projects

The extension's automatic project detection is centered on the supported agent workflows described by the source, including Python and Node.js setups. A C# agent or an ASP.NET integration may need additional project-specific setup for dependencies and entry points.

That is not a blocker, but it is a reason to inspect what the command actually detects. Make sure required NuGet packages are restored, the agent entry point is runnable without an IDE-only environment, and the local configuration has the same assumptions your test expects.

The local loop also creates a good place for repeatable conversation tests. Write down a few turns that cover the agent's main behavior: a normal request, a tool call, a validation failure, and a follow-up that depends on previous context. Replay those conversations after changing the agent rather than judging one successful response.

## Local Does Not Mean Risk-Free

A local process can still access network resources, environment variables, files, and credentials. Keep the permissions narrow and use a development identity. Do not copy production secrets into a local `.env` file just because the command makes testing convenient.

Conversation state is another boundary. Persistent identifiers are helpful for multi-turn testing, but they can make a test appear to pass because it inherited context from an earlier run. Start a fresh conversation when checking isolation, and record which state a test expects.

Logs are an advantage of local development. Capture the request, tool activity, and failure details before changing code. That evidence is much easier to inspect locally than after a remote deployment has compressed the problem into a status message.

## Recommendations for .NET Teams

1. Add a local run and invoke step to the agent project's developer documentation.
2. Keep local and remote targets explicit, especially when testing data access.
3. Create a small set of repeatable multi-turn conversation scenarios.
4. Use development identities and test resources only.
5. Deploy after the local behavior is understood, then run separate cloud integration checks.

The Azure Developer CLI extension makes agent development feel more like ordinary application development: edit, run, invoke, inspect, repeat. That is exactly the right direction. The fast loop should be local, while deployment validation remains a deliberate second stage.