---
title: "Removing the Monkey Work of Migration with Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape walks through migrating a real AWS Terraform deployment to Azure Bicep — extracting deployment intent and remapping architecture rather than doing a 1:1 syntax conversion."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — a walkthrough of Git-Ape (git agentic platform engineering tool) migrating a real AWS Terraform repo to Azure, focusing on intent extraction rather than line-by-line conversion.

## The input: contoso-migration

The source is a real Terraform project (`contoso-migration`) that deploys a Next.js app on AWS — EC2 for compute, ALB for load balancing, S3 for artifacts, and IAM keys for identity. Cost: ~$34/month. The goal isn't to reproduce the same infrastructure on Azure; it's to figure out what the deployment is actually trying to do and rebuild that on Azure-native services.

## Step 1: Validation and auth

Git-Ape starts by validating all required CLI tools — `az`, `aws`, `gh`, `jq`, `git` — and confirming active auth sessions before touching anything. No partial runs.

## Step 2: Intent extraction

The agent reads the entire source repo through the GitHub API and extracts the deployment intent: runtime (Node.js), compute type, ingress pattern, artifact handling, identity model, networking, and monitoring. This is the key step — it's building a semantic model of what the deployment does, not what Terraform keywords it uses.

## Step 3: Service mapping

AWS services get mapped to Azure equivalents:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → App Service built-in load balancing
- IAM roles/keys → Managed Identity
- Terraform → Bicep + GitHub Actions

## Step 4: Critique agent

Before generating output, a critique agent runs and catches two blocking issues:

1. **Build-on-startup anti-pattern** — the original Terraform was running `npm install && npm run build` on EC2 at startup. Fix: build in CI, deploy a ready artifact.
2. **Unnecessary Blob Storage** — S3 was used for artifact staging that could be eliminated with proper CI/CD. The critique agent dropped it entirely.

## Step 5: Generated output

The result is ~80 lines of Bicep instead of the original 200+ lines of Terraform. The agent created a new GitHub repo with `infra/main.bicep` and `.github/workflows/deploy.yml` and removed all AWS-specific files.

## Security posture comparison

The migration also produced a meaningful security upgrade:

| AWS original | Azure output |
|---|---|
| HTTP only | HTTPS only, TLS 1.2 |
| SSH open to 0.0.0.0/0 | No SSH exposure |
| IAM access keys | OIDC + Managed Identity |
| No monitoring | Application Insights |

Cost: ~$13/month vs the original $34/month.

## What makes this different from a syntax converter

The critique agent step is what separates this from a mechanical translation. It caught patterns that would have worked on AWS but would be wrong on Azure — and fixed them instead of replicating them. The output isn't "AWS in Azure syntax"; it's an Azure-native deployment that achieves the same goal more cleanly.

See the [full walkthrough](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) for the complete agent trace and generated files.
