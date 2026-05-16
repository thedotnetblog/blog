---
title: "VS Code 1.119 : OpenTelemetry pour les sessions d'agents, intégration du navigateur et sécurité"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (mai 2026) ajoute le traçage OpenTelemetry pour les sessions d'agents, le partage d'onglets de navigateur, des améliorations de confiance et de sécurité, et un correctif de sécurité 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) est sorti le 6 mai 2026 (avec un correctif de sécurité 1.119.1 peu après). La version se concentre sur l'observabilité des agents, l'interaction avec le navigateur et la réduction des interruptions.

## Traçage OpenTelemetry pour les sessions d'agents

C'est la fonctionnalité phare pour ceux qui font tourner des agents en production ou qui déboguent des workflows agentiques. Activez-la avec deux paramètres :

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Les traces suivent les conventions sémantiques GenAI. Chaque requête d'agent produit un span racine `invoke_agent` avec des spans enfants imbriqués : `chat`, `execute_tool` et `execute_hook`. L'utilisation des tokens est rapportée par requête — y compris les comptages de lecture et de création de cache.

Fonctionne avec l'agent local, l'agent de fond Copilot CLI et l'agent Claude. Tout backend compatible OTLP accepte les traces — le [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) fonctionne bien pour le développement local.

## Les agents peuvent maintenant accéder aux onglets du navigateur

Les agents peuvent demander l'accès à vos onglets de navigateur intégré — mais ce n'est pas automatique. Vous devez partager explicitement un onglet via le sélecteur de contexte, le glisser-déposer ou le contexte suggéré. Il y a un bouton de partage dans le navigateur pour révoquer l'accès. Quand un agent tente d'ouvrir un nouvel onglet sur le même domaine qu'un onglet ouvert (non partagé), VS Code vous demande de réutiliser l'onglet existant.

## Utilisation optimisée des tokens

Un modèle léger expérimental gère maintenant les listes de tâches des agents, gardant ce travail administratif hors du modèle principal plus coûteux. Réduit la consommation de tokens pour les tâches qui ne nécessitent pas une pleine capacité de raisonnement.

## Confiance et sécurité

Moins d'interruptions : VS Code 1.119 réduit les invites pour les demandes d'accès réseau et les écritures dans les dossiers temporaires par les agents. Le correctif 1.119.1 résout des problèmes de sécurité spécifiques — une mise à jour s'impose si ce n'est pas encore fait.

## Changement rapide vers l'aperçu Markdown

Petit mais utile : vous pouvez maintenant basculer rapidement l'éditeur actuel vers l'aperçu Markdown sans naviguer.

## VS Code Agents (préversion Insiders)

L'interface de session d'agents repensée — nouveau sélecteur de dépôts (local/repos/distant), améliorations des sous-sessions, polissage web et mobile, animations de progression — est disponible dans Insiders sur [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Journal des modifications complet : [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
