---
title: "The Agentic DevOps Playbook: From Broken Practices to Agent-Ready Delivery"
description: "Agents accelerate what a team does well and what it does poorly. A practical playbook for strengthening DevOps foundations, specifications, pipelines, and governance."
date: 2026-09-01
author: "Emiliano Montesdeoca"
tags: [devops, agents, ci-cd, strategy]
slug: agentic-devops-playbook
---

Original source: [DevOps Playbook for the Agentic Era](https://devblogs.microsoft.com/all-things-azure/agentic-devops-practices-principles-strategic-direction/)

Here's the uncomfortable truth: agents do not fix broken DevOps. They scale it. If CI/CD is fragile, agents break it faster. If test coverage is thin, agents ship untested code at higher velocity. If infrastructure is manually configured, agents produce deployments that drift from reality.

For .NET teams evaluating agent adoption, this principle is foundational. Before allowing agents to open pull requests or propose infrastructure changes, audit the delivery system that will receive their work.

## The Foundation Checklist

The source identifies six dimensions that determine whether a team is ready to scale agentic workflows: CI/CD pipelines, automated testing, infrastructure as code, security scanning, branch protection, and observability.

A .NET repository should have a reliable build, test, and deployment path that behaves consistently across environments. Unit, integration, and end-to-end tests should run on pull requests with meaningful thresholds. Environments should be provisioned through version-controlled templates with drift detection instead of being hand-tuned. Dependency scanning, secret detection, and code analysis should run as part of the pipeline.

Branch protection is the human boundary around agent-authored pull requests. Required reviews, status checks, and merge restrictions should be enforced by the repository rather than left to an agent's interpretation. Observability is the production feedback loop: logging, monitoring, alert ownership, and escalation paths determine whether an agent-introduced regression is visible.

These are not agent-specific luxuries. They are the same practices that make human-authored code reliable. Agents simply make the cost of missing them arrive faster.

## The Engineer's Role Changes

The source describes three emerging responsibilities: system designer, agent operator, and quality steward.

System designers define the constraints and specifications agents work within. That makes architecture documentation, repository skill profiles, and explicit testing conventions more important. Agent operators select which agent is appropriate for a task, define its scope, configure delegation, and monitor behavior. Quality stewards review whether the output matches the specification and preserves the intent of the change.

For .NET teams, this means documenting the patterns that often live only in senior developers' heads: approved NuGet packages, dependency injection conventions, async and cancellation behavior, error handling, logging, and required test types. The agent cannot reliably follow a convention that the repository never states.

The change is not that engineers stop writing code. They write more of the scaffolding, guardrails, and governance that let code-producing systems operate safely.

## Four Collaboration Zones

The playbook maps human and agent responsibilities across four zones.

In the IDE, humans define intent and review changes while agents generate code, refactors, and tests. In a pull request, agents can open changes and respond to comments, while branch protection and required human approval enforce the boundary. In CI/CD, agents can trigger builds or remediate failures within scope, but pipeline rules and provenance checks decide what is acceptable. In production, agents can detect anomalies or propose remediation, while people own rollback and high-risk decisions.

This model is more useful than a blanket rule such as "agents may not deploy." It asks what the agent is allowed to do in each context, what evidence it must produce, and which action requires a human decision.

## The Repository Becomes an Interface

Human teams can survive implicit conventions and tribal knowledge because people ask questions during onboarding and code review. Agents need those conventions to be explicit, machine-readable, and enforceable.

A repository operating with agents should document architecture patterns, dependency policies, testing expectations, file organization, and security requirements. Files such as `.github/copilot-instructions.md` and specification or constitution files can provide the context a senior engineer would receive when joining a project.

This is also a useful test of the documentation itself. If the instructions are too broad to verify or contradict the code, the agent will expose that ambiguity. Treat the repository guide as a maintained engineering artifact, not a prompt that was written once and forgotten.

## From Prompts to Specifications

The playbook argues for specification-driven development. Prompts are ephemeral and optimized for a single interaction. Specifications are versioned, reviewed, and stored beside the code they describe. They define why a feature exists, the constraints, the user expectations, and the acceptance criteria.

For a .NET feature, a useful specification might name the API contract, authorization behavior, migration constraints, test scenarios, and definition of done. The agent can use that information during implementation, and the pipeline can use it as a reference during verification. The specification becomes durable context rather than a chat transcript.

The maturity curve runs from ad hoc prompts to templates, structured specs, and living specs linked to code and tests. Most teams do not need to jump to the final stage. Start by versioning the acceptance criteria for one high-value workflow.

## Pipelines Must Actively Verify

Traditional pipelines ask whether code compiles, tests pass, and known vulnerabilities exist. Agentic pipelines need deeper questions: does the implementation match the specification, are generated tests meaningful, do dependencies exist in a legitimate registry, and does the code follow repository architecture rather than merely formatting rules?

Three layers help. Structural verification checks file placement, dependency rules, naming, and boundaries. Semantic verification checks behavior against acceptance criteria and integration tests. Provenance verification traces artifacts and dependencies to legitimate sources, reducing supply-chain and hallucinated-package risk.

For .NET developers, strict type checking and integration tests catch many invented API calls. Package allowlists and review gates reduce the chance that an agent adds an unapproved dependency. Path-based restrictions can protect deployment workflows and other sensitive files.

## Measure Outcomes, Not Activity

Lines of code, commits, and pull requests become especially misleading when agents generate them. Track features delivered, user impact, time to value, review time, revision cycles, first-pass verification rate, and defects caught in CI versus production.

These measures show whether agents are reducing the cost of delivery or simply increasing the volume of work that humans must inspect. They also reveal where better specifications or repository guidance would have the highest return.

## What .NET Teams Should Do Now

1. Audit build, test, IaC, security, branch protection, and observability foundations.
2. Document architectural and package conventions in the repository.
3. Version acceptance criteria for one representative feature.
4. Add structural, semantic, and provenance checks to agent-facing pipelines.
5. Define which agent actions require human approval and record the boundary.

Agentic DevOps is less about giving an agent more permission than about building a delivery system that can explain, verify, and contain the work it receives.