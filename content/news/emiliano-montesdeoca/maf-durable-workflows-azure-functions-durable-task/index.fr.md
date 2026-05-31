---
title: "Workflows Durables dans Microsoft Agent Framework : De In-Memory à Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "Le modèle de programmation de workflows de MAF prend désormais en charge l'exécution durable basée sur Durable Task — voici comment créer des workflows d'agents composables qui survivent aux redémarrages de processus et s'adaptent à Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

L'un des points douloureux avec les premiers workflows d'agents IA : ils sont fragiles. Un workflow multi-étapes de longue durée lié à un seul processus signifie que le redémarrage du processus = état perdu. Pour des démos simples, c'est acceptable. Pour des charges de travail en production, ce ne l'est pas.

Le modèle de programmation de workflows de Microsoft Agent Framework prend désormais en charge l'**exécution durable**, basée sur le framework Durable Task, avec hébergement Azure Functions. Voici comment fonctionne le modèle de programmation et pourquoi l'histoire de la durabilité compte.

## Les Blocs de Construction Fondamentaux

Les **Executors** sont l'unité fondamentale de travail. Chacun est typé — il prend une entrée spécifique et produit une sortie spécifique :

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // rechercher la commande, la retourner
        return new Order(Id: message.OrderId, ...);
    }
}
```

Les **Workflows** relient les executors en graphes dirigés en utilisant un constructeur fluide. Le framework gère l'exécution, le flux de données entre les étapes et la propagation des erreurs.

Vous pouvez modéliser :
- Des chaînes séquentielles (étape A → étape B → étape C)
- Fan-out/fan-in parallèle (exécuter les agents A, B, C en parallèle, agréger les résultats)
- Branchement conditionnel
- Approbations humain-dans-la-boucle (suspendre le workflow, attendre un signal externe)

## Le Runner In-Memory pour le Développement Local

Démarrer est rapide :

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Le package principal inclut un runner léger en cours de processus. Pas de dépendances externes, pas de base de données, pas de ressources Azure. Fonctionne très bien pour le développement local et les tests unitaires.

## Ajouter la Durabilité avec Durable Task

Quand un workflow doit survivre aux redémarrages de processus — parce qu'il est de longue durée, parce qu'il a des étapes humain-dans-la-boucle, parce qu'il se distribue sur de nombreux appels d'agents en parallèle — le runner in-memory n'est pas suffisant.

L'intégration Durable Task de MAF stocke l'état du workflow dans Azure Storage. Si le processus redémarre, le workflow reprend là où il s'était arrêté. Le modèle de programmation reste le même ; vous remplacez simplement le runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Les mêmes executors, le même graphe de workflow — basé sur un état durable.

## Hébergement Azure Functions

La troisième couche est l'hébergement Azure Functions. Votre workflow devient une application Function : déclenchez le workflow via un endpoint HTTP, et le runtime durable gère la mise à l'échelle, l'état et la fiabilité.

Cela signifie qu'un workflow multi-agents avec des appels parallèles, des branches conditionnelles et des approbations humaines peut s'adapter à un environnement Functions serverless sans gestion d'état personnalisée.

## Pourquoi C'est Important

La combinaison est significative pour les vrais systèmes IA :

- **Appels d'agents en parallèle** — distribuer vers plusieurs agents spécialisés simultanément sans blocage, agréger les résultats quand tous terminent
- **Processus de longue durée** — les workflows qui impliquent une approbation humaine ou des événements externes peuvent se suspendre et reprendre sur des heures ou des jours
- **Mise à l'échelle** — Azure Functions fait évoluer l'exécution horizontalement ; le framework Durable Task gère la coordination de l'état parallèle

Si vous construisez des workflows MAF au-delà de simples démos locaux, c'est le chemin vers l'exécution de qualité production.

Publication originale : [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
