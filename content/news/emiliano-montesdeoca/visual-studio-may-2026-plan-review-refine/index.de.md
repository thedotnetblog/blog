---
title: "Das Mai-Update von Visual Studio dreht sich eigentlich um bessere Kontrolle zwischen Idee und Änderung"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "Das Visual-Studio-Update im Mai bringt den Plan-Agenten, bessere Skill-Verwaltung, Sichtbarkeit des Kontextfensters und stärkere Multi-File-Diff-Erlebnisse. Das gemeinsame Thema ist mehr Kontrolle über den KI-gestützten Inner Loop."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *Dieser Beitrag wurde automatisch übersetzt. Lies das Original [hier]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}).* 

Das Interessanteste am Visual-Studio-Update im Mai ist nicht eine einzelne Funktion.

Es ist die gemeinsame Richtung.

Dieses Release verbessert weiter den Raum zwischen:

- einer Idee
- einem Plan
- einer generierten Änderung
- einer Überprüfung
- einem verfeinerten Ergebnis

Genau dieser Teil der KI-gestützten Entwicklung entscheidet darüber, ob sich der Workflow vertrauenswürdig oder chaotisch anfühlt.

## Die Funktionsliste ist vielfältig, aber die Absicht ist konsistent

Auf dem Papier umfasst dieses Release eine Mischung aus Dingen:

- der neue Plan-Agent
- Verbesserungen bei der Skill-Verwaltung
- Sichtbarkeit des Kontextfensters
- Multi-File-Summary-Diff
- Aufräumen des Copilot-bezogenen Workflows
- MSVC-Updates auf der C++-Seite

Das kann wie ein Sammelsurium wirken.

Ich denke das nicht.

Der rote Faden ist ziemlich klar: **Visual Studio versucht, Entwicklern mehr Kontrolle über KI-gestützte Arbeit zu geben, ohne sie auszubremsen.**

Genau dieses Trade-off sollte man anstreben.

## Der Plan-Agent ist das philosophische Zentrum des Releases

Auch wenn andere Funktionen wichtig sind, halte ich den Plan-Agenten immer noch für den aufschlussreichsten Teil dieses Updates.

Er macht etwas explizit, das viele von uns beim Einsatz von Coding-Agents gespürt haben:

schnell zu starten ist nicht dasselbe wie effektiv voranzukommen.

Das Release betont das noch einmal, indem es Planung, Überprüfung und kontrollierte Implementierung zu einer natürlicheren Abfolge macht.

Das ist gesund.

## Die Multi-File-Diff-Arbeit ist still und leise eine große Verbesserung

Ich denke auch, dass das Multi-File-Summary-Diff mehr Anerkennung verdient, als es wahrscheinlich bekommen wird.

Wenn Agents mehrere Dateien auf einmal ändern, wird das Review-Erlebnis zum Produkt.

Wenn sich das Überprüfen der Änderungen chaotisch anfühlt, sinkt das Vertrauen der Entwickler in den Workflow.

Wenn sich das Überprüfen der Änderungen stimmig anfühlt, nutzen Entwickler das Tool eher weiter.

Deshalb ist eine einheitliche Summary-Ansicht so wichtig. Sie senkt die kognitive Last, wenn man generierte Arbeit akzeptieren oder ablehnen soll.

## Der Kontextfenster-Indikator ist klüger, als er klingt

Ich mag auch den Kontextnutzungsindikator.

Das klingt vielleicht wie ein kleines Detail, aber es löst ein sehr reales KI-Workflow-Problem: nicht zu wissen, wann das Tool beginnt, den früheren Teil des Gesprächs zu vergessen.

Das sichtbar zu machen, ist eine gute Designentscheidung.

Es vergrößert das Modellkontextfenster nicht magisch. Aber es macht die Grenze sichtbar, und das ist oft das Nächstbeste.

## Meine Einschätzung

Dieses Update geht im Kern darum, Entwicklern mehr Sichtbarkeit und Kontrolle über die KI-gestützte Schleife zu geben.

Nicht mehr Neuheit.
Nicht mehr Chaos.
Mehr Kontrolle.

Das ist genau der richtige Bereich, um zu investieren, wenn KI-Tools in einem ernsthaften IDE-Workflow vertrauenswürdiger wirken sollen.

Originalbeitrag: [Visual-Studio-Update im Mai — Planen, Überprüfen, Verfeinern](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)