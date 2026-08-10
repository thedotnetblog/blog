---
title: "What 50,000 runs of a five-line eval reveals about agent efficiency"
description: "VS Code's 50,974-run say_hello eval shows how model planning, workspace exploration, tool choice, and narration affect the cost of even a trivial agent task."
date: 2026-11-09
author: "Emiliano Montesdeoca"
tags: ["Visual Studio Code", "GitHub Copilot", "Agents", "Evaluation", "AI Efficiency"]
slug: vscode-50000-runs-five-line-eval
---

Original source: [What 50,000 Runs of a 5-Line Eval Taught Us](https://code.visualstudio.com/blogs/2026/06/19/what-50000-runs-taught-us)

A good evaluation does not have to be complicated. The VS Code team ran the same tiny agent task more than 50,000 times: add `HELLO` to `HELLO.txt` in an empty workspace. The task is intentionally easy, which makes the interesting differences visible. When the answer is fixed, extra planning, exploration, narration, or tool calls are behavior signals rather than necessary problem-solving.

Across six months, the `say_hello` smoke test accumulated **50,974 runs across 30 models**. It became a small but useful window into how agents scale their effort to the task in front of them.

## The five-line eval

Each run begins with the same empty workspace, tools, and fixed prompt:

```yaml
promptSteps:
  - text: Add HELLO to HELLO.txt.
assertions:
  - check: file_exists("HELLO.txt")
  - check: file_contains("HELLO.txt", "HELLO")
```

The direct path is one `create_file` tool call with `HELLO` as the content. The harness includes the workspace state in the initial prompt, so the model does not need to list the directory or search for clues before creating the file.

The task is useful because it removes ambiguity. A change in pass rate, tool sequence, latency, or output tokens can be studied without first debating whether the task itself was underspecified.

## Models pass, but they do not work the same way

All the models pass the task most of the time. The distinction is how much work they perform to reach the same result.

The direct one-tool-call runs averaged roughly 50 output tokens, including the tool-call structure. One model took that path in 100% of passing runs. Two others used it in 73% and 71% of passing runs. A broad middle group took the direct path between 19% and 52% of the time. Several models used it in only 0.2% to 6% of passing runs, and five models never took it across thousands of passing runs.

The models that did not take the direct path still created the correct file. They might plan first, inspect internal state, list an empty directory, search for files, or use a patch tool designed for an existing file. The outcome is correct, but the path costs time and tokens without improving this particular result.

## Where the overhead comes from

The captured traces show recurring patterns:

- **Planning before acting:** 52% to 99% across the measurable models. One model planned in 99% of runs, and one run included four planning steps for a one-step task.
- **Exploring an empty workspace:** 56% to 96% for the models highlighted in the study.
- **Narrating the reasoning:** 1,441 to 3,676 output tokens for the highest-overhead models, far above the roughly 50-token floor.
- **Using a complex editing tool:** one model used the wrong patch/edit path in about 95% of runs.
- **Running a terminal command:** 3% to 14% for the models highlighted in the report, even though direct file creation was available.

These are not correctness failures. They are calibration failures for a trivial task. On a larger .NET refactoring, a plan or workspace exploration may be useful. On a request with one file, one content value, and two clear assertions, the same behavior is avoidable overhead.

## The bill reflects the extra effort

The study describes roughly 50 output tokens as a realistic minimum for this task. The highest-overhead models averaged 3,676, 2,120, and 1,441 output tokens, or about 29 to 74 times the realistic minimum. Other models landed between 400 and 1,000 tokens, while an efficient group stayed below 150.

The exact values belong to this eval and its anonymized model set, but the principle generalizes: with usage-based billing, output tokens are both a cost and a latency signal. A model that takes the same correct action with fewer unnecessary turns leaves more budget for the work that is actually difficult.

## Bigger does not automatically mean more overhead

The team expected larger models to overthink more, but the data did not support that hypothesis. A larger model in one family averaged 160 output tokens and 2.1 tool calls, while a smaller model from the same family averaged 485 output tokens and 3.7 tool calls. An anonymized mini model was the highest-overhead example at 3,676 output tokens.

The source’s interpretation is that training maturity and effort calibration may matter more than parameter count. That is useful for .NET teams choosing models for agents: benchmark the tasks you care about instead of assuming that model size predicts the cheapest or most disciplined behavior.

## Use a tiny eval without optimizing too narrowly

The `say_hello` task represents one short-horizon task with one correct answer. It should not become the only benchmark. The VS Code team continues to use broader suites such as VSC-Bench to check whether harness changes improve behavior across diverse work.

Still, a stable smoke test is easy to run before a benchmark suite, model onboarding, or infrastructure change. Capture more than pass/fail:

```json
{
  "tool_sequence": ["plan", "list_directory", "create_file"],
  "output_tokens": 210,
  "pass": true
}
```

That record explains why a passing run cost more than another passing run. It also gives an engineering team a way to notice harness regressions before they become expensive across long sessions.

## What to take into .NET development

1. Match the model’s effort to the task horizon; do not eliminate planning where it prevents real mistakes.
2. Run a small, unambiguous smoke task consistently and log its tool sequence.
3. Compare models on the repository and tasks your team actually supports.
4. Inspect the Chat Debug View when a supposedly simple request uses surprising tools or turns.
5. Keep a broad benchmark alongside the tiny eval so an optimization does not overfit the smoke test.

The most valuable lesson is not “never plan.” It is “know when planning earns its cost.” A five-line eval makes that judgment visible, and the same discipline helps keep agent-assisted .NET work efficient without sacrificing the reasoning needed for genuinely complex changes.