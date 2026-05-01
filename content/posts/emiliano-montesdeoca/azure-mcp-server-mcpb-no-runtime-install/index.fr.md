---
title: "Azure MCP Server Est Maintenant un .mcpb — Installez-le sans Aucun Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server est maintenant disponible en tant que MCP Bundle (.mcpb) — téléchargez-le, faites-le glisser dans Claude Desktop et c'est tout. Aucun Node.js, Python ou .NET requis."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Vous savez ce qui était pénible dans la configuration des serveurs MCP ? Vous aviez besoin d'un runtime. Node.js pour la version npm, Python pour pip/uvx, .NET SDK pour la variante dotnet.

L'[Azure MCP Server vient de changer cela](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Il est maintenant disponible en tant que `.mcpb` — un MCP Bundle — et la configuration se fait par glisser-déposer.

## Qu'est-ce qu'un MCP Bundle ?

Pensez-y comme à une extension VS Code (`.vsix`) ou une extension de navigateur (`.crx`), mais pour les serveurs MCP. Un fichier `.mcpb` est une archive ZIP autonome incluant le binaire du serveur et toutes ses dépendances.

## Comment l'installer

**1. Téléchargez le bundle pour votre plateforme**

Allez sur la [page GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) et téléchargez le fichier `.mcpb` pour votre OS et architecture.

**2. Installez dans Claude Desktop**

Le plus simple : faites glisser le fichier `.mcpb` dans la fenêtre Claude Desktop sur la page des paramètres Extensions (`☰ → Fichier → Paramètres → Extensions`). Vérifiez les détails du serveur, cliquez sur Installer, confirmez.

**3. Authentifiez-vous auprès d'Azure**

```bash
az login
```

C'est tout. Azure MCP Server utilise vos identifiants Azure existants.

## Ce que vous pouvez faire avec

Plus de 100 outils de services Azure directement depuis votre client IA :
- Interroger et gérer Cosmos DB, Storage, Key Vault, App Service, Foundry
- Générer des commandes `az` CLI pour n'importe quelle tâche
- Créer des modèles Bicep et Terraform

## Pour commencer

- **Téléchargement** : [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Dépôt** : [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs** : [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Consultez le [post complet](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
