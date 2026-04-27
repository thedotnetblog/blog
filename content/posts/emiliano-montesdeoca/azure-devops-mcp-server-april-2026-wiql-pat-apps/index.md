---
title: "Azure DevOps MCP Server April Update: WIQL Queries, PAT Auth, and Experimental MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "The Azure DevOps MCP Server gets WIQL-powered work item queries, Personal Access Token authentication, MCP annotations, and an experimental MCP Apps feature that packages common workflows into reusable tools."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

The Azure DevOps MCP Server keeps getting better. Dan Hellem's April update covers both the local and remote servers, and there are some genuinely useful additions here — especially if you've been using Copilot to navigate boards and repos.

## WIQL Query Support

The headline feature: a new `wit_query_by_wiql` tool that lets you run Work Item Query Language queries directly from your MCP client.

If you've used Azure Boards for any length of time, you know WIQL. It's the SQL-like query syntax for work items: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Having that available as an MCP tool means your Copilot sessions can now pull precise work item sets without you manually filtering or clicking through board views.

One caveat: on the remote MCP Server, this tool currently requires the **Insiders** feature flag while they validate query performance at scale. It'll come to everyone once the telemetry looks good.

## Personal Access Tokens on the Local Server

The local MCP Server now supports PAT authentication. This sounds like a minor quality-of-life fix, but it's actually important for integration scenarios — specifically when you're running the MCP server in a context where interactive authentication isn't available, or when you're connecting from external clients and automation.

Setup is documented in the [Getting Started guide](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat).

## MCP Annotations on the Remote Server

Annotations are metadata tags on MCP tools that tell LLMs how to use them safely. The Azure DevOps MCP Server is now implementing annotations for:

- **Read-only tools** — the LLM knows these are safe to call without user confirmation
- **Destructive tools** — the LLM knows to be cautious and confirm before proceeding
- **Open-world tools** — the LLM understands these may return unpredictable results

This is foundational for agent reliability. Without annotations, the LLM has to guess from the tool name whether it's safe to call. With annotations, the behavior is explicit and the agent can make better decisions.

## Wiki Tool Consolidation

The remote server is starting to consolidate related tools into fewer, more capable ones. The wiki tools are the first to get this treatment:

| New Tool | Replaces |
|----------|----------|
| `wiki` (read-only) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Fewer tools = better LLM performance. This is a consistent pattern across MCP server design — smaller, focused tool sets work better because the LLM doesn't have to reason about which of five similarly-named tools to pick.

## Experimental: MCP Apps

This is the most interesting addition, and it's clearly experimental. MCP Apps are packaged workflows that run inside the MCP server environment:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "mcp-server-azuredevops",
      "args": ["contoso", "-d", "core", "work", "work-items", "mcp-apps"]
    }
  }
}
```

The first example is `mcp_app_my_work_item` — a self-contained work item experience that lets you view, filter, and edit work items assigned to you, without manually chaining multiple tool calls.

The idea is compelling: instead of your agent calling `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` across multiple turns, a single MCP App provides the entire workflow as one structured, reusable unit. Reduced setup time, consistent behavior, fewer moving parts.

It's on the `mcp-apps-poc` branch right now, which tells you where it stands in terms of production readiness. But the direction is right — more workflow composition at the MCP layer, less ad-hoc tool chaining in your agent prompts.

## Wrapping up

The Azure DevOps MCP Server is maturing quickly. WIQL support and PAT auth are immediate wins for anyone using Copilot with Azure Boards. The annotation work makes the remote server safer for agentic use cases. And MCP Apps, while experimental, hints at where this is going: from raw tools to composable workflows.

Worth keeping an eye on the [documentation](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) as the remote server continues to evolve.

Original post by Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).
