---
title: "Où héberger vos agents IA sur Azure ? Un guide de décision pratique"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure propose six façons d'héberger des agents IA — des conteneurs bruts aux Foundry Hosted Agents entièrement gérés. Voici comment choisir la bonne option pour votre charge de travail .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Si vous construisez des agents IA avec .NET en ce moment, vous avez probablement remarqué quelque chose : il y a *beaucoup* de façons de les héberger sur Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — et tous semblent raisonnables jusqu'à ce que vous ayez réellement besoin d'en choisir un. Microsoft vient de publier un [guide complet sur l'hébergement d'agents IA sur Azure](https://devblogs.microsoft.com/all-things-azure/hostedagent/) qui clarifie tout ça, et je veux le décomposer du point de vue pratique d'un développeur .NET.

## Les six options en un coup d'œil

Voici comment je résumerais le paysage :

| Option | Idéal pour | Vous gérez |
|--------|-----------|------------|
| **Container Apps** | Contrôle total des conteneurs sans complexité K8s | Observabilité, état, cycle de vie |
| **AKS** | Conformité entreprise, multi-cluster, réseau personnalisé | Tout (c'est le but) |
| **Azure Functions** | Tâches d'agents événementielles et courtes | Presque rien — vrai serverless |
| **App Service** | Agents HTTP simples, trafic prévisible | Déploiement, config de scaling |
| **Foundry Agents** | Agents sans code via portail/SDK | Presque rien |
| **Foundry Hosted Agents** | Agents framework personnalisé avec infra gérée | Uniquement votre code d'agent |

Les quatre premières sont du compute généraliste — vous *pouvez* y exécuter des agents, mais elles n'ont pas été conçues pour ça. Les deux dernières sont natives aux agents : elles comprennent les conversations, les appels d'outils et les cycles de vie des agents comme des concepts de première classe.

## Foundry Hosted Agents — le sweet spot pour les développeurs .NET d'agents

C'est ce qui a attiré mon attention. Les Foundry Hosted Agents se situent pile au milieu : vous obtenez la flexibilité d'exécuter votre propre code (Semantic Kernel, Agent Framework, LangGraph — peu importe) mais la plateforme gère l'infrastructure, l'observabilité et la gestion des conversations.

La pièce clé est le **Hosting Adapter** — une fine couche d'abstraction qui connecte votre framework d'agents à la plateforme Foundry. Pour Microsoft Agent Framework, ça ressemble à ça :

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

C'est toute votre histoire d'hébergement. L'adapter gère la traduction de protocoles, le streaming via server-sent events, l'historique de conversation et le traçage OpenTelemetry — tout automatiquement. Pas de middleware personnalisé, pas de plomberie manuelle.

## Le déploiement est vraiment simple

J'ai déployé des agents sur Container Apps avant et ça fonctionne, mais on finit par écrire beaucoup de code de colle pour la gestion d'état et l'observabilité. Avec Hosted Agents et `azd`, le déploiement c'est :

```bash
# Installer l'extension agent IA
azd ext install azure.ai.agents

# Initialiser depuis un template
azd ai agent init

# Construire, pousser, déployer — terminé
azd up
```

Ce seul `azd up` construit votre conteneur, le pousse vers ACR, provisionne le projet Foundry, déploie les endpoints de modèle et démarre votre agent. Cinq étapes condensées en une seule commande.

## Gestion de conversations intégrée

C'est la partie qui fait gagner le plus de temps en production. Au lieu de construire votre propre store d'état de conversation, les Hosted Agents le gèrent nativement :

```python
# Créer une conversation persistante
conversation = openai_client.conversations.create()

# Premier tour
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Deuxième tour — le contexte est préservé
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Pas de Redis. Pas de store de sessions Cosmos DB. Pas de middleware personnalisé pour la sérialisation des messages. La plateforme gère tout simplement.

## Mon framework de décision

Après avoir passé en revue les six options, voici mon modèle mental rapide :

1. **Vous avez besoin de zéro infrastructure ?** → Foundry Agents (portail/SDK, pas de conteneurs)
2. **Vous avez du code d'agent personnalisé mais voulez un hébergement géré ?** → Foundry Hosted Agents
3. **Vous avez besoin de tâches d'agents événementielles et courtes ?** → Azure Functions
4. **Vous avez besoin d'un contrôle maximum des conteneurs sans K8s ?** → Container Apps
5. **Vous avez besoin de conformité stricte et multi-cluster ?** → AKS
6. **Vous avez un agent HTTP simple avec un trafic prévisible ?** → App Service

Pour la plupart des développeurs .NET qui construisent avec Semantic Kernel ou Microsoft Agent Framework, Hosted Agents est probablement le bon point de départ. Vous obtenez le scale-to-zero, OpenTelemetry intégré, la gestion des conversations et la flexibilité de framework — sans gérer Kubernetes ni monter votre propre stack d'observabilité.

## Pour conclure

Le paysage de l'hébergement d'agents sur Azure mûrit rapidement. Si vous démarrez un nouveau projet d'agent IA aujourd'hui, je considérerais sérieusement Foundry Hosted Agents avant de recourir à Container Apps ou AKS par habitude. L'infrastructure gérée fait gagner un temps réel, et le pattern hosting adapter vous permet de garder votre choix de framework.

Consultez le [guide complet de Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) et le [repo Foundry Samples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) pour des exemples fonctionnels.
