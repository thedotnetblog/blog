---
title: "Where Does Your Agent Remember Things? A Practical Guide to Chat History Storage"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Service-managed or client-managed? Linear or forking? The architectural decision that shapes what your AI agent can actually do — with code examples in C# and Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

When you build an AI agent, you spend most of your energy on the model, the tools, and the prompts. The question of *where the conversation history lives* feels like an implementation detail — but it's actually one of the most important architectural decisions you'll make.

It determines whether users can branch conversations, undo responses, resume sessions after a restart, and whether your data ever leaves your infrastructure. The [Agent Framework team published a deep dive on this](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) and it's worth understanding the full landscape.

## Two fundamental patterns

**Service-managed**: the AI service stores the conversation state. Your app holds a reference (a thread ID, a response ID) and the service automatically includes relevant history on each request. Simpler to set up. Less control.

**Client-managed**: your app maintains the full history and sends relevant messages with every request. The service is stateless. You control everything — what gets sent, how it's compressed, where it lives.

Neither is universally better. The right choice depends on what you're building.

## Service-managed: linear vs forking

Not all service-managed storage is the same. There are two distinct models:

**Linear (single-threaded)**: messages form an ordered sequence. You can append, but you can't branch. This is the traditional chat model — used by Foundry Prompt Agents and the now-deprecated OpenAI Assistants API. Great for chatbots and support agents. Terrible if you want "try again" or parallel exploration.

**Forking-capable**: each response has a unique ID, and new requests can reference *any* previous response as the continuation point. This is what the Responses API (Microsoft Foundry, Azure OpenAI, OpenAI) supports. Users can branch conversations, build "undo" flows, explore multiple answer paths.

If you're building any kind of agentic workflow where multiple paths might be explored, forking is a capability you want.

## Client-managed: you own the complexity

When the service doesn't store history, your app does everything:

- **Context window management** — you can't send unlimited history. You need truncation, sliding windows, summarization, or tool-call collapse strategies.
- **Persistence** — in-memory works for demos. Production needs a database, Redis, or blob storage.
- **Privacy** — conversation data never leaves your infrastructure unless you explicitly send it.

The upside on privacy is real. For sensitive applications where you can't have conversation history sitting on a third-party server, client-managed is the only option.

Agent Framework ships built-in compaction strategies for all the common patterns, so you don't have to build them from scratch. But you do need to choose and configure the right one.

## How Agent Framework abstracts this

The beauty of the framework is that your agent invocation code stays the same regardless of which storage model you're using. The `AgentSession` handles the underlying differences.

In C#:
```csharp
// Works with Chat Completions (client-managed)
// AND with Responses API (service-managed)
// The session handles the details.
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("My name is Alice.", session);
var second = await agent.RunAsync("What is my name?", session);
```

In Python:
```python
session = agent.create_session()
first = await agent.run("My name is Alice.", session=session)
second = await agent.run("What is my name?", session=session)
```

When you switch from OpenAI Chat Completions to the Responses API, you change the client configuration — not the agent invocation code.

## The Responses API is uniquely flexible

Most providers have a fixed storage model. The Responses API is the exception — it's configurable via the `store` parameter:

- **`store=true` (default)**: service stores each response, supports forking via response IDs. Service handles compaction.
- **`store=false`**: service is stateless, Agent Framework manages history client-side. You control compaction.
- **Conversations API**: linear thread model on top of Responses. Pass a conversation ID instead of a response ID.

Here's the client-managed mode in practice (C#):

```csharp
AIAgent agent = new OpenAIClient("<your_api_key>")
    .GetResponseClient("gpt-5.4-mini")
    .AsIChatClientWithStoredOutputDisabled()
    .AsAIAgent(new ChatClientAgentOptions
    {
        ChatOptions = new() { Instructions = "You are a helpful assistant." },
        ChatHistoryProvider = new InMemoryChatHistoryProvider()
    });
```

And in Python:

```python
agent = Agent(
    client=OpenAIChatClient(),
    name="StatelessAgent",
    instructions="You are a helpful assistant.",
    default_options={"store": False},
    context_providers=[InMemoryHistoryProvider("memory", load_messages=True)],
)
```

Swap `InMemoryHistoryProvider` for your `DatabaseHistoryProvider` when you're ready for production persistence.

## Provider quick reference

| Provider | Storage | Model | Compaction |
|----------|---------|-------|------------|
| OpenAI / Azure OpenAI Chat Completions | Client | N/A | You |
| Foundry Agent Service | Service | Linear | Service |
| Responses API (default) | Service | Forking | Service |
| Responses API (`store=false`) | Client | N/A | You |
| Anthropic Claude, Ollama | Client | N/A | You |

## How to choose

Start with these questions:

1. **Do you need conversation branching or "undo"?** → Forking service-managed (Responses API)
2. **Do you need full data sovereignty?** → Client-managed, with a database-backed provider
3. **Is this a simple chatbot or support flow?** → Service-managed linear is fine
4. **Do you need to migrate between providers later?** → Client-managed gives you portability

The most important thing: don't default to whatever is easiest to start with and forget to revisit it. Changing storage patterns after launch is painful.

## Wrapping up

Chat history storage shapes what your agents can actually do — not just in demos but in production, under real user behavior. Agent Framework's abstractions let you evolve your choice without rewriting your application logic, which is genuinely useful when you're still figuring out the right model.

Read the [full post](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) for the complete decision tree, the Conversations API walkthrough, and the compaction strategy details.
