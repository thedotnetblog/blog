---
title: "Construir Agentes É a Parte Fácil — Executá-los com Segurança É a Parte Difícil"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework e Agent Governance Toolkit se unem para aplicar políticas em tempo de execução, governar chamadas de ferramentas e fornecer logs de auditoria encadeados com Merkle — sem tocar nos prompts do agente."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Existe um padrão no desenvolvimento de agentes de IA que comecei a chamar de "arrependimento de demo". O agente funciona muito bem nas demos. Então alguém pergunta: o que acontece se ele chamar a ferramenta errada? E se acessar dados que não deveria? Quem auditou isso?

Microsoft Agent Framework te apoia na construção e orquestração. Agent Governance Toolkit (AGT) cobre a parte posterior — governança, aplicação de políticas e auditabilidade em tempo de execução.

## O Que Cada Projeto Realmente Faz

**Microsoft Agent Framework (MAF)** fornece o modelo de programação: workflows multi-agente, interoperabilidade do protocolo A2A, hooks de middleware, memória e hospedagem gerenciada via Foundry Agent Service. Lida com segurança de conteúdo no nível de entrada/saída do modelo.

**Agent Governance Toolkit (AGT)** se conecta a esse mesmo pipeline de middleware para governar *ações*. Cada chamada de ferramenta, acesso a recursos e mensagem inter-agentes é avaliada contra a política antes da execução. Overhead submilissegundo. Sem sidecars, sem proxies, sem prompts modificados.

```
Ação do Agente --> Verificação de Política --> Permitir / Negar --> Log de Auditoria    (< 0.1 ms)
```

Camadas diferentes, cobertura completa, um pipeline.

## Conectar-se É Apenas Adicionar Middleware

Em Python, o AGT adiciona ao mesmo parâmetro `middleware` que você usaria para registro ou filtros de conteúdo:

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

Em .NET, mesmo padrão via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Mesmo agente, mesma orquestração, mesmas ferramentas. O AGT adiciona capacidades de governança sem tocar na lógica do agente.

## O Que Você Obtém

- **GovernancePolicyMiddleware** — avalia cada ação contra regras de política declarativas
- **CapabilityGuardMiddleware** — lista de permissão das ferramentas que um agente pode chamar (a ferramenta `approve_small_loan` não está na lista permitida acima — deliberadamente)
- **RogueDetectionMiddleware** — detecta padrões de comportamento anômalo em tempo de execução
- **AuditTrailMiddleware** — log de auditoria encadeado com Merkle para que cada ação seja criptograficamente resistente a adulterações

Este último importa para conformidade. Uma cadeia Merkle significa que se alguém modificar o log, a cadeia quebra. A auditoria é a evidência.

## Cinco Cenários da Indústria

O repositório AGT inclui cinco cenários completos de ponta a ponta: serviços financeiros (agente de empréstimos), saúde (dados de pacientes), jurídico (revisão de contratos), governo (serviços ao cidadão) e manufatura (controle de qualidade). Cada um combina agentes MAF reais com middleware de governança AGT real.

Não são demos de brinquedo. São o tipo de cenários em que você realmente precisaria de governança em produção.

## Conclusão

Se você está construindo agentes que tocam dados reais, tomam decisões com consequências, ou executam sem supervisão em produção — a governança não é opcional. A combinação MAF + AGT fornece o stack completo: construa com Agent Framework, governe com AGT.

Ambos os projetos são open source. O artigo original tem links para os exemplos de código completos.

Post original: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
