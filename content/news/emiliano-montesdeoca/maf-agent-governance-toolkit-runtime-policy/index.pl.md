---
title: "Budowanie Agentów Jest Łatwą Częścią — Bezpieczne Ich Uruchamianie Jest Trudną Częścią"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework i Agent Governance Toolkit łączą siły, by egzekwować zasady środowiska uruchomieniowego, zarządzać wywołaniami narzędzi i dostarczać dzienniki audytu z łańcuchem Merkle — bez modyfikowania promptów agenta."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

W tworzeniu agentów AI jest wzorzec, który zacząłem nazywać „żalem po demo". Agent działa świetnie w demach. Potem ktoś pyta: co się stanie, jeśli wywoła złe narzędzie? Co jeśli uzyska dostęp do danych, do których nie powinien? Kto to zaudytował?

Microsoft Agent Framework wspiera Cię w budowaniu i orkiestracji. Agent Governance Toolkit (AGT) pokrywa część po tym — zarządzanie, egzekwowanie zasad i audytowalność w środowisku uruchomieniowym.

## Co Naprawdę Robi Każdy Projekt

**Microsoft Agent Framework (MAF)** dostarcza model programowania: wieloagentowe przepływy pracy, interoperabilność protokołu A2A, hooki middleware, pamięć i zarządzany hosting przez Foundry Agent Service. Obsługuje bezpieczeństwo treści na poziomie wejścia/wyjścia modelu.

**Agent Governance Toolkit (AGT)** podłącza się do tego samego pipeline middleware, by zarządzać *działaniami*. Każde wywołanie narzędzia, dostęp do zasobów i wiadomość między agentami są oceniane względem zasad przed wykonaniem. Narzut poniżej milisekundy. Bez sidecarów, bez proxy, bez modyfikowanych promptów.

```
Działanie Agenta --> Sprawdzenie Zasad --> Zezwól / Odrzuć --> Dziennik Audytu    (< 0.1 ms)
```

Różne warstwy, pełne pokrycie, jeden pipeline.

## Podłączenie To Tylko Dodanie Middleware

W Pythonie AGT dodaje się do tego samego parametru `middleware`, którego używałbyś do logowania lub filtrów treści:

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

W .NET ten sam wzorzec przez `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Ten sam agent, ta sama orkiestracja, te same narzędzia. AGT dodaje możliwości zarządzania bez modyfikowania logiki agenta.

## Co Otrzymujesz

- **GovernancePolicyMiddleware** — ocenia każde działanie względem deklaratywnych reguł zasad
- **CapabilityGuardMiddleware** — lista dozwolonych narzędzi, które agent może wywoływać (narzędzie `approve_small_loan` celowo nie jest na liście dozwolonych powyżej)
- **RogueDetectionMiddleware** — wykrywa anomalne wzorce zachowania w środowisku uruchomieniowym
- **AuditTrailMiddleware** — dziennik audytu z łańcuchem Merkle, by każde działanie było kryptograficznie odporne na manipulację

Ten ostatni liczy się dla zgodności z przepisami. Łańcuch Merkle oznacza, że jeśli ktoś zmodyfikuje dziennik, łańcuch się zerwie. Audyt jest dowodem.

## Pięć Scenariuszy Branżowych

Repozytorium AGT zawiera pięć kompletnych scenariuszy end-to-end: usługi finansowe (pracownik kredytowy), opieka zdrowotna (dane pacjentów), prawny (przegląd umów), rząd (usługi dla obywateli) i produkcja (kontrola jakości). Każdy łączy prawdziwych agentów MAF z prawdziwym middleware zarządzania AGT.

To nie są zabawkowe demo. To właśnie te scenariusze, gdzie naprawdę potrzebowałbyś zarządzania w produkcji.

## Podsumowanie

Jeśli budujesz agentów, którzy dotykają prawdziwych danych, podejmują decyzje z konsekwencjami lub działają bez nadzoru w produkcji — zarządzanie nie jest opcjonalne. Kombinacja MAF + AGT daje Ci pełny stos: zbuduj z Agent Framework, zarządzaj z AGT.

Oba projekty są open source. Oryginalny artykuł zawiera linki do pełnych przykładów kodu.

Oryginalny wpis: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
