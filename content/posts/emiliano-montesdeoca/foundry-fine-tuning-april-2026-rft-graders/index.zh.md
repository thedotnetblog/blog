---
title: "Foundry的RFT更便宜、更智能了 — 看看有什么变化"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry本月发布了三项RFT更新：o4-mini的全球训练、新的GPT-4.1模型评分器，以及一份能为你节省数小时调试时间的最佳实践指南。"
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}})。*

如果你正在开发依赖微调模型的.NET应用，这个月的Foundry更新值得关注。Reinforcement Fine-Tuning变得更易获取，价格也大幅降低。

完整详情请参阅[官方公告](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/)，这里是实用要点总结。

## o4-mini的全球训练

o4-mini是推理密集型和智能体工作负载的首选模型。重大消息：你现在可以从13+个Azure区域启动微调任务，与Standard训练相比，每token的训练费率更低。相同的基础设施，相同的质量，更广的覆盖范围。

如果你的团队分布在不同地区，这很重要。你不再局限于少数几个区域来进行训练。

以下是启动全球训练任务的REST API调用：

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

那个`trainingType: globalstandard`标志就是关键区别。

## 新模型评分器：GPT-4.1系列

评分器定义了模型优化所针对的奖励信号。此前，基于模型的评分器仅限于较少的模型集合。现在你有三个新选项：GPT-4.1、GPT-4.1-mini和GPT-4.1-nano。

什么时候应该使用模型评分器而不是确定性评分器？当你的任务输出是开放式的，当你需要在多个维度上进行部分评分，或者当你在构建智能体工作流且工具调用的正确性取决于语义上下文时。

关键在于，分层策略很实用：

- **GPT-4.1-nano** 用于初始迭代。低成本，快速反馈循环。
- **GPT-4.1-mini** 当你的评分标准稳定并需要更高保真度时使用。
- **GPT-4.1** 用于生产环境评分或每个评分决策都至关重要的复杂标准。

你甚至可以在单个RFT任务中混合使用评分器类型。用string-match来评判"正确答案"维度，用模型评分器来评估推理质量。说实话，这种灵活性才是它对实际工作负载真正有用的地方。

## RFT数据格式的陷阱

这是很多人会踩的坑。RFT的数据格式与SFT不同。每行的最后一条消息必须是User或Developer角色——不是Assistant。期望的答案放在顶层键中，如`reference_answer`，评分器会直接引用它。

如果你之前一直在做监督微调并想切换到RFT，你需要重新组织训练数据。不要跳过这一步，否则你的任务会静默失败。

## 为什么这对.NET开发者很重要

如果你通过Azure OpenAI SDK从.NET应用中调用微调模型，更便宜的训练意味着你可以更积极地迭代。模型评分器选项意味着你可以针对细微的任务进行微调——不仅仅是精确匹配场景。[GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md)上的最佳实践指南将为你节省真正的调试时间。

从小处开始。十到一百个样本。简单的评分器。验证循环。然后扩展。
