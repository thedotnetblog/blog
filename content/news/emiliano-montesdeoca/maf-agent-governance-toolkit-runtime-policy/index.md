---
title: "Building Agents Is the Easy Part — Running Them Safely Is the Hard Part"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework and Agent Governance Toolkit pair up to enforce runtime policy, govern tool calls, and provide Merkle-chained audit logs — without touching your agent prompts."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

There's a pattern in AI agent development that I've started calling "demo regret." The agent works great in demos. Then someone asks: what happens if it calls the wrong tool? What if it accesses data it shouldn't? Who audited that?

Microsoft Agent Framework has your back for building and orchestrating. Agent Governance Toolkit (AGT) covers the part after that — governance, policy enforcement, and auditability at runtime.

## What Each Project Actually Does

**Microsoft Agent Framework (MAF)** gives you the programming model: multi-agent workflows, A2A protocol interoperability, middleware hooks, memory, and managed hosting via Foundry Agent Service. It handles content safety at the model input/output level.

**Agent Governance Toolkit (AGT)** plugs into that same middleware pipeline to govern *actions*. Every tool call, resource access, and inter-agent message gets evaluated against policy before execution. Sub-millisecond overhead. No sidecars, no proxies, no prompts modified.

```
Agent Action --> Policy Check --> Allow / Deny --> Audit Log    (< 0.1 ms)
```

Different layers, complete coverage, one pipeline.

## Plugging In Is Just Adding Middleware

In Python, AGT adds to the same `middleware` parameter you'd use for logging or content filters:

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

In .NET, same pattern via `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Same agent, same orchestration, same tools. AGT adds governance capabilities without touching the agent logic.

## What You Get

- **GovernancePolicyMiddleware** — evaluates every action against declarative policy rules
- **CapabilityGuardMiddleware** — allowlists which tools an agent is permitted to call (the `approve_small_loan` tool isn't in the allowed list above — deliberate)
- **RogueDetectionMiddleware** — detects anomalous behavior patterns at runtime
- **AuditTrailMiddleware** — Merkle-chained audit log so every action is cryptographically tamper-evident

That last one matters for compliance. A Merkle chain means if anyone modifies the log, the chain breaks. The audit is the evidence.

## Five Industry Scenarios

The AGT repo ships five complete end-to-end scenarios: financial services (loan officer), healthcare (patient data), legal (contract review), government (citizen services), and manufacturing (quality control). Each one pairs real MAF agents with real AGT governance middleware.

These aren't toy demos. They're the kind of scenarios where you'd actually need governance in production.

## Wrapping Up

If you're building agents that touch real data, make decisions with consequences, or run unattended in production — governance isn't optional. The combination of MAF + AGT gives you the whole stack: build it with Agent Framework, govern it with AGT.

Both projects are open source. The original article has links to the full code samples.

Original post: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
