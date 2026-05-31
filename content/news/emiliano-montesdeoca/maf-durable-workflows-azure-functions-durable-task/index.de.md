---
title: "Langlebige Workflows in Microsoft Agent Framework: Von In-Memory zu Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "MAFs Workflow-Programmiermodell unterstützt jetzt dauerhafte Ausführung, die durch Durable Task gesichert wird — hier erfahren Sie, wie Sie zusammensetzbare Agent-Workflows erstellen, die Prozessneustarts überleben und über Azure Functions skalieren."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Einer der Schmerzpunkte bei frühen KI-Agent-Workflows: Sie sind fragil. Ein lang laufender Multi-Step-Workflow, der an einen einzelnen Prozess gebunden ist, bedeutet, dass Prozessneustart = verlorener Zustand. Für einfache Demos ist das in Ordnung. Für Produktionsworkloads ist es das nicht.

Das Workflow-Programmiermodell von Microsoft Agent Framework unterstützt jetzt **dauerhafte Ausführung**, gesichert durch das Durable Task-Framework, mit Azure Functions-Hosting. Hier erfahren Sie, wie das Programmiermodell funktioniert und warum die Dauerhaftigkeitsgeschichte wichtig ist.

## Die grundlegenden Bausteine

**Executors** sind die fundamentale Arbeitseinheit. Jeder ist typisiert — er nimmt eine bestimmte Eingabe und produziert eine bestimmte Ausgabe:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // Bestellung nachschlagen, zurückgeben
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflows** verbinden Executors zu gerichteten Graphen mit einem Fluent Builder. Das Framework übernimmt die Ausführung, den Datenfluss zwischen Schritten und die Fehlerfortpflanzung.

Sie können modellieren:
- Sequentielle Ketten (Schritt A → Schritt B → Schritt C)
- Paralleles Fan-out/Fan-in (Agenten A, B, C parallel ausführen, Ergebnisse aggregieren)
- Bedingte Verzweigung
- Human-in-the-Loop-Genehmigungen (Workflow pausieren, auf externes Signal warten)

## Der In-Memory-Runner für lokale Entwicklung

Der Einstieg ist schnell:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Das Kernpaket enthält einen leichtgewichtigen In-Process-Runner. Keine externen Abhängigkeiten, keine Datenbank, keine Azure-Ressourcen. Funktioniert hervorragend für lokale Entwicklung und Unit-Tests.

## Dauerhaftigkeit mit Durable Task hinzufügen

Wenn ein Workflow Prozessneustarts überleben muss — weil er lang läuft, weil er Human-in-the-Loop-Schritte hat, weil er auf viele parallele Agent-Aufrufe verteilt wird — reicht der In-Memory-Runner nicht aus.

MAFs Durable Task-Integration speichert den Workflow-Zustand in Azure Storage. Wenn der Prozess neu startet, wird der Workflow von dort fortgesetzt, wo er aufgehört hat. Das Programmiermodell bleibt gleich; Sie tauschen nur den Runner aus.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Dieselben Executors, derselbe Workflow-Graph — gesichert durch dauerhaften Zustand.

## Azure Functions-Hosting

Die dritte Schicht ist das Azure Functions-Hosting. Ihr Workflow wird zu einer Function-App: Lösen Sie den Workflow über einen HTTP-Endpoint aus, und die dauerhafte Laufzeit kümmert sich um Skalierung, Zustand und Zuverlässigkeit.

Das bedeutet, dass ein Multi-Agent-Workflow mit parallelen Aufrufen, bedingten Verzweigungen und menschlichen Genehmigungen über eine serverlose Functions-Umgebung skalieren kann, ohne benutzerdefinierte Zustandsverwaltung.

## Warum das wichtig ist

Die Kombination ist bedeutsam für echte KI-Systeme:

- **Parallele Agent-Aufrufe** — gleichzeitig auf mehrere spezialisierte Agenten verteilen ohne Blockierung, Ergebnisse aggregieren wenn alle abgeschlossen sind
- **Lang laufende Prozesse** — Workflows, die menschliche Genehmigung oder externe Ereignisse beinhalten, können über Stunden oder Tage pausieren und fortgesetzt werden
- **Skalierung** — Azure Functions skaliert die Ausführung horizontal; das Durable Task-Framework koordiniert den parallelen Zustand

Wenn Sie MAF-Workflows über einfache lokale Demos hinaus erstellen, ist dies der Weg zur produktionsreifen Ausführung.

Originalbeitrag: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
