---
title: "L’histoire de Foundry, de l’observabilité au ROI, est exactement ce qu’il faut aux plateformes d’agents sérieuses"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: "La dernière annonce Foundry sur l’observabilité compte parce qu’elle relie le tracing, l’évaluation, l’optimisation et le ROI dans une seule boucle opérationnelle pour les agents IA."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Observability
  - Evaluations
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Si les agents IA doivent vivre en production, l’observabilité ne peut pas s’arrêter aux logs et aux traces.

C’est pour cela que la nouvelle histoire de Foundry, de l’observabilité au ROI, paraît importante.

Le vrai message n’est pas « nous avons ajouté plus de tableaux de bord ».

Le vrai message est que les plateformes d’agents sérieuses ont besoin d’une boucle opérationnelle continue :

- tracer ce qui s’est passé
- évaluer si c’était bon
- optimiser ce qui doit être amélioré
- relier le résultat à la valeur métier

C’est une histoire bien plus solide que le discours flou habituel sur les plateformes.

## La phrase clé de l’article source dit tout

L’article d’origine commence par une phrase à laquelle je pense que toute équipe qui construit des agents devrait prêter attention :

> "Lancer un agent IA est la partie facile. Le garder précis, sûr et responsable en production est l’endroit où les équipes se bloquent."

C’est exactement vrai.

Nous avons déjà dépassé l’étape où la question principale était : « puis-je faire faire quelque chose de cool à un agent ? »

La question la plus difficile et la plus utile est :

**puis-je exploiter la chose une fois qu’elle commence à interagir avec de vrais utilisateurs, de vrais outils et de vrais coûts ?**

C’est là que Foundry essaie de faire avancer la conversation.

## Pourquoi c’est plus important qu’une autre démo d’agent

Beaucoup d’annonces d’agents IA se concentrent encore sur la création : construire l’agent, brancher les outils, router les tâches, publier l’interface.

Tout cela est très bien.

Mais les questions opérationnelles sont ce qui permet à la plupart des systèmes sérieux de devenir durables ou de devenir des expériences coûteuses :

- que fait réellement l’agent en production ?
- a-t-il fait la bonne chose ?
- se dégrade-t-il avec le temps ?
- est-il trop coûteux par rapport à la valeur qu’il crée ?
- quels changements de configuration ont réellement amélioré la qualité ?

C’est pourquoi je pense que l’annonce Foundry est plus importante qu’un simple récapitulatif de fonctionnalités. Elle essaie de définir une boucle d’Agent DevOps, pas seulement une histoire de création d’agent.

## La boucle en quatre parties est le vrai produit ici

L’article organise essentiellement la plateforme autour de quatre capacités :

- Trace
- Evaluate
- Monitor
- Optimize

C’est la bonne forme.

Je dirais même que toute plateforme qui veut être prise au sérieux pour des charges de travail d’agents en production finira par avoir besoin des quatre.

Le tracing seul ne suffit pas.

L’évaluation seule ne suffit pas.

L’optimisation sans preuves n’est qu’une supposition.

Et parler de ROI sans télémétrie relève généralement du théâtre.

## L’angle d’interopérabilité est particulièrement intelligent

L’une des décisions les plus fortes de l’annonce est que Foundry ne prétend pas que chaque agent sera construit dans un seul framework.

L’article source parle explicitement d’étendre le tracing et les évaluations à :

- LangChain
- LangGraph
- OpenAI SDK
- Microsoft Agent Framework
- des frameworks personnalisés via OpenTelemetry

C’est important.

Parce que le verrouillage de plateforme est l’un des moyens les plus rapides de rendre moins attrayante une histoire d’exploitation qui était pourtant utile.

Si les équipes peuvent conserver leurs choix de frameworks tout en bénéficiant de la télémétrie et des surfaces d’évaluation de niveau production, la friction diminue considérablement.

## L’évaluation par grille pourrait finir par compter plus que les gens ne l’imaginent

La partie évaluation par grille mérite aussi d’être mentionnée.

Je pense que c’est l’un des ajouts les plus pratiques de tout l’article.

Pourquoi ? Parce que le « bon » dépend du contexte.

L’article dit que l’évaluation par grille génère des « critères d’évaluation sensibles au contexte à partir du comportement prévu de votre agent ». C’est exactement la direction dont ces systèmes ont besoin.

Le scoring de qualité générique est utile.

Mais à terme, les équipes doivent évaluer les agents selon leurs propres standards :

- ton
- exécution des tâches
- respect des politiques
- attentes de latence
- limites de coût
- règles métier spécifiques au domaine

C’est là que l’évaluation devient opérationnellement significative plutôt qu’uniquement intéressante sur le plan académique.

## Le ROI est la partie la plus inconfortable, et c’est pour cela qu’elle compte

Je pense aussi que la partie ROI de l’annonce est importante précisément parce qu’elle est inconfortable.

L’article pose directement la question :

> "cet agent vaut-il ce qu’il coûte ?"

Cette question est souvent éludée dans les discussions sur l’IA.

Mais c’est la bonne question.

Si la plateforme peut vraiment relier le coût, l’exécution des tâches, le temps gagné et les traces de production en un seul endroit, cela donne à l’ingénierie et au leadership un langage commun bien meilleur.

Et franchement, ce langage commun est cruellement nécessaire.

## Mon avis

C’est l’une des meilleures annonces au niveau plateforme de cette série, parce qu’elle se concentre sur l’exploitation des agents, pas seulement sur leur création.

Et c’est là que le vrai travail difficile commence.

Les plateformes IA les plus solides des deux prochaines années ne seront pas seulement celles qui donnent accès à plus de modèles ou à plus de démonstrations. Ce seront celles qui aident les équipes à tracer le comportement, évaluer les résultats, optimiser en sécurité et justifier les coûts avec des preuves.

Cette histoire Foundry essaie d’aller exactement dans cette direction.

C’est pour cela qu’elle mérite d’être prise au sérieux.

Article original : [Build 2026: From observability to ROI for AI agents on any framework](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)