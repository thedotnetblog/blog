---
title: "Het Handoff-patroon: Wanneer Één Agent Niet Genoeg Is"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Het Handoff-orchestratiepatroon van Microsoft Agent Framework laat agenten beslissen wie de volgende beurt afhandelt — zonder de gesprekscontext te verliezen of topologieregels te schenden."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

Op een gegeven moment overtreft elk multi-agentsysteem een eenvoudige router. Het eerste teken is meestal wanneer een gespecialiseerde agent een vervolgvraag moet stellen, of halverwege een beurt beseft dat een andere agent zou moeten doorgaan. Een vaste pipeline faalt daar. Een eenmalige router faalt daar.

Dat is precies het probleem dat het Handoff-orchestratiepatroon in Microsoft Agent Framework is ontworpen op te lossen.

## Hoe Handoff Werkt

De ontwikkelaar declareert een graaf: dit zijn de agenten, dit zijn de randen ertussen. Het framework doet de rest — het synthetiseert een handoff-tool per uitgaande rand en injecteert deze in elke agent. Wanneer een agent besluit de controle over te dragen, roept deze de tool aan. Het framework handhaaft de topologie.

Drie dingen maken dit anders dan simpelweg agenten elkaar laten aanroepen:

1. **Één gedeeld transcript** — de ontvangende agent ziet de volledige gespreksgeschiedenis. Zonder opnieuw te beginnen.
2. **Topologiehandhaving** — een agent kan alleen handoff doen naar gedeclareerde bestemmingen. Routeringsbugs worden tijdens het schrijven gevangen, niet in productie.
3. **Natuurlijke beëindiging** — wanneer de actieve agent zijn beurt beëindigt zonder een handoff-tool aan te roepen, geeft de workflow de controle aan de gebruiker. Geen polling, geen expliciete exitvoorwaarden.

## Een Minimaal Voorbeeld

In .NET ziet het bouwen van een handoff-workflow er zo uit:

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

Triage kan naar beide specialisten sturen. Beide specialisten kunnen terugsturen naar triage. De graaf is cyclisch-compatibel maar ondersteunt terugwaartse randen wanneer dat nodig is ("ik heb meer informatie nodig" → terug naar onderzoek).

## Wanneer Handoff Gebruiken (en Wanneer Niet)

Handoff is een goede keuze wanneer:

- **Eigenaarschap kan veranderen midden in een gesprek** — een agent kan beseffen dat hij de verkeerde specialist is
- **Terugwaartse randen belangrijk zijn** — u moet mogelijk een eerdere stap opnieuw bezoeken zonder opnieuw te starten
- **Routeringsbeslissingen genuanceerd zijn** — de beslissing om over te dragen is contextueel en wordt beter genomen door het model dan door getypeerde predicaten

Het is *niet* de juiste keuze wanneer:

- Uw pipeline vast en sequentieel is — gebruik daarvoor de `Sequential`-workflow
- Elke stap onafhankelijk is — agenten die een transcript delen terwijl slechts één het nodig had is gewoon ruis
- U strikte verwerkingsgaranties nodig heeft — het niet-determinisme van modelgestuurde routering is niet wat u wilt

## Terugwaartse Randen en Human-in-the-Loop

Een van de interessantste vormen die Handoff mogelijk maakt zijn echte terugwaartse randen. Een agent kan beslissen "ik heb niet genoeg informatie" en terugsturen naar een onderzoeksstap — niet met een hardgecodeerde lus, maar omdat het model beslist dat dit de juiste keuze is.

Human-in-the-loop-interacties componeren ook op een natuurlijke manier. Wanneer een specialist gebruikersinvoer nodig heeft, geeft de workflow de controle via de standaard beurtlus terug aan de gebruiker, verzamelt het antwoord en hervat met volledige context. De agent is de conversatie nooit verloren.

## Conclusie

Handoff is een van die patronen die eenvoudig lijkt maar veel mogelijk maakt zodra u het hebt geïnternaliseerd: gedecentraliseerde routering, gedeelde context, afgedwongen topologie, natuurlijke beëindiging. Het is de juiste volgende stap wanneer uw agenten beginnen te zeggen "eigenlijk zou iemand anders dit moeten afhandelen."

Lees de volledige walkthrough in de originele post: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
