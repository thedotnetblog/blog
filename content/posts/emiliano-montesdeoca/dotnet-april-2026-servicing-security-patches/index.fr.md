---
title: ".NET Avril 2026 Servicing — Les correctifs de sécurité à appliquer dès aujourd'hui"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "La mise à jour de maintenance d'avril 2026 corrige 6 CVEs dans .NET 10, .NET 9, .NET 8 et .NET Framework — dont deux vulnérabilités d'exécution de code à distance."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}}).*

Les [mises à jour de maintenance d'avril 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) pour .NET et .NET Framework sont disponibles, et celle-ci inclut des correctifs de sécurité que vous allez vouloir appliquer rapidement. Six CVEs corrigés, dont deux vulnérabilités d'exécution de code à distance (RCE).

## Ce qui a été corrigé

Voici le résumé rapide :

| CVE | Type | Affecte |
|-----|------|---------|
| CVE-2026-26171 | Contournement de fonctionnalité de sécurité | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Exécution de code à distance** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Exécution de code à distance** | .NET 10, 9, 8 |
| CVE-2026-32203 | Déni de service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Déni de service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Déni de service | .NET Framework 2.0–4.8.1 |

Les deux CVEs RCE (CVE-2026-32178 et CVE-2026-33116) affectent le plus large éventail de versions .NET et devraient être la priorité.

## Versions mises à jour

- **.NET 10** : 10.0.6
- **.NET 9** : 9.0.15
- **.NET 8** : 8.0.26

Toutes sont disponibles via les canaux habituels — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), images de conteneurs sur MCR et gestionnaires de paquets Linux.

## Que faire

Mettez à jour vos projets et vos pipelines CI/CD vers les dernières versions corrigées. Si vous utilisez des conteneurs, récupérez les dernières images. Si vous êtes sur .NET Framework, consultez les [notes de version .NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) pour les correctifs correspondants.

Pour ceux qui font tourner .NET 10 en production (c'est la version actuelle), 10.0.6 est une mise à jour obligatoire. Idem pour .NET 9.0.15 et .NET 8.0.26 si vous êtes sur ces versions LTS. Deux vulnérabilités RCE, ce n'est pas quelque chose qu'on reporte.
