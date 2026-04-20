---
title: "Azure MCP Server 2.0 आ गया — Self-Hosted Agentic Cloud Automation यहाँ है"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 stable हो गया है — self-hosted remote deployments, 57 Azure services में 276 tools, और enterprise-grade security के साथ — यहाँ जानिए .NET developers के लिए agentic workflows बनाने में क्या मायने रखता है।"
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

अगर आप हाल ही में MCP और Azure के साथ कुछ बना रहे हैं, तो आप शायद पहले से जानते हैं कि local experience अच्छी तरह काम करता है। एक MCP server plug करें, अपने AI agent को Azure resources से बात करने दें, आगे बढ़ें। लेकिन जिस पल आपको उस setup को पूरी team के साथ share करना हो? वहाँ चीज़ें जटिल हो जाती थीं।

अब नहीं। Azure MCP Server [2.0 stable में आ गया है](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), और headline feature ठीक वही है जो enterprise teams माँग रही थीं: **self-hosted remote MCP server support**।

## Azure MCP Server क्या है?

संक्षिप्त परिचय। Azure MCP Server [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) specification को implement करता है और Azure की capabilities को structured, discoverable tools के रूप में expose करता है जिन्हें AI agents invoke कर सकते हैं। इसे अपने agent और Azure के बीच एक मानकीकृत bridge समझें — provisioning, deployment, monitoring, diagnostics, सब एक consistent interface के ज़रिए।

संख्याएं खुद बोलती हैं: **57 Azure services में 276 MCP tools**। यह गहरी coverage है।

## बड़ी बात: self-hosted remote deployments

यहाँ असली बात है। अपनी machine पर MCP locally चलाना dev और experiments के लिए ठीक है। लेकिन real team scenario में आपको चाहिए:

- Developers और internal agent systems के लिए shared access
- Centralized configuration (tenant context, subscription defaults, telemetry)
- Enterprise network और policy boundaries
- CI/CD pipelines में integration

Azure MCP Server 2.0 इन सभी को address करता है। आप इसे HTTP-based transport, proper authentication, और consistent governance के साथ एक centrally managed internal service के रूप में deploy कर सकते हैं।

Auth के लिए, आपको दो solid options मिलते हैं:

1. **Managed Identity** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) के साथ चलाने पर
2. **On-Behalf-Of (OBO) flow** — OpenID Connect delegation जो signed-in user के context में Azure APIs call करता है

वो OBO flow हम .NET developers के लिए खास दिलचस्प है। इसका मतलब है कि आपके agentic workflows किसी over-privileged service account से नहीं बल्कि user की actual permissions से operate कर सकते हैं। Principle of least privilege, सीधे built in।

## Security hardening

यह केवल एक feature release नहीं है — यह security भी है। 2.0 release में शामिल हैं:

- मज़बूत endpoint validation
- query-oriented tools में injection patterns के खिलाफ सुरक्षा
- dev environments के लिए tighter isolation controls

अगर आप MCP को एक shared service के रूप में expose करने जा रहे हैं, तो ये safeguards बेहद ज़रूरी हैं।

## इसे कहाँ use करें

Client compatibility की कहानी व्यापक है। Azure MCP Server 2.0 इनके साथ काम करता है:

- **IDEs**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **CLI agents**: GitHub Copilot CLI, Claude Code
- **Standalone**: simple setups के लिए local server
- **Self-hosted remote**: 2.0 का नया मुख्य feature

इसके अलावा Azure US Government और 21Vianet द्वारा संचालित Azure के लिए sovereign cloud support भी है, जो regulated deployments के लिए critical है।

## .NET developers के लिए यह क्यों मायने रखता है

अगर आप .NET के साथ agentic applications बना रहे हैं — चाहे वो Semantic Kernel हो, Microsoft Agent Framework हो, या आपका खुद का orchestration — Azure MCP Server 2.0 आपको एक production-ready तरीका देता है जिससे आपके agents Azure infrastructure के साथ interact कर सकें। कोई custom REST wrappers नहीं। कोई service-specific integration patterns नहीं। बस MCP।

कुछ दिन पहले आई [MCP Apps के लिए fluent API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) के साथ मिलकर, .NET MCP ecosystem तेज़ी से mature हो रहा है।

## शुरू करें

अपना path चुनें:

- **[GitHub Repo](https://aka.ms/azmcp)** — source code, docs, सब कुछ
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — containerized deployment
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE integration
- **[Self-hosting guide](https://aka.ms/azmcp/self-host)** — 2.0 का flagship feature

## निष्कर्ष

Azure MCP Server 2.0 बिल्कुल उस तरह का infrastructure upgrade है जो demo में flashy नहीं दिखता लेकिन व्यवहार में सब कुछ बदल देता है। Proper auth, security hardening, और sovereign cloud support के साथ self-hosted remote MCP का मतलब है कि MCP अब Azure पर real teams के लिए real agentic workflows बनाने के लिए तैयार है। अगर आप "enterprise-ready" signal का इंतज़ार कर रहे थे — यही वो है।
