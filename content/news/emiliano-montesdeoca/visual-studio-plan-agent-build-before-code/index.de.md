---
title: "Der neue Plan-Agent in Visual Studio löst ein sehr reales KI-Workflow-Problem"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "Der neue Plan-Agent in Visual Studio ist wichtig, weil er vor der Implementierung eine strukturierte Planungsphase schafft, genau das, was größere Features und Refactorings oft brauchen."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Dieser Beitrag wurde automatisch übersetzt. Lies das Original [hier]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

Einer der frustrierendsten KI-Coding-Workflows ist der, bei dem die Implementierung viel zu schnell beginnt.

Der Code kann sogar technisch vollkommen in Ordnung sein, aber er löst die falsche Version des Problems, das du im Kopf hattest.

Du wolltest ein Refactoring. Es begann mit einem Rewrite.
Du wolltest eine begrenzte Verbesserung. Es berührte die halbe Anwendung.
Du wolltest die Optionen durchsprechen. Es sprang direkt zu Dateiänderungen.

Deshalb ist der neue **Plan-Agent** in Visual Studio eine so nützliche Ergänzung.

## Das löst ein echtes Workflow-Problem, nicht nur ein kosmetisches

Der Originalbeitrag beschreibt eine sehr bekannte Situation: "**Der Code ist nicht falsch ... er ist nur nicht das, was du wolltest.**"

Dieser Satz ist perfekt.

Denn die Schwachstelle in vielen KI-gestützten Workflows ist nicht, ob das Modell Code erzeugen kann. Es ist, ob der Workflow genug Raum schafft, um sich vor dem Implementieren auf die beabsichtigte Form der Arbeit zu einigen.

Das ist besonders wichtig für:

- größere Features
- unbekannte Codebasen
- nicht triviale Refactorings
- architekturkritische Änderungen
- Arbeit, die vor dem Editieren ein Team-Review braucht

In solchen Situationen ist der direkte Sprung in die Implementierung oft der falsche Schritt.

## Planung ist kein Overhead, wenn die Aufgabe real ist

Ich denke, Teams unterschätzen manchmal, wie viel Zeit sie verlieren, wenn sie zu früh mit der Implementierung beginnen.

Wenn der Agent:

- die falschen Dateien anfasst
- den falschen Ansatz wählt
- eine wichtige Einschränkung übersieht
- einen nötigen Edge Case ignoriert

dann wird der vermeintlich „schnelle“ Start insgesamt zum langsameren Workflow.

Deshalb gefällt mir diese Funktion.

Sie schafft Raum für:

- klärende Fragen
- das Entwerfen eines Plans
- das direkte Bearbeiten des Plans
- das Teilen des Plans, bevor Codeänderungen beginnen

Das ist keine Bürokratie. Das ist oft einfach gute Ingenieursarbeit.

## Die Markdown-Plan-Datei ist eine kluge Wahl

Ein Detail, das ich besonders mag, ist, dass jeder Plan unter `.copilot/plans/plan-{title}.md` gespeichert wird.

Dadurch wird der Planungsschritt greifbar.

Der Plan steckt nicht in einem Chat-Transcript fest. Er wird zu etwas, das du:

- prüfen
- bearbeiten
- gedanklich versionieren
- mit dem Team besprechen
- bewusster in die Implementierung überführen

Das lässt die Funktion deutlich ernster wirken als nur eine vorübergehende Einleitung vor der Codegenerierung.

## Hier beginnen KI-Workflows, den Teamprozess zu respektieren

Ich denke, das ist eines der stärkeren Zeichen dafür, dass diese Tools reifer werden.

Die besten KI-Entwickler-Workflows sind nicht diejenigen, die alle Zwischenschritte entfernen. Es sind diejenigen, die die richtigen Zwischenschritte verbessern.

Und Planung ist einer dieser Schritte.

Wenn der Plan stark ist, wird Implementierung einfacher.
Wenn der Plan schwach ist, wird Implementierung laut und chaotisch.

Diese Funktion erkennt das direkt an.

## Meine Einschätzung

Das ist nicht nur eine KI-Nettheit.

Es ist eine Workflow-Verbesserung.

Und bei echten Features und echten Refactorings ist es genau die Art von Verbesserung, die viel unnötiges Churn, Review-Lärm und „Das meinte ich nicht“-Nacharbeit sparen kann.

Ich denke, immer mehr Agentenerlebnisse werden irgendwann etwas wie das brauchen.

Visual Studio ist dort früher angekommen, und zwar auf eine nützliche Art.

Originalbeitrag: [Vor dem Bauen planen: den Plan-Agenten in Visual Studio vorstellen](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)