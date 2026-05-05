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

Semantic Kernel (SK) is Microsoft's open-source SDK for building AI orchestration into .NET (and Python/Java) applications. It's the layer between your app code and LLMs: it handles prompts, plugins, memory, and multi-step planning so you don't have to wire everything together manually.

This tutorial gets you from zero to a working SK-powered console app that calls an LLM and uses a plugin.

## Prerequisites

- .NET 8 or later
- An OpenAI API key or an Azure OpenAI deployment

## Step 1: Install the SDK

```bash
dotnet new console -n SkDemo
cd SkDemo
dotnet add package Microsoft.SemanticKernel
```

## Step 2: Set up the kernel

The `Kernel` is the central object in SK. You configure it with an AI service (OpenAI, Azure OpenAI, or a local model):

```csharp
using Microsoft.SemanticKernel;

var builder = Kernel.CreateBuilder();

builder.AddOpenAIChatCompletion(
    modelId: "gpt-4o-mini",
    apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!
);

Kernel kernel = builder.Build();
```

## Step 3: Invoke a prompt

The simplest thing SK does: send a prompt to the LLM and get a response.

```csharp
var result = await kernel.InvokePromptAsync(
    "Summarize the key features of .NET 10 in three bullet points."
);

Console.WriteLine(result);
```

That's it for the basics. But SK's real power is in **plugins**.

## Step 4: Create a plugin

A plugin is a C# class whose methods SK can call as tools. Here's a simple one:

```csharp
using System.ComponentModel;
using Microsoft.SemanticKernel;

public class DatePlugin
{
    [KernelFunction, Description("Returns the current date and time.")]
    public string GetCurrentDate() => DateTime.UtcNow.ToString("R");
}
```

Register it with the kernel:

```csharp
kernel.ImportPluginFromObject(new DatePlugin());
```

## Step 5: Let the kernel call the plugin

Enable automatic function calling so the LLM can invoke plugins when needed:

```csharp
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

The model will call `GetCurrentDate()` automatically and incorporate the result into its response.

## What to explore next

- **Planners** — have SK break a complex task into steps and execute them
- **Memory** — add semantic search over your documents using embeddings
- **Agents** — build multi-agent workflows using the `AgentGroupChat` API

The [Semantic Kernel repo on GitHub](https://github.com/microsoft/semantic-kernel) has a rich set of samples in `dotnet/samples/` covering all of these scenarios.
