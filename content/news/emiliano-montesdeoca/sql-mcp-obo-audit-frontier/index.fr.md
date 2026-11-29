---
title: "La vraie frontière pour le SQL agentique : l'auditabilité avec OBO dans SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "L'authentification On-Behalf-Of dans Data API builder plus SQL MCP Server est un jalon de gouvernance majeur parce qu'Azure SQL peut enfin auditer l'humain derrière une action d'agent."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Il y a une vérité douloureuse dans les projets IA d'entreprise : beaucoup d'équipes s'obsèdent sur la qualité du modèle et ignorent la responsabilité. Quand un agent écrit ou lit des données de production, la première question de revue d'incident n'est pas « la réponse était-elle bonne ? ». C'est « qui a réellement fait ça ? »

Original source: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

C'est pourquoi le support OBO dans Data API builder 2.0 avec SQL MCP Server est une affaire plus importante qu'il n'y paraît au premier abord. Les approches par nom d'utilisateur/mot de passe et identité managée fonctionnent encore opérationnellement, mais toutes deux effondrent l'identité dans la limite du service. Les journaux montrent l'application ou le middleware, pas l'origine de la requête humaine. C'est acceptable pour de l'automatisation simple. Ce n'est pas acceptable pour des workflows agentiques réglementés.

Avec OBO, SQL authentifie le contexte utilisateur délégué, pas l'identité de l'hôte de l'outil. Cela vous donne un modèle d'audit fondamentalement meilleur : principal utilisateur, action, contexte d'instruction, et identifiant d'application de niveau intermédiaire ensemble. Vous obtenez la traçabilité sans perdre la surface de contrôle des outils MCP et des permissions d'entité DAB.

Mon avis est ferme ici : si votre agent peut toucher des données SQL sensibles, OBO devrait être votre architecture par défaut, pas une tâche de durcissement optionnelle. La configuration est plus impliquée, mais la dette d'identité est toujours payée plus tard, généralement lors d'incidents de sécurité, d'audits de conformité, ou d'escalades exécutives.

Conseils d'implémentation pratiques :

Commencez par valider le flux d'identité avec une vue minimale « WhoAmI » et des vérifications automatisées dans les tests d'intégration. Si le principal SQL ne correspond pas à l'utilisateur connecté, arrêtez et corrigez avant de livrer. Ensuite, câblez les requêtes Log Analytics pour SQLSecurityAuditEvents dans vos tableaux de bord SOC et alertez sur les actions à haut risque initiées via des chemins OBO. Enfin, alignez le RBAC et les permissions DAB pour que l'identité au niveau utilisateur et l'autorisation au niveau action restent cohérentes de bout en bout.

Un point de conception subtil mais important dans l'annonce concerne le comportement du cache. DAB bloque explicitement la mise en cache de réponse quand l'authentification déléguée par l'utilisateur est activée. Ce compromis est correct. Les astuces de performance qui peuvent divulguer des résultats à portée utilisateur ne valent pas le coup dans des environnements multi-tenants ou réglementés.

SQL MCP Server plus OBO est le début d'un modèle mature : des agents comme opérateurs contrôlés, des utilisateurs comme principaux responsables, des plans de données comme systèmes auditables. Si votre architecture ne peut pas répondre « qui a fait ça » avec confiance, ce n'est pas une IA prête pour la production, peu importe à quel point la démo est soignée.
