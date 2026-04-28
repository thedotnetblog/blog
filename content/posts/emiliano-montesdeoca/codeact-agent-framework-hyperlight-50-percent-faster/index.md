---
title: "CodeAct in Agent Framework: How to Cut Your Agent's Latency in Half"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct collapses multi-step tool chains into a single sandboxed code block — cutting latency by 52% and token usage by 64%. Here's what it means for your agents and when to reach for it."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

There's a moment in every agent project where you look at the trace and think: "why is this taking so long?" The model is fine. The tools work. But there are seven round trips to get a result you could compute in one shot.

That's exactly the problem CodeAct solves — and the [Agent Framework team just shipped alpha support for it](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) via a new `agent-framework-hyperlight` package.

## What is CodeAct?

The [CodeAct pattern](https://arxiv.org/abs/2402.01030) is elegantly simple: instead of giving the model a list of tools and letting it call them one by one, you give it a single `execute_code` tool and let it express the *entire plan* as a short Python program. The agent writes the code once, the sandbox runs it, and you get back a single consolidated result.

A five-step plan that used to be five model turns becomes one `execute_code` turn containing a Python script that calls your tools via `call_tool(...)`.

The benchmark in the repo makes this concrete. Eight users, dozens of orders, five tools (list users, get orders, discount rate, tax rate, compute line total). Same model, same tools, same prompt — just different wiring:

| Wiring | Time | Tokens |
|--------|------|--------|
| Traditional | 27.81s | 6,890 |
| CodeAct | 13.23s | 2,489 |
| **Improvement** | **52.4%** | **63.9%** |

That's not a micro-benchmark. That's a realistic workload with real orchestration overhead.

## The safety piece: Hyperlight micro-VMs

Here's the thing that made me actually excited about this: safety has historically been CodeAct's Achilles heel. If you're running model-generated code, where exactly is it running? Against your process? In a shared container?

The `agent-framework-hyperlight` package solves this with [Hyperlight](https://github.com/hyperlight-dev/hyperlight) micro-VMs. Every single `execute_code` call gets its own freshly created micro-VM — with its own memory, no host filesystem access beyond what you explicitly mount, and no network access beyond the domains you allow. Startup is measured in milliseconds. The isolation is basically free.

Your tools still run on the host (they're your code, with your access). The model-generated *glue* — the Python that decides which tools to call and in what order — runs sandboxed. That's the right split.

## Wiring it up

The minimal setup is straightforward:

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)

result = await agent.run(
    "Get the weather for Seattle and Amsterdam and compare them."
)
```

The provider registers `execute_code` on every run and injects the CodeAct instructions into the system prompt automatically. You don't need to write a custom prompt fragment.

## Mixing CodeAct with approval-gated tools

This is where it gets interesting. Not every tool should run inside the sandbox without approval. You might want to gate `send_email` or `charge_credit_card` individually. The framework handles this cleanly:

```python
@tool(approval_mode="always_require")
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email. Requires approval on every call."""
    ...

agent = Agent(
    client=client,
    name="MixedToolsAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
    tools=[send_email],  # invoked directly, approval-gated
)
```

Tools on the provider → the model reaches them via `call_tool(...)` inside the sandbox, cheap and chainable.  
Tools on the agent directly → the model calls them as first-class tool calls, approval applies individually.

That's a clean split: chainable data-lookup tools go through CodeAct, side-effect tools stay on the agent.

## When to use CodeAct (and when not to)

**Reach for CodeAct when:**
- The task chains many small tool calls (lookups, joins, computations, formatting)
- You care about latency and token cost
- You want strong per-call isolation on model-generated code by default
- Tools are cheap and safe to invoke in sequence

**Stick with traditional tool-calling when:**
- The agent only makes one or two tool calls per turn
- Each tool has side effects you want approved individually
- Tool descriptions are sparse or ambiguous — CodeAct relies on good docstrings

That last point matters. Because the model writes Python that calls your tools by name, docstrings and parameter annotations become part of the contract the model reasons about. Weak descriptions hurt CodeAct more than traditional tool-calling.

## Try it now

```bash
pip install agent-framework-hyperlight --pre
# or
uv add --prerelease=allow agent-framework-hyperlight
```

Samples are under [`python/packages/hyperlight/samples/`](https://github.com/microsoft/agent-framework/tree/main/python/packages/hyperlight/samples). The [benchmark sample](https://github.com/microsoft/agent-framework/blob/main/python/packages/hyperlight/samples/codeact_benchmark.py) is the best place to start — run it against your own tools to see if the wins apply to your workload.

Worth noting: Linux and Windows are supported today. macOS support is on the way. A .NET counterpart is also coming, so if you're on C#, keep an eye on the repo.

## Wrapping up

CodeAct isn't magic — it's a sensible pattern that was just too risky to use without proper sandboxing. Hyperlight changes that equation. Per-call micro-VM isolation, millisecond startup, 50%+ latency improvement on the right workloads. That's a combination worth experimenting with.

Check the [full post on the Agent Framework blog](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) for deeper coverage on filesystem mounts, network policy, and the standalone `HyperlightExecuteCodeTool` wiring.
