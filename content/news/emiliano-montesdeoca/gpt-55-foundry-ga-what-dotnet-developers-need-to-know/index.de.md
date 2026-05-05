---
title: "GPT-5.5 ist da und kommt zu Azure Foundry — Was .NET-Entwickler Wissen Müssen"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 ist allgemein verfügbar in Microsoft Foundry. Die Progression von GPT-5 zu 5.5, was sich wirklich verbessert hat und wie du heute damit anfängst."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Microsoft hat gerade bekannt gegeben, dass [GPT-5.5 allgemein in Microsoft Foundry verfügbar ist](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Wenn du Agenten auf Azure aufgebaut hast, ist das das Update, auf das du gewartet hast.

## Die GPT-5-Progression

- **GPT-5**: vereinte Reasoning und Geschwindigkeit in einem einzigen System
- **GPT-5.4**: stärkeres Multi-Step-Reasoning, frühe agentische Fähigkeiten für Unternehmen
- **GPT-5.5**: tieferes Langkontext-Reasoning, zuverlässigere agentische Ausführung, bessere Token-Effizienz

## Was sich wirklich geändert hat

**Verbessertes agentisches Coding**: GPT-5.5 hält Kontext über große Codebasen hinweg, diagnostiziert Architekturfehler und antizipiert Testanforderungen. Das Modell überlegt, *was sonst noch* eine Korrektur beeinflusst.

**Token-Effizienz**: Höherwertigere Ausgaben mit weniger Tokens und weniger Wiederholungen. Direkt niedrigere Kosten und Latenz für Produktions-Deployments.

**Langkontext-Analyse**: Verarbeitet umfangreiche Dokumente und Multi-Session-Historien ohne den Faden zu verlieren.

## Preise

| Modell | Eingabe ($/M Tokens) | Gecachte Eingabe | Ausgabe ($/M Tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Warum Foundry wichtig ist

Foundry Agent Service ermöglicht es, Agenten in YAML zu definieren oder sie mit Microsoft Agent Framework, GitHub Copilot SDK, LangGraph oder OpenAI Agents SDK zu verbinden — und sie als isolierte gehostete Agenten mit persistentem Dateisystem, eigener Microsoft Entra-Identität und Scale-to-zero-Preisen auszuführen.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Du bist ein hilfreicher Assistent.", name: "MeinAgent");
```

Sieh dir die [vollständige Ankündigung](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) für alle Details an.
