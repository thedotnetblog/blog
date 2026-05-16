---
title: "Supprimer le Travail Répétitif de la Migration avec l'Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape présente la migration d'un déploiement Terraform AWS réel vers Azure Bicep — en extrayant l'intention de déploiement et en remappant l'architecture plutôt qu'en effectuant une conversion syntaxique 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — une présentation de Git-Ape (outil git d'ingénierie de plateforme agentique) qui migre un vrai dépôt Terraform AWS vers Azure, en se concentrant sur l'extraction d'intention plutôt que sur une conversion ligne par ligne.

## L'entrée : contoso-migration

La source est un vrai projet Terraform (`contoso-migration`) qui déploie une application Next.js sur AWS — EC2 pour le calcul, ALB pour l'équilibrage de charge, S3 pour les artefacts, et des clés IAM pour l'identité. Coût : ~34 $/mois. L'objectif n'est pas de reproduire la même infrastructure sur Azure ; c'est de comprendre ce que le déploiement essaie réellement de faire et de le reconstruire avec des services natifs Azure.

## Étape 1 : Validation et authentification

Git-Ape commence par valider tous les outils CLI requis — `az`, `aws`, `gh`, `jq`, `git` — et en confirmant les sessions d'authentification actives avant de toucher quoi que ce soit. Pas d'exécutions partielles.

## Étape 2 : Extraction d'intention

L'agent lit l'intégralité du dépôt source via l'API GitHub et extrait l'intention de déploiement : runtime (Node.js), type de calcul, modèle d'ingress, gestion des artefacts, modèle d'identité, réseau et surveillance. C'est l'étape clé — elle construit un modèle sémantique de ce que fait le déploiement, pas quels mots-clés Terraform il utilise.

## Étape 3 : Correspondance de services

Les services AWS sont mappés vers leurs équivalents Azure :
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Équilibrage de charge intégré d'App Service
- Rôles/clés IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Étape 4 : Agent de critique

Avant de générer la sortie, un agent de critique s'exécute et détecte deux problèmes bloquants :

1. **Anti-modèle de build au démarrage** — le Terraform original exécutait `npm install && npm run build` sur EC2 au démarrage. Correction : construire dans CI, déployer un artefact prêt.
2. **Blob Storage inutile** — S3 était utilisé pour la mise en attente d'artefacts qui pouvait être éliminé avec un CI/CD approprié. L'agent de critique l'a supprimé entièrement.

## Étape 5 : Sortie générée

Le résultat est ~80 lignes de Bicep au lieu des 200+ lignes originales de Terraform. L'agent a créé un nouveau dépôt GitHub avec `infra/main.bicep` et `.github/workflows/deploy.yml` et supprimé tous les fichiers spécifiques à AWS.

## Comparaison de la posture de sécurité

La migration a également produit une amélioration significative de la sécurité :

| AWS original | Sortie Azure |
|---|---|
| HTTP uniquement | HTTPS uniquement, TLS 1.2 |
| SSH ouvert à 0.0.0.0/0 | Pas d'exposition SSH |
| Clés d'accès IAM | OIDC + Managed Identity |
| Pas de surveillance | Application Insights |

Coût : ~13 $/mois vs les 34 $/mois originaux.

## Ce qui le distingue d'un convertisseur de syntaxe

L'étape de l'agent de critique est ce qui sépare ceci d'une traduction mécanique. Il a détecté des modèles qui auraient fonctionné sur AWS mais seraient incorrects sur Azure — et les a corrigés plutôt que de les répliquer. La sortie n'est pas "AWS en syntaxe Azure" ; c'est un déploiement natif Azure qui atteint le même objectif plus proprement.

Consultez le [guide complet](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) pour la trace complète de l'agent et les fichiers générés.
