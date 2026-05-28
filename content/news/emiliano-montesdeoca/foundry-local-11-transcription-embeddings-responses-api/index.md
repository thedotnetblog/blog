---
title: "Foundry Local 1.1: Real-Time Transcription, Embeddings, and the Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 adds live microphone transcription, text embeddings, and Responses API support — all running locally with no cloud dependency, no network latency, no per-token cost."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 proved the concept: run AI models locally on Windows, macOS (Apple Silicon), and Linux x64 with a developer-friendly SDK. Version 1.1 adds three capabilities that cover a lot of real production use cases.

## Live Audio Transcription

The most significant new feature: real-time speech-to-text streaming directly from the microphone. Captions, voice UIs, meeting transcription, accessibility tooling — all running locally with zero cloud dependency.

The API is session-based and streams results as they arrive, with `is_final` markers to distinguish interim from finalized text. Available across all language bindings: JavaScript, C#, Python, and Rust.

Load a streaming speech model from the catalog, create a session with audio settings (sample rate, channels, language), start it, push raw PCM audio chunks, and consume the async stream of results. The post has full Python and C# examples.

## Text Embeddings

Semantic search, RAG pipelines, clustering, similarity matching — these all require embeddings. Foundry Local 1.1 adds embedding model support so you can generate vectors locally from the same SDK, without sending data to a cloud endpoint.

For applications where data residency matters or where you're processing sensitive content, local embedding generation is a meaningful capability.

## Responses API

Foundry Local now supports the [Responses API](https://platform.openai.com/docs/api-reference/responses) — the structured interface designed for agentic interactions. This adds:

- **Tool calling** — let locally-running models invoke tools you define
- **Multimodal vision-language input** — pass image + text to vision-capable models
- Compatible with the standard API shape, so existing agents targeting OpenAI's Responses API work against local models

## Package Size Improvements

Two changes reduce the JavaScript package size:
- The `koffi` FFI layer has been replaced with a custom Node-API C addon
- WebGPU execution provider ships as a separate plugin, so applications that don't need GPU acceleration don't pay the size cost

The C# SDK now targets lower framework versions for broader .NET compatibility.

## Why This Matters

The three capabilities together — transcription, embeddings, tool calling — cover the core building blocks of many AI applications. Running them locally means:
- No internet required
- No per-token costs
- No data leaving the machine
- Consistent latency regardless of network conditions

Foundry Local is the right choice for edge scenarios, privacy-sensitive workloads, offline applications, or anything where you want to avoid cloud dependency during development.

Original post: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
