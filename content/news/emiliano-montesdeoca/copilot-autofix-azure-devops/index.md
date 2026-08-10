---
title: "Copilot Autofix for GitHub Advanced Security for Azure DevOps"
description: "Copilot Autofix enters limited private preview for GitHub Advanced Security for Azure DevOps, generating AI-assisted fixes for supported CodeQL alerts in the Azure DevOps alert experience."
date: 2026-10-30
author: "Emiliano Montesdeoca"
tags: ["Azure DevOps", "Security", "GitHub Advanced Security", "CodeQL", "AI"]
slug: copilot-autofix-azure-devops
---

Original source: [Copilot Autofix for GitHub Advanced Security for Azure DevOps](https://devblogs.microsoft.com/devops/copilot-autofix-for-github-advanced-security-for-azure-devops/)

Finding a vulnerability is only the beginning of remediation. CodeQL can identify a SQL injection, path traversal issue, or hardcoded credential, but a security alert still needs a developer to understand the context, write a change, and send it through review. Copilot Autofix brings an AI-suggested fix into that same workflow for teams using GitHub Advanced Security for Azure DevOps.

The feature is available in **limited private preview**. Enrollment is processed in waves, and Microsoft says it may take a few weeks for the functionality to be enabled for an organization. That preview boundary matters: the feature is worth evaluating, but its output still belongs inside normal engineering and security review.

## From alert to pull request

When a developer opens a supported CodeQL alert in the repository’s **Advanced Security** tab, a **Generate fix** button is available. Autofix gathers the surrounding code and alert context, then returns an AI-suggested change as a pull request.

The developer can review the suggestion, refine it when necessary, and merge it through the existing process. Normal review and build gates run on the pull request. After the pull request merges and the next CodeQL scan completes, the alert resolves automatically.

That keeps the remediation path familiar. The new step is not an automatic production change; it is a way to move from an alert to a change under review without leaving the security experience to research the issue and create the first patch manually.

Autofix also works alongside CodeQL default setup. Default setup enables scanning without pipeline configuration, while Autofix turns supported resulting alerts into pull requests. Teams using explicit CodeQL tasks in their Azure Pipelines can use that route as well.

## What the preview covers

The limited private preview includes:

- **All CodeQL-supported languages**, including C/C++, C#, Go, Java, Kotlin, JavaScript, TypeScript, Python, Ruby, and Swift.
- **A curated set of CodeQL queries**, using the same set GitHub uses on GitHub.com and covering high-frequency vulnerability classes such as SQL injection, cross-site scripting, path traversal, and hardcoded credentials.
- **Backlog alerts** in the Advanced Security tab for the default branch.

The boundaries are as important as the language list. A rule outside the curated set or an alert on a non-default branch may not offer a generated fix during this preview. Microsoft says the next steps include bringing Autofix to all CodeQL alerts across all branches, followed by all code-scanning alerts.

## Billing is part of the rollout decision

Copilot Autofix is included with a GitHub Advanced Security for Azure DevOps license, but each fix generation consumes AI credits from the organization’s Azure billing meter. The credit represents the tokens used by the generation:

- **Input tokens** for the code context sent to the model
- **Output tokens** for the suggested change
- **Cached tokens** that reuse existing context

One GitHub AI credit equals $0.01 USD. The charge is billed to the Azure subscription linked to the Azure DevOps organization and appears as a separate meter in Azure Cost Management. The cost of an individual fix varies with the amount of surrounding code and the complexity of the change.

That makes a controlled pilot the sensible starting point. Enable Autofix on one or two repositories, watch daily usage, and review both the quality of suggestions and the cost before expanding the feature. In the Azure portal, the source points to **Subscription** > **Cost Management** > **Cost analysis** for monitoring charges.

## A responsible evaluation path

1. **Request preview enrollment.** Use the preview sign-up and wait for organization enablement.
2. **Confirm CodeQL scanning.** Configure CodeQL through default setup or the appropriate pipeline tasks.
3. **Enable the feature at repository level.** Keep the first rollout limited to a repository where the team can review suggestions closely.
4. **Generate a fix for a supported alert.** Open the alert in Advanced Security and select **Generate fix**.
5. **Review the pull request.** Check the security behavior, tests, and surrounding code before merging.
6. **Monitor usage and outcomes.** Track AI credits, review time, and whether the next CodeQL scan resolves the alert as expected.

Autofix shortens the distance between detection and a change in review, but it does not remove the need for security understanding. The useful result is not a button that bypasses judgment; it is a pull request that gives developers a stronger starting point while preserving the controls their repositories already use.