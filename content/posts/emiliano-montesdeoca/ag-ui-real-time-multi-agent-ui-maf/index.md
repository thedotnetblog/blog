---
title: "Building Real-Time Multi-Agent UIs That Don't Feel Like a Black Box"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI and Microsoft Agent Framework team up to give multi-agent workflows a proper frontend — with real-time streaming, human approvals, and full visibility into what your agents are doing."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

Here's the thing about multi-agent systems: they look incredible in demos. Three agents passing work around, solving problems, making decisions. Then you try to put it in front of actual users and... silence. A spinning indicator. No idea which agent is doing what or why the system is paused. That's not a product — that's a trust problem.

The Microsoft Agent Framework team just published a [fantastic walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) on pairing MAF workflows with [AG-UI](https://github.com/ag-ui-protocol/ag-ui), an open protocol for streaming agent execution events to a frontend over Server-Sent Events. And honestly? This is the kind of bridge we've been missing.

## Why this matters for .NET developers

If you're building AI-powered apps, you've probably hit this wall. Your backend orchestration works great — agents hand off to each other, tools fire, decisions get made. But the frontend has no clue what's happening behind the scenes. AG-UI fixes that by defining a standard protocol for streaming agent events (think `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) directly to your UI layer over SSE.

The demo they built is a customer support workflow with three agents: a triage agent that routes requests, a refund agent that handles money stuff, and an order agent that manages replacements. Each agent has its own tools, and the handoff topology is explicitly defined — no "figure it out from the prompt" vibes.

## The handoff topology is the real star

What caught my eye is how `HandoffBuilder` lets you declare a directed routing graph between agents:

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

Each `add_handoff` creates a directed edge with a natural-language description. The framework generates handoff tools for each agent based on this topology. So routing decisions are grounded in your orchestration structure, not just whatever the LLM feels like doing. That's a huge deal for production reliability.

## Human-in-the-loop that actually works

The demo showcases two interrupt patterns that any real-world agent app needs:

**Tool approval interrupts** — when an agent calls a tool marked with `approval_mode="always_require"`, the workflow pauses and emits an event. The frontend renders an approval modal with the tool name and arguments. No token-burning retry loops — just a clean pause-approve-resume flow.

**Information request interrupts** — when an agent needs more context from the user (like an order ID), it pauses and asks. The frontend shows the question, the user responds, and execution resumes from exactly where it stopped.

Both patterns stream as standard AG-UI events, so your frontend doesn't need custom logic per agent — it just renders whatever event comes through the SSE connection.

## Wiring it up is surprisingly simple

The integration between MAF and AG-UI is a single function call:

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

The `workflow_factory` creates a fresh workflow per thread, so each conversation gets isolated state. The endpoint handles all the SSE plumbing automatically. If you're already using FastAPI (or can add it as a lightweight layer), this is almost zero friction.

## My take

For us .NET developers, the immediate question is: "Can I do this in C#?" The Agent Framework is available for both .NET and Python, and the AG-UI protocol is language-agnostic (it's just SSE). So while this specific demo uses Python and FastAPI, the pattern translates directly. You could wire up an ASP.NET Core minimal API with SSE endpoints following the same AG-UI event schema.

The bigger takeaway is that multi-agent UIs are becoming a first-class concern, not an afterthought. If you're building anything where agents interact with humans — customer support, approval workflows, document processing — this combination of MAF orchestration and AG-UI transparency is the pattern to follow.

## Wrapping up

AG-UI + Microsoft Agent Framework gives you the best of both worlds: robust multi-agent orchestration on the backend and real-time visibility on the frontend. No more black-box agent interactions.

Check out the [full walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) and the [AG-UI protocol repo](https://github.com/ag-ui-protocol/ag-ui) to dig deeper.
