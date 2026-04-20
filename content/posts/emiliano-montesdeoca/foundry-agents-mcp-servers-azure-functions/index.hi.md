---
title: "Azure Functions पर अपने MCP Servers को Foundry Agents से कनेक्ट करें — यहाँ जानिए कैसे"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "अपना MCP server एक बार बनाएं, Azure Functions पर deploy करें, और Microsoft Foundry agents से proper auth के साथ connect करें। आपके tools हर जगह काम करते हैं — VS Code, Cursor, और अब enterprise AI agents।"
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "foundry-agents-mcp-servers-azure-functions" >}}).*

MCP ecosystem के बारे में मुझे एक बात बहुत पसंद है: आप अपना server एक बार बनाते हैं, और यह हर जगह काम करता है। VS Code, Visual Studio, Cursor, ChatGPT — हर MCP client आपके tools discover और use कर सकता है। अब Microsoft उस list में एक और consumer जोड़ रहा है: Foundry agents।

Azure SDK team की Lily Ma ने [एक practical guide publish की है](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) जो Azure Functions पर deploy किए गए MCP servers को Microsoft Foundry agents से connect करने के बारे में है। अगर आपके पास पहले से एक MCP server है, तो यह pure value-add है — कोई rebuilding की ज़रूरत नहीं।

## यह combination क्यों समझ में आता है

Azure Functions आपको scalable infrastructure, built-in auth, और MCP servers host करने के लिए serverless billing देता है। Microsoft Foundry आपको AI agents देता है जो reason, plan, और actions ले सकते हैं। दोनों को connect करने का मतलब है कि आपके custom tools — database query करना, business API call करना, validation logic चलाना — ऐसी capabilities बन जाती हैं जिन्हें enterprise AI agents autonomously discover और use कर सकते हैं।

मुख्य बात: आपका MCP server वैसा ही रहता है। आप बस Foundry को एक और consumer के रूप में जोड़ रहे हैं। वही tools जो आपके VS Code setup में काम करते हैं, अब एक AI agent को power करते हैं जिससे आपकी team या customers interact करते हैं।

## Authentication के विकल्प

यहीं पर यह post वास्तव में value add करती है। आपके scenario के अनुसार चार auth methods:

| Method | Use Case |
|--------|----------|
| **Key-based** (default) | Development या Entra auth के बिना servers |
| **Microsoft Entra** | Managed identities के साथ production |
| **OAuth identity passthrough** | Production जहाँ हर user individually authenticate करता है |
| **Unauthenticated** | Dev/testing या केवल public data |

Production के लिए, agent identity के साथ Microsoft Entra recommended path है। OAuth identity passthrough तब है जब user context मायने रखता है — agent users को sign in के लिए prompt करता है, और हर request user का अपना token carry करती है।

## इसे कैसे सेट करें

High-level flow:

1. **अपना MCP server Azure Functions पर deploy करें** — [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript, और Java के लिए samples उपलब्ध हैं
2. **अपने function app पर built-in MCP authentication enable करें**
3. **अपना endpoint URL पाएं** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Foundry में MCP server को tool के रूप में जोड़ें** — portal में अपना agent navigate करें, एक नया MCP tool जोड़ें, endpoint और credentials दें

फिर Agent Builder playground में एक ऐसा prompt भेजकर test करें जो आपके किसी tool को trigger करे।

## मेरा नज़रिया

यहाँ composability की कहानी वाकई मज़बूत हो रही है। अपना MCP server एक बार .NET (या Python, TypeScript, Java) में बनाएं, Azure Functions पर deploy करें, और हर MCP-compatible client इसे use कर सकता है — coding tools, chat apps, और अब enterprise AI agents। यह एक "एक बार लिखो, हर जगह use करो" pattern है जो वास्तव में काम करता है।

.NET developers के लिए विशेष रूप से, [Azure Functions MCP extension](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) इसे straightforward बनाता है। आप अपने tools को Azure Functions के रूप में define करें, deploy करें, और आपके पास Azure Functions की सभी security और scaling के साथ एक production-grade MCP server है।

## निष्कर्ष

अगर आपके पास Azure Functions पर चलने वाले MCP tools हैं, तो उन्हें Foundry agents से connect करना एक quick win है — आपके custom tools server में कोई code changes किए बिना proper auth के साथ enterprise AI capabilities बन जाते हैं।

हर authentication method के step-by-step निर्देशों के लिए [पूरी guide](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) पढ़ें, और production setups के लिए [detailed docs](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) देखें।
