---
title: "Votre Agent IA a un Problème d'Identité (Et Voici le Modèle qui le Résout)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Un nouveau modèle azd de Curity et Microsoft montre comment créer des agents IA qui utilisent des tokens OAuth de courte durée avec des scopes à grain fin — pour que les agents ne puissent jamais voir des données qu'ils ne devraient pas voir."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Il y a un moment dans chaque projet d'agent IA qui ressemble à ceci : la démo fonctionne parfaitement, l'agent interprète le langage naturel, appelle les bonnes API, retourne les bonnes données. Ensuite vous commencez à penser aux vrais utilisateurs.

Qu'est-ce qui empêche la session d'agent d'un utilisateur de voir les données d'un autre utilisateur ? Et si l'agent est trompé par une injection de prompt ? Et s'il appelle un outil d'une manière inattendue ?

Ce ne sont pas des cas limites. Ce sont des décisions de conception que vous devez prendre avant de livrer.

Un nouveau modèle `azd` de Curity et Microsoft vous donne une référence fonctionnelle pour exactement ce problème.

## Le Problème Central : Authentification ≠ Autorisation

La plupart des exemples d'agents gèrent bien l'authentification des utilisateurs. Ils gèrent mal l'autorisation. Savoir *qui* est l'utilisateur ne vous dit pas *quelles données* il devrait voir.

Une application cliente traditionnelle fait des appels d'API prévisibles. Un agent IA est non déterministe — il interprète le langage naturel et décide quoi appeler. Il peut être créatif. Il peut aussi se tromper. Et s'il est manipulé par injection de prompt, vous avez besoin de règles qui ne dépendent pas du bon comportement de l'IA.

La solution démontrée par ce modèle : **des tokens de courte durée qui transportent exactement les bonnes informations pour chaque saut**.

## Comment Fonctionne la Chaîne de Tokens

Le modèle utilise des tokens d'accès OAuth 2.0 avec échange de tokens pour réduire les permissions à chaque étape. Un token utilisateur est échangé deux fois avant d'atteindre le serveur MCP :

1. **Premier échange** — réduit la portée et convertit le token opaque en JWT
2. **Deuxième échange** — ajoute l'identité de l'agent et une nouvelle audience pour le saut du serveur MCP

À quoi ressemble le token du serveur MCP :

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

Le `customer_id` est intégré dans le token par le serveur d'autorisation, pas passé comme paramètre que l'agent contrôle. L'API vérifie le token, pas les instructions de l'agent.

Cela signifie : même si quelqu'un trompe l'agent pour qu'il essaie d'obtenir les données d'un autre client, le token ne l'autorisera pas.

## Ce que le Modèle Déploie

Avec quelques commandes `azd` vous obtenez :

- Un agent backend sur Microsoft Foundry (C#, SDK Microsoft A2A et MCP)
- Un serveur MCP exposant un exemple d'API de portefeuille
- Curity Identity Server comme serveur d'autorisation, aux côtés d'Entra ID pour l'authentification
- Des passerelles API externes et internes gérant l'échange de tokens et la journalisation d'audit
- Bicep pour toute l'infrastructure Azure : Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, stockage

Tout le modèle est inspecTable et personnalisable.

## Le Principe de Conception qui Vaut la Peine d'être Emprunté

Même si vous n'utilisez pas Curity, le modèle est transférable : **les agents ne devraient jamais avoir un accès permanent à l'API**. Chaque action devrait utiliser un token de courte durée avec le scope minimum nécessaire pour cet appel spécifique, émis pour l'identité spécifique de l'agent, portant les claims dont l'API a besoin pour prendre des décisions d'autorisation.

Cela résiste aux agents créatifs, aux erreurs et à l'injection de prompt d'une façon que "assurez-vous simplement que l'agent ne fait pas de mauvaises choses" ne fera jamais.

## Conclusion

Les modèles de sécurité pour les agents IA sont encore en cours d'élaboration dans l'industrie. Ce modèle est l'une des implémentations de référence les plus complètes que j'ai vues — il couvre le flux d'autorisation réel, pas seulement l'authentification.

Post original : [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
