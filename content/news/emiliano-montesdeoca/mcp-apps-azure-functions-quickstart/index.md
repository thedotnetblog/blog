---
title: "MCP Apps on Azure Functions: Moving Beyond Text-Only Interfaces"
description: "Azure Functions can host MCP tools and interactive UI resources, giving AI clients dashboards, forms, and workflow interfaces alongside structured responses."
date: 2026-08-31
author: "Emiliano Montesdeoca"
tags: [azure, functions, mcp, serverless]
slug: mcp-apps-azure-functions-quickstart
---

Original source: [MCP Apps on Azure Functions: Quickstart with TypeScript](https://devblogs.microsoft.com/azure-sdk/mcp-apps-on-azure-functions-quickstart-with-typescript/)

The traditional MCP interaction model is text-based. A model sends a structured request, the server returns structured data, and the model decides how to explain it. MCP Apps add another possibility: the server can return an interactive HTML interface such as a dashboard, map, form, or workflow view that renders inside MCP-compatible hosts including Visual Studio Code Copilot, Claude, and ChatGPT.

For .NET developers, this is significant because many internal tools are not really text problems. Deployment status, tenant configuration, approval steps, and operational data are easier to inspect when the user can interact with the result.

## Why MCP Apps Matter

The source's weather example makes the distinction concrete. A text-only tool returns weather data and asks the model to narrate it. An MCP App returns a widget that can display the data and let the user explore it. The interface can support clickable maps or charts, a one-page form for complex setup, rich media, live updates, or multi-step approvals.

This is not a reason to turn every tool into a UI. Text remains the simplest and most accessible response for many requests. The useful question is where conversation is forcing the user through a sequence of questions that an interface could collect or present more clearly.

For a .NET team, good first candidates include a non-critical deployment dashboard, a configuration wizard, or a read-only report with filters. Start with a workflow where the interactive state improves comprehension without giving the widget permission to perform a high-impact action.

## Tools and Resources Have Different Jobs

Azure Functions provides abstractions for both sides of the pattern. MCP tools handle server-side logic: they process client requests, call backend services, and return structured data. MCP resources serve UI payloads such as interactive HTML, JSON documents, or formatted content.

The weather sample includes a `GetWeather` MCP tool and a weather widget resource. Azure Functions serves the resource, the client renders it, and the widget calls the tool when it needs weather data. The UI remains responsive in the client while server-side logic remains responsible for data retrieval.

That separation is worth preserving when designing a .NET implementation. Keep backend authorization, data access, validation, and business rules in the server-side tool. Treat the resource as a client-side view with a narrow interface to those tools. Do not move sensitive logic into HTML or assume that an embedded widget can safely call backend services directly.

The quickstart uses TypeScript, but the source links to .NET, Java, and Python samples. Use the .NET sample and the current Azure Functions MCP binding documentation as the implementation reference for a C# project. The TypeScript API names in the article are useful for understanding the shape of the design, not a promise that the same syntax exists in .NET.

## Local Development and Deployment

The sample's local loop is intentionally ordinary: clone the repository, install dependencies, build, and start the Functions host. The local MCP endpoint is `http://0.0.0.0:7071/runtime/webhooks/mcp`, which can be inspected with MCP Inspector or a compatible client.

For a .NET team, the equivalent discipline is to make the local endpoint and test data explicit. Run the Functions host locally, exercise the tool definition and resource handler with a small set of requests, and verify what the client actually renders. A successful function build does not prove that the embedded UI can load, call the tool, or handle a failed response.

Deployment uses infrastructure as code and Azure Developer CLI commands in the sample. Keep the resource definition, function configuration, and deployment settings under source control. The first deployment should be a low-risk environment where authentication and rendering can be inspected without exposing operational data.

## Security Is Part of the UI Contract

Azure Functions supports function keys and built-in MCP authentication with OAuth. The source points to OAuth for enterprise-grade security, and that distinction matters. Function keys may be convenient for a local experiment, but an MCP App that can view or change sensitive data needs an identity boundary that matches the consequence of the action.

Validate authorization on the server-side tool, not only in the UI. A user may interact with the widget, but the tool remains the authority for access and input validation. Avoid placing secrets in the resource payload, and test what happens when a user opens the resource without permission or when a tool request returns an error.

MCP is still evolving. Tool definitions, resource schemas, and host support can change. Pin dependencies, track the binding version, and include a small compatibility test in the deployment pipeline before making the app part of a critical workflow.

## What .NET Developers Should Try

1. Read the .NET sample alongside the TypeScript quickstart to understand the shared architecture.
2. Choose a read-only dashboard or form as the first experiment.
3. Keep tools responsible for authorization, validation, and data access.
4. Test locally with MCP Inspector before deploying to Azure.
5. Use OAuth and version your dependencies before exposing sensitive workflows.

MCP Apps are not merely prettier tool responses. They change how an AI client can help a user complete a task. Azure Functions makes the serverless hosting path approachable, but the quality of the result still depends on a clean separation between interactive presentation and protected business logic.