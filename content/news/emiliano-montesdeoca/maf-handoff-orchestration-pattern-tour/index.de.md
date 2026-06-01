---
title: "Das Handoff-Muster: Wenn Ein Agent Nicht Ausreicht"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Das Handoff-Orchestrierungsmuster von Microsoft Agent Framework ermöglicht es Agenten zu entscheiden, wer den nächsten Zug übernimmt — ohne Gesprächskontext zu verlieren oder Topologieregeln zu verletzen."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

Irgendwann überwächst jedes Multi-Agent-System einen einfachen Router. Das erste Anzeichen ist meist, wenn ein Spezialistenagent eine Folgefrage stellen muss oder mitten im Zug erkennt, dass ein anderer Agent weitermachen sollte. Eine feste Pipeline scheitert dort. Ein Ein-Schuss-Router scheitert dort.

Genau das ist das Problem, für das das Handoff-Orchestrierungsmuster in Microsoft Agent Framework konzipiert wurde.

## Wie Handoff Funktioniert

Der Entwickler deklariert einen Graphen: Hier sind die Agenten, hier sind die Kanten zwischen ihnen. Das Framework erledigt den Rest — es synthetisiert pro ausgehende Kante ein Handoff-Tool und injiziert es in jeden Agenten. Wenn ein Agent entscheidet, die Kontrolle abzugeben, ruft er das Tool auf. Das Framework setzt die Topologie durch.

Drei Dinge unterscheiden das von einfachem gegenseitigen Aufrufen der Agenten:

1. **Ein gemeinsames Transkript** — der empfangende Agent sieht den gesamten Gesprächsverlauf. Kein Neustart von Null.
2. **Topologiedurchsetzung** — ein Agent kann nur an deklarierte Ziele übergeben. Routing-Bugs werden beim Erstellen erkannt, nicht in der Produktion.
3. **Natürliche Beendigung** — wenn der aktive Agent seinen Zug beendet, ohne ein Handoff-Tool aufzurufen, gibt der Workflow an den Benutzer ab. Kein Polling, keine expliziten Exit-Bedingungen.

## Ein Minimales Beispiel

In .NET sieht das Erstellen eines Handoff-Workflows so aus:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage kann an jeden Spezialisten senden. Beide Spezialisten können zurück zu Triage senden. Der Graph ist azyklisch-freundlich, unterstützt aber Rückkanten wenn Sie sie brauchen ("Ich brauche mehr Informationen" → zurück zur Recherche).

## Wann Handoff Verwenden (und Wann Nicht)

Handoff ist eine gute Wahl wenn:

- **Ownership sich mitten im Gespräch ändern kann** — ein Agent erkennt möglicherweise, dass er der falsche Spezialist ist
- **Rückkanten wichtig sind** — Sie müssen möglicherweise einen früheren Schritt erneut aufsuchen, ohne neu zu starten
- **Routing-Entscheidungen unscharf sind** — die Entscheidung zum Handoff ist kontextuell und vom Modell besser getroffen als durch typisierte Prädikate

Es ist *nicht* die richtige Wahl wenn:

- Ihre Pipeline fest und sequentiell ist — verwenden Sie dafür den `Sequential`-Workflow
- Jeder Schritt unabhängig ist — Agenten, die ein Transkript teilen, wo nur einer davon es brauchte, ist nur Rauschen
- Sie strenge Verarbeitungsgarantien benötigen — der Nichtdeterminismus des modellgesteuerten Routings ist nicht das, was Sie wollen

## Rückkanten und Human-in-the-Loop

Eine der interessanteren Formen, die Handoff ermöglicht, sind echte Rückkanten. Ein Agent kann entscheiden "Ich habe nicht genug Informationen" und zu einem Rechercheschritt zurückrouten, nicht mit einer harkodierten Schleife, sondern weil das Modell entscheidet, dass es der richtige Schritt ist.

Human-in-the-Loop-Interaktionen komponieren sich ebenfalls natürlich. Wenn ein Spezialist Benutzereingaben benötigt, gibt der Workflow über die Standard-Zugschleife zurück an den Benutzer, sammelt die Antwort und setzt mit vollständigem Kontext fort. Der Agent hat die Konversation nie verloren.

## Fazit

Handoff ist eines dieser Muster, das einfach klingt, aber viel ermöglicht, sobald man es verinnerlicht hat: dezentrales Routing, gemeinsamer Kontext, erzwungene Topologie, natürliche Beendigung. Es ist der richtige nächste Schritt, wenn Ihre Agenten anfangen zu sagen "eigentlich sollte das jemand anderes übernehmen."

Lesen Sie den vollständigen Durchgang im Originalbeitrag: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
