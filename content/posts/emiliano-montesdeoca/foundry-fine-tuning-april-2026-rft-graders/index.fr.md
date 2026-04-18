---
title: "Le RFT de Foundry est désormais moins cher et plus intelligent — Voici ce qui a changé"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry a publié trois mises à jour RFT ce mois-ci : l'entraînement global pour o4-mini, de nouveaux évaluateurs de modèle GPT-4.1 et un guide de bonnes pratiques qui vous fera gagner des heures de débogage."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Si vous développez des applications .NET qui reposent sur des modèles fine-tunés, les mises à jour Foundry de ce mois méritent votre attention. Le Reinforcement Fine-Tuning est devenu plus accessible et nettement moins cher.

Les détails complets sont dans l'[annonce officielle](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), mais voici le résumé pratique.

## Entraînement Global pour o4-mini

o4-mini est le modèle de référence pour les charges de travail intensives en raisonnement et agentiques. La grande nouvelle : vous pouvez désormais lancer des jobs de fine-tuning depuis plus de 13 régions Azure avec des tarifs d'entraînement par token inférieurs par rapport à l'entraînement Standard. Même infrastructure, même qualité, plus grande portée.

Si votre équipe est répartie géographiquement, c'est important. Vous n'êtes plus limité à une poignée de régions pour entraîner.

Voici l'appel API REST pour lancer un job d'entraînement global :

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

Ce flag `trainingType: globalstandard` fait toute la différence.

## Nouveaux Évaluateurs de Modèle : Famille GPT-4.1

Les évaluateurs définissent le signal de récompense contre lequel votre modèle optimise. Jusqu'à présent, les évaluateurs basés sur des modèles étaient limités à un ensemble restreint de modèles. Vous avez maintenant trois nouvelles options : GPT-4.1, GPT-4.1-mini et GPT-4.1-nano.

Quand faut-il utiliser des évaluateurs de modèle plutôt que des déterministes ? Quand la sortie de votre tâche est ouverte, quand vous avez besoin de notation partielle sur plusieurs dimensions, ou quand vous construisez des workflows agentiques où la justesse des appels d'outils dépend du contexte sémantique.

Le truc, c'est que la stratégie de niveaux est pratique :

- **GPT-4.1-nano** pour les premières itérations. Coût faible, boucles de feedback rapides.
- **GPT-4.1-mini** une fois que votre grille d'évaluation est stable et que vous avez besoin de plus de fidélité.
- **GPT-4.1** pour l'évaluation en production ou les grilles complexes où chaque décision de notation compte.

Vous pouvez même mixer les types d'évaluateurs dans un seul job RFT. Utilisez le string-match pour la dimension "bonne réponse" et un évaluateur de modèle pour évaluer la qualité du raisonnement. Cette flexibilité est honnêtement ce qui le rend utile pour des charges de travail réelles.

## Le Piège du Format de Données RFT

C'est ce qui fait trébucher les gens. Le format de données RFT est différent du SFT. Le dernier message de chaque ligne doit avoir le rôle User ou Developer — pas Assistant. La réponse attendue va dans une clé de niveau supérieur comme `reference_answer` que l'évaluateur référence directement.

Si vous faisiez du supervised fine-tuning et que vous voulez passer au RFT, vous devez restructurer vos données d'entraînement. Ne sautez pas cette étape ou vos jobs échoueront silencieusement.

## Pourquoi C'est Important pour les Développeurs .NET

Si vous appelez des modèles fine-tunés depuis vos applications .NET via le SDK Azure OpenAI, un entraînement moins cher signifie que vous pouvez itérer plus agressivement. Les options d'évaluateurs de modèle signifient que vous pouvez fine-tuner pour des tâches nuancées — pas seulement des scénarios de correspondance exacte. Et le guide de bonnes pratiques sur [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) vous fera gagner un temps réel de débogage.

Commencez petit. Dix à cent échantillons. Évaluateur simple. Validez la boucle. Puis montez en charge.
