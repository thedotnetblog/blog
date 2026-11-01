---
title: "Microsoft Foundry Juni 2026: Von Feature-Drops zu einer gelenkten Agentenplattform"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Die Juni-Foundry-Updates signalisieren einen Plattformübergang: Distribution, Tooling, Memory, Beobachtbarkeit und Optimierung konvergieren zu einem Enterprise-tauglichen Agentenbetriebs-Stack."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

Die Juni 2026 Foundry-Welle ist nicht nur eine weitere monatliche Zusammenfassung. Sie markiert einen Reifegradübergang von "coole Agenten bauen" zu "Agenten als gelenkte Unternehmenssysteme betreiben." Diese Unterscheidung ist wichtiger als jede einzelne Funktion.

Originalquelle: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Drei Updates definieren den Wandel. Erstens erreichte die Agentenveröffentlichung für Microsoft 365 Copilot und Teams GA, was die Verteilung von kundenspezifischen Integrationsprojekten zu einer meinungsstarken Deployment-Bahn verschiebt. Zweitens erhielten Toolboxes stärkere Erkennungs- und Ausführungskontrollen, einschließlich Toolsuchen und Routinen. Drittens wurde Beobachtbarkeit plus Optimierung zu einem bewussten geschlossenen Kreislauf, nicht zu einem nachträglichen Einfall.

Meine Meinung: Dies ist das wichtigste Muster im Release. Tracing, Evaluierung, Optimierung und kontrollierte Einführung bilden das minimal lebensfähige Betriebsmodell für nicht-deterministische Systeme. Wenn Sie nur eines dieser Stücke haben, haben Sie Telemetrie oder Tuning, aber keine Governance.

Claude GA in Foundry ist auch strategisch, aber hauptsächlich nicht wegen der Modellqualität. Der größere Wert ist die Unternehmensintegration: Entra-Auth, RBAC, Abrechnungskontinuität und Policy-Ausrichtung. Teams, die von direkten Modell-Endpunkten zu Foundry wechseln, sollten dies als operative Konsolidierung betrachten, nicht nur als Anbieterwechsel.