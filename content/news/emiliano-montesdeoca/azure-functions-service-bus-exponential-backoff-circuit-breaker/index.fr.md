---
title: "Arrêtez de Pilonner une Dépendance en Difficulté : Patterns de Retry pour Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "L'exponential backoff et les patterns de circuit breaker sont désormais pris en charge nativement pour les Azure Functions déclenchées par Service Bus — voici comment ils fonctionnent et pourquoi vous avez besoin des deux."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Voici comment une panne récupérable devient une interruption dans une application Functions : une dépendance commence à générer des timeouts, chaque instance Function effectue des nouvelles tentatives immédiatement et indéfiniment, la dépendance reçoit des centaines de requêtes concurrentes échouées, et ce qui a commencé comme un problème transitoire se transforme en un événement de contre-pression à l'échelle du système.

Vous connaissez probablement cette histoire. Azure Functions scale rapidement — c'est tout le principe. Mais "scaler rapidement" et "réessayer immédiatement" ensemble peuvent rendre les défaillances dramatiquement pires.

Deux patterns aident. Exponential backoff et circuit breaker. Les deux sont désormais pris en charge nativement pour les Azure Functions déclenchées par Service Bus.

## Deux Patterns, Rôles Différents

Ces patterns sont complémentaires, pas des alternatives :

**L'exponential backoff** répond à : *quand devrais-je réessayer ?*
Il augmente le délai entre les tentatives pour qu'une dépendance ait le temps de récupérer. Au niveau du message, rythmant le timing des nouvelles tentatives.

**Le circuit breaker** répond à : *devrais-je appeler cette dépendance en ce moment ?*
Il arrête les appels répétés vers une dépendance non saine après qu'un seuil d'échec est atteint, puis sonde prudemment après une période de refroidissement. Au niveau du système, prévenant les tempêtes de retry.

Vous voulez les deux. Le backoff gère le rythme des tentatives par message. Le circuit breaker gère les décisions de santé agrégées.

## Pourquoi C'est Particulièrement Important pour Service Bus

La file absorbe le trafic en rafale, ce qui est bien. Mais sans contrôles, la file peut grossir pendant que les workers continuent de gaspiller des ressources de calcul sur des appels qui vont échouer. Les messages empoisonnés restent actifs plus longtemps qu'ils ne le devraient. Les partitions chaudes ou la capacité limitée en aval créent des problèmes en cascade.

Le design plus sécurisé :

1. Détecter la panne transitoire
2. Retarder la prochaine tentative avec exponential backoff
3. Arrêter d'appeler la dépendance quand un seuil d'échec est atteint (circuit ouvert)
4. Reprendre prudemment après une période de refroidissement (sonde de circuit)
5. Déplacer le travail irrécupérable vers dead-letter ou une voie de quarantaine

## À Quoi Ressemble le Support Natif

Le nouveau support s'intègre avec le modèle d'hôte Azure Functions existant — pas de bibliothèques supplémentaires, pas d'implémentations personnalisées. La configuration va dans votre `host.json` :

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

La configuration du circuit breaker définit le seuil d'échec et l'intervalle de réinitialisation pour que les dépendances non saines ne soient pas harcelées pendant la récupération.

## Langages Couverts

Ce n'est pas uniquement pour .NET. La fonctionnalité couvre dotnet, JavaScript, TypeScript et Python — l'ensemble complet des langages supportés par le trigger Service Bus dans Azure Functions.

## Conclusion

Les patterns de retry ne sont pas passionnants à configurer jusqu'à la première fois qu'une interruption en aval fait que vos Functions aggravent le problème au lieu de se dégrader gracieusement. Les configurer de manière proactive est peu coûteux. Les implémenter pendant un incident ne l'est pas.

Post original : [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
