---
title: "Azure DevOps corrige enfin l'éditeur Markdown dont tout le monde se plaignait"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'éditeur Markdown d'Azure DevOps pour les work items obtient une distinction plus claire entre mode aperçu et édition. Un petit changement qui résout un problème de workflow vraiment agaçant."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azure-devops-markdown-editor-work-items.md" >}}).*

Si vous utilisez Azure Boards, vous avez probablement vécu ça : vous lisez la description d'un work item, peut-être en vérifiant les critères d'acceptation, et vous double-cliquez accidentellement. Boom — vous êtes en mode édition. Vous ne vouliez rien modifier. Vous étiez en train de lire.

Dan Hellem [a annoncé le correctif](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), et c'est un de ces changements qui semblent petits mais qui éliminent une vraie friction de votre workflow quotidien.

## Ce qui a changé

L'éditeur Markdown pour les champs texte des work items s'ouvre désormais en **mode aperçu par défaut**. Vous pouvez lire et interagir avec le contenu — suivre les liens, vérifier le formatage — sans risquer d'entrer accidentellement en mode édition.

Quand vous voulez vraiment éditer, vous cliquez sur l'icône d'édition en haut du champ. Quand vous avez terminé, vous revenez explicitement au mode aperçu. Simple, intentionnel, prévisible.

## Pourquoi c'est plus important qu'il n'y paraît

Le [fil de feedback communautaire](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) était long. Le comportement de double-clic pour éditer a été introduit avec l'éditeur Markdown en juillet 2025, et les plaintes ont commencé presque immédiatement.

Pour les équipes qui font du sprint planning, du refinement ou du code review avec Azure Boards, ce type de micro-friction s'accumule.

## État du déploiement

Ce changement est déjà en cours de déploiement pour un sous-ensemble de clients et s'étendra à tous dans les deux à trois prochaines semaines.

## Pour conclure

Toute amélioration n'a pas besoin d'être une fonctionnalité phare. Parfois la meilleure mise à jour consiste simplement à supprimer quelque chose d'agaçant. C'est exactement ça — un petit correctif UX qui rend Azure Boards moins hostile pour les gens qui veulent juste lire leurs work items tranquillement.
