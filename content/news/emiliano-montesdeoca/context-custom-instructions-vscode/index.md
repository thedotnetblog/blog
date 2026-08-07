---
title: "Your .NET Repository Needs a Context Layer Before It Needs a Bigger Prompt"
date: 2026-08-08
author: "Emiliano Montesdeoca"
description: "Custom instructions turn Copilot from a general assistant into a teammate that understands a .NET repository's conventions, architecture, and delivery rules."
tags:
  - dotnet
  - github-copilot
  - vscode
  - developer-productivity
  - ai
---

Original source: [Context is all you need: Better AI results with custom instructions](https://code.visualstudio.com/blogs/2025/03/26/custom-instructions)

Most teams try to improve AI-assisted development by writing longer prompts. That is usually the wrong first move.

The better move is to give the tool a durable context layer: the conventions, architectural boundaries, commands, and review expectations that apply to every change in the repository. The Visual Studio Code team calls this custom instructions, and the idea is especially useful for .NET codebases where a short request can touch project references, analyzers, tests, hosting, and deployment decisions all at once.

## The prompt should not carry the repository's memory

A prompt such as "add an endpoint for orders" leaves too many decisions open. Which API style? Which validation library? Where do application services live? Are errors returned as `ProblemDetails`? Which test project owns the behavior? Does the solution use minimal APIs, controllers, or a vertical slice layout?

You can answer those questions every time, but then the prompt becomes a second configuration file. Worse, it becomes a private configuration file that only exists in one developer's chat history.

The source article's most practical recommendation is a simple `.github/copilot-instructions.md` file. Copilot can discover it automatically, which means the repository can state its working agreements once and let every contributor benefit from them.

For a .NET solution, I would start with something like this:

```markdown
# Repository guidance

## Architecture

- Keep HTTP concerns in the Web project.
- Put business rules in application services or vertical slices.
- Keep EF Core queries in the data-access boundary.
- Do not reference infrastructure projects from the domain project.

## .NET conventions

- Use nullable reference types and treat warnings as errors.
- Prefer async APIs and pass CancellationToken through application boundaries.
- Return ProblemDetails for API errors.
- Add or update tests for every behavior change.

## Validation

- Run `dotnet format --verify-no-changes` before opening a pull request.
- Run `dotnet test --solution .` for the full test suite.
- Do not introduce a new package when an existing project dependency already solves the problem.
```

This is not a replacement for analyzers, tests, or code review. It is the shared explanation around those mechanisms. The compiler can tell you that a nullable value is unsafe; the instructions can tell Copilot how this repository expects that case to be handled.

## Keep instructions close to the thing they govern

One large instruction file is a useful starting point, but it can become another wall of prose. The source article also describes referencing separate files through workspace settings. That lets a team keep specialized guidance where it belongs.

For example, a repository might have:

```text
.github/
  copilot-instructions.md
docs/
  api-conventions.md
  database-conventions.md
  testing-conventions.md
.vscode/
  settings.json
```

Then workspace settings can point Copilot at the relevant files:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": "./docs/api-conventions.md" },
    { "file": "./docs/database-conventions.md" },
    { "file": "./docs/testing-conventions.md" }
  ]
}
```

I like this approach because it mirrors how a .NET solution is usually organized. API guidance can talk about contracts and versioning without repeating database rules. Testing guidance can explain fixture lifetimes and integration-test dependencies without making every code-generation request carry the entire platform manual.

The important constraint is ownership. If a file is referenced by the workspace, it needs to be reviewed like code. Stale instructions are worse than no instructions because they make incorrect output look intentional.

## Prompt files are reusable workflows, not magic spells

The announcement also introduces prompt files: Markdown files under `.github/prompts` that package a repeatable request. This is where custom instructions move from passive context to team workflow.

A prompt file for a new vertical slice might ask Copilot to inspect an existing slice, create the request and handler, add validation, add tests, and report the commands it ran. Another could describe the checks for a migration or a production incident.

The value is not that Copilot has learned a secret incantation. The value is that the team has made its process visible, reviewable, and repeatable.

For us .NET developers, that distinction matters. A prompt file should not hide decisions that belong in code or CI. It should make the path through those decisions easier to follow. If a prompt file says "add tests," it should name the test project, test framework, and required command. If it says "add an endpoint," it should point to a real neighboring implementation.

## What I would do in a real repository

I would roll this out in three small steps:

1. Add a short root instruction file with architecture boundaries, commands, and non-negotiable quality rules.
2. Add one prompt file for the most repetitive workflow, such as creating an API slice or diagnosing a failed build.
3. Review the generated changes and the instructions together after a week of use.

That last step is the one teams skip. The useful question is not whether Copilot produced more code. It is whether the repository needed fewer corrections after the first draft. If the answer is no, improve the context before asking for a more elaborate prompt.

## The practical takeaway

Custom instructions are not a way to outsource engineering judgment. They are a way to keep engineering judgment from disappearing into individual conversations.

Start with the repository's boundaries, commands, and examples. Keep specialized guidance in focused files. Turn repeated workflows into prompt files. Then let tests, analyzers, and review remain the final authority.

The best AI result is often the one that required the smallest prompt because the repository already explained the important parts.