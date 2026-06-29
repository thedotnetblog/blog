---
title: "Getting Started with Semantic Kernel"
date: 2026-02-10
author: "Emiliano Montesdeoca"
description: "A practical first look at Semantic Kernel — the open-source SDK from Microsoft for building AI-powered .NET applications with LLMs, plugins, and memory."
tags:
  - semantic-kernel
  - ai
  - dotnet
  - azure
---

Semantic Kernel (SK) is Microsoft's open-source SDK for building AI orchestration into .NET, Python, and Java applications. Think of it as the layer between your application code and the model. It helps you structure prompts, register plugins, route function calls, and manage multi-step interactions without forcing you to glue every piece together by hand.

That matters because a production AI app is usually more than a single prompt. You need configuration, tool access, memory, chat history, and a way to keep the system understandable as the workflow grows. SK is designed for that middle layer, where your app knows what it wants to do but still needs a model to help do it.

This tutorial takes you from a fresh console app to a working SK-powered example that calls an LLM and uses a plugin. The goal is not to cover every feature. The goal is to give you a clear mental model you can build on.

## Why Semantic Kernel exists

If you call an LLM directly, you get flexibility but not much structure. You still need to decide where prompts live, how tools are exposed, how chat state is stored, and how the app should respond when the model needs help from the outside world.

SK exists to make those decisions explicit. The kernel is the composition root. Plugins expose C# methods to the model. Prompt execution settings control how the model behaves. Memory and chat history help the app stay coherent across turns. That gives you a predictable architecture instead of a loose collection of prompt calls.

## Prerequisites

- .NET 8 or later
- An OpenAI API key or an Azure OpenAI deployment
- A console app where you can test prompts safely

## Step 1: Install the SDK

Create a new project and install the package:

```bash
dotnet new console -n SkDemo
cd SkDemo
dotnet add package Microsoft.SemanticKernel
```

The package gives you the kernel, plugin abstractions, and the prompt execution primitives you need for the rest of the tutorial. Once the package is in place, the next step is deciding how your app will talk to a model.

## Step 2: Set up the kernel

The `Kernel` is the central object in SK. It holds the services your app uses to talk to the model and it gives you a place to register plugins and other shared capabilities. You can think of it as the runtime container that keeps your AI logic organized.

```csharp
using Microsoft.SemanticKernel;

var builder = Kernel.CreateBuilder();

builder.AddOpenAIChatCompletion(
    modelId: "gpt-4o-mini",
    apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!
);

Kernel kernel = builder.Build();
```

If you are using Azure OpenAI instead of the public OpenAI API, the shape is the same even though the connection details differ. The important part is that the model configuration is centralized in one place rather than scattered across every call site.

## Step 3: Invoke a prompt

The simplest thing SK does is send a prompt to the model and return the response.

```csharp
var result = await kernel.InvokePromptAsync(
    "Summarize the key features of .NET 10 in three bullet points."
);

Console.WriteLine(result);
```

This is the baseline. Before you add chat history, plugins, or planners, it is useful to verify that the model connection works and that the prompt path behaves as expected. A tiny prompt test can save a lot of time when you later debug tool calling or memory behavior.

## Step 4: Create a plugin

Plugins are where SK becomes more interesting. A plugin is just a C# class with methods the model can call as tools. That gives you a clean way to expose deterministic application logic to a probabilistic model.

```csharp
using System.ComponentModel;
using Microsoft.SemanticKernel;

public class DatePlugin
{
    [KernelFunction, Description("Returns the current date and time.")]
    public string GetCurrentDate() => DateTime.UtcNow.ToString("R");
}
```

The plugin method should be small, predictable, and clearly described. The description matters because the model uses it to decide when the function is relevant. In production code, good plugin design usually means each function does one thing, returns a simple shape, and avoids side effects unless those side effects are intentional.

Register the plugin with the kernel:

```csharp
kernel.ImportPluginFromObject(new DatePlugin());
```

At this point the kernel can see the plugin, but the model still needs to be told that it is allowed to use tools automatically.

## Step 5: Let the kernel call the plugin

Automatic function calling is where the flow starts to feel intelligent. Instead of the app manually deciding when to call `GetCurrentDate()`, the model can ask for it as part of answering the user.

```csharp
using Microsoft.SemanticKernel.Connectors.OpenAI;

var settings = new OpenAIPromptExecutionSettings
{
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
};

var result = await kernel.InvokePromptAsync(
    "What is today's date? Format it nicely.",
    new KernelArguments(settings)
);

Console.WriteLine(result);
```

The important distinction is that the model is not directly running arbitrary code. It is selecting from functions you explicitly registered, and SK is handling the orchestration around that selection. That keeps the boundary between application logic and model behavior much safer and easier to inspect.

## How to think about SK in a real app

Once you move past the toy example, SK usually becomes part of a larger architecture. You might keep chat history in a database, use embeddings for semantic search, register several plugins for different parts of your domain, or build an agent workflow on top of the same kernel.

The core pattern stays the same. The model should be good at interpretation and language generation. Your code should be good at state, rules, and side effects. Semantic Kernel helps you keep those responsibilities separated instead of mixing them into one long prompt.

That separation also makes testing easier. You can unit test plugin methods directly. You can test prompt behavior separately. You can review the execution settings that control tool usage, instead of guessing why the model decided to call a function.

## What to watch for

- Keep prompts specific enough that the model does not have to guess at the desired output.
- Treat plugins like public APIs and document them well.
- Be careful with secrets and file access; the model should only see what it truly needs.
- Review model and connector settings before you ship, because defaults that are fine in a demo may not be ideal in production.

These are the same trade-offs you would manage in any application with external dependencies, but AI systems make them more visible because the behavior is less deterministic.

## What to explore next

From here, the natural next steps are planners, memory, and agents. Planners let SK break a larger task into smaller pieces. Memory lets you add semantic search over your own data. Agents let you build multi-step workflows with clearer boundaries between roles.

If you want examples, the [Semantic Kernel repository on GitHub](https://github.com/microsoft/semantic-kernel) has a broad set of samples in `dotnet/samples/` that show how these pieces fit together in real applications.
