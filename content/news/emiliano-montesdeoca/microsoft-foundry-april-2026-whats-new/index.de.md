---
title: "Microsoft Foundry April 2026: Foundry Local GA, GPT-5.5, CodeAct mit Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Aprils Foundry-Zusammenfassung ist umfangreich: Foundry Local erreicht GA, GPT-5.5 kommt, Agent Framework erhält OpenTelemetry-Tracing, CodeAct führt Python in Hyperlight-Micro-VMs aus, und das Agent Monitoring Dashboard ist verfügbar."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Ein geschäftiger Monat für Microsoft Foundry. Hier sind die wichtigsten Ankündigungen.

## Foundry Local ist Allgemein Verfügbar

Foundry Local — Microsofts plattformübergreifende lokale KI-Laufzeit — wechselt von der Vorschau zu GA auf Windows, macOS (Apple Silicon) und Linux x64. Produktionsreife lokale Modellinferenz mit einem entwicklerfreundlichen SDK. Version 1.1 fügt Transkriptions-, Embeddings- und Responses-API-Unterstützung hinzu.

## GPT-5.5

Das neueste Modell der GPT-5-Familie ist jetzt in Foundry verfügbar. Standardquota für Tier 5- und Tier 6-Abonnements. Wenn Sie mit früheren GPT-5-Varianten gearbeitet haben, lohnt es sich, dies für Ihre Anwendungsfälle zu evaluieren.

## Agent Framework Tracing in Foundry

Diesen Monat werden zwei Tracing-Funktionen in der Vorschau bereitgestellt:

**Microsoft Agent Framework Tracing** — MAF-Agenten können jetzt OpenTelemetry-Traces in Foundry ausgeben. Debuggen Sie das Agentenverhalten, verfolgen Sie die mehrstufige Ausführung, zeigen Sie Latenz und Fehler über Tool-Aufrufe hinweg an. Dies schließt eine echte Lücke: zu wissen, *was Ihr Agent tatsächlich getan hat* in der Produktion, nicht nur, was er zurückgegeben hat.

**Hosted-Agent-Tracing** — Sitzungen, Tool-Aufrufe und Ausführungsschritte von gehosteten Agenten erscheinen ebenfalls in Foundry-Traces. Dieselbe Observability-Geschichte erstreckt sich auf die gehostete Ebene.

## CodeAct mit Hyperlight (Alpha)

Dies ist die technisch interessanteste Ergänzung: Agent Framework kann jetzt Python-Code in [Hyperlight](https://github.com/hyperlight-dev/hyperlight)-Micro-VMs ausführen.

CodeAct ist das Muster, bei dem ein Agent Python-Code als Tool generiert und ausführt. Die offensichtliche Sorge ist die Sicherheit — Sie führen vom Modell generierten Code aus. Hyperlights Micro-VMs bieten Isolation auf Prozessebene mit nahezu nativer Startzeit, was sandboxed Code-Ausführung ohne den Overhead vollständiger Container oder VMs praktisch macht.

Für agentische Workflows, bei denen Code-Ausführung notwendig ist, ist dies eine erhebliche Sicherheitsverbesserung gegenüber dem Ausführen von Code im Host-Prozess.

## Agent Monitoring Dashboard (Vorschau)

Ein einheitliches Betriebs-Dashboard, das Token-Nutzung, Latenz, Ausführungserfolgsrate und Evaluator-Scores in einer Ansicht kombiniert. Der Unterschied zu regulären Observability-Dashboards: Es enthält Evaluierungsergebnisse zusammen mit Betriebsmetriken, sodass Sie "der Agent ist langsamer" mit "Evaluator-Scores sind gesunken" korrelieren können — oder bestätigen, dass sie nicht zusammenhängen.

## Benutzerdefinierte Evaluatoren für Kontinuierliche Evaluierung (Vorschau)

Sie können jetzt eigene code- oder prompt-basierte Evaluatoren in kontinuierliche Evaluierungspipelines einbringen. Bisher war die kontinuierliche Evaluierung auf integrierte Evaluatoren beschränkt. Benutzerdefinierte Evaluatoren ermöglichen es Ihnen, teamspezifische Qualitätskriterien in Ihrer Produktions-Überwachungsschleife durchzusetzen.

## Agenteninventar in der Steuerungsebene

Die Operate-Ansicht der Foundry-Steuerungsebene zeigt jetzt alle unterstützten Agenten über ein Abonnement hinweg: Foundry-Agenten, Azure SRE Agent, Logic Apps-Agentenschleifen und registrierte benutzerdefinierte Agenten. Eine Ansicht, um zu verstehen, was bereitgestellt ist und wo.

Originalbeitrag: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
