---
title: "Microsoft Agent Framework Partie 3 : Des outils aux workflows — Les blocs s'emboîtent"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "La partie 3 de la série Building Blocks for AI en .NET couvre le Microsoft Agent Framework — des agents simples avec des outils aux workflows multi-agents avec mémoire. Voici ce qui compte vraiment."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Si vous avez suivi la série Building Blocks for AI en .NET, vous savez que la Partie 1 nous a donné `IChatClient` (l'interface universelle de modèles) et la Partie 2 `Microsoft.Extensions.VectorData` (recherche sémantique et RAG). Ces deux éléments sont fondamentaux et utiles indépendamment. Mais c'est ici que tout commence à se connecter.

La Partie 3 porte sur le [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — et franchement, c'est la pièce que j'attendais de voir arriver dans .NET. La version 1.0 est sortie en avril. L'API est stable. Il est temps de construire de vrais agents.

## Ce qu'est vraiment un agent (vs. un chatbot)

Avant de plonger dans le code, clarifions cette distinction. Un chatbot reçoit un input, appelle un modèle, retourne un output. Boucle simple.

Un agent a de l'*autonomie*. Il peut raisonner sur une tâche, décider quels outils utiliser, les appeler, évaluer les résultats et décider quoi faire ensuite — tout cela sans que vous écriviez une logique étape par étape pour chaque scénario. Vous lui donnez des outils et des instructions, et il s'occupe de l'orchestration.

Voyez-le ainsi : `IChatClient` c'est comme avoir une conversation. Un agent c'est comme déléguer une liste de tâches à quelqu'un.

## Votre premier agent en 10 lignes

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

La méthode d'extension `.AsAIAgent()` est le pont. Même pattern que `.AsIChatClient()` de MEAI — elle enveloppe le SDK du fournisseur dans une abstraction stable. Fonctionne avec Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry ou des modèles locaux.

Le streaming fonctionne aussi :

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Donner des outils à l'agent

C'est là que les agents cessent d'être des chatbots sophistiqués. Les outils sont des fonctions que le modèle peut décider d'appeler selon ce que l'utilisateur demande. Pas de logique de routage nécessaire — le modèle le détermine lui-même.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Deux choses à noter. Premièrement, `AIFunctionFactory` vient de MEAI — la même factory d'outils que vous utiliseriez avec un `IChatClient` normal. Si vous avez déjà défini des outils pour des scénarios de chat, ils fonctionnent ici aussi.

Deuxièmement, les attributs `Description` sont très importants. C'est comment le modèle comprend ce que fait un outil et quand l'utiliser. Traitez-les comme de la documentation pour votre IA, pas pour les humains.

## Sessions : Des conversations avec une vraie mémoire

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Sans session, chaque appel à `RunAsync` est sans état. Avec une session, l'agent sait à quelle blague vous faites référence. `AgentSession` préserve l'historique de conversation entre les tours.

Pour les services sans état en production, les sessions se sérialisent proprement :

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... stockez-le quelque part ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

C'est crucial si votre agent s'exécute dans un environnement serverless ou mis à l'échelle horizontalement.

## AIContextProvider : Mémoire persistante entre les sessions

Les sessions préservent l'historique *au sein* d'une session. Mais qu'en est-il de connaître des choses sur un utilisateur entre les sessions ? `AIContextProvider` gère cela.

Il a deux hooks :
- **`ProvideAIContextAsync`** — s'exécute *avant* chaque interaction, injecte du contexte dans l'agent
- **`StoreAIContextAsync`** — s'exécute *après* chaque interaction, permet d'apprendre et de persister

Le pattern est élégant : vous pouvez empiler plusieurs providers — un pour les préférences utilisateur, un pour les interactions récentes, un qui interroge votre store VectorData pour des documents pertinents. Ce dernier est exactement le pattern RAG de la Partie 2, s'exécutant maintenant automatiquement à chaque appel d'agent.

## Workflows multi-agents

C'est là que le framework mérite son nom. Il inclut un système de workflows basé sur des graphes où les executors (agents, fonctions, quoi que ce soit) se connectent via des arêtes.

Quelques patterns supportés nativement :

- **Séquentiel** : La sortie de l'Agent A alimente l'Agent B
- **Concurrent (fan-out/fan-in)** : Dispatch vers plusieurs agents en parallèle, collecte des résultats
- **Routage conditionnel** : Achemine le travail vers différents agents selon la sortie
- **Boucles écrivain-critique** : Un agent écrit, un autre évalue, boucle jusqu'à approbation
- **Sub-workflows** : Composition hiérarchique de workflows

Un exemple écrivain-critique :

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Propre, lisible, et le routage basé sur des conditions signifie que vous n'écrivez pas la logique de boucle vous-même.

## Human-in-the-Loop

Tout ne devrait pas s'exécuter de manière entièrement autonome. Pour les opérations sensibles — écritures en base de données, transactions financières, envoi de communications — vous voulez qu'un humain approuve avant que l'agent n'exécute.

Le framework a un support intégré pour cela via `FunctionApprovalRequestContent` et `FunctionApprovalResponseContent`. L'agent propose l'appel d'outil, votre code applicatif le présente à l'utilisateur, et la réponse détermine si l'exécution se poursuit.

C'est la bonne façon de penser aux agents dans les contextes d'entreprise : pas entièrement autonomes, mais *autonomie avec des garde-fous*.

## Vue d'ensemble

Si vous prenez du recul :

- **MEAI** vous donne une interface universelle vers n'importe quel modèle
- **VectorData** donne à vos agents accès à la connaissance de votre organisation via la recherche sémantique
- **Agent Framework** orchestre tout — utilise `IChatClient` en interne, se compose avec des context providers, et coordonne via des workflows

Chaque pièce a été conçue pour se composer avec les autres. Consultez le [post original de Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) et le [dépôt GitHub de l'Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) pour les exemples complets.

## Conclusion

Le post Partie 3 du Microsoft Agent Framework boucle la boucle de la série Building Blocks. Pour les développeurs .NET qui veulent construire des agents IA — pas seulement des chatbots, de vrais agents qui utilisent des outils, se souviennent de choses et coordonnent — c'est votre voie.

La version stable 1.0 signifie que vous pouvez construire avec cela en production. Si vous attendiez de vous lancer dans le développement d'agents en .NET, c'est le bon moment.
