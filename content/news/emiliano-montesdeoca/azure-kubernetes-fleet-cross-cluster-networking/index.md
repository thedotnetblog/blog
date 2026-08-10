---
title: "Azure Kubernetes Fleet Manager brings managed cross-cluster networking"
description: "Azure Kubernetes Fleet Manager enters public preview with Cilium-based cross-cluster networking, global service discovery, observability, and policy management across AKS clusters."
date: 2026-09-10
author: "Emiliano Montesdeoca"
tags: ["Azure", "Kubernetes", "AKS", "Containers", "Networking"]
slug: azure-kubernetes-fleet-cross-cluster-networking
---

Original source: [Powering multi-cluster workloads with seamless cross-cluster networking for Azure Kubernetes Fleet Manager](https://azure.microsoft.com/en-us/blog/powering-multi-cluster-workloads-with-seamless-cross-cluster-networking-for-azure-kubernetes-fleet-manager/)

Running one Kubernetes cluster is already an operational discipline. Running a fleet introduces a second problem: services and workloads need to move across cluster and region boundaries without turning every failover, shared service, or capacity decision into a custom networking project.

Microsoft has announced the **public preview of cross-cluster networking for Azure Kubernetes Fleet Manager**. The feature extends the Kubernetes networking model across clusters using Azure CNI powered by Cilium and Advanced Container Networking Services. The goal is direct communication between workloads in joined clusters while retaining cluster-level isolation and governance.

## The networking tax of a fleet

Organizations use multiple Azure Kubernetes Service clusters for regulatory boundaries, regional disaster recovery, blast-domain isolation, or workload placement. Traditional approaches often require VPNs, gateways, and manually maintained service discovery. That plumbing adds latency and gives platform teams another set of moving parts to operate whenever a cluster changes.

Fleet Manager already handles workload propagation and staged update orchestration. Cross-cluster networking addresses the remaining gap: making the network between member clusters a managed part of the fleet rather than a collection of per-cluster exceptions.

The implementation uses **Cilium** for the dataplane and **Kubefleet** for fleet-level orchestration. Both are active CNCF projects, so the capability builds on an open-source foundation while Microsoft manages the lifecycle pieces around it.

## What the preview provides

The source highlights several capabilities:

- **East-west connectivity:** eBPF-based routing allows pods to communicate across clusters without additional proxies or gateways.
- **Global service discovery:** annotate a Kubernetes Service with `service.cilium.io/global=true` to make it global across joined member clusters, enabling endpoint discovery, load balancing, and failover.
- **Multi-cluster observability:** aggregated metrics, logs, and flow visibility provide a unified view of network health.
- **Unified security and governance:** network policies and identity-based security can follow workloads across cluster boundaries.
- **Managed lifecycle:** Fleet Manager handles certificates and network configuration instead of requiring teams to maintain the multi-cluster components manually.

The result is not merely a new route between clusters. It is a platform capability for exposing selected services across a fleet while keeping the platform team responsible for the network model and its operational boundaries.

## Resilience without hiding the boundaries

Cross-cluster networking is useful for shared-services clusters and global services that route traffic toward healthy endpoints. It can support architectures designed to tolerate a single-cluster or single-region failure, but the feature does not make failure planning disappear.

Applications still need clear ownership of state, retries, timeouts, data replication, and regional dependencies. A global Service can expose endpoints across member clusters; it does not decide whether a stateful .NET service is safe to fail over or whether a request should be retried after a regional network event. Platform networking and application resilience remain related but separate design concerns.

That separation is helpful for .NET teams. Use the fleet network to simplify service reachability, then test the application behavior under endpoint loss, delayed responses, and a changed cluster location. The managed network lowers infrastructure work; it does not replace distributed-systems testing.

## Prerequisites and setup

The preview requires:

1. **Azure CNI powered by Cilium** as the networking dataplane.
2. **Advanced Container Networking Services** enabled for the clusters.
3. **Fleet membership** for the clusters that should communicate.
4. **A cross-cluster network profile** associated with those members.
5. **Global Service annotations** for services that should be discoverable across clusters.

Once configured, Fleet Manager deploys and manages the required components. The source describes direct pod-to-pod communication across clusters without additional gateways or overlays, reducing the amount of Cilium multi-cluster infrastructure that teams must assemble themselves.

## A practical evaluation path

1. Pick a non-critical service that is representative of the organization’s normal AKS deployment.
2. Join a small set of clusters to a Fleet and document the existing service-discovery assumptions.
3. Enable the network profile and expose one carefully selected Service globally.
4. Measure connectivity, failover, policy enforcement, and observability before adding more workloads.
5. Test the .NET application when an endpoint or member cluster disappears, not only when every cluster is healthy.

Cross-cluster networking for Azure Kubernetes Fleet Manager is a meaningful step toward making a Kubernetes fleet feel like one governed platform. The useful promise is operational simplicity: direct connectivity, global discovery, and managed lifecycle without asking every application team to become a specialist in multi-cluster network plumbing.---
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