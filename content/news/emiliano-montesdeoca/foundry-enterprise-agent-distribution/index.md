---
title: "From Building Agents to Working with Them: Enterprise Agent Distribution in Microsoft Foundry"
description: "Publishing, Autopilot agents, and Agent-to-Agent communication move Foundry agents into Microsoft 365 and Teams with identity and governance in the design."
date: 2026-10-13
author: "Emiliano Montesdeoca"
tags: ["Microsoft Foundry", "Enterprise AI", "Agents", "Teams", ".NET"]
slug: foundry-enterprise-agent-distribution
---

Original source: [From Building Agents to Working with Them: Enterprise Agent Distribution in Microsoft Foundry](https://devblogs.microsoft.com/foundry/from-building-agents-to-working-with-them-enterprise-agent-distribution-in-microsoft-foundry/)

The framing in this announcement is the part worth remembering: the past year was about building agents, and the next year is about putting them to work. Those are different engineering problems. An agent that works in a development project is not automatically an agent that employees can find, trust, and use inside the tools where their work already happens.

Foundry's three announcements target that last mile: publishing agents to Microsoft 365 Copilot and Teams, Autopilot agents in public preview, and incoming Agent-to-Agent communication in public preview. Together they move the conversation from an individual chat session toward shared, governed work.

## Publishing Changes the Surface

Foundry agents can be published directly into Microsoft 365 Copilot and Teams without rebuilding the agent for each surface. The agent keeps its development capabilities while moving through a governed publishing pipeline before becoming available across an organization.

That matters because enterprise users do not want another endpoint to remember. They want an agent to appear where a conversation, document, meeting, or decision already exists. The source describes a shift from a simple prompt-and-response pattern to "Goal -> Ongoing execution -> Checkpoints -> Collaboration." That is a better model for tasks that need time, approvals, or escalation.

For a .NET team, this changes what success looks like in a pilot. Do not only ask whether the agent answers a question correctly. Ask whether a user can assign it a goal, see progress, understand what it needs, approve a consequential action, and recover when the agent needs a human. The surrounding interaction is now part of the product.

The publishing status also matters. The source says Microsoft 365 Copilot and Teams publishing is generally available next month relative to the announcement. Treat that as the availability boundary of the article, and verify the current service status before making it part of a production rollout.

## Autopilot Agents Are Team Participants

Autopilot agents are in public preview and operate autonomously with their own identity. They have user accounts with productivity licenses, including email, calendar, OneDrive, and Teams access, as well as a place in the organization chart.

That identity model is more consequential than the word "autopilot." An agent that can participate in shared spaces is not merely a faster assistant for one person. It can hold ongoing responsibilities across a team, which means access, accountability, and communication rules need to be explicit before anyone gives it a real workstream.

The Workstream Manager sample shows the intended pattern. It lives in Teams group chats, reads dynamic knowledge from conversation history and shared sources, tracks tasks and deadlines, summarizes discussions into action items, follows up on overdue work, surfaces risks, and coordinates updates. The sample is available in C# and Python, which gives .NET teams a concrete place to study the interaction model.

The sample's guardrails are as useful as its capabilities. A manager onboards the agent and controls access with commands such as `/access add`, `/access remove`, and `/access list`. The agent tracks commitments with owner, description, status, and ETA. It can produce an on-demand workstream summary, and in group chats it responds when addressed rather than interrupting every human side conversation.

Those details are product design, not decoration. An agent that talks too often becomes noise. An agent that records a commitment without a visible owner becomes a new source of ambiguity. Pilot teams should define who can authorize the agent, which channels it may read, and which actions it may take without approval.

## Agent-to-Agent Communication Extends the System

Enterprise work rarely fits inside one agent's specialty. Foundry already supported calling remote A2A agents as a tool; the announcement adds incoming A2A in public preview. Developers can expose a Foundry agent as an A2A endpoint, publish its agent card, and let other agents invoke it through the open protocol regardless of framework or cloud.

This is a useful architectural direction because agents do not need to be rebuilt or hard-wired together to operate as a system. A research agent can hand off a task to a domain agent, and a workflow agent can use a specialized agent the way it uses another tool.

The security boundary is clear in the source: every call is authenticated with Microsoft Entra ID and anonymous access is not allowed. For .NET developers, that means A2A should be designed as an identity and contract boundary, not simply as an HTTP endpoint. Define what the receiving agent accepts, what it returns, how failures are represented, and which identity is allowed to call it.

Start with one narrow handoff. Keep the delegated task observable and make the originating agent responsible for explaining the result to the user. Distributed autonomy without traceability is just distributed debugging.

## Enterprise Controls Arrive Early

Every Foundry agent receives an Entra agent identity and is registered in Microsoft Agent 365. The source presents this as a foundation for IT to see, approve, and manage agents across the organization. Admin approval, scoping, secure publishing, and visibility are part of the path before an agent goes organization-wide.

That is the right order. Governance should begin during development, not after the first agent has acquired access to shared data. A team should know which identity an agent uses, which administrator approves it, where it may be discovered, and how to disable it before a pilot begins.

## What .NET Teams Should Do Next

1. Pilot publishing in a team space where the work is already collaborative.
2. Study the C# Workstream Manager sample and copy its access and notification discipline before copying its autonomy.
3. Define an explicit approval boundary for Autopilot actions, especially those involving email, documents, or project systems.
4. Experiment with one incoming A2A endpoint and document its identity, contract, and failure behavior.
5. Verify preview and general-availability status before committing to a broad rollout.

The important shift is from building an agent that can work to operating an agent that a team can work with. Distribution, identity, conversation etiquette, and handoff contracts are not deployment details. They are the product.