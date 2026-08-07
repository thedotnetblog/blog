---
title: "Extending VS Code with Model Context Protocol: Beyond Static Tools"
description: "VS Code's implementation of MCP transforms how agents interact with external services, from databases to deployment systems. A deep dive into spec-first engineering and ecosystem growth."
date: 2026-08-09
author: Emiliano Montesdeoca
tags: [VS Code, MCP, agent-extensibility, protocol-standards, developer-tools, ecosystem]
slug: extending-vs-code-with-mcp
---

Original source: [Beyond the tools, adding MCP in VS Code](https://code.visualstudio.com/blogs/2025/05/12/agent-mode-meets-mcp)

# Extending VS Code with Model Context Protocol: Beyond Static Tools

When VS Code first introduced agent mode, it opened a new door to developer workflows—but that door had walls. Agents could inspect your workspace, run builds, debug tests. But they couldn't reach outside to interact with databases, APIs, deployment systems, or any external service without custom VS Code extensions.

That's where the Model Context Protocol (MCP) changes the game.

Think of MCP as the HTTP for AI agents—a standardized way for AI models to connect with real tools and services. Instead of each editor building custom integrations for each tool, MCP lets servers publish their capabilities in a consistent way. GitHub, Playwright, Azure, and Perplexity have all shipped MCP servers. And VS Code didn't just adopt it; they went all-in on spec-first engineering, implementing deep MCP features that server developers can rely on.

## Why MCP Matters More Than You'd Think

The shift from VS Code's custom **Tools** API to MCP wasn't obvious at first. After all, VS Code had thousands of extensions. Why standardize on an external protocol?

The answer is ecosystem velocity. As David Soria Parra, MCP co-creator, put it: "I'm excited to see what developers will build now that they have access to the full spectrum of MCP features within VS Code." That statement captures something crucial—open standards attract network effects. When Playwright can ship a server for frontend verification and it "just works" in VS Code, Neovim, and any other client, you've unlocked a multiplier effect.

A concrete quote from the VS Code blog: "MCP is best understood as a protocol for connecting AI agents to a wide range of external tools and services in a consistent way, much like how HTTP standardized communication for the web."

## Three Design Principles That Got MCP Right in VS Code

VS Code's integration philosophy shaped how MCP works. Three principles stand out:

**Simplicity over configuration.** The **MCP: Add Server** command lets you install a server from NPM, PyPI, or Docker in seconds. No JSON editing. Websites can offer "Install in VS Code" buttons. VS Code even auto-discovers configurations from other clients like Claude Desktop.

**Security by default.** Managing API keys used to mean checking passwords into `.env` files (or worse, `.gitignore` violations). VS Code added input variables that prompt once, encrypt secrets, and store them securely. Teams can share configurations without risking credentials.

**User control, always.** The tool picker shows you exactly which tools an agent can access per session. Logs surface transparently. You can start, stop, and restart servers from the UI. This is extensibility that respects developer autonomy.

## Beyond Tools: The Full Specification Emerges

Early MCP integration focused on **tools**—discrete actions like "search code" or "create issue." But the protocol is richer than that.

VS Code now supports the complete MCP spec, including:

- **Roots**: Servers understand your workspace structure upfront instead of guessing. Enables use cases like finding all TODOs across a monorepo or auto-detecting project types.
- **Dynamic tool discovery**: Servers can change which tools are available on the fly based on context or detected frameworks.
- **Tool annotations**: Servers provide metadata—human-readable names, read-only flags—that help agents behave smarter and users understand what's happening.
- **Streamable HTTP transport**: Remote servers can now scale independently with enterprise-grade security.

The newest frontier is **Authorization**—Microsoft, Anthropic, Okta, Auth0, and Stytch collaborated on a spec that cleanly separates Resource Providers from Authorization Servers. Instead of building custom OAuth, MCP servers delegate to existing identity providers. The GitHub MCP Server demonstrates this perfectly, using your existing GitHub authentication in VS Code.

## Practical Pattern: Roots in Action

Here's why roots matter. Suppose you're working in a monorepo with ten microservices. An MCP server can receive a list of all workspace folders on startup:

```json
{
  "roots": [
    { "uri": "file:///workspace/service-auth", "name": "auth-service" },
    { "uri": "file:///workspace/service-api", "name": "api-service" },
    { "uri": "file:///workspace/service-web", "name": "web-frontend" }
  ]
}
```

The server can then tailor its tool set—expose database migration tools only for backend services, show deployment commands only for services that have infrastructure definitions. Agents get smarter without manual configuration.

## The Caveat: Adoption Isn't Instant

MCP is powerful, but server developers still need to build servers. The protocol is only as useful as the ecosystem around it. Right now, you have GitHub, Playwright, Azure, and Perplexity. That's a strong start, but compared to the breadth of VS Code extensions, it's still small.

More importantly, supporting the full spec requires work. VS Code has landed the foundation, but authorization, prompts, resources, and sampling all need careful implementation. Server developers are still learning how to use these features effectively.

## My Take: This Is How Standards Win

VS Code could have built MCP support as a checkbox—minimal compliance, move on. Instead, they went spec-first. They contribute to the spec itself, they implement the full feature set, they built the security model right. They're shaping the protocol as it matures.

That matters because standards win through leadership, not just adoption. HTTP won because browsers and servers both got better at using it. MCP will win if VS Code, Neovim, Claude Desktop, and others all push the ecosystem forward together.

For .NET teams specifically, this means: start building MCP servers for your infrastructure if you have agents in your workflow. A server that lets an agent query your database, provision resources, or run deployment pipelines isn't a luxury—it's becoming the baseline for any serious AI-assisted development experience.

## What To Do Next

1. **Explore existing servers** at [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers). Test the GitHub, Playwright, or Azure servers.
2. **Prototype with roots and dynamic tools.** If you build a custom server, implement workspace roots and try dynamic tool discovery. See how context-aware your agents become.
3. **Watch authorization.** As the new auth spec matures, build with it from the start. It's the path to enterprise-safe AI agents.

VS Code's bet on MCP isn't just about features—it's about betting on a future where agents are first-class citizens in our tools, and standards matter more than lock-in.

Happy coding.