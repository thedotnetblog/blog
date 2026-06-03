---
title: "NL2SQL est l'injection SQL de l'ère agentique"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Avant de laisser un agent interroger votre base de données en langage naturel, lisez ceci. NL2SQL semble simple jusqu'à ce que vous réfléchissiez à la complétude du schéma, à l'indéterminisme et à ce que SQL MCP Server résout vraiment."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Il existe une version du discours NL2SQL qui semble parfaite : les utilisateurs posent des questions en langage naturel, les agents génèrent du SQL, les données reviennent. Moins d'écrans, moins de requêtes, moins de code. Simple.

Puis vous y réfléchissez cinq minutes de plus.

## Les problèmes dont personne ne parle dans la démo

**Les schémas n'ont pas été conçus pour expliquer les choses.** Noms de tables cryptiques, noms de colonnes incohérents, relations techniquement valides mais sémantiquement invalides sans prédicats supplémentaires — c'est normal dans les bases de données d'entreprise. Ce ne sont pas des bugs, c'est simplement l'histoire accumulée des changements métier. Mais quand vous demandez à un modèle d'inférer l'intention d'un schéma qui n'a pas été conçu pour communiquer l'intention, le modèle essaiera quand même. Il ne s'arrêtera pas. Il générera sa meilleure requête et retournera des résultats avec assurance.

**Les modèles ne sont pas déterministes.** Posez la même question sur la même base de données deux fois et vous pourriez obtenir du SQL différent. Le modèle calcule des probabilités, et de légères variations de contexte produisent des sorties différentes. Vous ne pouvez pas tester votre chemin vers une garantie que l'agent génère toujours la bonne requête.

**La révision par l'utilisateur ne passe pas à l'échelle.** "Vérifiez simplement chaque requête avant l'exécution" semble sûr. Mais cela suppose que les utilisateurs sont des experts à la fois dans le modèle de données et en SQL — exactement les personnes qui n'avaient pas besoin de l'interface en langage naturel. Cela introduit également une surcharge cognitive et une nouvelle classe de biais de confirmation, où les utilisateurs submergés par la complexité des requêtes approuvent des requêtes invalides plutôt que de les investiguer.

**Et puis il y a l'injection.** Dans le développement SQL traditionnel, la paramétrisation a résolu l'injection parce que la saisie utilisateur remplissait des paramètres, pas la structure SQL. Avec NL2SQL, le modèle génère le SQL lui-même. Le prompt, le contexte du schéma, l'historique de conversation et les données récupérées influencent tous ce qui est exécuté. Si quelqu'un élabore un prompt qui change ce que le modèle génère, c'est de l'injection — pas au niveau des paramètres, mais au niveau de la génération des requêtes. Et contrairement à la suppression d'une table (évident, récupérable), l'injection NL2SQL produit des requêtes qui retournent des résultats incorrects sans aucune erreur visible. Des décisions métier sont prises sur de mauvaises données.

## Ce que SQL MCP Server résout réellement

C'est là que l'article fait son point pratique le plus utile. Plutôt que de donner à un agent un accès arbitraire au schéma et d'espérer le meilleur, SQL MCP Server expose une **surface API organisée** construite sur [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

La différence est importante : l'agent ne génère pas de SQL. Il appelle des endpoints nommés qui retournent des formes de résultat prédéfinies. Le SQL est écrit une fois, par un développeur, et est déterministe. Le non-déterminisme de l'agent se limite à choisir *quel* endpoint appeler, pas à construire des requêtes arbitraires.

C'est analogue à ce que la paramétrisation a fait pour l'injection SQL dans le modèle d'application traditionnel — vous supprimez la capacité de construire des requêtes arbitraires à partir d'entrées non fiables.

## La bonne question

L'article ne dit pas "n'utilisez jamais NL2SQL." Il dit : soyez délibéré sur *où* vous l'appliquez et *ce que* vous exposez. Pour une analyse exploratoire dans un environnement contrôlé, avec un schéma limité et un accès en lecture seule, NL2SQL pourrait convenir. Pour les systèmes de production où les décisions métier dépendent des résultats, une couche API organisée est significativement plus sûre.

Honnêteté : certains problèmes sont vraiment mieux résolus avec des requêtes structurées derrière des endpoints nommés qu'avec du langage naturel vers SQL. SQL MCP Server vous donne cette option sans abandonner entièrement l'interface agentique.

Publication originale : [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
