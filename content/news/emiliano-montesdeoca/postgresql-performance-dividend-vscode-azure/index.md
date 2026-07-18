---
title: 'PostgreSQL Performance Work Should Happen Where You Code'
date: 2026-07-20
author: 'Emiliano Montesdeoca'
description: 'The best PostgreSQL tuning workflow is not more dashboards, but tighter feedback loops inside the editor.'
tags:
  - postgresql
  - azure
  - visual-studio-code
  - database-performance
  - devops
---

Original source: [The performance dividend: Optimizing PostgreSQL on Azure directly in Visual Studio Code](https://azure.microsoft.com/en-us/blog/the-performance-dividend-optimizing-postgresql-on-azure-directly-in-visual-studio-code/)

I agree with the core thesis of this Azure update: performance work fails less from missing tools and more from fractured context. Most teams already have monitoring, query editors, and ops dashboards. What they lack is continuity from signal to action.

The PostgreSQL extension direction in VS Code matters because it shortens that path. When server metrics, query plans, and advisor recommendations appear in the same place developers already edit SQL, teams move from diagnosis to fix faster. That sounds obvious, but in real organizations it is a structural shift. Context switches are where ownership gets dropped.

Here is the practical part for engineering leads. If you want measurable gains, do not introduce these capabilities as optional nice-to-haves. Make them part of your review workflow:

- **Require a query plan screenshot or summary** for every non-trivial query change.
- **Track top advisor recommendations weekly** and assign owners, not just alerts.
- **Treat schema-aware IntelliSense and search_path correctness** as prevention tooling, not convenience.

The article also positions Azure HorizonDB as forward-looking while keeping Azure Database for PostgreSQL as today’s production default. That is exactly the right framing. Teams get in trouble when they turn preview-era technology excitement into operational commitments too early. Stability first, then selective experimentation.

My strong take: **performance culture is an editor problem before it is a cloud problem**. If tuning only happens in firefights and war rooms, you are not doing performance engineering, you are doing performance incident response. The VS Code integration story helps teams shift left, where cheaper fixes live.

There is one caveat. Integrated recommendations can create overconfidence if teams stop validating assumptions against workload behavior. AI-assisted tuning and advisor hints are accelerators, not substitutes for benchmark discipline. You still need baselines, repeatable load tests, and regression gates.

If your organization runs PostgreSQL on Azure at scale, the right move now is to standardize this integrated workflow, then instrument cycle time from issue detection to mitigation. The performance dividend is real, but only if you operationalize it. Otherwise, it is just another feature demo.

**Bottom line:** do not buy more observability. **Collapse the distance between insight and change.**
