---
title: "Agents Bouwen Is het Gemakkelijke Deel — Ze Veilig Uitvoeren Is het Moeilijke Deel"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework en Agent Governance Toolkit werken samen om runtimebeleid af te dwingen, toolaanroepen te beheren en Merkle-geketende auditlogs te bieden — zonder de prompts van de agent aan te raken."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Er is een patroon in de ontwikkeling van AI-agents dat ik ben gaan noemen 'demo-spijt'. De agent werkt geweldig in demo's. Dan vraagt iemand: wat gebeurt er als hij de verkeerde tool aanroept? Wat als hij toegang krijgt tot data waarvan dat niet mag? Wie heeft dat gecontroleerd?

Microsoft Agent Framework helpt u bij het bouwen en orkestreren. Agent Governance Toolkit (AGT) dekt het deel daarna — governance, beleidshandhaving en controleerbaarheid tijdens uitvoering.

## Wat Elk Project Echt Doet

**Microsoft Agent Framework (MAF)** biedt u het programmeermodel: multi-agent workflows, A2A-protocol interoperabiliteit, middleware-hooks, geheugen en beheerde hosting via Foundry Agent Service. Het regelt inhoudsbeveiliging op het niveau van de modelinvoer/-uitvoer.

**Agent Governance Toolkit (AGT)** verbindt met diezelfde middleware-pipeline om *acties* te beheren. Elke toolaanroep, resourcetoegang en inter-agentbericht wordt geëvalueerd aan het beleid voordat het wordt uitgevoerd. Sub-milliseconde overhead. Geen sidecars, geen proxies, geen gewijzigde prompts.

```
Agentactie --> Beleidscontrole --> Toestaan / Weigeren --> Auditlog    (< 0.1 ms)
```

Verschillende lagen, volledige dekking, één pipeline.

## Aansluiten Betekent Gewoon Middleware Toevoegen

In Python voegt AGT toe aan dezelfde `middleware`-parameter die u zou gebruiken voor logging of inhoudsfilters:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

In .NET hetzelfde patroon via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Dezelfde agent, dezelfde orkestratie, dezelfde tools. AGT voegt governancemogelijkheden toe zonder de agentlogica aan te raken.

## Wat U Krijgt

- **GovernancePolicyMiddleware** — evalueert elke actie aan declaratieve beleidsregels
- **CapabilityGuardMiddleware** — allowlist welke tools een agent mag aanroepen (de tool `approve_small_loan` staat bewust niet in de toegestane lijst hierboven)
- **RogueDetectionMiddleware** — detecteert afwijkende gedragspatronen tijdens uitvoering
- **AuditTrailMiddleware** — Merkle-geketend auditlog zodat elke actie cryptografisch tamper-evident is

Die laatste telt voor compliance. Een Merkle-keten betekent dat als iemand het log wijzigt, de keten breekt. De audit is het bewijs.

## Vijf Industriescenario's

De AGT-repository bevat vijf volledige end-to-end scenario's: financiële diensten (kredietbeoordelaar), gezondheidszorg (patiëntgegevens), juridisch (contractbeoordeling), overheid (burgerdiensten) en productie (kwaliteitscontrole). Elk koppelt echte MAF-agents aan echte AGT-governance-middleware.

Dit zijn geen speelgoeddemo's. Dit zijn de scenario's waar u daadwerkelijk governance in productie nodig zou hebben.

## Conclusie

Als u agents bouwt die echte data raken, beslissingen met gevolgen nemen, of onbeheerd in productie draaien — is governance niet optioneel. De combinatie MAF + AGT geeft u de volledige stack: bouw het met Agent Framework, beheer het met AGT.

Beide projecten zijn open source. Het oorspronkelijke artikel bevat links naar de volledige codevoorbeelden.

Origineel bericht: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
