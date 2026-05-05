---
title: "L'Ingénierie de Plateformes Agentique Devient Réalité — Git-APE Montre Comment"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Le projet Git-APE de Microsoft concrétise l'ingénierie de plateformes agentique — en utilisant les agents GitHub Copilot et Azure MCP pour transformer des requêtes en langage naturel en infrastructure cloud validée."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "agentic-platform-engineering-git-ape" >}}).*

L'ingénierie de plateformes est un de ces termes qui sonne bien en conférence mais qui signifie généralement « on a construit un portail interne et un wrapper Terraform. » La vraie promesse — une infrastructure en self-service qui soit réellement sécurisée, gouvernée et rapide — a toujours été à quelques pas.

L'équipe Azure vient de publier la [Partie 2 de leur série sur l'ingénierie de plateformes agentique](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), et celle-ci porte sur l'implémentation concrète. Ils l'appellent **Git-APE** (oui, l'acronyme est intentionnel), et c'est un projet open source qui utilise les agents GitHub Copilot plus les serveurs Azure MCP pour transformer des requêtes en langage naturel en infrastructure validée et déployée.

## Ce que Git-APE fait concrètement

L'idée principale : au lieu que les développeurs apprennent des modules Terraform, naviguent dans des UIs de portails ou déposent des tickets à l'équipe plateforme, ils parlent à un agent Copilot. L'agent interprète l'intention, génère de l'Infrastructure-as-Code, la valide contre les politiques et déploie — le tout dans VS Code.

Voici la mise en place :

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Ouvre le workspace dans VS Code, et les fichiers de configuration de l'agent sont automatiquement découverts par GitHub Copilot. Tu interagis directement avec l'agent :

```
@git-ape deploy a function app with storage in West Europe
```

L'agent utilise Azure MCP Server en interne pour interagir avec les services Azure. La configuration MCP dans les paramètres de VS Code active des capacités spécifiques :

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Pourquoi c'est important

Pour ceux d'entre nous qui construisent sur Azure, cela déplace la conversation de l'ingénierie de plateformes de « comment construire un portail » à « comment décrire nos garde-fous comme des APIs. » Quand l'interface de ta plateforme est un agent IA, la qualité de tes contraintes et politiques devient le produit.

Le blog de la Partie 1 posait la théorie : des APIs bien décrites, des schémas de contrôle et des garde-fous explicites rendent les plateformes agent-ready. La Partie 2 prouve que ça marche en livrant des outils concrets. L'agent ne génère pas aveuglément des ressources — il valide contre les bonnes pratiques, respecte les conventions de nommage et applique les politiques de ton organisation.

Le nettoyage est tout aussi simple :

```
@git-ape destroy my-resource-group
```

## Mon avis

Je serai honnête — ici c'est plus le pattern que l'outil spécifique qui compte. Git-APE lui-même est une démo/architecture de référence. Mais l'idée sous-jacente — les agents comme interface de ta plateforme, MCP comme protocole, GitHub Copilot comme hôte — c'est la direction que prend l'expérience développeur en entreprise.

Si tu es une équipe plateforme qui cherche comment rendre son outillage interne agent-friendly, il n'y a pas de meilleur point de départ. Et si tu es un développeur .NET qui se demande comment ça se connecte à ton monde : Azure MCP Server et les agents GitHub Copilot fonctionnent avec n'importe quel workload Azure. Ton API ASP.NET Core, ton stack .NET Aspire, tes microservices containerisés — tout ça peut être la cible d'un flux de déploiement agentique.

## Pour conclure

Git-APE est un aperçu précoce mais concret de l'ingénierie de plateformes agentique en pratique. Clone le [repo](https://github.com/Azure/git-ape), essaie la démo et commence à réfléchir à comment les APIs et politiques de ta plateforme devraient se présenter pour qu'un agent puisse les utiliser en toute sécurité.

Lis le [post complet](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) pour le walkthrough et les vidéos de démo.
