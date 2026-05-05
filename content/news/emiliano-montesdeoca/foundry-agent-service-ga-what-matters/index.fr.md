---
title: "Foundry Agent Service est GA : Ce qui compte vraiment pour les développeurs d'agents .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Le Foundry Agent Service de Microsoft vient de passer en GA avec le réseau privé, Voice Live, les évaluations de production et un runtime multi-modèle ouvert. Voici ce que vous devez savoir."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Soyons honnêtes — construire un prototype d'agent IA est la partie facile. La partie difficile, c'est tout ce qui suit : le mettre en production avec un isolement réseau approprié, exécuter des évaluations qui signifient réellement quelque chose, gérer les exigences de conformité, et ne rien casser à 2h du matin.

Le [Foundry Agent Service vient de passer en GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), et cette version est focalisée comme un laser sur ce fossé du "tout ce qui suit".

## Construit sur la Responses API

Le titre principal : le Foundry Agent Service de nouvelle génération est construit sur l'OpenAI Responses API. Si vous construisez déjà avec ce protocole, migrer vers Foundry nécessite des changements de code minimaux. Ce que vous gagnez : sécurité entreprise, réseau privé, RBAC Entra, traçabilité complète et évaluation — par-dessus votre logique d'agent existante.

L'architecture est intentionnellement ouverte. Vous n'êtes pas verrouillé à un fournisseur de modèle ou un framework d'orchestration. Utilisez DeepSeek pour la planification, OpenAI pour la génération, LangGraph pour l'orchestration — le runtime gère la couche de cohérence.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Si vous venez du package `azure-ai-agents`, les agents sont maintenant des opérations de première classe sur `AIProjectClient` dans `azure-ai-projects`. Supprimez la dépendance standalone et utilisez `get_openai_client()` pour piloter les réponses.

## Réseau privé : le bloqueur entreprise supprimé

C'est la fonctionnalité qui débloque l'adoption enterprise. Foundry supporte maintenant le réseau privé complet de bout en bout avec BYO VNet :

- **Aucun egress public** — le trafic de l'agent ne touche jamais l'internet public
- **Injection de conteneurs/sous-réseaux** dans votre réseau pour la communication locale
- **Connectivité des outils incluse** — serveurs MCP, Azure AI Search, agents de données Fabric fonctionnent tous sur des chemins privés

Ce dernier point est critique. Ce ne sont pas seulement les appels d'inférence qui restent privés — chaque invocation d'outil et appel de récupération reste aussi à l'intérieur de votre périmètre réseau. Pour les équipes opérant sous des politiques de classification de données qui interdisent le routage externe, c'est ce qui manquait.

## Authentification MCP bien faite

Les connexions aux serveurs MCP supportent maintenant le spectre complet des patterns d'authentification :

| Méthode d'auth | Quand l'utiliser |
|----------------|------------------|
| Basée sur clé | Accès partagé simple pour les outils internes à l'organisation |
| Entra Agent Identity | Service à service ; l'agent s'authentifie comme lui-même |
| Entra Managed Identity | Isolation par projet ; pas de gestion de credentials |
| OAuth Identity Passthrough | Accès délégué par utilisateur ; l'agent agit au nom des utilisateurs |

OAuth Identity Passthrough est le plus intéressant. Quand les utilisateurs doivent donner à un agent l'accès à leurs données personnelles — leur OneDrive, leur organisation Salesforce, une API SaaS scopée par utilisateur — l'agent agit en leur nom avec des flux OAuth standard. Pas d'identité système partagée prétendant être tout le monde.

## Voice Live : voix à voix sans la plomberie

Ajouter la voix à un agent signifiait auparavant assembler STT, LLM et TTS — trois services, trois sauts de latence, trois surfaces de facturation, le tout synchronisé à la main. **Voice Live** condense tout ça en une seule API managée avec :

- Détection sémantique de l'activité vocale et de fin de tour (comprend le sens, pas juste le silence)
- Suppression du bruit et annulation d'écho côté serveur
- Support du barge-in (les utilisateurs peuvent interrompre en pleine réponse)

Les interactions vocales passent par le même runtime d'agent que le texte. Mêmes évaluateurs, mêmes traces, même visibilité des coûts. Pour le support client, le service terrain ou les scénarios d'accessibilité, ça remplace ce qui nécessitait auparavant un pipeline audio personnalisé.

## Évaluations : de la case à cocher au monitoring continu

C'est là que Foundry devient sérieux sur la qualité en production. Le système d'évaluation a maintenant trois couches :

1. **Évaluateurs prêts à l'emploi** — cohérence, pertinence, fondement, qualité de récupération, sécurité. Connectez à un dataset ou au trafic en direct et obtenez des scores.

2. **Évaluateurs personnalisés** — encodez votre propre logique métier, standards de ton et règles de conformité spécifiques au domaine.

3. **Évaluation continue** — Foundry échantillonne le trafic de production en direct, exécute votre suite d'évaluateurs et affiche les résultats dans des tableaux de bord. Configurez des alertes Azure Monitor pour quand le fondement baisse ou que les seuils de sécurité sont dépassés.

Tout est publié dans Azure Monitor Application Insights. Qualité de l'agent, santé de l'infrastructure, coûts et télémétrie applicative — tout au même endroit.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Six nouvelles régions pour les agents hébergés

Les agents hébergés sont maintenant disponibles dans East US, North Central US, Sweden Central, Southeast Asia, Japan East et plus. C'est important pour les exigences de résidence des données et pour comprimer la latence quand votre agent tourne près de ses sources de données.

## Pourquoi c'est important pour les développeurs .NET

Même si les exemples de code dans l'annonce GA sont Python-first, l'infrastructure sous-jacente est agnostique au langage — et le SDK .NET pour `azure-ai-projects` suit les mêmes patterns. La Responses API, le framework d'évaluation, le réseau privé, l'auth MCP — tout cela est disponible depuis .NET.

Si vous attendiez que les agents IA passent de "démo cool" à "je peux réellement livrer ça au travail", cette version GA est le signal. Réseau privé, authentification appropriée, évaluation continue et monitoring de production sont les pièces qui manquaient.

## Pour conclure

Foundry Agent Service est disponible maintenant. Installez le SDK, ouvrez [le portail](https://ai.azure.com) et commencez à construire. Le [guide de démarrage rapide](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) vous amène de zéro à un agent en fonctionnement en quelques minutes.

Pour le deep-dive technique complet avec tous les exemples de code, consultez l'[annonce GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
