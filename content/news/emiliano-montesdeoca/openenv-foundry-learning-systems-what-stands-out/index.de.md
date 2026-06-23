---
title: "OpenEnv und Foundry treiben die Diskussion über statische Agents hinaus"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "Die neue OpenEnv-und-Foundry-Geschichte hat weit mehr mit zu tun als mit Schlagworten rund um Reinforcement Learning. Es geht eigentlich um Agentensysteme, die sich anhand echter Geschäftsergebnisse über die Zeit evaluieren, optimieren und verbessern lassen."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *Dieser Beitrag wurde automatisch übersetzt. Lies das Original [hier]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

Die meisten Agentendiskussionen enden immer noch bei der Inferenz.

Kann das Modell die Eingabe beantworten? Kann es das Tool aufrufen? Kann es die Aufgabe einmal erledigen?

Die neue **OpenEnv + Foundry**-Diskussion ist interessant, weil sie das Gespräch in eine ehrgeizigere Richtung lenken will: **Wie baut man ein Agentensystem, das sich im Laufe der Zeit tatsächlich verbessert?**

Das ist eine deutlich bessere Frage.

## Der entscheidende Wandel führt von Antworten zu Lernschleifen

Der Foundry-Beitrag rahmt das Problem über Umgebungen, Evals, Rubrics, Optimierung und Post-Training ein.

Das lässt sich in einem Satz zusammenfassen:

**Das Ziel ist nicht mehr nur, einen Agenten auszuführen, sondern eine Schleife zu besitzen, die den Agenten anhand deiner tatsächlichen Ergebnisse misst und verbessert.**

Genau darauf sollten Entwickler meiner Meinung nach achten.

Denn sobald man es so sieht, ist das dauerhafte Asset nicht nur das Modell oder der Prompt. Es ist das System darum herum:

- die Umgebung, in der es handelt
- die Rubrik, die es bewertet
- die Traces, die erklären, was passiert ist
- der Optimierer, der die Konfiguration verbessert

Das ist eine deutlich unternehmensreifere Denkweise.

## Warum das wichtig ist, auch wenn du keine RL-Forschung machst

Seien wir ehrlich: Begriffe wie OpenEnv, Post-Training und World-Modeling können viele Entwickler sofort abschalten.

Die praktische Erkenntnis ist aber einfacher als die Terminologie.

Selbst wenn du nie direkt eine Trainingsschleife anfasst, prägt diese Arbeit die Plattformgeschichte für die zukünftige Agentenentwicklung:

- Evaluierungen werden erstklassig
- Optimierung wird kontinuierlich statt gelegentlich
- Umgebungen werden zu wiederverwendbaren Assets
- besseres Agentenverhalten wird messbar, nicht nur „fühlt sich in Demos besser an“

Das ist ein großer Schritt nach vorn.

## Meine Einschätzung

Das Klügste an dieser Ankündigung ist nicht irgendein einzelnes Forschungsdetail.

Es ist der Rahmen.

Microsoft versucht klar, das Ökosystem von statischer Prompt-Programmierung hin zu **outcome-driven Agentensystemen** zu verschieben. Systeme, die sich evaluieren, abstimmen, steuern und schrittweise verbessern lassen.

Dort liegt der echte Plattformwert.

Und wenn du heute Agents baust, selbst auf Anwendungsebene, lohnt es sich, diese Entwicklung im Blick zu behalten.

Originalbeitrag: [Outcome-getriebene Lernsysteme: Enterprise-RL mit OpenEnv und Foundry](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)