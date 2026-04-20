---
title: "Foundry का RFT सस्ता और स्मार्ट हो गया — यहाँ जानिए क्या बदला"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry ने इस महीने तीन RFT updates ship किए: o4-mini के लिए global training, नए GPT-4.1 model graders, और एक best practices guide जो आपके debugging के घंटे बचाएगी।"
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

अगर आप fine-tuned models पर निर्भर .NET apps बना रहे हैं, तो इस महीने के Foundry updates पर ध्यान देने लायक हैं। Reinforcement Fine-Tuning अब और accessible और काफी सस्ती हो गई है।

पूरी जानकारी [official announcement](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/) में है, लेकिन यहाँ practical breakdown है।

## o4-mini के लिए Global Training

o4-mini reasoning-heavy और agentic workloads के लिए go-to model है। बड़ी खबर: अब आप Standard training की तुलना में कम per-token training rates के साथ 13+ Azure regions से fine-tuning jobs launch कर सकते हैं। वही infrastructure, वही quality, व्यापक पहुँच।

अगर आपकी team geographies में फैली हुई है, तो यह मायने रखता है। अब आप training के लिए कुछ ही regions तक सीमित नहीं हैं।

Global training job शुरू करने के लिए REST API call यहाँ है:

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

वह `trainingType: globalstandard` flag ही मुख्य अंतर है।

## नए Model Graders: GPT-4.1 Family

Graders वह reward signal define करते हैं जिसके आधार पर आपका model optimize करता है। अब तक, model-based graders models के एक छोटे set तक सीमित थे। अब आपको तीन नए विकल्प मिलते हैं: GPT-4.1, GPT-4.1-mini, और GPT-4.1-nano।

Deterministic graders की बजाय model graders कब use करें? जब आपका task output open-ended हो, जब आपको कई dimensions में partial credit scoring चाहिए, या जब आप ऐसे agentic workflows बना रहे हों जहाँ tool-call correctness semantic context पर निर्भर करती है।

बात यह है — tiering strategy practical है:

- **GPT-4.1-nano** शुरुआती iterations के लिए। कम cost, fast feedback loops।
- **GPT-4.1-mini** जब आपका grading rubric stable हो और आपको higher fidelity चाहिए।
- **GPT-4.1** production grading या complex rubrics के लिए जहाँ हर scoring decision मायने रखती है।

आप एक ही RFT job में grader types भी mix कर सकते हैं। "correct answer" dimension के लिए string-match और reasoning quality evaluate करने के लिए model grader। यह flexibility ही इसे real workloads के लिए उपयोगी बनाती है।

## RFT Data Format की समस्या

यह लोगों को अटकाती है। RFT data format SFT से अलग है। हर row का आखिरी message User या Developer role का होना चाहिए — Assistant का नहीं। Expected answer एक top-level key जैसे `reference_answer` में जाता है जिसे grader directly reference करता है।

अगर आप supervised fine-tuning कर रहे हैं और RFT पर switch करना चाहते हैं, तो आपको अपना training data restructure करना होगा। यह step skip न करें वरना आपके jobs silently fail होंगे।

## .NET Developers के लिए यह क्यों मायने रखता है

अगर आप Azure OpenAI SDK के ज़रिए .NET apps से fine-tuned models call कर रहे हैं, तो सस्ती training का मतलब है कि आप अधिक aggressively iterate कर सकते हैं। Model grader options का मतलब है कि आप nuanced tasks के लिए fine-tune कर सकते हैं — सिर्फ exact-match scenarios नहीं। और [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) पर best practices guide आपका real debugging time बचाएगी।

छोटे से शुरू करें। दस से सौ samples। Simple grader। Loop validate करें। फिर scale करें।
