---
title: "Microsoft Foundry Mars 2026 — GPT-5.4, Agent Service en GA et la Refonte du SDK Qui Change Tout"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La mise à jour de mars 2026 de Microsoft Foundry est massive : Agent Service passe en GA, GPT-5.4 apporte un raisonnement fiable, le SDK azure-ai-projects se stabilise dans tous les langages, et Fireworks AI amène les modèles ouverts sur Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}}).*

Les posts mensuels « Quoi de neuf dans Microsoft Foundry » sont généralement un mélange d'améliorations incrémentales et de fonctionnalités phares occasionnelles. L'[édition de mars 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) ? C'est pratiquement que des fonctionnalités phares. Foundry Agent Service passe en GA, GPT-5.4 arrive en production, le SDK reçoit une version stable majeure, et Fireworks AI apporte l'inférence de modèles ouverts sur Azure. Voyons ce qui compte pour les développeurs .NET.

## Foundry Agent Service est prêt pour la production

C'est la grande nouvelle. Le runtime d'agents de nouvelle génération est en disponibilité générale — construit sur l'API Responses d'OpenAI, compatible au niveau du protocole avec les agents OpenAI, et ouvert aux modèles de plusieurs fournisseurs. Si vous construisez avec l'API Responses aujourd'hui, migrer vers Foundry ajoute la sécurité entreprise, le réseau privé, le RBAC Entra, le traçage complet et l'évaluation par-dessus votre logique d'agent existante.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Ajouts clés : réseau privé de bout en bout, extension de l'authentification MCP (y compris le passthrough OAuth), aperçu de Voice Live pour les agents voix-à-voix, et agents hébergés dans 6 nouvelles régions.

## GPT-5.4 — la fiabilité plutôt que l'intelligence brute

GPT-5.4 n'est pas question d'être plus intelligent. C'est une question de fiabilité. Un raisonnement plus solide sur de longues interactions, une meilleure adhérence aux instructions, moins d'échecs en cours de workflow, et des capacités intégrées d'utilisation d'ordinateur. Pour les agents en production, cette fiabilité compte bien plus que les scores de benchmarks.

| Modèle | Tarif (par M tokens) | Idéal pour |
|--------|---------------------|------------|
| GPT-5.4 (≤272K) | $2.50 / $15 sortie | Agents en production, code, workflows documentaires |
| GPT-5.4 Pro | $30 / $180 sortie | Analyse approfondie, raisonnement scientifique |
| GPT-5.4 Mini | Économique | Classification, extraction, appels d'outils légers |

La stratégie intelligente est le routage : GPT-5.4 Mini gère le travail à haut volume et faible latence tandis que GPT-5.4 prend les requêtes nécessitant un raisonnement intensif.

## Le SDK est enfin stable

Le SDK `azure-ai-projects` a publié des versions stables dans tous les langages — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, et .NET 2.0.0 (1er avril). La dépendance `azure-ai-agents` a disparu — tout vit sous `AIProjectClient`. Installez avec `pip install azure-ai-projects` et le paquet inclut `openai` et `azure-identity` comme dépendances directes.

Pour les développeurs .NET, cela signifie un seul paquet NuGet pour toute la surface Foundry. Fini le jonglage entre des SDKs d'agents séparés.

## Fireworks AI amène les modèles ouverts sur Azure

Peut-être l'ajout le plus intéressant architecturalement : Fireworks AI traitant plus de 13 billions de tokens par jour à ~180K requêtes/seconde, maintenant disponible via Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, et MiniMax M2.5 au lancement.

La vraie histoire est le **bring-your-own-weights** — téléchargez des poids quantifiés ou fine-tunés depuis n'importe où sans changer la pile de service. Déployez en mode serverless pay-per-token ou en débit provisionné.

## Autres points forts

- **Phi-4 Reasoning Vision 15B** — raisonnement multimodal pour graphiques, diagrammes et mises en page de documents
- **Evaluations GA** — évaluateurs prêts à l'emploi avec surveillance continue de production intégrée à Azure Monitor
- **Priority Processing** (Preview) — voie de calcul dédiée pour les charges de travail sensibles à la latence
- **Voice Live** — runtime voix-à-voix connecté directement aux agents Foundry
- **Tracing GA** — inspection de bout en bout des traces d'agents avec tri et filtrage
- **Dépréciation de PromptFlow** — migration vers Microsoft Framework Workflows d'ici janvier 2027

## Conclusion

Mars 2026 est un tournant pour Foundry. Agent Service en GA, SDKs stables dans tous les langages, GPT-5.4 pour des agents de production fiables, et inférence de modèles ouverts via Fireworks AI — la plateforme est prête pour des charges de travail sérieuses.

Lisez le [récapitulatif complet](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) et [créez votre premier agent](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) pour commencer.
