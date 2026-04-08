---
title: "构建不像黑盒的实时多智能体UI"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI和Microsoft Agent Framework联手为多智能体工作流提供真正的前端——实时流式传输、人工审批，以及对智能体行为的完整可视化。"
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}})。*

多智能体系统的问题在于：它们在演示中看起来令人难以置信。三个智能体互相传递工作、解决问题、做出决策。然后你试图把它展示给真实用户，得到的却是……沉默。一个旋转的加载指示器。完全不知道哪个智能体在做什么，或者系统为什么暂停了。这不是产品——这是信任问题。

Microsoft Agent Framework团队刚刚发布了一篇[精彩的教程](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)，介绍如何将MAF工作流与[AG-UI](https://github.com/ag-ui-protocol/ag-ui)配合使用。AG-UI是一个开放协议，通过Server-Sent Events将智能体执行事件流式传输到前端。说实话，这正是我们一直缺少的桥梁。

## 为什么这对.NET开发者很重要

如果你在构建AI驱动的应用，可能已经遇到过这堵墙。你的后端编排工作得很好——智能体之间传递任务、工具触发、决策做出。但前端完全不知道幕后发生了什么。AG-UI通过定义一个标准协议来解决这个问题，将智能体事件（想想`RUN_STARTED`、`STEP_STARTED`、`TOOL_CALL_*`、`TEXT_MESSAGE_*`）通过SSE直接传输到你的UI层。

他们构建的演示是一个包含三个智能体的客户支持工作流：一个路由请求的分诊智能体、一个处理退款事务的退款智能体，以及一个管理换货的订单智能体。每个智能体都有自己的工具，交接拓扑是明确定义的——没有"从提示词中猜测"的感觉。

## 交接拓扑才是真正的主角

让我眼前一亮的是`HandoffBuilder`如何让你声明智能体之间的有向路由图：

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

每个`add_handoff`创建一条带有自然语言描述的有向边。框架基于这个拓扑为每个智能体生成交接工具。因此路由决策是基于你的编排结构，而不是LLM随意决定的。这对生产环境的可靠性意义重大。

## 真正有效的人机协作

演示展示了任何真实世界智能体应用都需要的两种中断模式：

**工具审批中断** ——当智能体调用标记为`approval_mode="always_require"`的工具时，工作流暂停并发出事件。前端渲染一个包含工具名称和参数的审批模态框。没有烧掉token的重试循环——只是一个干净的暂停-审批-恢复流程。

**信息请求中断** ——当智能体需要用户提供更多上下文（比如订单ID）时，它会暂停并询问。前端显示问题，用户回答，执行从停止的地方精确恢复。

两种模式都作为标准AG-UI事件进行流式传输，所以你的前端不需要针对每个智能体的自定义逻辑——只需渲染通过SSE连接传来的任何事件。

## 接入出奇地简单

MAF和AG-UI之间的集成就是一个函数调用：

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

`workflow_factory`为每个线程创建一个新的工作流，这样每个对话都有隔离的状态。端点自动处理所有SSE管道。如果你已经在使用FastAPI（或者可以把它作为轻量层添加），这几乎是零摩擦的。

## 我的看法

对于我们.NET开发者来说，第一个问题是："我能用C#做这个吗？"Agent Framework同时支持.NET和Python，AG-UI协议是语言无关的（只是SSE）。所以虽然这个特定演示使用Python和FastAPI，但模式可以直接移植。你可以用ASP.NET Core最小API配合SSE端点，遵循相同的AG-UI事件模式来实现。

更重要的启示是，多智能体UI正在成为一等公民的关注点，而不是事后才想到的事情。如果你在构建任何需要智能体与人类交互的东西——客户支持、审批工作流、文档处理——MAF编排加AG-UI透明度的组合就是应该遵循的模式。

## 总结

AG-UI + Microsoft Agent Framework给你两全其美：后端强大的多智能体编排和前端的实时可视化。不再有黑盒式的智能体交互。

查看[完整教程](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/)和[AG-UI协议仓库](https://github.com/ag-ui-protocol/ag-ui)以深入了解。
