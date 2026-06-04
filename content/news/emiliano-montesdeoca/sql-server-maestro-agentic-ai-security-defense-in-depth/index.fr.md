---
title: "MAESTRO, Défense en Profondeur et Pourquoi SQL Server Est Maintenant une Frontière de Sécurité pour l'IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "L'IA agentique introduit des menaces pour lesquelles les modèles STRIDE traditionnels n'ont pas été conçus. Voici comment Microsoft SQL se mappe au framework MAESTRO pour fournir une frontière d'exécution gouvernée."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Les modèles de menaces de sécurité sont construits sur des hypothèses concernant qui ou quoi fait les demandes. STRIDE suppose des acteurs humains interagissant avec des systèmes via des interfaces définies. Les agents d'IA ne fonctionnent pas de cette façon.

## STRIDE N'a Pas Été Conçu pour les Agents d'IA

Les systèmes agentiques opèrent de manière autonome, enchaînent des outils via des appels API, prennent des décisions sur les données à récupérer et les actions à exécuter, et peuvent recevoir des instructions de plusieurs sources — prompts utilisateur, résultats d'outils, données récupérées. Le modèle de menaces STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) ne capture pas adéquatement les vecteurs d'attaque spécifiques aux agents comme l'injection de prompts, l'empoisonnement de contexte ou l'abus d'outils.

La Cloud Security Alliance a publié le framework MAESTRO spécifiquement pour le risque des agents d'IA.

## Le Framework MAESTRO

MAESTRO organise le risque d'IA agentique en sept couches :

1. **Foundation Models** — les LLM sous-jacents et leurs vulnérabilités d'entraînement
2. **Data Operations** — récupération, stockage et manipulation des données
3. **Agent Frameworks** — le middleware d'orchestration et de coordination des agents
4. **Deployment & Infrastructure** — où les agents s'exécutent et comment ils sont configurés
5. **Evaluation & Observability** — surveillance du comportement des agents dans le temps
6. **Security & Compliance** — contrôles d'accès, audit et conformité réglementaire
7. **Agent Ecosystem** — comment les agents interagissent entre eux et avec des outils externes

Chaque couche a des vecteurs d'attaque spécifiques que les contrôles de sécurité traditionnels n'adressent pas directement.

## Microsoft SQL Comme Frontière d'Exécution Gouvernée

SQL Server 2025 se mappe aux couches MAESTRO de manières concrètes :

**Couche Data Operations** : `AI_GENERATE_EMBEDDINGS` intégré dans T-SQL maintient les opérations vectorielles dans la frontière gouvernée de la base de données. Les données n'ont pas besoin de quitter vers le service de modèle pour le traitement des embeddings.

**Couches Security & Compliance** : La sécurité au niveau des lignes (RLS) et le masquage dynamique des données (DDM) s'appliquent indépendamment de la façon dont la demande est arrivée — qu'elle provienne d'un utilisateur humain ou d'un agent d'IA. L'agent ne peut pas contourner des contrôles qui sont imposés par la base de données elle-même.

**Couche Agent Frameworks** : Les procédures stockées servent de frontières d'outils. Au lieu de donner aux agents un accès SQL arbitraire, vous définissez les opérations autorisées comme des procédures et les exposez comme des outils d'agent. Les requêtes paramétrées empêchent l'injection au niveau d'exécution.

**Couche Evaluation & Observability** : La journalisation d'audit et Query Store capturent ce que chaque agent a réellement exécuté — pas seulement ce qu'on lui a demandé de faire. Cette traçabilité est critique pour les enquêtes d'incidents dans les systèmes agentiques où l'attribution est complexe.

## Défense en Profondeur pour l'IA Agentique

Le principe reste le même que dans la sécurité traditionnelle : aucun contrôle unique n'est suffisant. Ce qui change, c'est quels contrôles sont les plus importants pour les agents :

**Réduire le rayon d'impact** : les frontières d'outils des procédures stockées signifient qu'un agent compromis ne peut exécuter que des opérations prédéfinies. Il ne peut pas pivoter vers des requêtes arbitraires.

**Observabilité** : vous devez être capable de répondre "qu'a fait exactement cet agent ?" après un incident. Les systèmes d'IA agentique sans traçabilité au niveau de la base de données ont des angles morts que la journalisation applicative ne couvre pas.

**Exécution contrainte** : la paramétrisation, RLS et DDM sont des atouts de sécurité indépendamment de si l'appelant est humain. Ne les affaiblissez pas pour accommoder les agents.

**Responsabilité** : la journalisation d'audit de SQL Server crée un registre de qui (quel agent, avec quelles credentials) a exécuté quoi à quel moment. Cela compte lorsque les systèmes agentiques prennent des actions avec des conséquences réelles dans le monde.

SQL Server 2025 n'a pas été construit pour résoudre le risque agentique de manière abstraite — il a été construit pour être une base de données relationnelle. Mais la gouvernance qui rend une base de données d'entreprise fiable s'avère être exactement ce qui rend sécurisée une frontière d'exécution d'agents.

Post original : [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
