---
title: "Mission Control für Coding-Agents: Eine einheitliche Erfahrung in VS Code"
description: "VS Code führt lokale, Cloud-, CLI- und Third-Party-Coding-Agents in Agent Sessions zusammen, damit Entwickler autonome Arbeiten verfolgen, unterbrechen und koordinieren können."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> *Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

# Mission Control für Coding-Agents: Eine einheitliche Erfahrung in VS Code

Ein einzelner Coding-Assistent ist leicht zu verstehen. Mehrere Agents, die an verschiedenen Orten arbeiten, nicht.

Ein Agent läuft lokal in VS Code. Ein anderer arbeitet in der Cloud an einem GitHub-Issue. Ein CLI-Agent existiert im Terminal. Ein Third-Party-Coding-Agent kann ein anderes Session-Modell und unterschiedliche Limits haben. Ohne eine gemeinsame Ansicht verbringen Entwickler mehr Zeit damit, ihre Arbeit zu verfolgen, als sie zu überwachen.

VS Code löst dieses Koordinationsproblem mit einer einheitlichen Agent-Erfahrung: Agent Sessions. Dies ist ein Ort, um Agents zu starten, ihren Status zu sehen, ihre Gespräche zu öffnen und einzugreifen, wenn sich der Plan ändert.

Es geht weniger darum, einen weiteren Agent hinzuzufügen, sondern vielmehr darum, mehrere Agents handhabbar zu machen.

## Eine Ansicht für verschiedene Arten von Arbeit

Der Originalartikel beschreibt vier verschiedene Teilnehmer: lokales GitHub Copilot, Copilot Coding Agent in der Cloud, GitHub Copilot CLI und OpenAI Codex für berechtigte Copilot-Abonnenten.

Sie haben unterschiedliche Stärken:

- Ein lokaler Agent kann den aktuellen Workspace inspizieren und schnelle Änderungen vornehmen.
- Ein Cloud-Coding-Agent kann asynchron an einem Issue arbeiten und einen Pull Request öffnen.
- Ein CLI-Agent passt zu Terminal-lastigen Workflows und Betriebsbefehlen.
- Ein anderer Anbieter kann ein anderes Modell oder einen anderen Reasoning-Stil bieten.

Agent Sessions gibt diesen Aufgaben eine gemeinsame Basis. Sie können sehen, was läuft, was es tut, und wo Sie das Gespräch fortsetzen können.

Diese Sichtbarkeit ist wichtig, da autonome Arbeit Koordination nicht aufhebt. Sie macht Koordination zu einer First-Class-Engineering-Aufgabe.

## Unterbrechungen sind Teil des Workflows

Der Originalartikel macht eine einfache Beobachtung: „Es ist üblich, eine Eingabeaufforderung zu senden und sich dann zu realisieren, dass Sie etwas Wichtiges vergessen haben." Zuvor war die Wahl oft, zu warten oder abzubrechen. Mit Chat-Editoren können Sie eine aktive Session öffnen und Informationen hinzufügen, während der Agent arbeitet.

Das ist näher an echter Zusammenarbeit. Anforderungen ändern sich. Ein Test offenbart eine Annahme. Ein Reviewer bemerkt, dass eine API rückwärtskompatibel bleiben muss. Der nützliche Agent ist nicht der, der nie einer Korrektur bedarf; es ist der, der Korrektur aufnehmen kann, ohne die ganze Aufgabe zu verlieren.

Für .NET-Arbeiten könnte eine Unterbrechung so einfach sein wie:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

Die Anweisung ist kurz, weil das Repository bereits den größeren Kontext trägt. Die Session ist der Ort, um die Richtung zu korrigieren, nicht um das gesamte System zu rekapitulieren.

## Benutzerdefinierte Agents verwandeln Team-Gewohnheiten in Rollen

VS Code führt auch spezialisierte Agents wie Plan ein. Anstatt sofort zu implementieren, stellt ein Planning-Agent Fragen zum Umfang, zu Komponenten, Bibliotheken und Einschränkungen, bevor er eine Implementierungsspezifikation produziert.

Dieses Muster ist über einen eingebauten Agent hinaus nützlich. Ein Team kann fokussierte Rollen definieren:

- **Research** sammelt Belege und schreibt einen kurzen Decision Record.
- **Review** prüft eine Änderung gegen Repository-Konventionen.
- **Testing** identifiziert fehlende Fälle und schlägt einen Testplan vor.
- **Architecture** vergleicht Optionen, ohne Dateien zu ändern.

Eine kleine benutzerdefinierte Agent-Definition könnte so aussehen:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

Der nützliche Teil ist nicht das YAML. Es ist die explizite Trennung der Verantwortlichkeiten. Ein Planning-Agent sollte nicht leise Produktionscode bearbeiten. Ein Review-Agent sollte nicht das Design umschreiben, das er evaluieren soll.

## Subagents reduzieren Kontext-Kollisionen

Lange Konversationen sammeln unrelevanten Kontext. Subagents bieten einen isolierten Workspace für eine begrenzte Forschungsaufgabe, dann wird das Ergebnis zur Hauptsession zurückgegeben.

Das passt gut zu Fragen wie:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

Der Hauptagent konzentriert sich auf die Implementierung, während der Forschungsagent eine engere Frage bearbeitet. Das gleiche Prinzip gilt für Teams: klare Delegation erzeugt bessere Ergebnisse als mehrere Agents mit überlappender Autorität.

## Der Vorbehalt: Mehr Agents bedeuten mehr Koordination

Agent Sessions können Aktivität anzeigen, können aber nicht Eigentumskonflikte lösen. Zwei Agents, die den gleichen Bereich bearbeiten, können immer noch ein Merge-Problem verursachen. Ein Cloud-Agent und ein lokaler Agent können inkompatible Annahmen treffen. Ein benutzerdefinierter Agent kann eine Empfehlung produzieren, die ein anderer Agent ignoriert.

Setzen Sie Grenzen:

1. Ein Agent besitzt die Implementierung für einen gegebenen Branch.
2. Research-Agents geben Artefakte zurück, nicht ungeverfolgte Änderungen.
3. Pull Requests bleiben die Review-Grenze.
4. Agent-Namen und Prompts geben an, was sie ändern dürfen.
5. Session-Ausgabe wird beibehalten, wenn sie eine wichtige Entscheidung erklärt.

## Meine Ansicht

Die Multi-Agent-Zukunft ist keine Warteschlange von Chat-Fenstern. Es ist ein kleines Team mit Rollen, Übergaben und Verantwortlichkeit.

Agent Sessions ist wertvoll, weil es diese Realität anerkennt. Es gibt Entwicklern eine Kontrollfläche für Arbeit, die bereits über Editor, Terminal und Cloud stattfindet. Der nächste Produktivitätsgewinn wird weniger davon kommen, mehr Agents zu haben, sondern vielmehr davon, ihre Grenzen deutlich zu machen.

Für ein .NET-Team würde ich mit einem Planning-Agent und einem Implementation-Agent starten. Verwenden Sie die Planning-Ausgabe als Issue- oder Pull-Request-Spezifikation, dann lassen Sie den Implementation-Agent innerhalb dieser Grenze arbeiten. Messen Sie die Überarbeit, bevor Sie mehr Rollen hinzufügen.

Die beste Mission Control ist immer noch die, die Eigentümerschaft offensichtlich macht.
