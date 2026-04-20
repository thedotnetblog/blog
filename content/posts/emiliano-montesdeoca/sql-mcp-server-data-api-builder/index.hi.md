---
title: "SQL MCP Server — AI एजेंट्स को डेटाबेस एक्सेस देने का सही तरीका"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Data API builder का SQL MCP Server AI एजेंट्स को सुरक्षित, निर्धारित डेटाबेस एक्सेस देता है — बिना schema उजागर किए या NL2SQL पर निर्भर हुए। RBAC, caching, multi-database support — सब कुछ built-in।"
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "sql-mcp-server-data-api-builder" >}}).*

सच बात करें तो: आज उपलब्ध अधिकांश database MCP servers डरावने हैं। वे एक natural language query लेते हैं, तुरंत SQL generate करते हैं, और उसे आपके production data पर चला देते हैं। क्या गलत हो सकता है? (सब कुछ। सब कुछ गलत हो सकता है।)

Azure SQL टीम ने अभी [SQL MCP Server पेश किया](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), और यह एक मौलिक रूप से अलग दृष्टिकोण अपनाता है। Data API builder (DAB) 2.0 की एक feature के रूप में बना, यह AI एजेंट्स को database operations तक structured, निर्धारित access देता है — NL2SQL के बिना, आपका schema उजागर किए बिना, और हर कदम पर पूरे RBAC के साथ।

## NL2SQL क्यों नहीं?

यह सबसे दिलचस्प design निर्णय है। Models निर्धारित नहीं होते, और complex queries में सूक्ष्म त्रुटियाँ पैदा होने की सबसे अधिक संभावना होती है। जो queries उपयोगकर्ता AI से generate करवाना चाहते हैं, वही non-deterministic तरीके से produce होने पर सबसे अधिक जाँच की माँग करती हैं।

इसके बजाय, SQL MCP Server एक **NL2DAB** दृष्टिकोण अपनाता है। एजेंट Data API builder की entity abstraction layer और built-in query builder के साथ काम करता है ताकि accurate, well-formed T-SQL निर्धारित रूप से produce की जा सके। उपयोगकर्ता के लिए परिणाम वही रहता है, लेकिन hallucinated JOINs या accidental data exposure का जोखिम नहीं रहता।

## सात tools, सात सौ नहीं

SQL MCP Server database के आकार चाहे जो हो, ठीक सात DML tools expose करता है:

- `describe_entities` — उपलब्ध entities और operations खोजें
- `create_record` — rows insert करें
- `read_records` — tables और views query करें
- `update_record` — rows modify करें
- `delete_record` — rows हटाएं
- `execute_entity` — stored procedures चलाएं
- `aggregate_records` — aggregation queries

यह समझदारी है क्योंकि context windows एजेंट की सोचने की जगह हैं। सैकड़ों tool definitions से भर देने पर reasoning के लिए कम जगह बचती है। सात fixed tools एजेंट को *navigate करने* की बजाय *सोचने* पर केंद्रित रखते हैं।

प्रत्येक tool को individually enable या disable किया जा सकता है:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## तीन commands में शुरुआत

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

बस, आपका SQL MCP Server आपकी Customers table expose कर के चल पड़ा। Entity abstraction layer का मतलब है कि आप नाम और columns को alias कर सकते हैं, प्रत्येक role के लिए fields सीमित कर सकते हैं, और ठीक वही नियंत्रित कर सकते हैं जो एजेंट देखता है — बिना internal schema की जानकारी उजागर किए।

## Security की कहानी पक्की है

यहीं Data API builder की परिपक्वता काम आती है:

- **हर layer पर RBAC** — प्रत्येक entity परिभाषित करती है कि कौन से roles read, create, update, या delete कर सकते हैं, और कौन से fields दिखते हैं
- **Azure Key Vault integration** — connection strings और secrets सुरक्षित रूप से manage होते हैं
- **Microsoft Entra + custom OAuth** — production-grade authentication
- **Content Security Policy** — एजेंट raw SQL के बजाय एक controlled contract के माध्यम से interact करते हैं

Schema abstraction विशेष रूप से महत्वपूर्ण है। आपके internal table और column names एजेंट को कभी नहीं दिखते। आप entities, aliases, और descriptions परिभाषित करते हैं जो AI interaction के लिए उचित हों — आपके database ERD के लिए नहीं।

## Multi-database और multi-protocol

SQL MCP Server Microsoft SQL, PostgreSQL, Azure Cosmos DB, और MySQL को support करता है। और क्योंकि यह एक DAB feature है, आपको एक ही configuration से REST, GraphQL, और MCP endpoints एक साथ मिलते हैं। वही entity definitions, वही RBAC rules, वही security — तीनों protocols में।

DAB 2.0 में auto-configuration आपके database को inspect करके dynamically configuration बना सकती है, अगर आप rapid prototyping के लिए कम abstraction से comfortable हैं।

## मेरा नजरिया

AI एजेंट्स के लिए enterprise database access इसी तरह काम करनी चाहिए। "अरे LLM, मेरे लिए कुछ SQL लिखो और production पर चला दो" वाला तरीका नहीं। बल्कि: एक well-defined entity layer, deterministic query generation, हर कदम पर RBAC, caching, monitoring, और telemetry। यह सबसे अच्छे अर्थ में उबाऊ है।

.NET डेवलपर्स के लिए, integration की कहानी साफ है — DAB एक .NET tool है, MCP Server एक container के रूप में चलता है, और यह Azure SQL के साथ काम करता है, जिसे हम में से अधिकांश पहले से उपयोग कर रहे हैं। अगर आप ऐसे AI एजेंट्स बना रहे हैं जिन्हें data access चाहिए, तो यहाँ से शुरू करें।

## अंतिम बात

SQL MCP Server मुफ्त, open-source है, और कहीं भी चलता है। यह Microsoft की तरफ से AI एजेंट्स को सुरक्षित database access देने का prescriptive तरीका है। शुरुआत करने के लिए [पूरी पोस्ट](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) और [documentation](https://aka.ms/sql/mcp) देखें।
