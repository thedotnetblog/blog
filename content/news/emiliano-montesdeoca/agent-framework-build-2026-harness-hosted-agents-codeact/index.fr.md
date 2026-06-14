---
title: "Agent Harness, Hosted Agents et CodeAct : voilà la mise à jour d'Agent Framework sur laquelle je me concentrerais"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "L'annonce d'Agent Framework à Build 2026 est dense, mais les fils les plus importants sont le modèle de harness, les agents hébergés par Foundry et CodeAct pour réduire la surcharge d'orchestration."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

La grande annonce Agent Framework à Build couvre beaucoup de choses, mais trois thèmes me sautent immédiatement aux yeux :

- **le fait que le harness devienne une pièce de runtime plus centrale**
- **les agents hébergés dans Foundry qui offrent une voie vers la production**
- **CodeAct qui réduit la surcharge d'orchestration en plusieurs étapes**

Ce sont les éléments que je garderais à l'œil.

## Le harness devient le véritable centre de gravité

Le post source décrit le harness comme la couche où le raisonnement du modèle rencontre l'exécution réelle.

C'est la bonne description, et c'est aussi pour cela que je pense que cette partie compte plus que beaucoup de fonctionnalités prises isolément.

Dès qu'un agent a besoin de :

- accès aux fichiers
- exécution de shell
- modes de planification
- tâches à faire
- mémoire de session
- flux d'approbation

vous ne parlez plus seulement d'un prompt et d'un modèle.

Vous parlez du comportement d'exécution.

C'est là que les frameworks deviennent vraiment utiles ou qu'ils restent des jouets.

Et Microsoft Agent Framework essaie clairement de devenir plus utile exactement à cette couche.

## Les agents hébergés sont l'endroit où l'histoire du local vers la production devient concrète

Je pense aussi que la partie hosted agents est l'un des volets les plus stratégiques de l'annonce.

Le post source dit explicitement que c'est la façon la plus simple de donner à cet agent un foyer en production.

Cette formule compte, parce que la plupart des frameworks d'agents sont encore bien plus solides pour l'expérimentation locale que pour le déploiement opérationnel.

Si les agents hébergés de Foundry rendent le passage du développement local vers :

- la montée en charge
- l'observabilité
- l'identité managée
- la gestion de session
- le versionnage

beaucoup plus simple, alors cela comble l'un des plus grands écarts de l'écosystème actuel des agents.

C'est une amélioration importante.

## CodeAct est l'idée technique la plus enthousiasmante de la mise à jour

Si je devais choisir le concept technique le plus intéressant du billet, je choisirais probablement CodeAct.

Le problème qu'il essaie de résoudre est très réel : trop de workflows d'agents en plusieurs étapes coûtent cher, parce que la boucle d'orchestration elle-même consomme trop de tours de modèle.

Donc, quand le post source affiche un résultat comme :

- 52.4% plus rapide
- 63.9% de tokens en moins

cela attire immédiatement mon attention.

Bien sûr, ce sont des chiffres de benchmark liés à une charge de travail représentative, pas une loi universelle. Mais l'idée générale reste très convaincante.

Si le modèle peut compresser une chaîne d'appels d'outils en une forme d'exécution plus efficace, l'économie des systèmes d'agents peut changer sensiblement.

## Ce que je pense que les développeurs devraient réellement retenir de cette mise à jour

La leçon importante n'est pas le nombre de fonctionnalités livrées.

La leçon, c'est que le framework se renforce là où les applications réelles en ont le plus besoin :

- runtime
- chemin de déploiement
- efficacité d'exécution
- patterns opérationnels intégrés

C'est le genre de signal de maturité qui m'importe bien plus qu'une autre liste superficielle de fonctionnalités IA.

## Mon avis

Cette mise à jour compte parce qu'elle n'ajoute pas seulement davantage de surface.

Elle renforce l'histoire du runtime et du déploiement autour des agents d'une manière qui devrait compter pour les applications réelles, surtout pour les équipes qui veulent passer des expérimentations locales à des systèmes qu'elles peuvent vraiment exécuter et maintenir.

C'est là que le framework devient plus convaincant.

Et si je suivais cette version de près, le harness, les agents hébergés et CodeAct seraient clairement les trois axes sur lesquels je concentrerais le plus mon attention.

Article original : [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
