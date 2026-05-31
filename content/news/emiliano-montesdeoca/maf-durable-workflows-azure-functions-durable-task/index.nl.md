---
title: "Duurzame Workflows in Microsoft Agent Framework: Van In-Memory naar Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "Het workflow-programmeermodel van MAF ondersteunt nu duurzame uitvoering die wordt ondersteund door Durable Task — hier leest u hoe u samengestelde agent-workflows kunt bouwen die procesherstart overleven en schalen over Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Een van de pijnpunten bij vroege AI-agent-workflows: ze zijn kwetsbaar. Een langlopende multi-stap-workflow die gebonden is aan een enkel proces betekent dat procesherstart = verloren toestand. Voor eenvoudige demo's is dat prima. Voor productie-workloads niet.

Het workflow-programmeermodel van Microsoft Agent Framework ondersteunt nu **duurzame uitvoering**, ondersteund door het Durable Task-framework, met Azure Functions-hosting. Hier leest u hoe het programmeermodel werkt en waarom het verhaal van duurzaamheid ertoe doet.

## De Kernbouwstenen

**Executor's** zijn de fundamentele werkeenheid. Elk is getypeerd — het neemt een specifieke invoer en produceert een specifieke uitvoer:

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
        // zoek de bestelling op, geef deze terug
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflows** verbinden executor's tot gerichte grafieken met behulp van een fluent builder. Het framework verwerkt uitvoering, gegevensstroom tussen stappen en foutpropagatie.

U kunt modelleren:
- Sequentiële ketens (stap A → stap B → stap C)
- Parallelle fan-out/fan-in (agenten A, B, C parallel uitvoeren, resultaten aggregeren)
- Conditionele vertakking
- Human-in-the-loop-goedkeuringen (workflow pauzeren, wachten op extern signaal)

## De In-Memory Runner voor Lokale Ontwikkeling

Beginnen gaat snel:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Het kernpakket bevat een lichtgewicht in-process runner. Geen externe afhankelijkheden, geen database, geen Azure-resources. Werkt uitstekend voor lokale ontwikkeling en unit-testen.

## Duurzaamheid Toevoegen met Durable Task

Wanneer een workflow procesherstart moet overleven — omdat het langlopend is, omdat het human-in-the-loop-stappen heeft, omdat het verspreid is over veel parallelle agentaanroepen — is de in-memory runner onvoldoende.

De Durable Task-integratie van MAF slaat workflowstatus op in Azure Storage. Als het proces herstart, hervat de workflow waar het was gebleven. Het programmeermodel blijft hetzelfde; u wisselt alleen de runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Dezelfde executor's, dezelfde workflowgrafiek — ondersteund door duurzame toestand.

## Azure Functions-hosting

De derde laag is Azure Functions-hosting. Uw workflow wordt een Function-app: activeer de workflow via een HTTP-endpoint, en de duurzame runtime verwerkt schaling, toestand en betrouwbaarheid.

Dit betekent dat een multi-agent-workflow met parallelle aanroepen, conditionele vertakkingen en menselijke goedkeuringen kan schalen in een serverless Functions-omgeving zonder aangepast statusbeheer.

## Waarom Dit Belangrijk Is

De combinatie is significant voor echte AI-systemen:

- **Parallelle agentaanroepen** — tegelijkertijd distribueren naar meerdere gespecialiseerde agenten zonder blokkering, resultaten aggregeren wanneer alle voltooid zijn
- **Langlopende processen** — workflows die menselijke goedkeuring of externe gebeurtenissen omvatten kunnen pauzeren en hervatten over uren of dagen
- **Schaling** — Azure Functions schaalt de uitvoering horizontaal; het Durable Task-framework beheert de coördinatie van parallelle toestand

Als u MAF-workflows bouwt die verder gaan dan eenvoudige lokale demo's, is dit het pad naar productiekwaliteitsuitvoering.

Originele post: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
