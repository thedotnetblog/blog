---
title: "Azure Cobalt 200: Purpose-Built Arm Compute for Agentic Workloads"
description: "Azure Cobalt 200 Arm-based VMs enter early access preview with up to 50% generational CPU performance gains, stronger storage and networking, and broader .NET-ready options."
date: 2026-09-26
author: "Emiliano Montesdeoca"
tags: [azure-cobalt, compute, virtual-machines, ai-infrastructure, dotnet, performance]
slug: azure-cobalt-200-agentic-ai-vms
---

Original source: [New Azure Cobalt 200 VMs deliver 50% performance improvement, fully optimized for modern agentic AI workloads](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/)

The infrastructure behind agentic applications is not only the model. It includes API tiers, context aggregation, caches, databases, data pipelines, and the services that coordinate many sequential decisions. Azure's Cobalt 200 announcement targets that cloud-native layer with Arm-based virtual machines designed for scale-out and Linux-based agentic AI workloads.

Cobalt 200 is in early access preview and promises up to 50% better generational performance over Cobalt 100. That headline is useful, but the real evaluation question for a .NET team is whether the performance, compatibility, availability, and price fit its own service boundary.

## What Cobalt 200 Changes

Cobalt 200 is built around Arm Neoverse V3 Compute Subsystems and a 3nm process. The VMs include a larger cache hierarchy with 3 MB of L2 cache per core and 192 MB of system-level L3 cache. Each core is a full physical core with dedicated cache, which the announcement connects to sustained performance and isolation for agentic workloads.

The generational improvements include up to 50% better CPU performance, 20% higher remote-storage IOPS with NVMe, 10% better remote-storage throughput with NVMe, and 15% higher network bandwidth. Results vary by workload, so these numbers should be treated as a reason to benchmark, not as a universal application multiplier.

The cloud workload figures are also broad: up to 135% better database performance, up to 40% better web serving, up to 45% better communication encryption, and up to 80% better caching compared with Cobalt 100. Those categories map well to the supporting services around agents, but a real .NET service may be limited by database latency, external APIs, serialization, or model calls instead of CPU.

## VM Families and Storage Choices

Cobalt 200 scales to 128 vCPUs and expands the portfolio beyond general-purpose and memory-optimized families. High-Memory Optimized Mpsv4/Mpdsv4 VMs reach 84 vCPUs with a 16:1 memory-to-vCPU ratio. Storage Optimized Lpsv5 VMs add local NVMe and support storage-heavy or data-preparation workloads.

All series provide up to 85 Gbps of network bandwidth and 70 Gbps of remote-storage throughput, except Mpsv4/Mpdsv4, which provide up to 70 Gbps of network bandwidth and 46 Gbps of remote-storage throughput. Lpsv5 includes local NVMe across its sizes, while other series offer choices around local disks and remote disk types.

This gives platform teams more room to match a workload to its bottleneck. A .NET API tier may prefer a general-purpose family. An in-memory cache or large relational database may need memory optimization. A preprocessing or indexing stage may benefit from local storage. Keep those choices in infrastructure code so a VM-family experiment remains reversible.

Azure Boost integration improves remote storage IOPS and throughput with NVMe and increases network bandwidth. The exact benefit still depends on the workload and storage path. Measure it with realistic request sizes, concurrency, and failure behavior rather than a synthetic CPU loop.

## Arm Compatibility for .NET

The announcement says Cobalt 200 is fully compatible with workloads running on Cobalt 100 and highlights native Arm versions of C++, .NET, Java, Python, and Rust. GitHub Actions supports Arm through hosted and self-hosted runners, AKS supports Arm agent nodes and mixed x86/Arm clusters, and Arm-native container images are increasingly available.

For a modern .NET application, the runtime and container may already be in good shape. That does not guarantee that every native dependency, diagnostic agent, base image, or third-party library is ready. Test the complete image, including monitoring and build tooling, on Arm. Pay attention to packages with native assets, platform-specific scripts, and any workload that invokes external binaries.

A mixed AKS cluster can provide a gradual path, but scheduling, image manifests, architecture labels, and node-pool policies must be explicit. Do not let a deployment silently land on an architecture your image was not tested against.

## Preview and Availability Boundaries

Cobalt 200 is available in early access preview in West US3, East US2, Central US, Sweden Central, East US, West US2, Spain Central, and Indonesia Central, with more regions planned. Pricing and production availability need to be confirmed for the target region.

The source also describes Microsoft services and partners evaluating the platform, including Dataverse, Azure SQL Database, Teradata, Elastic, Arm, and Canonical. That is useful ecosystem evidence, but it does not replace a benchmark for your service or establish an SLA for a preview VM family.

## Recommendations for .NET Teams

1. Request early access only for a workload with a measurable CPU, cache, storage, or network bottleneck.
2. Build and run the full .NET container, including native dependencies and observability agents, on Arm.
3. Compare Cobalt 100 and Cobalt 200 with production-shaped traffic and concurrency.
4. Use mixed AKS node pools or staged VM deployment to keep rollback available.
5. Keep infrastructure definitions generic enough to target x86 when a dependency or region requires it.

Cobalt 200 is interesting because it treats the agent platform as a systems problem. The right adoption path is not to chase a 50% headline; it is to find the part of your .NET service that is actually constrained and prove that the new hardware changes that constraint.