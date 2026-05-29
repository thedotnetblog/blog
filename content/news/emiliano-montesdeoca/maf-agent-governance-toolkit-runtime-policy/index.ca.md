---
title: "Construir Agents És la Part Fàcil — Executar-los de Forma Segura És la Part Difícil"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework i Agent Governance Toolkit s'uneixen per aplicar polítiques d'execució, governar les crides a eines i proporcionar registres d'auditoria encadenats amb Merkle — sense tocar els prompts de l'agent."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Hi ha un patró en el desenvolupament d'agents d'IA que he començat a anomenar "penediment de demo". L'agent funciona molt bé en les demos. Llavors algú pregunta: què passa si crida l'eina equivocada? I si accedeix a dades que no hauria? Qui ho ha auditat?

Microsoft Agent Framework us dóna suport en la construcció i l'orquestració. Agent Governance Toolkit (AGT) cobreix la part posterior — governança, aplicació de polítiques i auditabilitat en temps d'execució.

## Què Fa Realment Cada Projecte

**Microsoft Agent Framework (MAF)** us proporciona el model de programació: fluxos de treball multi-agent, interoperabilitat del protocol A2A, hooks de middleware, memòria i allotjament gestionat a través de Foundry Agent Service. Gestiona la seguretat de contingut a nivell d'entrada/sortida del model.

**Agent Governance Toolkit (AGT)** es connecta al mateix pipeline de middleware per governar les *accions*. Cada crida a eina, accés a recursos i missatge entre agents s'avalua contra la política abans de l'execució. Sobrecàrrega de submil·lisegon. Sense sidecars, sense proxies, sense prompts modificats.

```
Acció Agent --> Verificació Política --> Permetre / Denegar --> Registre Auditoria    (< 0.1 ms)
```

Capes diferents, cobertura completa, un pipeline.

## Connectar-se És Només Afegir Middleware

A Python, AGT s'afegeix al mateix paràmetre `middleware` que faríeu servir per al registre o els filtres de contingut:

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

A .NET, el mateix patró via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Mateix agent, mateixa orquestració, mateixes eines. AGT afegeix capacitats de governança sense tocar la lògica de l'agent.

## Què Obteniu

- **GovernancePolicyMiddleware** — avalua cada acció contra regles de política declaratives
- **CapabilityGuardMiddleware** — llista d'autoritzats quines eines un agent té permís de cridar (l'eina `approve_small_loan` no és a la llista permesa per sobre — deliberadament)
- **RogueDetectionMiddleware** — detecta patrons de comportament anòmal en temps d'execució
- **AuditTrailMiddleware** — registre d'auditoria encadenat amb Merkle perquè cada acció sigui criptogràficament resistent a manipulacions

L'últim importa per al compliment normatiu. Una cadena Merkle significa que si algú modifica el registre, la cadena es trenca. L'auditoria és l'evidència.

## Cinc Escenaris de la Indústria

El repositori AGT inclou cinc escenaris complets de cap a cap: serveis financers (oficial de préstecs), sanitat (dades de pacients), legal (revisió de contractes), govern (serveis al ciutadà) i fabricació (control de qualitat). Cada un combina agents MAF reals amb middleware de governança AGT real.

No són demos de joguina. Són el tipus d'escenaris on realment necessitaríeu governança en producció.

## Conclusió

Si esteu construint agents que toquen dades reals, prenen decisions amb conseqüències, o s'executen sense supervisió en producció — la governança no és opcional. La combinació MAF + AGT us dóna la pila completa: construïu-lo amb Agent Framework, governeu-lo amb AGT.

Tots dos projectes són de codi obert. L'article original té enllaços als exemples de codi complets.

Publicació original: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
