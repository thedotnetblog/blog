---
title: "SQL MCP Server sur Azure App Service — Sans Conteneurs"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Le SQL MCP Server peut désormais s'exécuter sur Azure App Service sans Docker ni Kubernetes. Voici ce que cela signifie pour les développeurs .NET qui construisent des agents IA communiquant avec des bases de données SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Soyons honnêtes : chaque fois que je lis "nécessite un conteneur" dans un tutoriel, une petite partie de moi soupire. Les conteneurs sont formidables — jusqu'à ce que ton équipe n'ait pas de stratégie de conteneurs, et soudain une fonctionnalité qui semblait simple se retrouve bloquée par une complexité d'orchestration que personne n'avait anticipée.

C'est pourquoi celui-ci a retenu mon attention. Le SQL MCP Server peut désormais s'exécuter sur Azure App Service — sans Docker, sans Kubernetes, juste avec la même configuration Data API Builder (DAB) qui expose ta base de données SQL via MCP, REST et GraphQL.

## Qu'est-ce que le SQL MCP Server ?

Contexte rapide si tu ne le connais pas encore. Le SQL MCP Server se place entre ton agent IA et ta base de données SQL. Au lieu de donner à ton agent un accès direct à la base de données (une très mauvaise idée), il expose tes tables et vues comme une couche d'abstraction — des entités avec des permissions définies.

Il est construit sur [Data API Builder](https://learn.microsoft.com/fr-fr/azure/data-api-builder/), ce qui signifie qu'un seul fichier de configuration gère MCP *et* REST *et* GraphQL simultanément. Ton agent parle à l'endpoint MCP. Ton application traditionnelle parle à REST ou GraphQL. Même config, même runtime, surfaces différentes.

C'est vraiment utile. Tu ne maintiens pas deux couches d'API séparées.

## Le Problème des Conteneurs (et la Solution)

Le modèle de déploiement original du SQL MCP Server utilisait des conteneurs. Cela fonctionne bien dans beaucoup d'équipes — mais pas toutes. De nombreuses équipes .NET standardisent sur Azure App Service ou des VMs. Exiger un runtime de conteneur juste pour exposer un endpoint SQL ajoute de la friction que personne n'a demandée.

Le nouveau guide montre comment contourner entièrement le conteneur. Tout fonctionne avec une commande `dab start`, hébergé sur App Service comme un processus web .NET 8 standard.

```bash
# Installer Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Initialiser la configuration
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Ajouter une entité
dab add products --source dbo.products --permissions "authenticated:*"

# Configurer le fournisseur d'auth App Service
dab configure --runtime.host.authentication.provider AppService

# Démarrer le serveur
dab start
```

À ce stade, tu as MCP à `/mcp`, REST et GraphQL depuis le même processus, et rien qui tourne dans un conteneur.

## Authentification Sans Clés d'API Partagées

C'est la partie que j'apprécie le plus. Quand tu déploies sur App Service, tu configures Microsoft Entra ID comme fournisseur d'authentification. Pas de secrets partagés dans les fichiers de configuration, pas de clés d'API à faire tourner.

La chaîne de connexion reste dans une variable d'environnement App Service (pas dans `dab-config.json`), et l'endpoint MCP est protégé par l'authentification de la plateforme. Si tu es déjà aligné sur Entra ID pour tes charges de travail Azure, cela s'intègre naturellement.

Pour le développement local, tu passes en mode `Simulator` et transport STDIO. Tu reviens en mode `AppService` avant le déploiement. Propre et explicite.

## Déploiement sur App Service

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Ensuite tu déploies ton projet DAB en utilisant la méthode de déploiement de code que ton équipe utilise déjà. Le détail clé : c'est un déploiement de **code**, pas de conteneur.

## Pourquoi C'est Important pour les Développeurs .NET

Si tu construis des agents IA en .NET, ton agent devra tôt ou tard communiquer avec une base de données. Le SQL MCP Server te donne une façon structurée de le faire sans exposer des chaînes de connexion brutes.

Consulte le guide complet dans le [billet original](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) et le [dépôt d'exemple sur GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusion

Le SQL MCP Server sur App Service est une option pragmatique solide pour les équipes .NET qui souhaitent donner à leurs agents un accès structuré aux données SQL sans stratégie de conteneurs. Essaie-le — tes agents apprécieront la surface d'API propre.
