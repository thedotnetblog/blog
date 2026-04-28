---
title: "Azure SDK अप्रैल 2026: AI Foundry 2.0 और .NET डेवलपरों को क्या जानना चाहिए"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "अप्रैल 2026 की Azure SDK रिलीज़ Azure.AI.Projects 2.0.0 stable, महत्वपूर्ण breaking changes, Cosmos DB के critical security fixes, और .NET के लिए नई Provisioning libraries की लहर लेकर आती है।"
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

मासिक SDK releases को अक्सर छोड़ देना आसान होता है। इस बार कुछ ऐसी चीज़ें हैं जिन पर ध्यान देना चाहिए — खासकर अगर आप AI Foundry, Java में Cosmos DB, या .NET code से infrastructure provisioning कर रहे हैं।

## Azure.AI.Projects 2.0.0 — ऐसे breaking changes जो मायने रखते हैं

`Azure.AI.Projects` NuGet package कुछ बड़े architectural changes के साथ stable 2.0.0 तक पहुंचता है। अगर आप पहले से preview इस्तेमाल कर रहे हैं, तो ये बदलाव हुए हैं:

- **Namespace splits**: Evaluations `Azure.AI.Projects.Evaluation` में चले गए हैं, और memory operations `Azure.AI.Projects.Memory` में। आपको अपने `using` statements अपडेट करने होंगे।
- **Renamed types**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Naming conventions**: अब boolean properties लगातार `Is*` convention का पालन करती हैं

यह वही तरह के breaking changes हैं जो एक बार चोट पहुंचाते हैं और फिर हमेशा सही लगते हैं। अगर आपने preview पर build किया है, imports अपडेट करें और compiler को बाकी बदलाव बताने दें।

अच्छी खबर: यह अब stable है। आप इस API पर अब भरोसा कर सकते हैं।

## Cosmos DB Java: गंभीर सुरक्षा fix (RCE)

यह गंभीर है। Java Cosmos DB library (`azure-cosmos`) version 4.79.0 में **Remote Code Execution vulnerability (CWE-502)** के लिए critical security fix शामिल है।

समस्या `CosmosClientMetadataCachesSnapshot`, `AsyncCache`, और `DocumentCollection` में Java deserialization थी। fix Java deserialization को JSON-based serialization से बदल देता है, जिससे deserialization attacks की पूरी श्रेणी खत्म हो जाती है।

अगर आपके पास Azure Cosmos DB इस्तेमाल करने वाली कोई Java services हैं, तो तुरंत 4.79.0 पर अपडेट करें। यह वैकल्पिक नहीं है।

## .NET के लिए नई Provisioning libraries

इस महीने कई stable Provisioning libraries 1.0.0 पर पहुंचीं — ये वो libraries हैं जो आपको ARM templates या Bicep की जगह C# code में Azure infrastructure परिभाषित करने देती हैं:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

कई और beta.1 में हैं, जिनमें API Management, Batch, Compute, Monitor, MySQL, और Security Center शामिल हैं। अगर आप .NET से infrastructure-as-code कर रहे हैं — खासकर Aspire deployments के साथ — तो ये libraries आपका entry point हैं।

## Azure AI Agents Java: 2.0.0 GA

Java Azure AI Agents library भी इस महीने general availability तक पहुंचती है। मुख्य breaking changes:

- कई enum types को `ExpandableStringEnum`-आधारित classes में बदला गया है (नए values के लिए अधिक लचीला)
- `*Param` model classes का नाम बदलकर `*Parameter` किया गया है
- `MCPToolConnectorId` → `McpToolConnectorId` (consistent casing)
- `beginUpdateMemories` के लिए नया convenience overload

## Wrap Up

इस महीने .NET developers के लिए headline यह है कि `Azure.AI.Projects 2.0.0` stable हो गया है — अगर आप AI Foundry के साथ build कर रहे हैं, तो अब stable पर pin करने और imports अपडेट करने का समय है। Cosmos DB इस्तेमाल करने वाले Java shops के लिए security update urgent है।

Full release notes [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases) पर हैं। Original post: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).