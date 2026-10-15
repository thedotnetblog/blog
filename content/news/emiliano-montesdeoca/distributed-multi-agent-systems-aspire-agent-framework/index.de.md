---
title: "Aspire + Agent Framework beginnt wie der echte Multi-Agent-Stack auszusehen"
date: 2026-06-13
author: "Emiliano Montesdeoca"
description: "Das neue AlpineAI-Beispiel zeigt, was passiert, wenn Aspire und Microsoft Agent Framework für ein echtes verteiltes Multi-Agent-System verwendet werden. Der wichtige Teil ist nicht die Ski-Demo. Es ist das Architekturmuster dahinter."
tags:
  - Aspire
  - Agent Framework
  - .NET
  - Microsoft Foundry
  - Architecture
---

Multi-Agent-Demos sind derzeit überall.

Das Problem ist, dass viele von ihnen genau vor dem Teil aufhören, der im echten Leben wehtut: Deployment-Form, Service-Verkabelung, Health, Telemetrie, Laufzeitgrenzen und das schlichte Chaos verteilter Systeme.

Deshalb ist die neue **Aspire + Microsoft Agent Framework**-Beispiel beachten.

Nein, der interessante Teil ist nicht das Skiresort-Concierge-Szenario.

Der interessante Teil ist, dass das Beispiel ein viel realistischeres Muster für den Bau eines verteilten Agent-Systems zeigt mit:

- benutzerdefiniert gehosteten Agenten
- Prompt-Agenten
- mehreren Laufzeiten
- Servicereferenzen
- Live-Datenquellen
- Beobachtbarkeit und Deployment-Struktur

Das ist die wahre Geschichte.

## Aspire macht den schwierigen Teil, den Menschen normalerweise im Kopf behalten

Was mir hier am besten gefällt, ist nicht einmal die Agent-Logik. Es ist die Tatsache, dass der **Anwendungsgraph explizit ist**.

Aspire wird verwendet, um zu beschreiben:

- welche Dienste existieren
- wovon sie abhängen
- welche Modell-Deployments sie benötigen
- welche Laufzeit jeder Dienst verwendet
- welche Health- und Deployment-Beziehungen existieren

Das ist wichtig, weil verteilte Agent-Systeme schnell unübersichtlich werden. Wenn die Topologie nur in den Köpfen der Menschen und in zufälligen Setup-Dokumenten existiert, wird Ihr System sofort fragil.

## Meine Meinung

Das Wichtige, was dieses Beispiel beweist, ist nicht, dass Multi-Agent-Apps möglich sind. Das wussten wir bereits.

Es beweist, dass der Microsoft-Stack beginnt, eine kohärente Antwort auf die nächste Frage zu bieten:

**wie baut man Multi-Agent-Systeme, die sich noch bedienbar anfühlen?**

Aspire für den Graphen. Agent Framework für die Laufzeitabstraktionen. Foundry für verwaltete KI-Ressourcen und Hosting. Diese Kombination beginnt sich weniger experimentell und mehr wie eine echte Plattformgeschichte anzufühlen.

Das ist es, was ich hier beobachten würde.

Originalquelle: [Distributed multi-agent systems with Aspire and Microsoft Agent Framework](https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework/)