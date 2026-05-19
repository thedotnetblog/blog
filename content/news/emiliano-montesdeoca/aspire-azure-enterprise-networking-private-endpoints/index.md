---
title: "Private Endpoints, VNets, NSGs — Aspire Handles the Networking Now"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Aspire's new Azure enterprise networking support lets you model VNets, private endpoints, NAT gateways, NSGs, and Network Security Perimeters directly in your AppHost — no infrastructure drift required."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Here's a scenario I've seen too many times. The app is done. The demo is great. Then the security checklist shows up: take storage off the public internet, run inside a VNet, provide outbound IPs for the partner allowlist, prove that only the right subnets talk to the right services.

At that point the application model and the infrastructure model start drifting apart in ways that are painful to maintain.

Aspire's new Azure enterprise networking support addresses this directly. You describe the network shape next to the resources that use it, in your AppHost.

## The Building Blocks

Here's what each Azure networking concept is for, distilled:

| Feature | Use it when | Why it matters |
|---------|------------|----------------|
| Virtual network | You need a private address space | The network boundary for subnets, private endpoints, and routing |
| Subnet | You need to separate workloads inside the VNet | Each part of the system gets its own address range and policy surface |
| Delegated subnet | A platform service (like ACA) needs to manage a subnet | Lets the service place managed infrastructure in your VNet safely |
| NAT gateway | You need predictable outbound public IPs | Stable address for allowlists and auditing |
| Private endpoint | You want a PaaS resource reachable privately | Puts a private IP for that service inside your VNet, removes public exposure |
| NSG | You need subnet-level traffic rules | Explicit allow/deny for inbound and outbound traffic per subnet |

## Describing It in Your AppHost

The key shift here is that you're modeling the network *alongside* the resources that use it, not in a separate Bicep file that drifts away from the app model over time.

From the AppHost, you can:

- Create VNets and subnets with `AddVirtualNetwork()` and `AddSubnet()`
- Attach a NAT gateway to subnets for stable outbound IPs
- Create private endpoints for storage, Key Vault, SQL, and other PaaS services
- Define NSGs with inbound and outbound security rules
- Configure Network Security Perimeters for cross-resource policies

The result is that when you run `azd up`, the infrastructure matches what the app model says it needs. Not what a manually maintained template says.

## Why This Matters for Real Applications

A few things that become significantly easier once the network is modeled in Aspire:

**Private endpoints for Key Vault and storage** — you describe `WithPrivateEndpoint()` on those resources, and Aspire handles the DNS zone configuration and endpoint attachment. The app never changes.

**Consistent outbound IPs** — add a NAT gateway to the relevant subnet and every outbound request from your app goes through a known, stable IP. Partners can allowlist it. Auditors can trace it.

**NSG rules from code** — instead of clicking through the portal or maintaining a Bicep snippet, your security rules live in the AppHost alongside the resources they protect.

This is the kind of integration that doesn't make demos exciting but makes production systems maintainable.

## Wrapping Up

Network security showing up late in the project lifecycle is a solved problem if you model it alongside the app from the start. Aspire's enterprise networking support makes that possible without requiring a separate infrastructure track.

Full details in the original post: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
