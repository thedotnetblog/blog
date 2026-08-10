---
title: "Discovery to Execution: Scaling Agents with Toolboxes and Routines in Microsoft Foundry"
description: "How Tool Search, Skills, and Routines reduce the operational friction between an agent prototype and a production workflow."
date: 2026-10-12
author: "Emiliano Montesdeoca"
tags: ["Microsoft Foundry", "AI Agents", "Toolboxes", "Routines", ".NET"]
slug: foundry-toolboxes-routines
---

Original source: [Discovery to Execution: Scaling Agents with Toolboxes and Routines in Microsoft Foundry](https://devblogs.microsoft.com/foundry/toolbox-build-26/)

Tooling does not break at a small scale. It breaks when a team moves to production. AI adoption accelerates, and so does the number of tools available to an agent. The interesting part of Microsoft's Foundry announcement is that it treats tool discovery, reusable procedures, governance, and run control as one operating problem rather than four unrelated features.

A prototype with five tools is easy to understand. A production agent with 50 or 200 tools is a different system. Tool definitions consume context, similar capabilities compete for the model's attention, and the code that starts an agent becomes surrounded by scheduler and authentication glue. Toolboxes and Routines are aimed at that transition.

## Tool Search Keeps the Context Usable

The Tool Search preview addresses the most immediate scaling problem. Without it, every tool definition is sent to the model on every turn. At large toolbox sizes, that adds input tokens even when most tools are irrelevant, consumes context that could hold the conversation and domain data, and increases the chance that the agent selects a similar-but-wrong tool.

With Tool Search enabled, the toolbox exposes two meta-tools: `tool_search` describes the capability the agent needs, and `call_tool` invokes a discovered tool by name. The remaining tools stay hidden until the agent asks for them. That is a much cleaner contract than presenting the entire catalog on every request.

The toolbox still needs deliberate curation. Foundry supports pinning tools that should always be visible, adding context that explains how a team uses a tool, and auto-pinning frequently used tools so a search round trip does not become unnecessary overhead. This is a useful reminder that discovery is not purely a model problem. The tool owner controls names, descriptions, visibility, and the distinction between an essential operation and an edge-case integration.

For a .NET team, I would measure before changing the architecture. Record the number of tools, input token usage, tool-selection errors, and the latency of a discovery round trip. Tool Search is most compelling when the toolbox is genuinely broad, not merely because a preview feature exists.

## A Catalog That Connects the Agent to Work

Tool discovery is only half the problem. An agent that can find tools but cannot reach the business context remains a demo. Foundry's catalog brings together Work IQ, Fabric IQ, browser automation, and managed MCP servers from the Azure Connector Namespace.

Work IQ, in preview, gives agents access to organizational context without exposing raw data. Fabric IQ, also in preview, connects agents to operational and analytical business state through ontology, Fabric data agents, and Power BI semantic models. Browser automation brings MCP-native web automation to hosted agents through Playwright workspaces, with live visibility and control when workflows hit an edge case.

The managed connector story is practical. Adding a connector can provision a managed MCP server for systems such as Jira, Confluence, LinkedIn, and Box. That removes custom integration work, but it does not remove architecture work. The team still needs to decide what the agent may read, what it may change, and how identity and approval behave across the connected system.

For .NET developers building support, fulfillment, scheduling, or operational agents, this is the point where an integration should be judged by its data boundary. Ask whether the source of truth is governed, whether permissions are preserved, and whether a human can inspect an action before it changes a record.

## Skills Make Procedures Portable

The announcement draws a useful distinction: tools tell an agent what it can do, while Skills tell it how to do it. Skills are in preview and turn procedures that were previously scattered across repositories, scripts, and runtime setup into versioned, immutable capabilities attached to a toolbox.

Agents discover and load Skills through MCP resources at startup, without custom wiring. That makes them a good home for an escalation procedure, validation sequence, or formatting template that needs to be shared consistently.

The important word is versioned. A procedure is part of the behavior of the agent, so changing it should be reviewable and reversible. For a .NET team, treat a Skill like a runbook or a package contract: state when it applies, what inputs it expects, which steps are mandatory, and what evidence marks completion. Do not hide an architectural decision inside a procedure that nobody reviews.

## Routines Simplify the "When"

Toolboxes answer what an agent can access. Routines, in preview, address when and how it runs. Foundry Agent Service can take a schedule or event trigger and associate it with an agent action, while keeping invocation, permissions, connections, and run history with the agent in the same project.

That can replace a surprising amount of glue for lightweight automation: a daily summary, a one-time reminder, or a periodic check. It is not a universal workflow engine. The source is explicit that branching, multiple agents, human approvals, or complex state belong in a workflow instead.

That boundary is exactly right. Use Routines when the trigger and action are simple enough to explain in one sentence. Keep a workflow when the execution graph itself is part of the business logic. For .NET teams, this prevents a small scheduled agent from growing into a collection of Functions, queues, and authorization code before anyone has decided whether the complexity is necessary.

## Governance Is Part of the Toolbox

As tool use scales, guardrails need to cover tool inputs and outputs. Foundry Control Plane guardrails can help block calls that violate compliance requirements, expose sensitive data, trigger unsafe content, or drift from the intended task. Because they integrate with Toolbox, the policy can follow the tool call across agent experiences.

My recommended order is straightforward: inventory the tools, measure selection and token costs, introduce Tool Search for a real scale problem, package one repeated procedure as a Skill, and pilot a simple event or schedule with Routines. Keep complex orchestration in a workflow and make every connector's identity boundary explicit.

The useful promise here is not that Foundry removes engineering. It gives teams better places to put the engineering: discovery rules in the toolbox, repeatable behavior in Skills, run control in Routines, and policy in guardrails.