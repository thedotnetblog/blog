---
title: "VS Code 1.110: Making Agents Practical for Complex Tasks"
description: "The February release brings better agent visibility, session persistence, browser verification, and extensibility to long-running .NET development workflows."
date: 2026-08-24
author: "Emiliano Montesdeoca"
tags: [vscode, agents, development-workflow]
slug: vscode-1-110-agent-improvements
---

# VS Code 1.110: Making Agents Practical for Complex Tasks

Original source: [February 2026 (version 1.110)](https://code.visualstudio.com/updates/v1_110)

VS Code 1.110 focuses on the part of agent development that demos tend to skip: operating an agent once the task is large, multi-step, and connected to a real codebase. The release adds more visibility into execution, better ways to preserve context, browser tools for verification, and extensibility that can be packaged for reuse.

For .NET developers, that changes the question from "can an agent generate this?" to "can I supervise this workflow without guessing what happened?"

## More Visibility Into Agent Execution

The Agent Debug panel replaces the older diagnostics-oriented experience with a view of the session's activity. It shows which prompt files, skills, hooks, and custom configurations were loaded, along with the order of important events and tool calls.

That is useful even when the agent appears to be behaving correctly. If a custom instruction did not load, a tool received an unexpected parameter, or a hook ran at the wrong point, the debug view gives you evidence instead of a vague failure. For a .NET repository with project instructions, analyzers, and multiple services, that distinction matters.

Use the panel when developing custom agents or skills. Confirm the intended files were loaded, inspect the tool boundary, and keep a record of what the session actually did. It is especially valuable when two agents are running in parallel and their results seem inconsistent.

The permission model is also easier to control from a session. Commands such as `/autoApprove` and `/disableAutoApprove` make the autonomy decision explicit in the conversation. That convenience comes with a serious warning: skipping confirmations allows terminal commands and edits to proceed without an approval pause. Enable it only after the task and repository boundary are clear.

## Browser Verification Closes a Loop

The release adds agentic browser tools for navigating, interacting with, and taking screenshots of web pages from the editor. An agent can make a change, inspect the running application, and use what it sees to guide the next iteration.

For ASP.NET Core and Blazor work, this can shorten the distance between a generated UI change and a verified result. A developer can ask an agent to implement a component, start the local application, and inspect the rendered page rather than relying only on markup and compiler output.

The feature is experimental, and organization administrators can control it. Browser support also depends on the model and tool configuration. Treat it as a verification aid, not as permission to skip human review. A screenshot can show that a page renders; it does not prove that authorization, accessibility, data validation, or error handling are correct.

Keep browser checks bounded. Use test data, avoid real production sessions, and make the expected state explicit. The more powerful the browser tool becomes, the more important the environment boundary is.

## Preserve Context Without Losing Control

Long-running sessions become easier to manage with plan memory, manual `/compact` control, and chat forking. Instead of relying entirely on automatic compaction, a developer can decide what should survive a context reduction. Forking lets you explore an alternative design without destroying the original conversation.

That is a good fit for multi-day .NET work. Preserve decisions about a database schema or API contract, fork before exploring a different dependency injection approach, and keep the original session available as a reference.

Memory is not a substitute for durable project documentation. If a decision matters after the chat is gone, put it in the repository: an ADR, a design note, a test, or a project instruction. Session memory is useful for continuity; source control remains the durable record.

## Plugins and Skills Make Repetition Explicit

Agent plugins package skills, commands, agents, MCP servers, and hooks. The release also supports creating customizations from chat through commands such as `/create-prompt`, `/create-skill`, `/create-agent`, and `/create-hook`.

For .NET teams, this opens a practical path for repeatable work: a skill for adding an Entity Framework migration, a hook that runs formatting checks, or an agent that reviews an ASP.NET endpoint against local conventions. Start with a workflow you already repeat and make its inputs and outputs explicit.

Do not package a vague instruction and call it automation. A useful skill states what it may inspect, what it may change, and which validation command must pass.

## Recommendations for .NET Developers

1. Use the Agent Debug panel when building custom skills or troubleshooting an unexpected tool call.
2. Try browser tools against a local ASP.NET or Blazor app with non-sensitive test data.
3. Use `/compact` deliberately and record durable architectural decisions in the repository.
4. Keep auto-approval scoped to trusted, disposable environments and bounded tasks.
5. Turn repeated .NET workflows into small skills with explicit validation.

VS Code 1.110 is a maturity release. The headline is not that agents can do more; it is that developers can see, interrupt, preserve, and verify more of what agents do.