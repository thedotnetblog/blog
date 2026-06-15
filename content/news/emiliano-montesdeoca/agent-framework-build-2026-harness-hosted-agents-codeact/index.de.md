---
title: "Agent Harness, Hosted Agents und CodeAct: Auf dieses Agent-Framework-Update würde ich mich konzentrieren"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Die Agent-Framework-Ankündigung auf der Build 2026 ist vollgepackt, aber die wichtigsten Linien sind das Harness-Modell, die in Foundry gehosteten Agents und CodeAct zur Reduzierung des Orchestrierungsaufwands."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Die große Agent-Framework-Ankündigung auf der Build deckt viel ab, aber drei Themen stechen für mich sofort heraus:

- **das Harness, das zu einem wichtigeren Teil der Runtime wird**
- **Foundry Hosted Agents, die einen Produktionspfad bieten**
- **CodeAct, das den Aufwand für mehrstufige Orchestrierung reduziert**

Das sind die Punkte, auf die ich achten würde.

## Das Harness wird zum eigentlichen Dreh- und Angelpunkt

Der Quellbeitrag beschreibt das Harness als die Ebene, auf der Modelldenken auf echte Ausführung trifft.

Das ist die richtige Beschreibung, und genau deshalb halte ich diesen Teil für wichtiger als viele einzelne Feature-Aufzählungen.

Sobald ein Agent braucht:

- Dateizugriff
- Shell-Ausführung
- Planungsmodi
- To-dos
- Sitzungs-Speicher
- Freigabeworkflows

sprichst du nicht mehr nur über einen Prompt plus ein Modell.

Du sprichst über Laufzeitverhalten.

Genau dort werden Frameworks entweder nützlich oder bleiben Spielzeug.

Und Microsoft Agent Framework versucht klar, genau diese Ebene deutlich nützlicher zu machen.

## Hosted Agents sind der Punkt, an dem die Local-to-Production-Geschichte real wird

Ich denke auch, dass der Hosted-Agents-Teil einer der strategisch wichtigsten Aspekte der Ankündigung ist.

Der Quellbeitrag sagt ausdrücklich, dass dies der einfachste Weg ist, diesem Agenten eine Produktionsheimat zu geben.

Diese Formulierung ist wichtig, weil die meisten Agent-Frameworks lokal immer noch deutlich stärker sind als im operativen Deployment.

Wenn Foundry Hosted Agents den Wechsel von der lokalen Entwicklung zu:

- Skalierung
- Observability
- Managed Identity
- Sitzungsverwaltung
- Versionierung

spürbar einfacher machen, dann schließt das eine der größten Lücken im aktuellen Agent-Ökosystem.

Das wäre ein echter Fortschritt.

## CodeAct ist die spannendste technische Idee im Update

Wenn ich das interessanteste technische Konzept im Beitrag auswählen müsste, würde ich wahrscheinlich CodeAct nehmen.

Das Problem, das es lösen will, ist sehr real: Zu viele mehrstufige Agent-Workflows sind teuer, weil die Orchestrierungsschleife selbst zu viele Modellrunden verbraucht.

Wenn der Quellbeitrag dann ein Ergebnis wie dieses zeigt:

- 52.4% schneller
- 63.9% weniger Tokens

zieht das sofort meine Aufmerksamkeit auf sich.

Natürlich sind das Benchmark-Werte für eine repräsentative Arbeitslast, kein allgemeines Gesetz. Aber die größere Idee bleibt trotzdem überzeugend.

Wenn das Modell eine Tool-Calling-Kette in eine effizientere Ausführungsform verdichten kann, verändert das die Wirtschaftlichkeit von Agentensystemen deutlich.

## Was Entwickler aus diesem Update wirklich mitnehmen sollten

Die wichtige Lehre ist nicht, wie viele Features ausgeliefert wurden.

Die Lehre ist, dass das Framework genau dort stärker wird, wo echte Anwendungen es am meisten brauchen:

- Runtime-Schicht
- Deployment-Pfad
- Ausführungseffizienz
- eingebaute Betriebsabläufe

Solche Reifesignale sind mir deutlich wichtiger als noch eine oberflächliche AI-Feature-Checkliste.

## Meine Einschätzung

Dieses Update zählt nicht nur, weil es mehr Oberfläche hinzufügt.

Es stärkt die Runtime- und Deployment-Geschichte rund um Agents auf eine Weise, die für reale Anwendungen wichtig sein sollte, besonders für Teams, die von lokalen Experimenten zu Systemen wechseln wollen, die sie wirklich betreiben und pflegen können.

Genau dort wird das Framework überzeugender.

Und wenn ich diese Version genau verfolgen würde, wären Harness, Hosted Agents und CodeAct ganz klar die Punkte, auf die ich die meiste Aufmerksamkeit richten würde.

Originalbeitrag: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
