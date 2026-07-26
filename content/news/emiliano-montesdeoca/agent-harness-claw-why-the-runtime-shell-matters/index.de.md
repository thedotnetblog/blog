---
title: "Agent-Harnesses sind wichtig, weil Prompts nicht ausreichen"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "Die neue Agent-Framework-Claw-und-Harness-Walkthrough ist eine nützliche Erinnerung daran, dass echte Agenten eine Laufzeitumgebung um das Modell herum brauchen: Werkzeuge, Planung, Speicher, Sitzungen und eine praktische Ausführungsschleife."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Einer der häufigsten Fehler in der Agent-Entwicklung ist zu glauben, der Prompt sei das Produkt.

Ist er nicht.

Die neue **Agent-Harness-und-Claw**-Walkthrough des Microsoft Agent Framework-Teams ist wertvoll, weil sie den Fokus auf den Teil legt, der wirklich bestimmt, ob sich ein Agent nutzbar anfühlt: die Laufzeithülle um das Modell.

Dazu gehören:

- Werkzeuge (Tools)
- Planung (Planning)
- Sitzungszustand (Session State)
- Speicher (Memory)
- Ausführungsmodi
- eine nutzbare Konsole oder Schnittstelle für Iterationen

Dort hören Agenten auf, clevere Demos zu sein, und fühlen sich an wie Software.

## Das Harness-Muster ist praxistauglich

Was mir gefällt, ist, wie zugänglich die Idee ist.

Sie beginnen mit einem Chat-Client.

Dann wickeln Sie ihn in ein Harness mit Anweisungen und Werkzeugen.

Dann führen Sie ihn durch eine Shell aus, die Planung, Aufgaben, Sitzungen und Streaming-Interaktion unterstützt.

Das ist ein gesundes Muster, weil es Zuständigkeiten klar trennt:

- das Modell übernimmt die logische Schlussfolgerung
- das Harness übernimmt das Laufzeitverhalten
- die App entscheidet, welche Werkzeuge und Erfahrungen wichtig sind

## Das passt sehr gut zur Arbeitsweise von .NET-Entwicklern

Die Harness-Idee passt auch gut zur .NET-Denkweise.

Wir arbeiten in der Regel besser, wenn Laufzeitverhalten explizit und komponierbar ist. Middleware, Pipelines, Optionen, Provider und Adapter fühlen sich in dieser Welt natürlich an.

Deshalb glaube ich, dass Agent Framework gute Chancen hat, bei .NET-Entwicklern anzukommen. Es zwingt niemanden in eine magische Abstraktion. Es gibt Ihnen strukturierte Laufzeitbausteine, die Sie zusammenschalten können.

## Meine Meinung

Der nützlichste Teil dieses Beitrags ist die Erinnerung daran, dass Agenten mehr brauchen als ein gutes Modell und einen cleveren Anweisungstext.

Sie brauchen eine Laufzeithülle, die ihnen Struktur, Speicher, Werkzeugzugriff, Planung und eine brauchbare Entwicklerschleife bietet.

Das gibt Ihnen das Harness.

Und ehrlich gesagt, deshalb lohnt es sich, auf dieses Muster zu achten.

Originalbeitrag: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)