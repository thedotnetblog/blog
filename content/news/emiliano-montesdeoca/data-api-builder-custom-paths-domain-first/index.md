---
title: 'Data API Builder Custom Paths Let You Design APIs for Humans, Not Tables'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Compound REST paths in DAB are a small feature with big architectural impact for domain-oriented API design.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Original source: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

The new compound REST path support in Data API Builder might look like a minor configuration improvement, but it actually solves a long-standing API design tension: database topology leaking into public endpoint design.

Default entity-based routes are great for quick starts. They are often wrong for long-term product APIs. Real systems need route structures that match business concepts, ownership boundaries, and consumer mental models.

That is why this DAB change matters. You can keep generated API convenience while presenting a cleaner domain-first surface.

My opinionated take is simple: if your API path structure mirrors raw table names in production, you are usually optimizing for backend convenience at the expense of client clarity.

With custom paths, teams can model better boundaries, such as sales, billing, support, or partner-specific surfaces. This does not replace proper API governance, but it gives DAB users a practical way to align route design with product language.

Practical guidance for teams adopting this feature:

Define a naming policy before adding paths ad hoc. Inconsistent subsegments become long-term clutter.

Map endpoints to bounded contexts, not organizational charts. Teams change; domain semantics should be stable.

Treat path structure as part of your versioning strategy and document breaking changes explicitly.

Validate authorization behavior along custom route structures so route clarity is paired with security clarity.

What I appreciate in DAB generally is the leverage model: you get pagination, filtering, projection, and other endpoint mechanics without writing repetitive controller code. Custom paths make that leverage more production-ready by reducing one of the biggest objections from API architects.

There is one caveat. Better path composition can tempt teams to expose too much too quickly because generation feels easy. Guardrails still matter: keep entity exposure deliberate, apply policy centrally, and avoid building accidental public contracts from internal schema experiments.

For .NET organizations under delivery pressure, this feature is a productivity unlock if used with discipline. You can move faster than handcrafted API layers while still preserving a coherent and business-friendly endpoint surface.

Bottom line: DAB custom paths are not about prettifying URLs. They are about reclaiming API design intent while keeping the operational efficiency of generated endpoints.
