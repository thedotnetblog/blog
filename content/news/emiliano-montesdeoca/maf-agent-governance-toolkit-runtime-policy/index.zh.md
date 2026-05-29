---
title: "构建智能体是容易的部分——安全运行它们才是难的部分"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 与 Agent Governance Toolkit 协同工作，在运行时执行策略、管理工具调用并提供 Merkle 链式审计日志——无需修改智能体提示词。"
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

在 AI 智能体开发中，有一个我开始称为"演示后悔"的模式。智能体在演示中运行良好。然后有人问：如果它调用了错误的工具会怎样？如果它访问了不该访问的数据？谁审计了这个？

Microsoft Agent Framework 为构建和编排提供支持。Agent Governance Toolkit（AGT）覆盖之后的部分——治理、策略执行以及运行时可审计性。

## 每个项目的实际用途

**Microsoft Agent Framework (MAF)** 提供编程模型：多智能体工作流、A2A 协议互操作性、中间件钩子、内存以及通过 Foundry Agent Service 进行托管。它在模型输入/输出层面处理内容安全。

**Agent Governance Toolkit (AGT)** 插入相同的中间件管道以管理*操作*。每次工具调用、资源访问和智能体间消息在执行前都会根据策略进行评估。亚毫秒级开销。无 sidecar，无代理，无修改的提示词。

```
智能体操作 --> 策略检查 --> 允许 / 拒绝 --> 审计日志    (< 0.1 ms)
```

不同层次，完整覆盖，一个管道。

## 接入只需添加中间件

在 Python 中，AGT 添加到与日志记录或内容过滤器相同的 `middleware` 参数：

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

在 .NET 中，通过 `.Use()` 使用相同模式：

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

相同的智能体，相同的编排，相同的工具。AGT 在不修改智能体逻辑的情况下添加治理能力。

## 你能获得什么

- **GovernancePolicyMiddleware** — 根据声明式策略规则评估每个操作
- **CapabilityGuardMiddleware** — 白名单规定智能体允许调用哪些工具（上面 `approve_small_loan` 工具故意不在允许列表中）
- **RogueDetectionMiddleware** — 在运行时检测异常行为模式
- **AuditTrailMiddleware** — Merkle 链式审计日志，使每个操作在密码学上防篡改

最后一点对合规性很重要。Merkle 链意味着如果有人修改日志，链就会断裂。审计即证据。

## 五个行业场景

AGT 代码库包含五个完整的端到端场景：金融服务（贷款专员）、医疗（患者数据）、法律（合同审查）、政府（公民服务）和制造（质量控制）。每个场景都将真实的 MAF 智能体与真实的 AGT 治理中间件配对。

这些不是玩具演示。它们是您在生产中实际需要治理的那类场景。

## 总结

如果您正在构建涉及真实数据、做出有后果决策或在生产中无人监管运行的智能体——治理不是可选的。MAF + AGT 的组合提供完整的技术栈：用 Agent Framework 构建，用 AGT 治理。

两个项目都是开源的。原文包含完整代码示例的链接。

原文链接：[Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
