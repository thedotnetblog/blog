---
title: "FIDES ist genau die deterministische Agenten-Sicherheitsgeschichte, von der ich mehr sehen möchte"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Die neuen FIDES-Funktionen in Agent Framework sind wichtig, weil sie die Abwehr von Prompt Injection weg von Heuristiken und hin zu durchsetzbarer Richtlinie auf Basis markierter Inhalte und Middleware-Prüfungen verschieben."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "index.md" >}}).*

Prompt-Injection-Abwehr fühlt sich oft an, als würde sie auf unsicherem Boden stehen.

Du fügst einen stärkeren Systemprompt hinzu. Du fügst einen Filter hinzu. Du legst ein paar Allowlists an. Und hoffst, dass die nächste seltsame Eingabe die Annahmen nicht zerstört.

Deshalb ist **FIDES** interessant.

Der starke Teil der Geschichte ist, dass er Sicherheit in Richtung etwas Deterministischeres verschiebt:

- Labels auf Inhalten
- Weitergabe der Labels durch den Workflow
- Durchsetzung über Middleware, bevor privilegierte Tools ausgeführt werden
- klare Richtliniengrenzen dafür, was untrusted context beeinflussen darf

## Der Ausgangsartikel ist auf die richtige Weise klar

Er beginnt mit dem Satz, dass Prompt Injection "**das Risiko Nummer 1 in den OWASP LLM Top 10**" sei.

Gut.

Ich mag diese Art von Klartext hier, weil zu viele Teams Agentensicherheit immer noch behandeln, als wäre sie ein Zukunftsthema statt ein aktuelles Runtime-Designproblem.

Und der Artikel setzt das mit einem starken praktischen Kontrast fort: Die meisten heutigen Abwehrmechanismen sind heuristisch, während FIDES das System in Richtung Richtlinie und Durchsetzung bewegen will.

Das ist genau der richtige Wandel.

## Warum das überzeugender ist als ein weiteres Sicherheits-Whitepaper

Viele Texte über KI-Sicherheit bleiben abstrakt.

Dieser Beitrag macht etwas Besseres. Er geht ein sehr konkretes Beispiel durch: einen GitHub-Issue-Triage-Agenten, einen bösartigen Issue-Body, einen privilegierten Dateizugriff und einen Versuch, einen öffentlichen Kommentar zu leaken.

Das ist nützlich, weil es die ganze Diskussion in einen tatsächlichen Workflow einbettet.

Und sobald man dieses Szenario sieht, wird der Wert deterministischer Kontrollen viel leichter verständlich.

## Die Kernidee ist nicht "mach das Modell schlauer"

Das Wichtigste hier ist, dass FIDES nicht verlangt, dass das Modell magisch besser darin wird, Angriffe zu erkennen.

Es verändert den Laufzeitvertrag.

Das bedeutet:

- Inhalte werden markiert
- Labels werden weitergegeben
- Tools deklarieren, was sie akzeptieren
- Middleware blockiert unsichere Pfade vor der Ausführung

Das ist ein viel gesünderer Ansatz.

Denn sobald der Agent Tools mit echten Konsequenzen aufrufen kann, darf Sicherheit nicht nur davon abhängen, ob das Modell einen guten Tag hatte.

## Meine Einschätzung

Genau diese Richtung in der Agentensicherheit möchte ich häufiger sehen.

Nicht "Vertrau darauf, dass das Modell schlechte Anweisungen ignoriert", sondern "baue den Richtlinienzaun in die Laufzeit ein".

Das ist ein deutlich gesünderes Modell.

Und wenn Agenten-Frameworks in der Produktion ernst genommen werden wollen, brauchen sie mehr Geschichten wie diese.

Originalpost: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)