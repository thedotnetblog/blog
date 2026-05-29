---
title: "Costruire Agenti È la Parte Facile — Eseguirli in Sicurezza È la Parte Difficile"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework e Agent Governance Toolkit si uniscono per applicare le policy di runtime, governare le chiamate agli strumenti e fornire log di audit con catena Merkle — senza toccare i prompt dell'agente."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

C'è un pattern nello sviluppo di agenti IA che ho iniziato a chiamare "rimpianto della demo". L'agente funziona benissimo nelle demo. Poi qualcuno chiede: cosa succede se chiama lo strumento sbagliato? E se accede a dati a cui non dovrebbe? Chi ha fatto l'audit?

Microsoft Agent Framework ti supporta per la costruzione e l'orchestrazione. Agent Governance Toolkit (AGT) copre la parte successiva — governance, applicazione delle policy e auditability a runtime.

## Cosa Fa Davvero Ciascun Progetto

**Microsoft Agent Framework (MAF)** ti offre il modello di programmazione: workflow multi-agente, interoperabilità del protocollo A2A, hook middleware, memoria e hosting gestito tramite Foundry Agent Service. Gestisce la content safety a livello di input/output del modello.

**Agent Governance Toolkit (AGT)** si collega a quella stessa pipeline middleware per governare le *azioni*. Ogni chiamata a strumento, accesso alle risorse e messaggio inter-agente viene valutato rispetto alla policy prima dell'esecuzione. Overhead inferiore al millisecondo. Nessun sidecar, nessun proxy, nessun prompt modificato.

```
Azione Agente --> Controllo Policy --> Consenti / Nega --> Log Audit    (< 0.1 ms)
```

Layer diversi, copertura completa, una pipeline.

## Integrarsi È Solo Aggiungere Middleware

In Python, AGT si aggiunge allo stesso parametro `middleware` che useresti per il logging o i filtri di contenuto:

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

In .NET, lo stesso pattern via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Stesso agente, stessa orchestrazione, stessi strumenti. AGT aggiunge capacità di governance senza toccare la logica dell'agente.

## Cosa Ottieni

- **GovernancePolicyMiddleware** — valuta ogni azione rispetto alle regole di policy dichiarative
- **CapabilityGuardMiddleware** — allowlist di quali strumenti un agente è autorizzato a chiamare (lo strumento `approve_small_loan` non è nell'elenco consentiti sopra — deliberatamente)
- **RogueDetectionMiddleware** — rileva pattern di comportamento anomalo a runtime
- **AuditTrailMiddleware** — log di audit con catena Merkle per rendere ogni azione crittograficamente resistente alle manomissioni

Quest'ultimo conta per la conformità. Una catena Merkle significa che se qualcuno modifica il log, la catena si spezza. L'audit è la prova.

## Cinque Scenari di Settore

Il repository AGT include cinque scenari completi end-to-end: servizi finanziari (ufficiale prestiti), sanità (dati pazienti), legale (revisione contratti), governo (servizi ai cittadini) e produzione (controllo qualità). Ognuno abbina veri agenti MAF con vero middleware di governance AGT.

Non sono demo giocattolo. Sono il tipo di scenari in cui avresti davvero bisogno di governance in produzione.

## Conclusione

Se stai costruendo agenti che toccano dati reali, prendono decisioni con conseguenze, o girano incustoditi in produzione — la governance non è opzionale. La combinazione MAF + AGT ti dà l'intero stack: costruiscilo con Agent Framework, governalo con AGT.

Entrambi i progetti sono open source. L'articolo originale ha link agli esempi di codice completi.

Post originale: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
