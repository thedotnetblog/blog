---
title: "Foundry Toolboxes: AI Agents के लिए एक Unified Endpoint"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry ने Toolboxes को Public Preview में launch किया है — AI Agent tools को एकल MCP-compatible endpoint के माध्यम से manage और expose करने का एक तरीका।"
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

एक problem है जो boring लगती है जब तक खुद face न करो: organization multiple AI agents बना रही है, हर एक को tools चाहिए, और हर team scratch से configure कर रही है। Same web search integration, same Azure AI Search config, same GitHub MCP server connection — लेकिन अलग repository में, अलग team द्वारा, अलग credentials के साथ, और कोई shared governance नहीं।

Microsoft Foundry ने [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) को Public Preview में launch किया, और यह उस problem का direct answer है।

## Toolbox क्या है

Toolbox एक named, reusable bundle of tools है जो एक बार Foundry में define होता है और single MCP-compatible endpoint के through expose होता है। कोई भी agent runtime जो MCP बोलता है वो इसे consume कर सकता है — Foundry Agents में कोई lock-in नहीं।

Promise simple है: **build once, consume anywhere**। Tools define करो, authentication centrally configure करो (OAuth passthrough, Entra managed identity), endpoint publish करो। जिस agent को वो tools चाहिए वो endpoint से connect करे और सभी मिल जाएं।

## चार pillars (आज दो available)

| Pillar | Status | क्या करता है |
|--------|--------|-------------|
| **Discover** | Coming soon | Manual search बिना approved tools खोजना |
| **Build** | Available | Tools को reusable bundle में group करना |
| **Consume** | Available | Single MCP endpoint सभी tools expose करता है |
| **Govern** | Coming soon | Centralized auth + सभी tool calls की observability |

## Practical Example

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Documentation search करो और GitHub issues का जवाब दो",
    tools=[
        {"type": "web_search", "description": "Public documentation search"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Publish होने के बाद Foundry unified endpoint देता है। एक connection, सभी tools।

## Foundry Agents में lock-in नहीं

Toolboxes Foundry में **create और manage** होते हैं, लेकिन consumption surface open MCP protocol है। Microsoft Agent Framework या LangGraph के custom agents, GitHub Copilot और अन्य MCP-enabled IDEs, कोई भी MCP-speaking runtime इन्हें use कर सकता है।

## अभी क्यों important है

Multi-agent wave production में पहुंच रही है। हर नया agent duplicate configuration, stale credentials और inconsistent behavior की नई surface है। Build + Consume foundation centralization शुरू करने के लिए काफी है। जब Govern pillar आएगा, पूरी agent fleet के लिए fully observable, centrally controlled tool layer मिलेगी।

## निष्कर्ष

यह अभी भी early है — Public Preview, Python SDK पहले, Discover और Govern अभी आने हैं। लेकिन model solid है और MCP-native design का मतलब है कि यह उन tools के साथ काम करता है जो already build हो रहे हैं। [Official announcement](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) देखें।
