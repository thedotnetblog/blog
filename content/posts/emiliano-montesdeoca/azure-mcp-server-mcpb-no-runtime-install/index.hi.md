---
title: "Azure MCP Server अब .mcpb है — बिना किसी Runtime के इंस्टॉल करें"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server अब MCP Bundle (.mcpb) के रूप में उपलब्ध है — डाउनलोड करें, Claude Desktop में ड्रैग करें और हो गया। Node.js, Python या .NET की जरूरत नहीं।"
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

क्या आप जानते हैं MCP सर्वर सेटअप में क्या परेशान करता था? एक runtime की जरूरत थी। npm version के लिए Node.js, pip/uvx के लिए Python, dotnet variant के लिए .NET SDK।

[Azure MCP Server ने अभी यह बदल दिया](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)। यह अब `.mcpb` — एक MCP Bundle — के रूप में उपलब्ध है और सेटअप drag-and-drop है।

## MCP Bundle क्या है?

इसे VS Code extension (`.vsix`) या browser extension (`.crx`) की तरह सोचें, लेकिन MCP servers के लिए। एक `.mcpb` फाइल एक self-contained ZIP archive है जिसमें server binary और सभी dependencies शामिल हैं।

## कैसे इंस्टॉल करें

**1. अपने प्लेटफॉर्म के लिए bundle डाउनलोड करें**

[GitHub Releases page](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) पर जाएं और अपने OS और architecture के लिए `.mcpb` फाइल डाउनलोड करें।

**2. Claude Desktop में इंस्टॉल करें**

सबसे आसान तरीका: Extensions settings page (`☰ → File → Settings → Extensions`) खुलने पर `.mcpb` फाइल को Claude Desktop window में drag और drop करें। Server details review करें, Install पर क्लिक करें, confirm करें।

**3. Azure में authenticate करें**

```bash
az login
```

बस इतना। Azure MCP Server आपके मौजूदा Azure credentials का उपयोग करता है।

## क्या कर सकते हैं

अपने AI client से सीधे 100+ Azure service tools तक पहुंच:
- Cosmos DB, Storage, Key Vault, App Service, Foundry query और manage करें
- किसी भी task के लिए `az` CLI commands generate करें
- Bicep और Terraform templates बनाएं

## शुरुआत करने के लिए

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repo**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

[पूरी पोस्ट](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/) देखें।
