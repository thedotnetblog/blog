---
title: "PostgreSQL on Azure in VS Code Is Really About Tightening the Performance Loop"
date: 2026-06-29
author: "Emiliano Montesdeoca"
description: "The newer PostgreSQL-on-Azure experience in VS Code matters because it reduces the distance between metrics, tuning guidance, query analysis, and actual developer action. That is the real performance dividend."
tags:
  - PostgreSQL
  - Azure
  - VS Code
  - Performance
  - Databases
---

Database performance work gets expensive mostly because the feedback loop is fragmented.

Metrics are in one place. Query plans are in another. Tuning advice is somewhere else. The editor is detached from all of it.

That is why the updated **PostgreSQL on Azure experience in VS Code** is more interesting than it may first appear.

## The core value is loop compression

The strongest theme in the update is that diagnosis and action are getting pulled closer together:

- server metrics in the editor
- Azure Advisor recommendations in context
- better query plan visibility
- AI-assisted analysis

That makes performance work less fragmented, and that is usually where the real productivity gain comes from.

## My take

This is not only about PostgreSQL features.

It is about reducing the operational distance between seeing a problem and acting on it. That is the kind of tooling improvement that pays off over time.

Original post: [The performance dividend: Optimizing PostgreSQL on Azure directly in Visual Studio Code](https://azure.microsoft.com/en-us/blog/the-performance-dividend-optimizing-postgresql-on-azure-directly-in-visual-studio-code/)