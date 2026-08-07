---
title: "Cosmos DB Security for Day One: Start with Entra ID"
description: "A practical security checklist for a new Cosmos DB app: identity-based access, scoped RBAC, network restrictions, parameterized queries, logging, and backup."
date: 2026-09-14
author: "Emiliano Montesdeoca"
tags: [azure-cosmos-db, security, entra-id, identity-management, best-practices]
slug: cosmosdb-security-starter-guide
---

Original source: [I'm Starting a New Cosmos DB App. What Security Do I Actually Need?](https://devblogs.microsoft.com/cosmosdb/im-starting-a-new-cosmos-db-app-what-security-do-i-actually-need/)

## The Common Mistake

You create a Cosmos DB account. Azure gives you two keys and a connection string. They work immediately, so they often make it into development, staging, and production before anyone revisits the decision.

The problem is not that keys are complicated. They are bearer tokens. Anyone who has one can read, modify, or delete data, and shared keys do not give you reliable identity attribution. If one leaks into a log, screenshot, `.env` file, or pull request, rotation means updating every dependent system that may have copied it.

The source's recommendation is straightforward: start with Entra ID from day one, including development, and make identity-based access the normal application path.

## Control Plane and Data Plane

A secure Cosmos DB setup starts with two separate questions.

The control plane governs who can create or delete accounts, databases, and containers or change account settings. Azure RBAC manages that access. The data plane governs who can read, write, query, and delete documents. Cosmos DB RBAC manages the built-in data roles.

A typical application should have data-plane access only, with the smallest role and scope it needs. Developers need their own identity for local work. CI/CD needs the permissions required to deploy, which may differ from what the application needs at runtime. Avoid giving every system the same connection string or credential.

This distinction is easy to lose when an application is first created. Record it in infrastructure code and in the application's deployment documentation so a broad control-plane permission does not quietly become the default.

## The Minimum Viable Setup

### 1. Disable local authentication

Run:

```bash
az cosmosdb update --name <your-account> --resource-group <your-rg> --disable-local-auth true
```

Once disabled, keys no longer work and access requires an Entra ID identity. If you are not ready to disable keys, at minimum keep connection strings out of source control, use a secure store such as Key Vault, and enable secret scanning.

### 2. Give the app an identity

For App Service, Functions, Container Apps, AKS, or similar Azure compute, assign a system-assigned managed identity. For local development, use your developer identity through `az login` or another supported credential. `DefaultAzureCredential` lets the same SDK pattern work across those environments.

### 3. Assign a narrowly scoped data role

The source highlights the Cosmos DB Built-in Data Reader and Built-in Data Contributor roles. Scope the assignment to the account, database, or container according to the actual need rather than defaulting to the broadest scope.

### 4. Connect without keys

A .NET client can use the account endpoint with `DefaultAzureCredential`:

```csharp
using Azure.Identity;
using Microsoft.Azure.Cosmos;

var client = new CosmosClient(
    accountEndpoint: "https://<your-account>.documents.azure.com:443/",
    tokenCredential: new DefaultAzureCredential()
);
```

The same code can use a developer login locally, managed identity in Azure, and a service principal or federated identity in CI/CD. That removes secrets from application configuration, but it does not remove the need to scope and audit the identity.

### 5. Turn on diagnostic logging

Route diagnostic settings to Log Analytics before an incident. The source recommends categories such as `DataPlaneRequests`, `QueryRuntimeStatistics`, `PartitionKeyStatistics`, and `ControlPlaneRequests`. High-volume data-plane logs can be expensive, so choose retention and sampling deliberately.

### 6. Restrict network access

The default endpoint is publicly reachable. Start with an IP allowlist for known office and CI/CD egress addresses, then evaluate Private Endpoints and VNet integration as the environment matures.

### 7. Parameterize queries

Cosmos DB NoSQL accepts JSON, and the application is responsible for preventing malformed or injection-friendly query construction. Do not concatenate user input:

```csharp
var query = new QueryDefinition("SELECT * FROM c WHERE c.userId = @userId")
    .WithParameter("@userId", userInput);
```

Parameterization is necessary, but continue validating document shape, size, and authorization in the application.

### 8. Enable continuous backup

Continuous backup provides point-in-time restore options for mistakes and other data loss scenarios. Choose the 7- or 30-day tier according to recovery requirements, and enable it at account creation when possible.

## What Can Wait

The source deliberately separates day-one controls from later investments. Private Endpoints and VNet integration can follow an initial IP allowlist. Customer-managed keys may be required for compliance but add operational overhead. Microsoft Defender for Cosmos DB is strongly recommended once production data is present, but it does not replace identity, network, query, or backup basics.

The expensive decision to postpone is identity. Migrating from keys later touches deployments, environments, and SDK calls. Starting with `DefaultAzureCredential` avoids turning that migration into a breaking project.

## Recommendations for .NET Teams

1. Put identity and role assignments in infrastructure code.
2. Use separate developer, runtime, and deployment identities.
3. Scope Cosmos DB roles to the smallest useful resource.
4. Test logging, network restrictions, parameterization, and restore before production.
5. Keep connection strings and keys out of source control even during the transition.

A secure Cosmos DB default is not an enterprise ceremony. It is choosing an identity boundary before the first business feature makes the insecure path difficult to change.