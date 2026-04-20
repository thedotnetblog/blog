---
title: "Azure MCP Server 2.0 आया — Self-Hosted Agentic Cloud Automation यहाँ है"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 stable हो गया है self-hosted remote deployments, 57 Azure services में 276 tools, और enterprise-grade security के साथ — .NET developers के लिए क्या मायने रखता है।"
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

अगर आप हाल ही में MCP और Azure के साथ कुछ build कर रहे हैं, तो आप शायद जानते हैं कि local experience अच्छी तरह काम करती है। लेकिन जब आपको यह setup team भर में share करना हो? वहाँ चीजें complicated हो जाती थीं।

अब नहीं। Azure MCP Server [2.0 stable हो गया](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), और headline feature वही है जो enterprise teams ने माँगी थी: **self-hosted remote MCP server support**।

## Azure MCP Server क्या है?

Azure MCP Server [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) specification implement करता है और Azure capabilities को structured, discoverable tools के रूप में expose करता है। Numbers खुद बोलते हैं: **57 Azure services में 276 MCP tools**।

## बड़ी बात: self-hosted remote deployments

Real team scenario में आपको चाहिए:
- Developers और internal agent systems के लिए shared access
- Centralized configuration
- Enterprise network और policy boundaries
- CI/CD pipelines में integration

Azure MCP Server 2.0 यह सब address करता है। Auth के लिए दो options:

1. **Managed Identity** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) के साथ
2. **On-Behalf-Of (OBO) flow** — user के actual permissions के साथ

## Security hardening

2.0 release में जोड़ा गया:
- Stronger endpoint validation
- Query-oriented tools में injection patterns के खिलाफ protection
- Dev environments के लिए tighter isolation controls

## Getting started

- **[GitHub Repo](https://aka.ms/azmcp)** — source code, docs
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — containerized deployment
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE integration
- **[Self-hosting guide](https://aka.ms/azmcp/self-host)** — 2.0 का flagship feature

Azure MCP Server 2.0 enterprise teams के लिए MCP को real agentic workflows के लिए ready बनाता है।
