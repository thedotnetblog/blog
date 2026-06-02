---
title: "Microsoft Foundry Avril 2026 : Foundry Local GA, GPT-5.5, CodeAct avec Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Le récapitulatif Foundry d'avril est chargé : Foundry Local atteint la GA, GPT-5.5 arrive, Agent Framework reçoit le traçage OpenTelemetry, CodeAct exécute Python dans des micro-VMs Hyperlight, et le tableau de bord de surveillance des agents est disponible."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Un mois chargé pour Microsoft Foundry. Voici les annonces les plus importantes.

## Foundry Local est Généralement Disponible

Foundry Local — le runtime d'IA local multiplateforme de Microsoft — passe de la préversion à la GA sur Windows, macOS (Apple Silicon) et Linux x64. Inférence de modèles locaux prête pour la production avec un SDK convivial pour les développeurs. La version 1.1 ajoute la transcription, les embeddings et la prise en charge de l'API Responses.

## GPT-5.5

Le dernier modèle de la famille GPT-5 est maintenant disponible dans Foundry. Quota par défaut pour les abonnements Tier 5 et Tier 6. Si vous avez travaillé avec des variantes antérieures de GPT-5, cela vaut la peine d'être évalué pour vos cas d'utilisation.

## Traçage d'Agent Framework dans Foundry

Deux fonctionnalités de traçage sont disponibles en préversion ce mois-ci :

**Traçage de Microsoft Agent Framework** — Les agents MAF peuvent maintenant émettre des traces OpenTelemetry dans Foundry. Déboguez le comportement des agents, tracez l'exécution en plusieurs étapes, exposez la latence et les erreurs dans les appels d'outils. Cela comble un vrai manque : savoir *ce que votre agent a réellement fait* en production, pas seulement ce qu'il a retourné.

**Traçage des agents hébergés** — Les sessions, appels d'outils et étapes d'exécution des agents hébergés apparaissent également dans les traces Foundry. La même histoire d'observabilité étendue au niveau hébergé.

## CodeAct avec Hyperlight (Alpha)

C'est l'ajout techniquement le plus intéressant : Agent Framework peut désormais exécuter du code Python dans des micro-machines virtuelles [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct est le modèle où un agent génère et exécute du code Python comme outil. La préoccupation évidente est la sécurité — vous exécutez du code généré par le modèle. Les micro-VMs d'Hyperlight fournissent une isolation au niveau du processus avec un temps de démarrage proche du natif, rendant l'exécution de code en sandbox pratique sans la surcharge de conteneurs ou de VMs complets.

Pour les flux de travail agentiques où l'exécution de code est nécessaire, c'est une amélioration de sécurité significative par rapport à l'exécution de code dans le processus hôte.

## Tableau de Bord de Surveillance des Agents (Préversion)

Un tableau de bord d'opérations unifié combinant l'utilisation des tokens, la latence, le taux de succès des exécutions et les scores des évaluateurs en une seule vue. La distinction par rapport aux tableaux de bord d'observabilité classiques : il inclut les résultats d'évaluation aux côtés des métriques opérationnelles, vous permettant de corréler « l'agent est plus lent » avec « les scores de l'évaluateur ont chuté » — ou de confirmer qu'ils ne sont pas liés.

## Évaluateurs Personnalisés d'Évaluation Continue (Préversion)

Vous pouvez maintenant apporter vos propres évaluateurs basés sur du code ou des prompts dans les pipelines d'évaluation continue. Auparavant, l'évaluation continue était limitée aux évaluateurs intégrés. Les évaluateurs personnalisés vous permettent d'appliquer des critères de qualité spécifiques à votre équipe dans votre boucle de surveillance en production.

## Inventaire des Agents dans le Plan de Contrôle

La vue Operate du Plan de Contrôle Foundry affiche désormais tous les agents pris en charge dans un abonnement : agents Foundry, Azure SRE Agent, boucles d'agents Logic Apps et agents personnalisés enregistrés. Une vue pour comprendre ce qui est déployé et où.

Publication originale : [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
