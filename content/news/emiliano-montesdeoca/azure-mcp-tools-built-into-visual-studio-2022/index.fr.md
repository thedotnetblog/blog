---
title: "Les outils Azure MCP sont désormais intégrés dans Visual Studio 2022 — Aucune extension nécessaire"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Les outils Azure MCP sont livrés avec la charge de travail développement Azure dans Visual Studio 2022. Plus de 230 outils, 45 services Azure, zéro extension à installer."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}}).*

Si vous avez utilisé les outils Azure MCP dans Visual Studio via l'extension séparée, vous connaissez la chanson — installer le VSIX, redémarrer, espérer que rien ne casse, gérer les incompatibilités de versions. Cette friction, c'est terminé.

Yun Jung Choi a [annoncé](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) que les outils Azure MCP sont désormais livrés directement avec la charge de travail développement Azure dans Visual Studio 2022. Pas d'extension. Pas de VSIX. Pas de danse du redémarrage.

## Ce que ça signifie concrètement

À partir de Visual Studio 2022 version 17.14.30, le Azure MCP Server est inclus dans la charge de travail développement Azure. Si vous avez déjà cette charge de travail installée, il suffit de l'activer dans GitHub Copilot Chat et c'est parti.

Plus de 230 outils couvrant 45 services Azure — accessibles directement depuis la fenêtre de chat. Listez vos comptes de stockage, déployez une app ASP.NET Core, diagnostiquez des problèmes App Service, interrogez Log Analytics — le tout sans ouvrir un onglet de navigateur.

## Pourquoi c'est plus important qu'il n'y paraît

Voici le truc avec l'outillage développeur : chaque étape supplémentaire est de la friction, et la friction tue l'adoption. Avoir MCP en tant qu'extension séparée signifiait des incompatibilités de versions, des échecs d'installation, et une chose de plus à maintenir à jour. L'intégrer dans la charge de travail signifie :

- **Un seul chemin de mise à jour** via le Visual Studio Installer
- **Pas de décalage de version** entre l'extension et l'IDE
- **Toujours à jour** — le MCP Server se met à jour avec les releases régulières de VS

Pour les équipes qui standardisent sur Azure, c'est un vrai gain. Vous installez la charge de travail une fois, activez les outils, et ils sont disponibles à chaque session.

## Ce que vous pouvez faire avec

Les outils couvrent l'intégralité du cycle de développement via Copilot Chat :

- **Apprendre** — posez des questions sur les services Azure, les bonnes pratiques, les patterns d'architecture
- **Concevoir et développer** — obtenez des recommandations de services, configurez le code de votre application
- **Déployer** — provisionnez des ressources et déployez directement depuis l'IDE
- **Dépanner** — interrogez les logs, vérifiez l'état des ressources, diagnostiquez les problèmes en production

Un exemple rapide — tapez ceci dans Copilot Chat :

```
List my storage accounts in my current subscription.
```

Copilot appelle les outils Azure MCP en coulisses, interroge vos abonnements, et renvoie une liste formatée avec les noms, emplacements et SKUs. Pas besoin du portail.

## Comment l'activer

1. Mettez à jour vers Visual Studio 2022 **17.14.30** ou supérieur
2. Assurez-vous que la charge de travail **Azure development** est installée
3. Ouvrez GitHub Copilot Chat
4. Cliquez sur le bouton **Select tools** (l'icône des deux clés)
5. Activez **Azure MCP Server**

C'est tout. Ça reste activé entre les sessions.

## Un bémol

Les outils sont désactivés par défaut — vous devez les activer manuellement. Et les outils spécifiques à VS 2026 ne sont pas disponibles dans VS 2022. La disponibilité des outils dépend également des permissions de votre abonnement Azure, comme sur le portail.

## La vue d'ensemble

Cela fait partie d'une tendance claire : MCP est en train de devenir le standard pour exposer les outils cloud dans les IDEs de développement. Nous avons déjà vu la [release stable d'Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) et des intégrations MCP dans VS Code et d'autres éditeurs. L'intégrer dans le système de charges de travail de Visual Studio est la progression naturelle.

Pour nous développeurs .NET qui vivons dans Visual Studio, ça élimine encore une raison de basculer vers le portail Azure. Et honnêtement, moins on change d'onglet, mieux c'est.
