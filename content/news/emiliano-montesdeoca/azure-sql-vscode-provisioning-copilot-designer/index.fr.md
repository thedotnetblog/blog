---
title: "L'extension MSSQL pour VS Code devient discrètement une plateforme beaucoup plus vaste"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "La dernière mise à jour de l'extension MSSQL ajoute le provisioning Azure SQL, la conception de schémas assistée par Copilot, Data API Builder et des notebooks. Le plus intéressant, c'est la quantité de travail de base de données qui peut désormais rester dans VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

L'extension MSSQL pour VS Code grandit depuis un moment, mais cette dernière mise à jour rend la direction beaucoup plus claire.

Ce n'est plus seulement « se connecter et exécuter quelques requêtes ».

Avec le **provisioning Azure SQL**, **Schema Designer avec Copilot**, les **SQL Notebooks** et **Data API Builder** tous poussés dans un seul release, l'extension devient un espace de travail beaucoup plus complet pour le développement centré sur les bases de données.

## L'accroche pratique, c'est le provisioning directement depuis l'éditeur

L'article source dit qu'on peut désormais créer une base de données cloud entièrement gérée « directement depuis votre éditeur et sans coût » en utilisant le niveau gratuit.

C'est le genre de fonctionnalité qui paraît petite jusqu'à ce qu'on réalise combien de friction de configuration elle supprime.

Pour beaucoup de développeurs, la partie agaçante des expérimentations lourdes en données n'est pas SQL en soi. C'est le fossé d'environnement entre :

- l'idée
- la base de données
- le schéma
- l'API
- un backend testable

Si ce fossé se réduit dans un seul outil, tout le workflow devient plus attrayant.

## Voilà à quoi ressemble un inner loop plus fort pour le travail sur les données

Ce que j'aime dans cette version, c'est qu'elle garde davantage du workflow base de données au même endroit :

- provisionner la base de données
- concevoir le schéma
- revoir les changements
- générer des scripts ORM
- exposer des APIs
- tester les endpoints
- documenter et interroger via des notebooks

C'est une histoire bien plus convaincante que de traiter SQL comme un outil annexe déconnecté dans la stack.

## Le workflow de schéma assisté par Copilot, c'est là que la valeur IA devient réelle

Les ajouts du concepteur de schémas sont particulièrement intéressants, parce qu'ils semblent trouver un bon équilibre.

La valeur n'est pas « l'IA conçoit votre modèle de données et vous lui faites confiance aveuglément ».

La valeur, c'est :

- des points de départ plus rapides
- une revue visuelle
- le suivi des changements
- une sortie orientée migration
- des contrôles explicites accepter/annuler

C'est un workflow IA bien plus sain qu'une génération automatique complète sans chemin d'inspection.

Et pour le travail sur les bases de données, la capacité de revue compte énormément.

## Data API Builder est un multiplicateur discret

L'autre fonctionnalité que je n'ignorerais pas est l'intégration de Data API Builder.

Si vous pouvez passer du schéma à :

- REST
- GraphQL
- des endpoints MCP

dans le même environnement, cela crée une voie très efficace pour les prototypes backend et les outils internes.

Cela ne remplace pas une ingénierie backend plus profonde. Mais cela raccourcit clairement le chemin entre une idée de base de données et une interface fonctionnelle.

## Mon avis

Cette version fait ressembler l'extension MSSQL à une petite plateforme dans VS Code plutôt qu'à un simple add-on.

Pour les développeurs qui construisent des APIs, des outils de données, des outils d'administration ou des prototypes basés sur SQL, c'est une évolution significative.

Et si Microsoft continue à resserrer cette boucle, l'extension deviendra beaucoup plus stratégique que beaucoup de gens ne le pensent encore.

Article original : [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)