---
title: 'Visual Studio Juni-Update: Nutzungstransparenz und MCP-Vertrauen sind die wichtigsten Funktionen'
date: 2026-07-24
author: 'Emiliano Montesdeoca'
description: 'Die wichtigsten Teile dieses Releases sind nicht kosmetisch; sie verbessern Governance und Vertrauen in KI-gestützte Workflows.'
tags:
  - visual-studio
  - github-copilot
  - mcp
  - cplusplus
  - developer-experience
---

Originalquelle: [Visual Studio June Update – Track Your Usage, Trust Your Tools](https://devblogs.microsoft.com/visualstudio/visual-studio-june-update-track-your-usage-trust-your-tools/)

Dieser Visual Studio-Release hat viele nette Quality-of-Life-Ergänzungen, aber zwei Updates ragen für ernsthafte Teams heraus: Copilot-Nutzungstransparenz und MCP-Vertrauensvalidierung.

Da sich die KI-gestützte Entwicklung hin zur nutzungsbasierten Abrechnung verschiebt, ist Transparenz keine reine Komfortmetrik mehr. Sie ist eine Planungsanforderung. Echtzeit-Nutzungsfenster und Schwellenwertwarnungen helfen Teams, Überraschungskostenspitzen zu vermeiden und gesündere Nutzungsnormen zu schaffen. Ohne diese Transparenz werden Diskussionen über Produktivitätssteigerungen schnell zu Spekulationen.

Der MCP-Vertrauensvalidierungsfluss ist strategisch noch wichtiger. Tooling-Ökosysteme werden dynamisch, und dynamische Systeme brauchen explizite Vertrauensgrenzen. Das Vergleichen von Startkonfiguration und Capability-Fingerabdrücken mit vertrauenswürdigen Baselines ist genau die richtige Standardhaltung.

Meine starke Meinung: Jede KI-integrierte IDE sollte dies standardmäßig tun. Stille Capability-Drift in Tool-Servern ist ein inakzeptables Risiko für Unternehmensumgebungen.

Der C++-Modernisierungsagent GA für MSVC-Upgrades ist ein weiterer praktischer Gewinn. Upgrade-Arbeit wird normalerweise aufgeschoben, weil sie mühsam und riskant ist. Geführte und automatisierte Pfade innerhalb der IDE zu haben, senkt die Hürde, aktuell zu bleiben, besonders für größere Legacy-Codebasen.