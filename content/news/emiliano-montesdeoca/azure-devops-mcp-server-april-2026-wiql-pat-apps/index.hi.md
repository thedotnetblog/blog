---
title: "Azure DevOps MCP Server अप्रैल अपडेट: WIQL क्वेरी, PAT प्रमाणीकरण, और प्रयोगात्मक MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server को WIQL-आधारित work item queries, Personal Access Token प्रमाणीकरण, MCP annotations, और एक प्रयोगात्मक MCP Apps फ़ीचर मिलता है जो आम workflows को reusable tools में पैक करता है।"
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

Azure DevOps MCP Server लगातार बेहतर हो रहा है। Dan Hellem का अप्रैल अपडेट local और remote दोनों servers को कवर करता है, और यहाँ कुछ सचमुच उपयोगी additions हैं — खासकर अगर आपने boards और repos navigate करने के लिए Copilot का इस्तेमाल किया है।

## WIQL क्वेरी समर्थन

सबसे बड़ी ख़बर: एक नया `wit_query_by_wiql` tool, जो आपको MCP client से सीधे Work Item Query Language queries चलाने देता है।

अगर आपने कुछ समय से Azure Boards इस्तेमाल किया है, तो WIQL आपको पता होगा। यह work items के लिए SQL-जैसी query syntax है: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. इसे एक MCP tool के रूप में उपलब्ध कराना मतलब है कि आपकी Copilot sessions अब हाथ से filter किए बिना या board views में क्लिक किए बिना सटीक work item sets ला सकती हैं।

एक चेतावनी: remote MCP Server पर, इस tool के लिए अभी **Insiders** feature flag चाहिए, जब तक वे scale पर query performance validate कर रहे हैं। Telemetry अच्छा दिखते ही यह सबके लिए उपलब्ध होगा।

## Local Server पर Personal Access Tokens

Local MCP Server अब PAT authentication support करता है। यह छोटी quality-of-life fix जैसी लग सकती है, लेकिन integration scenarios के लिए यह अहम है — खासकर जब आप MCP server को ऐसे context में चला रहे हों जहाँ interactive authentication उपलब्ध नहीं है, या जब आप external clients और automation से connect कर रहे हों।

Setup के steps [Getting Started guide](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat) में documented हैं।

## Remote Server पर MCP Annotations

Annotations MCP tools पर metadata tags हैं जो LLMs को उन्हें सुरक्षित तरीके से इस्तेमाल करना बताते हैं। Azure DevOps MCP Server अब इन चीज़ों के लिए annotations लागू कर रहा है:

- **Read-only tools** — model जानता है कि इन्हें user confirmation के बिना call करना सुरक्षित है
- **Destructive tools** — model जानता है कि सावधान रहना है और आगे बढ़ने से पहले confirm करना है
- **Open-world tools** — model समझता है कि ये अप्रत्याशित results दे सकते हैं

यह agent reliability के लिए बुनियादी है। Annotations के बिना, model को tool name से अंदाज़ा लगाना पड़ता है कि उसे call करना सुरक्षित है या नहीं। Annotations के साथ, behavior explicit हो जाता है और agent बेहतर decisions ले सकता है।

## Wiki Tools का Consolidation

Remote server संबंधित tools को कम लेकिन अधिक सक्षम tools में consolidate करना शुरू कर रहा है। Wiki tools सबसे पहले इस treatment को पा रहे हैं:

| नया tool | Replace करता है |
|----------|----------|
| `wiki` (read-only) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

कम tools = बेहतर model performance। यह MCP server design में एक consistent pattern है — छोटे, focused tool sets बेहतर काम करते हैं क्योंकि model को पाँच लगभग-एक जैसे tools में से चुनने की ज़रूरत नहीं पड़ती।

## Experimental: MCP Apps

यह सबसे दिलचस्प addition है, और यह साफ़ तौर पर experimental है। MCP Apps ऐसे packaged workflows हैं जो MCP server environment के अंदर चलते हैं:

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

पहला example `mcp_app_my_work_item` है — एक self-contained work item experience जो आपको अपने assigned work items देखने, filter करने और edit करने देता है, बिना कई tool calls को manually chain किए।

Idea compelling है: आपके agent के `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` को कई turns में call करने के बजाय, एक single MCP App पूरे workflow को एक structured, reusable unit के रूप में देता है। Setup time कम, behavior consistent, और moving parts कम।

## Wrap Up

Azure DevOps MCP Server तेज़ी से mature हो रहा है। WIQL support और PAT auth किसी भी Copilot + Azure Boards user के लिए immediate wins हैं। Annotation work remote server को agentic use cases के लिए safer बनाता है। और MCP Apps, भले ही experimental हों, इस दिशा का संकेत देते हैं: raw tools से composable workflows की ओर।

Remote server के evolve होने के साथ [documentation](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) पर नज़र रखना worthwhile है।

Original post by Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).