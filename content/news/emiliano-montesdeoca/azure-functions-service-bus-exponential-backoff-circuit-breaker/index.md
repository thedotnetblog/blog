---
title: "Stop Hammering a Struggling Dependency: Retry Patterns for Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Exponential backoff and circuit breaker patterns are now natively supported for Service Bus-triggered Azure Functions — here's how they work and why you want both."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Here's how a recoverable fault becomes an outage in a Functions app: a dependency starts timing out, every Function instance retries immediately and indefinitely, the dependency gets hammered with hundreds of concurrent failed requests, and what started as a transient hiccup turns into a system-wide backpressure event.

You probably know this story. Azure Functions scale out fast — that's the whole point. But "scale out fast" and "retry immediately" together can make failures dramatically worse.

Two patterns help. Exponential backoff and circuit breaker. Both are now natively supported for Service Bus-triggered Azure Functions.

## Two Patterns, Different Roles

These patterns are complementary, not alternatives:

**Exponential backoff** answers: *when should I try again?*
It increases the delay between retries so a dependency has time to recover. Message-level, pacing the retry timing.

**Circuit breaker** answers: *should I call this dependency at all right now?*
It stops repeated calls to an unhealthy dependency after a failure threshold is hit, then probes carefully after a cooldown period. System-level, preventing retry storms.

You want both. Backoff handles per-message retry pacing. Circuit breaker handles aggregate health decisions.

## Why This Matters Especially for Service Bus

The queue absorbs burst traffic, which is good. But without controls, the queue can grow while workers keep wasting compute on calls that will fail. Poison messages stay active longer than they should. Hot partitions or limited downstream capacity create cascading problems.

The safer design:

1. Detect transient failure
2. Delay the next attempt with exponential backoff
3. Stop calling the dependency when a failure threshold is reached (circuit open)
4. Resume carefully after a cooldown period (circuit probe)
5. Move irrecoverable work to dead-letter or a quarantine path

## What the Native Support Looks Like

The new support integrates with the existing Azure Functions host model — no extra libraries, no custom implementations. Configuration goes in your `host.json`:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

Circuit breaker configuration sets the failure threshold and reset interval so unhealthy dependencies don't get pummeled during recovery.

## Languages Covered

This isn't .NET only. The feature covers dotnet, JavaScript, TypeScript, and Python — the full set of Service Bus trigger supported languages in Azure Functions.

## Wrapping Up

Retry patterns aren't exciting to configure until the first time a downstream outage causes your Functions to compound the problem instead of gracefully degrading. Setting these up proactively is cheap. Retrofitting them during an incident is not.

Original post: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
