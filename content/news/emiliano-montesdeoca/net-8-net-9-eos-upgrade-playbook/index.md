---
title: '.NET 8 and .NET 9 End of Support: Treat This as a Delivery Deadline'
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: 'November 10, 2026 is not just a support date; it is the point where postponed upgrade risk becomes explicit.'
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Original source: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

This announcement is straightforward, and teams should respond with equal clarity: if you plan to keep shipping on .NET 8 or .NET 9 past November 10, 2026, you are making an intentional unsupported-runtime decision.

Applications will keep running. That is not the point. The point is that security and servicing updates stop. Once that happens, every known vulnerability without a backport path becomes your operational liability.

My opinionated take: **organizations often treat framework upgrades as optional maintenance** and then pay for that decision in emergency windows, audit findings, and rushed vendor escalations. Upgrade planning should be a product roadmap item, not a side quest.

A practical migration stance for .NET teams:

- **Set .NET 10 retargeting as a dated objective**, not an open-ended backlog item.
- **Run compatibility and regression testing** in parallel with feature work now, not in Q4.
- **Track dependency and hosting readiness** as separate workstreams, because many failures happen outside the project file.
- **Use Upgrade Assistant and breaking-change documentation** early to front-load surprises.

If you own shared libraries used by multiple products, publish your .NET 10 support timeline publicly inside your org. Downstream teams need lead time.

Visual Studio’s out-of-support component marking also matters operationally. It creates a clear signal that toolchain cleanup is part of staying compliant. Teams that ignore this usually drift into mixed SDK states and inconsistent build behavior.

One under-discussed detail is that .NET 8 and .NET 9 converge on the same end date. This compresses upgrade windows for organizations that staggered adoption expecting more cushion. If you moved to .NET 9 for feature access, you still land on the same support cliff.

For platform leads, the decision matrix is simple: **migrate before deadline, or document and accept unsupported risk** with compensating controls. There is no third option where nothing changes.

The good news is that .NET 10 is an LTS target through November 2028, which buys stable runway once you complete the move.

Do not wait for the final Patch Tuesday to start. Treat this as a delivery deadline with security implications, because that is exactly what it is.
