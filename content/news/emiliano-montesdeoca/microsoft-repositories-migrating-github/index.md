---
title: "What Microsoft's GitHub Migration Says About AI-Native .NET Teams"
description: "Microsoft's CAP organization moved more than 1,600 repositories and 3,100 developers to GitHub while retaining Azure Boards and Azure Pipelines, offering a practical hybrid migration pattern."
date: 2026-10-08
author: "Emiliano Montesdeoca"
tags: [devops, github, azure-devops, migration, dotnet]
slug: microsoft-repositories-migrating-github
---

Original source: [How Microsoft is migrating repositories to GitHub](https://devblogs.microsoft.com/devops/how-microsoft-is-migrating-repositories-to-github/)

A repository host used to be mostly a version-control decision. Microsoft is making the case that it is now also an AI product decision. The source puts it plainly: "repository location is becoming a strategic decision" for organizations trying to capture the value of AI-native development.

That argument is more useful when it comes with an operational example. At Build 2026, Microsoft described how the Copilot, Agents, and Platforms organization migrated more than 1,600 repositories and 3,100 developers to GitHub while continuing to use Azure Boards and Azure Pipelines where those workflows remain important. For .NET teams, the interesting lesson is not that every repository should move immediately. It is that a migration can separate where code lives from the planning and CI/CD tools a team already knows.

## The scale is large, but the approach is incremental

CAP operates roughly 4,000 active repositories across 53 Azure DevOps organizations. With two dedicated engineering leads and a small supporting group, the organization migrated more than 80% of its in-scope repositories and 45% of its developers to GitHub. The migration included large repositories supporting services such as Dynamics CRM and omnichannel CRM, while some of the most complex repositories remain on Azure DevOps.

That detail matters because it removes the usual false choice between a big-bang migration and doing nothing. The teams moved a substantial portfolio while leaving a path for harder cases. The source expects tools such as Enterprise Live Migrator to help with more complex monorepos, but the immediate playbook is still sequencing: move what can move cleanly, learn from it, and keep development moving in the harder repositories.

For an organization with a large .NET portfolio, I would make the first wave intentionally boring. Choose independent repositories with clear build boundaries, a manageable contributor group, and a test suite that can prove the migrated workflow behaves like the old one. The goal of the pilot is not a dramatic platform victory. It is evidence about pull requests, branch policies, build permissions, release connections, and developer friction.

## Why GitHub is part of the AI decision

CAP's stated driver is earlier access to GitHub capabilities such as Copilot Coding Agent, Code Review, Copilot Chat, and other agentic workflows. Engineers can use those experiences across VS Code, Visual Studio, the GitHub Copilot CLI, GitHub Mobile, and the GitHub app.

The source gives a concrete example beyond chat assistance. CAP engineers run agentic workflows that scan repositories for security, performance, and governance issues, open GitHub Issues, and route remediation to Copilot Coding Agent. Windows Runners extend that workflow to Windows projects, which is directly relevant to many .NET codebases that cannot treat Linux as a drop-in build environment.

The practical question for a .NET team is not whether an AI feature looks impressive in a demo. It is whether the repository, permissions, issues, pull requests, and build environment are arranged so that an agent can act safely. A small pilot should measure the quality of generated changes and the review burden, not just the number of Copilot interactions.

## Keep the workflows that already work

CAP did not treat GitHub as a requirement to abandon Azure DevOps. Migrated repositories use the Azure Pipelines GitHub app to connect existing pipelines to the new repository location. Teams also use `AB#` syntax in GitHub pull requests to link changes to Azure Boards work items.

That hybrid model gives a .NET organization room to preserve mature build and release pipelines while developers learn GitHub's pull-request and repository conventions. It also turns the migration into a narrower change: move the source and collaboration surface first, then decide independently whether Actions, GitHub Projects, or another service should replace an existing Azure DevOps workflow.

There is still integration work to test. Validate service connections, webhook behavior, status checks, branch protections, package feeds, release triggers, and permissions for every repository type in the pilot. A pipeline that runs on a developer's branch is not enough; the migration is successful only when the full path from issue to pull request to deployment remains trustworthy.

## What changes for developers?

The platform shift brings a learning curve. Azure DevOps extensions often center on UI customizations, while GitHub customization leans more heavily on APIs, Actions, and integrations. Teams need new conventions for repository settings, issue automation, code ownership, and agent permissions.

CAP eased that transition by pairing developers with prior GitHub experience and preserving familiar Azure Boards and Azure Pipelines workflows where they still added value. I would do the same, and I would publish a short migration runbook for the daily operations that otherwise create needless support work: creating a pull request, linking an `AB#` work item, rerunning a required check, finding a failed pipeline, and requesting access to a repository.

GitHub also offers a non-AI benefit for a fragmented organization. Consolidating repositories into one GitHub organization can improve code discovery when teams previously searched across dozens of Azure DevOps organizations. The multi-surface experience is useful too, but code discoverability is the kind of quiet improvement that compounds across a large engineering group.

## My recommendation

Treat this as a staged architecture and workflow decision, not a brand migration. Start with a measured group of smaller repositories, connect Azure Pipelines and Azure Boards, and validate the developer path end to end. Then use the evidence to decide which repositories should move next and which complex monorepos need more preparation.

Microsoft's CAP example shows that GitHub can be adopted for AI-native development without forcing an organization to abandon critical DevOps workflows overnight. For .NET teams, that is the actionable part: change the repository boundary first, keep delivery stable, and earn the next migration wave with results.

Resources:

- [GitHub Enterprise Importer](https://docs.github.com/en/migrations/using-github-enterprise-importer)
- [Azure Pipelines GitHub app](https://github.com/apps/azure-pipelines)
- [Agentic workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)
- [Windows Runners for Copilot Coding Agent](https://github.blog/changelog/2026-02-18-use-copilot-coding-agent-with-windows-projects/)
