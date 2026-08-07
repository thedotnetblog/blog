---
title: "VS Code Implements Full MCP Specification: Enterprise Security Meets Extensibility"
description: "Complete Model Context Protocol support arrives with authorization, prompts, resources, and sampling. A milestone in standardized AI agent integration and enterprise-grade security."
date: 2026-08-12
author: "Emiliano Montesdeoca"
tags:
  - mcp
  - enterprise-security
  - vscode
  - agents
  - authorization
  - specification
slug: complete-mcp-spec-in-vs-code
---

Original source: [The Complete MCP Experience: Full Specification Support in VS Code](https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support)

When VS Code added MCP support in May, it delivered the foundation: tools and workspace awareness. In June, the editor announced support for the complete Model Context Protocol specification.

That is more than another integration checkbox. Authorization, prompts, resources, and sampling turn MCP from a collection of callable tools into a protocol for secure, context-rich agent workflows. For .NET teams building internal assistants or extending development environments, the important change is architectural: external capabilities can now be designed as interoperable services instead of one-off editor extensions.

## Authorization Moves Credentials to the Right Boundary

The most consequential addition is the authorization work. MCP servers often need access to protected resources, but asking every server to implement its own OAuth flow creates a large and repetitive attack surface.

The specification separates the MCP server as a resource provider from the authorization server that authenticates the user. That lets a server delegate identity to an existing provider instead of storing and managing every credential itself.

The source describes the collaboration behind this work across Microsoft, Anthropic, and identity companies including Okta/Auth0, Stytch, and Descope. The result is a better default for remote servers: authenticate through established identity systems and let the client mediate the user's consent.

For an enterprise .NET application, the principle is familiar. Keep business APIs responsible for their resources, keep identity in the identity boundary, and make the delegation explicit. MCP is applying that same separation to agent integrations.

Streamable HTTP makes the model useful beyond a local process. A remote MCP server can scale independently while retaining a defined authentication flow. The GitHub MCP Server is the practical example from the announcement: a remote server with OAuth integration that can use VS Code's existing GitHub authentication and account management.

## Prompts Package Workflows, Not Just Text

Tools are useful when an agent needs to perform one action. Prompts are useful when the user needs to start a coordinated workflow.

MCP prompts can be dynamic and context-aware. A server can tailor the starting point to the current workspace or project state, and VS Code exposes server-provided prompts alongside user-defined prompts. The invocation pattern is deliberately discoverable:

```text
/mcp.servername.promptname
```

That matters for teams because a prompt can become a repeatable entry point for a release check, an incident investigation, or a repository review. The server still owns the workflow context, while the client provides a consistent place to invoke it.

The recommendation is to treat prompts as product surfaces. Give them names that describe an outcome, document the required permissions, and make the first action understandable to a reviewer. A prompt that quietly triggers a dozen mutations is harder to trust than one that makes its plan visible.

## Resources Make Agent Output Usable

Resources represent semantic information that an agent or developer can interact with directly. A screenshot returned by Playwright can be brought into the workspace, annotated, and shared. Logs returned by a debugging tool can stream live updates instead of arriving as an opaque block of text.

This is an important distinction for .NET tooling. Build diagnostics, test reports, traces, and deployment observations are not merely strings. They have structure, provenance, and often a lifecycle. Modeling them as resources gives the client more options for rendering and handling them without every server inventing a custom UI.

The practical design question is ownership. Decide which system is the source of truth, how long a resource remains valid, and what permissions apply when it is shared. A live resource should also have limits: update frequency, size, and cancellation behavior need to be explicit.

## Sampling Lets Servers Ask for Reasoning

Sampling allows an MCP server to make language-model requests through the client. Instead of every server carrying its own AI SDK, API key, and model policy, it can request reasoning through the user's existing model access.

That opens useful patterns. A database server could inspect operational data and ask the model to explain a performance anomaly. A deployment server could summarize failed rollout signals before presenting a recommendation. A multi-agent workflow could delegate a bounded reasoning step to a specialized service.

The capability also creates obligations. Sampling can consume subscription quota or incur cost, and the user needs visibility into that request. Servers should explain why they need sampling, constrain the context they send, and avoid turning a simple tool call into an unbounded inference loop.

## What This Means for .NET Teams

The full specification is a reason to evaluate MCP as infrastructure, but not a reason to connect every system immediately. Start with one bounded workflow and make its permissions observable.

A sensible sequence is:

1. Connect to a remote MCP server with OAuth and inspect the consent boundary.
2. Add a read-only prompt for a workflow your team repeats manually.
3. Return structured resources such as build logs or test artifacts.
4. Evaluate sampling only after measuring its cost and data flow.

The caveat is that full client support does not make every server production-ready. Authorization providers may differ, self-hosted systems may need additional identity work, and streamed resources can grow quickly without rate limits. MCP gives the pieces; the service owner still has to design the operating model.

VS Code's complete MCP support is a signal that the protocol is maturing from an experiment into shared agent infrastructure. For .NET developers, the next move is practical: build one small, secure integration, measure it, and let the protocol earn a larger place in your architecture.