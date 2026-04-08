---
title: "Connectez vos serveurs MCP sur Azure Functions aux agents Foundry — Voici comment"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Construisez votre serveur MCP une fois, déployez-le sur Azure Functions et connectez-le aux agents Microsoft Foundry avec une authentification appropriée. Vos outils fonctionnent partout — VS Code, Cursor, et maintenant les agents IA d'entreprise."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}}).*

Voici ce que j'adore dans l'écosystème MCP : vous construisez votre serveur une fois, et il fonctionne partout. VS Code, Visual Studio, Cursor, ChatGPT — chaque client MCP peut découvrir et utiliser vos outils. Maintenant, Microsoft ajoute un autre consommateur à cette liste : les agents Foundry.

Lily Ma de l'équipe Azure SDK [a publié un guide pratique](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) sur la connexion de serveurs MCP déployés sur Azure Functions avec les agents Microsoft Foundry. Si vous avez déjà un serveur MCP, c'est de la valeur ajoutée pure — aucune reconstruction nécessaire.

## Pourquoi cette combinaison a du sens

Azure Functions vous offre une infrastructure évolutive, une authentification intégrée et une facturation serverless pour héberger des serveurs MCP. Microsoft Foundry vous offre des agents IA capables de raisonner, planifier et agir. Les connecter signifie que vos outils personnalisés — interroger une base de données, appeler une API métier, exécuter une logique de validation — deviennent des capacités que les agents IA d'entreprise peuvent découvrir et utiliser de manière autonome.

Le point clé : votre serveur MCP reste le même. Vous ajoutez simplement Foundry comme un autre consommateur. Les mêmes outils qui fonctionnent dans votre configuration VS Code alimentent maintenant un agent IA avec lequel votre équipe ou vos clients interagissent.

## Options d'authentification

C'est là que l'article apporte vraiment de la valeur. Quatre méthodes d'authentification selon votre scénario :

| Méthode | Cas d'usage |
|---------|------------|
| **Basée sur clé** (par défaut) | Développement ou serveurs sans auth Entra |
| **Microsoft Entra** | Production avec identités managées |
| **Passthrough d'identité OAuth** | Production où chaque utilisateur s'authentifie individuellement |
| **Sans authentification** | Dev/tests ou données publiques uniquement |

Pour la production, Microsoft Entra avec identité d'agent est le chemin recommandé. Le passthrough d'identité OAuth est pour les cas où le contexte utilisateur compte — l'agent demande aux utilisateurs de se connecter, et chaque requête porte le propre token de l'utilisateur.

## Mise en place

Le flux général :

1. **Déployez votre serveur MCP sur Azure Functions** — des exemples sont disponibles pour [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript et Java
2. **Activez l'authentification MCP intégrée** sur votre function app
3. **Obtenez votre URL d'endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Ajoutez le serveur MCP comme outil dans Foundry** — naviguez vers votre agent dans le portail, ajoutez un nouvel outil MCP, fournissez l'endpoint et les credentials

Testez ensuite dans le playground de l'Agent Builder en envoyant un prompt qui déclenchera l'un de vos outils.

## Mon avis

L'histoire de la composabilité devient vraiment solide ici. Construisez votre serveur MCP une fois en .NET (ou Python, TypeScript, Java), déployez-le sur Azure Functions, et chaque client compatible MCP peut l'utiliser — outils de programmation, apps de chat, et maintenant agents IA d'entreprise. C'est un pattern « écrire une fois, utiliser partout » qui fonctionne réellement.

Pour les développeurs .NET spécifiquement, l'[extension MCP Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) rend les choses simples. Vous définissez vos outils comme des Azure Functions, vous déployez, et vous avez un serveur MCP prêt pour la production avec toute la sécurité et la scalabilité qu'Azure Functions fournit.

## Pour conclure

Si vous avez des outils MCP qui tournent sur Azure Functions, les connecter aux agents Foundry est un gain rapide — vos outils personnalisés deviennent des capacités IA d'entreprise avec une authentification appropriée et sans modification de code côté serveur.

Lisez le [guide complet](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) pour des instructions pas à pas sur chaque méthode d'authentification, et consultez la [documentation détaillée](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) pour les configurations de production.
