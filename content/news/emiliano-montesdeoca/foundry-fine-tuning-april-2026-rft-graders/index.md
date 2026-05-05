---
title: "Foundry's RFT Just Got Cheaper and Smarter — Here's What Changed"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry shipped three RFT updates this month: global training for o4-mini, new GPT-4.1 model graders, and a best practices guide that'll save you hours of debugging."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

If you're building .NET apps that rely on fine-tuned models, this month's Foundry updates are worth paying attention to. Reinforcement Fine-Tuning just got more accessible and significantly cheaper.

The full details are in the [official announcement](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), but here's the practical breakdown.

## Global Training for o4-mini

o4-mini is the go-to model for reasoning-heavy and agentic workloads. The big news: you can now launch fine-tuning jobs from 13+ Azure regions with lower per-token training rates compared to Standard training. Same infrastructure, same quality, broader reach.

If your team is spread across geographies, this matters. You're no longer pinned to a handful of regions to train.

Here's the REST API call to kick off a global training job:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

That `trainingType: globalstandard` flag is the key difference.

## New Model Graders: GPT-4.1 Family

Graders define the reward signal your model optimizes against. Until now, model-based graders were limited to a smaller set of models. Now you get three new options: GPT-4.1, GPT-4.1-mini, and GPT-4.1-nano.

When should you reach for model graders instead of deterministic ones? When your task output is open-ended, when you need partial credit scoring across multiple dimensions, or when you're building agentic workflows where tool-call correctness depends on semantic context.

Here's the thing -- the tiering strategy is practical:

- **GPT-4.1-nano** for initial iterations. Low cost, fast feedback loops.
- **GPT-4.1-mini** once your grading rubric is stable and you need higher fidelity.
- **GPT-4.1** for production grading or complex rubrics where every scoring decision counts.

You can even mix grader types in a single RFT job. Use string-match for the "correct answer" dimension and a model grader for evaluating reasoning quality. That flexibility is honestly what makes this useful for real workloads.

## The RFT Data Format Gotcha

This trips people up. RFT data format is different from SFT. The last message in each row must be a User or Developer role -- not Assistant. The expected answer goes in a top-level key like `reference_answer` that the grader references directly.

If you've been doing supervised fine-tuning and want to switch to RFT, you need to restructure your training data. Don't skip this step or your jobs will fail silently.

## Why This Matters for .NET Developers

If you're calling fine-tuned models from your .NET apps through the Azure OpenAI SDK, cheaper training means you can iterate more aggressively. The model grader options mean you can fine-tune for nuanced tasks -- not just exact-match scenarios. And the best practices guide on [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) will save you real debugging time.

Start small. Ten to a hundred samples. Simple grader. Validate the loop. Then scale.
