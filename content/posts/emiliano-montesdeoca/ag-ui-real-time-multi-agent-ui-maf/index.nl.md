---
title: "Real-Time Multi-Agent UI's Bouwen Die Niet Aanvoelen als een Black Box"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI en Microsoft Agent Framework werken samen om multi-agent workflows een proper frontend te geven — met real-time streaming, menselijke goedkeuringen en volledige zichtbaarheid in wat je agents doen."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Dit is de werkelijkheid over multi-agent systemen: ze zien er geweldig uit in demo's. Drie agents die werk aan elkaar doorgeven, problemen oplossen, beslissingen nemen. Dan probeer je het aan echte gebruikers te tonen en... stilte. Een draaiende indicator. Geen idee welke agent wat doet of waarom het systeem gepauzeerd is. Dat is geen product — dat is een vertrouwensprobleem.

Het Microsoft Agent Framework-team heeft zojuist een [fantastisch overzicht](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) gepubliceerd over het koppelen van MAF-workflows aan [AG-UI](https://github.com/ag-ui-protocol/ag-ui), een open protocol voor het streamen van agent-uitvoeringsgebeurtenissen naar een frontend via Server-Sent Events. En eerlijk gezegd? Dit is precies de brug die we misten.

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Als je AI-aangedreven apps bouwt, ben je waarschijnlijk al tegen deze muur opgelopen. Je backend-orkestratie werkt prima — agents geven werk aan elkaar door, tools worden uitgevoerd, beslissingen worden genomen. Maar de frontend heeft geen idee wat er achter de schermen gebeurt. AG-UI lost dit op door een standaardprotocol te definiëren voor het streamen van agentgebeurtenissen (`RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) rechtstreeks naar je UI-laag via SSE.

De demo die ze bouwden is een klantenserviceworkflow met drie agents: een triageagent die verzoeken routeert, een terugbetalingsagent die financiële zaken afhandelt, en een orderagent die vervangingen beheert. Elke agent heeft zijn eigen tools, en de handoff-topologie is expliciet gedefinieerd — geen "bedenk het maar uit de prompt"-sfeer.

## De handoff-topologie is de echte ster

Wat mij opviel is hoe `HandoffBuilder` je in staat stelt een gerichte routeringsgraf tussen agents te declareren:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Elke `add_handoff` maakt een gerichte koppeling met een beschrijving in natuurlijke taal. Het framework genereert handoff-tools voor elke agent op basis van deze topologie. Routeringsbeslissingen zijn daardoor gegrond in jouw orkestratiestucture, niet in wat het LLM toevallig wil doen. Dat is enorm belangrijk voor betrouwbaarheid in productie.

## Human-in-the-loop die echt werkt

De demo toont twee onderbrekingspatronen die elke echte agentapp nodig heeft:

**Tool-goedkeuringsonderbrekingen** — wanneer een agent een tool aanroept die is gemarkeerd met `approval_mode="always_require"`, pauzeert de workflow en stuurt een gebeurtenis. De frontend toont een goedkeuringsmodal met de toolnaam en argumenten. Geen token-verspillende herhalingsloops — gewoon een nette pauze-goedkeur-hervat-stroom.

**Informatieverzoekonderbrekingen** — wanneer een agent meer context van de gebruiker nodig heeft (zoals een order-ID), pauzeert het en vraagt. De frontend toont de vraag, de gebruiker antwoordt, en de uitvoering gaat verder precies waar het gestopt was.

Beide patronen worden gestreamd als standaard AG-UI-gebeurtenissen, zodat je frontend geen aangepaste logica per agent nodig heeft — het rendert gewoon wat er via de SSE-verbinding binnenkomt.

## Het aansluiten is verrassend eenvoudig

De integratie tussen MAF en AG-UI is één functieaanroep:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

De `workflow_factory` maakt een nieuwe workflow per thread, zodat elke conversatie geïsoleerde toestand heeft. Het endpoint regelt alle SSE-infrastructuur automatisch. Als je FastAPI al gebruikt (of het als lichte laag kunt toevoegen), is dit vrijwel nul wrijving.

## Mijn kijk

Voor ons als .NET-ontwikkelaars is de directe vraag: "Kan ik dit in C# doen?" Agent Framework is beschikbaar voor zowel .NET als Python, en het AG-UI-protocol is taalonafhankelijk (het is gewoon SSE). Dus hoewel deze specifieke demo Python en FastAPI gebruikt, is het patroon direct overdraagbaar. Je kunt een ASP.NET Core minimal API aansluiten met SSE-endpoints die hetzelfde AG-UI-gebeurtenisschema volgen.

De grotere les is dat multi-agent UI's een prioriteit worden, geen bijzaak. Als je iets bouwt waarbij agents met mensen interageren — klantenservice, goedkeuringsworkflows, documentverwerking — is deze combinatie van MAF-orkestratie en AG-UI-transparantie het te volgen patroon.

## Samenvatting

AG-UI + Microsoft Agent Framework geeft je het beste van beide werelden: robuuste multi-agent orkestratie op de backend en real-time zichtbaarheid op de frontend. Geen black-box agentinteracties meer.

Bekijk de [volledige walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) en de [AG-UI protocol repository](https://github.com/ag-ui-protocol/ag-ui) om dieper te gaan.
