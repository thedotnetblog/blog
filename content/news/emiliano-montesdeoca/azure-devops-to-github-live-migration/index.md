---
title: "Enterprise Live Migrations: Moving from Azure DevOps Repo to GitHub with minimal disruption"
description: "Microsoft introduces Enterprise Live Migrations in limited public preview, helping teams move Azure DevOps repositories to GitHub with continuous synchronization and a short cutover window."
date: 2026-10-20
author: "Emiliano Montesdeoca"
tags: ["Azure DevOps", "GitHub", "DevOps", "Repository Migration", "Cloud Strategy"]
slug: azure-devops-to-github-live-migration
---

Original source: [Enterprise Live Migrations: Moving from Azure DevOps Repo to GitHub with minimal disruption](https://devblogs.microsoft.com/devops/enterprise-live-migrations/)

For many enterprise teams, repository migration is not difficult because Git is mysterious. It is difficult because the repository is active, connected to automation, and expected to remain available while the business keeps moving. A migration approach that requires an extended freeze, sometimes lasting days, is hard to reconcile with critical workloads and continuous delivery.

Microsoft is addressing that constraint with **Enterprise Live Migrations (ELM)**, now available in limited public preview. The important idea is simple: begin the migration without locking the Azure DevOps repository, keep changes synchronized to GitHub while development continues, and schedule a short cutover when the team is ready.

## A migration in three stages

ELM follows a staged workflow:

1. **Start and validate.** Confirm that the repository is ready for migration.
2. **Continuous sync.** Keep GitHub up to date while developers continue working in Azure DevOps.
3. **Cutover.** Perform a final synchronization and transition GitHub to the system of record.

During most of the process, Azure DevOps remains fully writable. Developers do not have to stop work simply because the migration has started. When the team is ready to complete the transition, the cutover window is typically under 30 minutes.

That changes the operational shape of the project. Instead of treating migration as one large event that must be perfectly coordinated, a team can validate the path, let synchronization run, and choose a cutover window that fits its release calendar. The shorter outage does not eliminate planning, but it makes the planning much easier to contain.

## What is included in the preview

The current preview supports migrations to **GitHub Enterprise Cloud with data residency**. Microsoft describes a script-based migration experience as available today, with a UI-based experience coming soon. The feature is expected to remain in limited public preview over the next couple of months while the team refines the experience, adds features, and incorporates customer feedback.

Organizations interested in participating can [sign up for the preview](https://nam.dcv.ms/VeDNq3VRhX). The detailed migration guidance is available through the [Enterprise Live Migrations documentation](https://aka.ms/adoELM).

The preview status matters. A limited preview is the right time to learn the workflow with a controlled repository, not to assume that every repository in an estate will behave identically. The script-based experience also means that teams should understand the steps and prerequisites before planning a broad rollout.

## The repository is only one part of the move

ELM directly addresses the version-control transition: keeping repository contents synchronized and changing which platform is the system of record. A real platform migration still needs a separate inventory of the systems around that repository.

Before a cutover, document the Azure DevOps permissions, branch policies, service hooks, build and release integrations, secrets, and repository-specific conventions that must be recreated or redesigned in GitHub. The short cutover window reduces the time developers are interrupted; it does not automatically migrate every surrounding process.

This distinction is useful for .NET teams. A repository may contain the solution and its history, while the build depends on package feeds, signing, deployment identities, environment variables, and pipeline definitions stored elsewhere. Treat ELM as a way to reduce repository cutover risk, then give the adjacent automation its own migration checklist.

## A practical pilot for .NET teams

1. **Choose a representative repository.** Start with a non-critical service that still exercises the organization’s normal branch policies and CI workflow.
2. **Record the current state.** Capture permissions, integrations, hooks, package sources, and build assumptions before synchronization begins.
3. **Run the staged workflow.** Validate readiness, observe continuous synchronization, and measure the time and checks needed for final cutover.
4. **Schedule a focused window.** Even with a typical window under 30 minutes, choose a low-activity period and make the ownership of the final decision explicit.
5. **Verify the system of record.** Confirm that developers, automation, and release processes all point to the intended GitHub repository after the final sync.

Enterprise Live Migrations does not make migration invisible, but it makes the most disruptive part more manageable. For organizations moving from Azure Repos to GitHub Enterprise Cloud with data residency, continuous synchronization and a short cutover provide a practical way to modernize without pausing active development for days.