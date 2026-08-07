---
title: "Making Agents Practical for Real-World Development"
description: "VS Code's agent improvements address scale, memory, steering, hooks, browser verification, and reusable skills for multi-turn development work."
date: 2026-08-25
author: "Emiliano Montesdeoca"
tags: [vscode, agents, development-workflow, best-practices]
slug: vscode-making-agents-practical
---

# Making Agents Practical for Real-World Development

Original source: [Making agents practical for real-world development](https://code.visualstudio.com/blogs/2026/03/05/making-agents-practical-for-real-world-development)

The gap between an impressive agent demo and a useful Thursday afternoon is mostly operational. Real repositories have large outputs, accumulated conventions, interruptions, failed commands, and decisions that need to survive more than one chat turn.

VS Code's recent agent work is aimed at that gap. The useful story is not one spectacular capability. It is the collection of small controls that make an agent easier to supervise across a real development loop.

## Scale the Output Without Flooding the Session

Large terminal output and generated files can overwhelm a context window. VS Code now streams large outputs to temporary files and makes terminal output collapsible, so the conversation can remain focused on the decision rather than displaying every line.

That is relevant to .NET projects with verbose restores, test runs, generated migrations, and build logs. The agent can work with the result without turning the conversation into a wall of output.

Streaming does not solve architectural discovery. An agent still needs the relevant project structure, domain rules, and design constraints. If a migration touches a large model, point the agent to the schema and tests that define the intended behavior. Output management helps the context window; it does not create missing context.

A good practice is to keep large artifacts inspectable and named. Ask the agent to summarize the result, identify the file containing the full output, and state which lines or failures drove its next action.

## Memory Needs Human Direction

Agent memory can carry useful lessons across sessions, but the developer still needs to decide what matters. Manual context compaction lets you preserve specific decisions instead of trusting an automatic summary to retain every important detail.

For a long-running .NET feature, write instructions such as preserving the authentication flow decision or the database transaction boundary when compacting. Then verify the next response against the actual code. Memory should reduce repetition, not become an invisible source of truth.

The same principle applies to the repository. If a convention is important, encode it in tests, documentation, or project instructions. A chat memory can help today; source control is what the whole team can inspect tomorrow.

## Redirect Without Throwing Away the Work

An agent that takes the wrong direction creates an awkward choice: wait for it to finish, cancel it, or start over. Steering and message queueing make that choice less costly. You can redirect the next step while allowing the current operation to finish when it is safe, or queue a follow-up when the plan is still sound.

Forking a chat session is useful when an architectural question has multiple plausible answers. Explore one dependency injection or data-access approach in a fork, keep the original available, and compare the resulting plans before changing the repository.

These controls do not make generated decisions correct. They make supervision cheaper, which is a more durable improvement.

## Hooks Encode Team Standards

Hooks run at lifecycle points such as session start, before edits, or after tool calls. They turn a repeated reminder into a repository-level guardrail. A hook can request formatting, block a sensitive file change, or trigger a validation action.

For a .NET team, use hooks carefully. A formatting check may be a good default. Blocking edits to a deployment file may also be sensible. A hook that runs a long integration suite before every small edit will frustrate developers and encourage them to disable the whole system.

Keep the policy close to the risk. Make the hook's failure message actionable, and ensure the command works in the same environment as the agent. Hooks are automation, so they deserve the same review as build scripts.

## Browser Tools Verify the Running Result

Browser agent tools can navigate, interact with, and capture screenshots of a running web application. For ASP.NET Core and Blazor developers, that provides a path from generated UI code to an observable result inside the editor.

Use it for bounded checks: does the route load, does the component display the expected test data, does a form show the validation state? Keep authentication, real customer data, and destructive actions outside the experiment. A browser screenshot is evidence of one state, not a replacement for automated tests or accessibility review.

## Skills Make Good Workflows Repeatable

Reusable skills package procedures that teams otherwise restate in every session. A .NET team might define one for preparing an Entity Framework migration, another for adding OpenAPI documentation, and another for reviewing asynchronous code.

The best skill has a narrow trigger, known inputs, and a validation command. Start with a procedure that is repetitive but not ambiguous. A skill should make team knowledge easier to apply, not hide a complicated decision behind a slash command.

## The Practical Recommendation

Adopt these capabilities in layers. First make large outputs and session steering comfortable. Then add one hook and one project-specific skill. Finally, try browser verification for a local web workflow.

Measure the result by review effort and recovery time, not by how autonomous the agent appears. Practical agents are the ones a team can understand, redirect, and validate when the happy path ends.