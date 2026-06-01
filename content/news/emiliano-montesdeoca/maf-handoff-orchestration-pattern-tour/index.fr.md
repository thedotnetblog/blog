---
title: "Le Modèle Handoff : Quand Un Agent Ne Suffit Pas"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Le modèle d'orchestration Handoff de Microsoft Agent Framework permet aux agents de décider qui gère le prochain tour — sans perdre le contexte de la conversation ni enfreindre les règles de topologie."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

À un moment donné, tout système multi-agents dépasse un simple routeur. Le premier signe apparaît généralement quand un agent spécialiste doit poser une question de suivi, ou réalise en milieu de tour qu'un autre agent devrait continuer. Un pipeline fixe échoue là. Un routeur à passage unique échoue là.

C'est exactement le problème que le modèle d'orchestration Handoff dans Microsoft Agent Framework est conçu pour résoudre.

## Comment Fonctionne Handoff

Le développeur déclare un graphe : voici les agents, voici les arêtes entre eux. Le framework fait le reste — il synthétise un outil handoff par arête sortante et l'injecte dans chaque agent. Quand un agent décide de passer le contrôle, il appelle l'outil. Le framework applique la topologie.

Trois choses rendent cela différent du fait d'avoir simplement des agents qui s'appellent mutuellement :

1. **Une transcription partagée** — l'agent récepteur voit l'intégralité de l'historique de conversation. Pas de recommencement à zéro.
2. **Application de la topologie** — un agent ne peut faire handoff qu'à des cibles déclarées. Vous détectez les bugs de routage au moment de l'authoring, pas en production.
3. **Terminaison naturelle** — quand l'agent actif termine son tour sans appeler un outil handoff, le workflow cède à l'utilisateur. Pas de polling, pas de conditions de sortie explicites.

## Un Exemple Minimal

En .NET, construire un workflow handoff ressemble à ceci :

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage peut envoyer à l'un ou l'autre spécialiste. Les deux spécialistes peuvent renvoyer vers triage. Le graphe est compatible avec l'acyclique mais prend en charge les arêtes arrière quand vous en avez besoin ("j'ai besoin de plus d'informations" → retour à la recherche).

## Quand Utiliser Handoff (et Quand Ne Pas Le Faire)

Handoff est un bon choix quand :

- **La propriété peut changer en cours de conversation** — un agent peut réaliser qu'il est le mauvais spécialiste
- **Les arêtes arrière comptent** — vous pourriez avoir besoin de revisiter une étape antérieure sans repartir à zéro
- **Les décisions de routage sont floues** — la décision de faire un handoff est contextuelle et mieux prise par le modèle que par des prédicats typés

Ce n'est *pas* le bon choix quand :

- Votre pipeline est fixe et séquentiel — utilisez le workflow `Sequential` pour cela
- Chaque étape est indépendante — des agents partageant une transcription où seul l'un d'eux en avait besoin n'est que du bruit
- Vous avez besoin de garanties strictes de traitement — le non-déterminisme du routage piloté par modèle n'est pas ce que vous voulez

## Arêtes Arrière et Humain-dans-la-Boucle

L'une des formes les plus intéressantes qu'Handoff permet est les vraies arêtes arrière. Un agent peut décider "je n'ai pas assez d'informations" et revenir à une étape de recherche, pas avec une boucle codée en dur, mais parce que le modèle décide que c'est la bonne décision.

Les interactions humain-dans-la-boucle se composent également naturellement. Quand un spécialiste a besoin d'une entrée de l'utilisateur, le workflow cède à l'utilisateur via la boucle de tour par défaut, recueille la réponse et reprend avec le contexte complet. L'agent n'a jamais perdu la conversation.

## Conclusion

Handoff est l'un de ces modèles qui semble simple mais permet beaucoup une fois intégré : routage décentralisé, contexte partagé, topologie appliquée, terminaison naturelle. C'est la prochaine étape appropriée quand vos agents commencent à dire "en fait, quelqu'un d'autre devrait gérer ça."

Lisez le guide complet dans le post original : [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
