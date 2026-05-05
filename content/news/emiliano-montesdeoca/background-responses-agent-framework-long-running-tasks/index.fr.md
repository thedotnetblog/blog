---
title: "Les réponses en arrière-plan dans Microsoft Agent Framework : fini l'angoisse des timeouts"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework permet maintenant de décharger les tâches IA longues avec des tokens de continuation. Voici comment fonctionnent les réponses en arrière-plan et pourquoi elles comptent pour vos agents .NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Si vous avez construit quoi que ce soit avec des modèles de raisonnement comme o3 ou GPT-5.2, vous connaissez la douleur. Votre agent commence à réfléchir à une tâche complexe, le client attend, et quelque part entre "ça va" et "est-ce que ça a planté ?" votre connexion expire. Tout ce travail ? Perdu.

Microsoft Agent Framework vient de livrer les [réponses en arrière-plan](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — et honnêtement, c'est une de ces fonctionnalités qui auraient dû exister depuis le premier jour.

## Le problème avec les appels bloquants

Dans un schéma requête-réponse traditionnel, votre client bloque jusqu'à ce que l'agent termine. Ça marche bien pour les tâches rapides. Mais quand vous demandez à un modèle de raisonnement de faire une recherche approfondie, une analyse en plusieurs étapes, ou de générer un rapport de 20 pages ? Vous regardez des minutes de temps réel. Pendant cette fenêtre :

- Les connexions HTTP peuvent expirer
- Les coupures réseau tuent toute l'opération
- Votre utilisateur fixe un spinner en se demandant s'il se passe quelque chose

Les réponses en arrière-plan inversent la donne.

## Comment fonctionnent les tokens de continuation

Au lieu de bloquer, vous lancez la tâche de l'agent et récupérez un **token de continuation**. Pensez-y comme un ticket de retrait dans un atelier de réparation — vous ne restez pas debout au comptoir à attendre, vous revenez quand c'est prêt.

Le flux est direct :

1. Envoyez votre requête avec `AllowBackgroundResponses = true`
2. Si l'agent supporte le traitement en arrière-plan, vous recevez un token de continuation
3. Interrogez à votre rythme jusqu'à ce que le token retourne `null` — ça signifie que le résultat est prêt

Voici la version .NET :

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Interroger jusqu'à complétion
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Si l'agent finit immédiatement (tâches simples, modèles qui n'ont pas besoin de traitement en arrière-plan), aucun token de continuation n'est renvoyé. Votre code fonctionne simplement — aucun traitement spécial nécessaire.

## Streaming avec reprise : la vraie magie

Le polling convient pour les scénarios fire-and-forget, mais que faire quand vous voulez un progrès en temps réel ? Les réponses en arrière-plan supportent aussi le streaming avec reprise intégrée.

Chaque mise à jour streamée porte son propre token de continuation. Si votre connexion tombe en plein stream, vous reprenez exactement là où vous en étiez :

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simuler une interruption réseau
}

// Reprendre exactement là où nous en étions
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

L'agent continue le traitement côté serveur indépendamment de ce qui se passe avec votre client. C'est de la tolérance aux pannes intégrée sans que vous écriviez de la logique de retry ou des circuit breakers.

## Quand utiliser ça concrètement

Tous les appels d'agent n'ont pas besoin de réponses en arrière-plan. Pour les completions rapides, vous ajoutez de la complexité pour rien. Mais voici où elles brillent :

- **Tâches de raisonnement complexe** — analyse en plusieurs étapes, recherche approfondie, tout ce qui fait vraiment réfléchir un modèle de raisonnement
- **Génération de contenu long** — rapports détaillés, documents en plusieurs parties, analyses approfondies
- **Réseaux peu fiables** — clients mobiles, déploiements edge, VPN d'entreprise instables
- **Patterns UX asynchrones** — soumettez une tâche, allez faire autre chose, revenez pour les résultats

Pour nous développeurs .NET qui construisons des apps enterprise, ce dernier point est particulièrement intéressant. Pensez à une app Blazor où un utilisateur demande un rapport complexe — vous lancez la tâche de l'agent, affichez un indicateur de progression, et le laissez continuer à travailler. Pas d'acrobaties WebSocket, pas d'infrastructure de file d'attente personnalisée, juste un token et une boucle de polling.

## Pour conclure

Les réponses en arrière-plan sont disponibles maintenant en .NET et Python via Microsoft Agent Framework. Si vous construisez des agents qui font plus que du simple Q&A, ça vaut le coup de l'ajouter à votre boîte à outils. Le pattern du token de continuation garde les choses simples tout en résolvant un vrai problème de production.

Consultez la [documentation complète](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) pour la référence API complète et plus d'exemples.
