---
title: "Cross-Cluster Networking for Kubernetes Fleet Manager: Seamless Multi-Region Workloads"
description: "Fleet Manager's Cilium-based cross-cluster networking extends Kubernetes connectivity across AKS clusters while preserving cluster-level isolation and governance."
date: 2026-09-10
author: "Emiliano Montesdeoca"
tags: [azure-kubernetes-service, fleet-manager, networking, cilium, multi-region]
slug: azure-kubernetes-fleet-cross-cluster-networking
---

Original source: [Powering multi-cluster workloads with seamless cross‑cluster networking for Azure Kubernetes Fleet Manager](https://azure.microsoft.com/en-us/blog/powering-multi-cluster-workloads-with-seamless-cross-cluster-networking-for-azure-kubernetes-fleet-manager/)

## The Old Tax on Multi-Cluster Deployments

Many Azure Kubernetes deployments run multiple clusters for regional recovery, regulatory boundaries, or blast-domain isolation. The hard part has been making those clusters cooperate without adding a second networking system that developers must understand.

The traditional approach often involves VPNs, gateways, manual service discovery, and extra latency. It can work, but every additional component becomes part of the incident surface. Platform teams also want to change cluster placement without forcing application teams to rewrite how services find one another.

Azure Kubernetes Fleet Manager's cross-cluster networking is now in public preview. It adds transparent east-west connectivity powered by Advanced Container Networking Services and Cilium, extending the Kubernetes networking model across clusters while preserving cluster-level isolation and governance.

## What the Preview Provides

The feature uses eBPF-based routing with Azure CNI powered by Cilium. Pods in joined clusters can communicate across cluster boundaries without application-level proxies or gateways. The source also highlights Kubefleet for fleet-level orchestration, keeping the capability aligned with open-source Kubernetes components.

Global service discovery is the most immediately visible application benefit. Add the `service.cilium.io/global=true` annotation to a Kubernetes Service and it becomes available across joined member clusters. Cross-cluster networking discovers the endpoints and provides transparent load balancing and failover.

The other pieces matter during operations. Aggregated metrics, logs, and flow visibility provide a unified view of network health. Network policies can be enforced across the fleet rather than stopping at a cluster boundary. Fleet Manager manages certificates and network configuration, reducing the amount of Cilium multi-cluster lifecycle work the platform team must own.

These capabilities are attractive, but public preview is an important qualifier. Test the control-plane behavior, failure modes, observability, and support path in your target regions before making it the only route for a critical workload.

## The Setup Shape

The prerequisites in the source are straightforward:

- Azure CNI powered by Cilium as the networking dataplane.
- Advanced Container Networking Services enabled.

The setup then follows three steps:

1. Join the AKS clusters to a Fleet.
2. Associate the member clusters with a cross-cluster network profile.
3. Deploy services with global annotations where cross-cluster communication is intended.

Once configured, Fleet Manager deploys and manages the required components. Direct pod-to-pod communication is available without manually assembling gateways or overlays.

That simplicity is the point of the managed approach, but it should not hide the new dependency. The application may be unaware of the network path while the platform team remains responsible for region placement, policies, DNS behavior, and recovery testing.

## Implications for .NET Architecture

The best application-level benefit is fewer infrastructure-specific workarounds. A .NET service can continue using normal Kubernetes service discovery instead of embedding custom cross-cluster DNS or application-level load balancing. For a global service, healthy endpoints can be selected across joined clusters.

That does not eliminate resilience work in the application. Timeouts, retries, idempotency, and circuit breaking still matter when a cluster or region becomes unavailable. Cross-cluster failover changes the available path; it does not make a failed downstream call harmless. Test how the .NET client behaves when endpoints disappear, latency changes, or a request is retried after a partial operation.

Shared-services architectures are a natural candidate: an authentication, logging, or platform service can be exposed to application clusters while policy remains centrally governed. Regional replicas can also serve local traffic while a second cluster provides capacity or recovery options.

Keep stateful services separate from the networking decision. Cross-cluster connectivity does not turn a database into a globally consistent database, and it does not remove the need to design data replication and ownership explicitly.

## Operability and Governance

The source emphasizes unified observability and identity-based security, which are valuable only when teams define what they expect to see. Before onboarding a workload, record the normal flow, the allowed namespaces or identities, and the behavior expected during a cluster outage.

Use a non-critical service to test global annotations first. Verify that DNS, endpoint selection, network policy, telemetry, and rollback all behave as expected. Then exercise a regional failure rather than assuming that the presence of a second endpoint equals disaster recovery.

For platform teams, document the boundary between Fleet Manager automation and application responsibility. Developers should know whether a service is global, where it may run, and which latency or availability assumptions are safe.

## Recommendations for AKS and .NET Teams

1. Treat the public preview as a controlled pilot with explicit rollback.
2. Start with a stateless, read-heavy service and test global discovery.
3. Validate .NET timeout, retry, and idempotency behavior during endpoint loss.
4. Confirm network policies and flow visibility across every member cluster.
5. Keep data replication and state ownership as separate architecture decisions.

Cross-cluster networking removes a large amount of infrastructure glue, but it does not remove the need for clear boundaries. The win is a simpler platform primitive that lets application teams think in services while platform teams manage the fleet.