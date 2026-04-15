---
title: "Azure DevOps Server Patch Avril 2026 — Correction du Complétion de PR et Mises à Jour de Sécurité"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server reçoit le Patch 3 avec une correction pour les échecs de complétion de PR, une validation améliorée à la déconnexion et la restauration des connexions PAT vers GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Petit rappel pour les équipes qui hébergent leur propre Azure DevOps Server : Microsoft a publié le [Patch 3 d'avril 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) avec trois correctifs ciblés.

## Ce qui a été corrigé

- **Échecs de complétion des pull requests** — une exception de référence nulle lors de l'auto-complétion des work items pouvait faire échouer les merges de PR. Si vous avez rencontré des erreurs aléatoires lors de la complétion de PR, c'est probablement la cause
- **Validation de la redirection à la déconnexion** — validation améliorée lors de la déconnexion pour empêcher d'éventuelles redirections malveillantes. C'est un correctif de sécurité à appliquer rapidement
- **Connexions PAT vers GitHub Enterprise Server** — la création de connexions par Personal Access Token vers GitHub Enterprise Server était cassée, c'est maintenant rétabli

## Comment mettre à jour

Téléchargez le [Patch 3](https://aka.ms/devopsserverpatch3) et lancez l'installateur. Pour vérifier que le patch est bien appliqué :

```bash
<patch-installer>.exe CheckInstall
```

Si vous utilisez Azure DevOps Server en auto-hébergement, Microsoft recommande vivement de rester sur le dernier patch pour la sécurité comme pour la fiabilité. Consultez les [notes de version](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) pour tous les détails.
