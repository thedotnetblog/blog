---
title: "Azure DevOps MCP Server Microsoft Foundry में आया: आपके AI Agents के लिए इसका क्या मतलब है"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server अब Microsoft Foundry में उपलब्ध है। अपने AI agents को कुछ ही क्लिक में DevOps workflows — work items, repos, pipelines — से सीधे जोड़ें।"
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-devops-mcp-server-microsoft-foundry" >}}).*

MCP (Model Context Protocol) इन दिनों बहुत चर्चा में है। अगर आप AI agent ecosystem को follow कर रहे हैं, तो आपने शायद देखा होगा कि MCP servers हर जगह दिखने लगे हैं — agents को एक मानकीकृत protocol के ज़रिए बाहरी tools और services के साथ interact करने की क्षमता देते हैं।

अब [Azure DevOps MCP Server Microsoft Foundry में उपलब्ध है](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), और यह उन integrations में से एक है जो आपको व्यावहारिक संभावनाओं के बारे में सोचने पर मजबूर करती है।

## यहाँ वास्तव में क्या हो रहा है

Microsoft ने Azure DevOps MCP Server को [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) के रूप में पहले ही release किया था — वह MCP server ही है। नया यह है कि Foundry integration आई है। अब आप अपने Foundry agents में tool catalog से सीधे Azure DevOps MCP Server जोड़ सकते हैं।

जो Foundry से परिचित नहीं हैं उनके लिए: यह Microsoft का unified platform है जो बड़े पैमाने पर AI-powered applications और agents बनाने और manage करने के लिए है। Model access, orchestration, evaluation, deployment — सब एक ही जगह।

## इसे Setup करना

Setup करना आश्चर्यजनक रूप से सीधा है:

1. अपने Foundry agent में जाएं **Add Tools** > **Catalog**
2. "Azure DevOps" खोजें
3. Azure DevOps MCP Server (preview) चुनें और **Create** पर क्लिक करें
4. अपना organization नाम डालें और connect करें

बस इतना। आपके agent को अब Azure DevOps tools तक access मिल गई।

## आप अपने agent की access को control कर सकते हैं

यहाँ वो हिस्सा है जो मुझे पसंद आया: आप all-or-nothing approach तक सीमित नहीं हैं। आप specify कर सकते हैं कि आपके agent के लिए कौन से tools उपलब्ध हों। तो अगर आप चाहते हैं कि वो केवल work items पढ़े लेकिन pipelines को न छुए, तो आप उसे configure कर सकते हैं। Principle of least privilege, अपने AI agents पर लागू।

यह enterprise scenarios के लिए मायने रखता है जहाँ आप नहीं चाहते कि एक agent गलती से deployment pipeline trigger कर दे क्योंकि किसी ने उससे "release में मदद करो" कहा।

## .NET teams के लिए यह क्यों दिलचस्प है

सोचिए यह व्यवहार में क्या enable करता है:

- **Sprint planning assistants** — agents जो work items pull कर सकते हैं, velocity data analyze कर सकते हैं, और sprint capacity suggest कर सकते हैं
- **Code review bots** — agents जो आपके PR context को समझते हैं क्योंकि वे वास्तव में आपके repos और linked work items पढ़ सकते हैं
- **Incident response** — agents जो work items create कर सकते हैं, recent deployments query कर सकते हैं, और bugs को recent changes से correlate कर सकते हैं
- **Developer onboarding** — "मुझे किस पर काम करना चाहिए?" का जवाब actual project data पर आधारित होगा

जो .NET teams पहले से CI/CD pipelines और project management के लिए Azure DevOps use कर रही हैं, उनके लिए एक AI agent का सीधे उन systems के साथ interact करना useful automation की दिशा में एक महत्वपूर्ण कदम है।

## बड़ी MCP तस्वीर

यह एक बड़े trend का हिस्सा है: MCP servers AI agents के बाहरी दुनिया से interact करने का मानक तरीका बनते जा रहे हैं। हम GitHub, Azure DevOps, databases, SaaS APIs — सब के लिए MCP servers देख रहे हैं — और Foundry वह hub बनता जा रहा है जहाँ ये सभी connections एक साथ आते हैं।

अगर आप .NET ecosystem में agents बना रहे हैं, तो MCP पर ध्यान देना ज़रूरी है। Protocol मानकीकृत है, tooling mature हो रहा है, और Foundry integration इसे manually server connections wire किए बिना accessible बनाती है।

## निष्कर्ष

Foundry में Azure DevOps MCP Server preview में है, इसलिए यह evolve होता रहेगा। लेकिन core workflow solid है: connect करें, tool access configure करें, और अपने agents को आपके DevOps data के साथ काम करने दें। अगर आप पहले से Foundry ecosystem में हैं, तो यह कुछ clicks की दूरी पर है। इसे try करें और देखें कि आप कौन से workflows बना सकते हैं।

पूरी setup और अधिक जानकारी के लिए [official announcement](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) देखें।
