---
title: "Agenten Zu Bauen Ist Der Einfache Teil — Sie Sicher Zu Betreiben Ist Der Schwierige Teil"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework und Agent Governance Toolkit arbeiten zusammen, um Laufzeitrichtlinien durchzusetzen, Tool-Aufrufe zu steuern und Merkle-verkettete Audit-Logs bereitzustellen — ohne die Prompts des Agenten zu ändern."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Es gibt ein Muster in der KI-Agenten-Entwicklung, das ich begonnen habe, „Demo-Bedauern" zu nennen. Der Agent funktioniert in Demos hervorragend. Dann fragt jemand: Was passiert, wenn er das falsche Tool aufruft? Was wenn er auf Daten zugreift, auf die er nicht sollte? Wer hat das geprüft?

Microsoft Agent Framework unterstützt Sie beim Aufbau und der Orchestrierung. Agent Governance Toolkit (AGT) deckt den Teil danach ab — Governance, Richtliniendurchsetzung und Prüfbarkeit zur Laufzeit.

## Was Jedes Projekt Wirklich Macht

**Microsoft Agent Framework (MAF)** bietet Ihnen das Programmiermodell: Multi-Agenten-Workflows, A2A-Protokoll-Interoperabilität, Middleware-Hooks, Speicher und verwaltetes Hosting über Foundry Agent Service. Es behandelt Content-Sicherheit auf der Ebene der Modell-Ein-/Ausgabe.

**Agent Governance Toolkit (AGT)** verbindet sich mit demselben Middleware-Pipeline, um *Aktionen* zu steuern. Jeder Tool-Aufruf, Ressourcenzugriff und Inter-Agenten-Nachricht wird vor der Ausführung gegen die Richtlinie bewertet. Sub-Millisekunden-Overhead. Keine Sidecars, keine Proxies, keine geänderten Prompts.

```
Agenten-Aktion --> Richtlinienprüfung --> Erlauben / Ablehnen --> Audit-Log    (< 0.1 ms)
```

Verschiedene Schichten, vollständige Abdeckung, eine Pipeline.

## Die Einbindung Ist Nur Middleware Hinzufügen

In Python fügt AGT denselben `middleware`-Parameter hinzu, den Sie für Protokollierung oder Inhaltsfilter verwenden würden:

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

In .NET dasselbe Muster via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Gleicher Agent, gleiche Orchestrierung, gleiche Tools. AGT fügt Governance-Funktionen hinzu, ohne die Agentenlogik zu berühren.

## Was Sie Bekommen

- **GovernancePolicyMiddleware** — bewertet jede Aktion gegen deklarative Richtlinienregeln
- **CapabilityGuardMiddleware** — Allowlist, welche Tools ein Agent aufrufen darf (das Tool `approve_small_loan` ist oben nicht in der Allowlist — absichtlich)
- **RogueDetectionMiddleware** — erkennt anomale Verhaltensmuster zur Laufzeit
- **AuditTrailMiddleware** — Merkle-verkettetes Audit-Log, damit jede Aktion kryptografisch manipulationssicher ist

Letzteres ist für die Compliance wichtig. Eine Merkle-Kette bedeutet: Wenn jemand das Log ändert, bricht die Kette. Das Audit ist der Beweis.

## Fünf Branchenszenarien

Das AGT-Repository enthält fünf vollständige End-to-End-Szenarien: Finanzdienstleistungen (Kreditsachbearbeiter), Gesundheitswesen (Patientendaten), Recht (Vertragsüberprüfung), Regierung (Bürgerdienste) und Fertigung (Qualitätskontrolle). Jedes kombiniert echte MAF-Agenten mit echter AGT-Governance-Middleware.

Das sind keine Spielzeug-Demos. Das sind die Szenarien, bei denen Sie in der Produktion tatsächlich Governance benötigen würden.

## Fazit

Wenn Sie Agenten entwickeln, die echte Daten berühren, Entscheidungen mit Konsequenzen treffen oder unbeaufsichtigt in der Produktion laufen — Governance ist nicht optional. Die Kombination MAF + AGT gibt Ihnen den vollständigen Stack: Mit Agent Framework bauen, mit AGT verwalten.

Beide Projekte sind Open Source. Der Originalartikel enthält Links zu den vollständigen Code-Beispielen.

Originalbeitrag: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
