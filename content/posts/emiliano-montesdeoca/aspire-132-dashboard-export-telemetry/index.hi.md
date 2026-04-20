---
title: "Aspire 13.2 के डैशबोर्ड में अब Telemetry API है — और यह सब कुछ बदल देता है"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 में स्मार्ट telemetry export, traces और logs के लिए programmable API, और GenAI visualization improvements आए हैं। जानें यह आपके debugging workflow के लिए क्यों मायने रखता है।"
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

अगर आप .NET Aspire के साथ distributed apps बना रहे हैं, तो आप पहले से जानते हैं कि dashboard पूरे experience की सबसे अच्छी चीज़ है। Aspire 13.2 ने इसे काफी बेहतर बनाया है।

## Telemetry export करना अब आसान है

Aspire 13.2 एक **Manage logs and telemetry** डायलॉग जोड़ता है जहाँ आप:
- सभी telemetry clear कर सकते हैं
- Selected telemetry को standard OTLP/JSON format में ZIP file में export कर सकते हैं
- उस ZIP को किसी भी Aspire dashboard में re-import कर सकते हैं

वह आखिरी part killer feature है। आप एक bug reproduce करें, telemetry export करें, अपने work item में attach करें, और आपका teammate इसे अपने dashboard में import करके देख सकता है कि आपने क्या देखा था।

## Telemetry API असली game changer है

Dashboard अब `/api/telemetry` के तहत एक HTTP API expose करता है:
- `GET /api/telemetry/resources` — telemetry वाले resources की list
- `GET /api/telemetry/spans` — filters के साथ spans query करें
- `GET /api/telemetry/logs` — filters के साथ logs query करें
- `GET /api/telemetry/traces` — traces list करें

यह `aspire agent mcp` और `aspire otel` CLI commands को power करता है।

## GenAI Telemetry व्यावहारिक हुई

VS Code Copilot chat और Copilot CLI `OTEL_EXPORTER_OTLP_ENDPOINT` configure करने को support करते हैं — Aspire dashboard पर point करें और आप अपने AI एजेंट्स को real time में telemetry के जरिए सोचते देख सकते हैं।

## समापन

Aspire 13.2 dashboard को "nice debugging UI" से "programmable observability platform" में बदलता है। [aspire.dev](https://aspire.dev) देखें।
