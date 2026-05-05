---
title: "Hooks azd en Python, TypeScript et .NET : fini les scripts shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "La CLI Azure Developer prend désormais en charge les hooks en Python, JavaScript, TypeScript et .NET. Plus besoin de basculer vers Bash juste pour lancer un script de migration."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Vous avez déjà eu un projet entièrement en .NET et vous avez quand même dû écrire des scripts Bash pour les hooks azd ? Vous connaissez la douleur. Pourquoi basculer vers la syntaxe shell pour une étape de pré-provisioning quand tout le reste du projet est en C# ?

Cette frustration a maintenant une solution officielle. La CLI Azure Developer [vient de publier la prise en charge multi-langages pour les hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), et c'est exactement aussi bien que ça en a l'air.

## Les hooks, en bref

Les hooks sont des scripts qui s'exécutent à des moments clés du cycle de vie d'`azd` — avant le provisioning, après le déploiement, etc. Définis dans `azure.yaml`, ils permettent d'injecter de la logique personnalisée sans modifier la CLI.

Avant, seuls Bash et PowerShell étaient supportés. Maintenant, on peut utiliser **Python, JavaScript, TypeScript ou .NET** — et `azd` s'occupe du reste automatiquement.

## Comment fonctionne la détection

Il suffit de pointer le hook vers un fichier et `azd` déduit le langage à partir de l'extension :

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Pas de configuration supplémentaire. Si l'extension est ambiguë, on peut ajouter `kind: python` (ou le langage correspondant) pour le préciser.

## Détails par langage

### Python

Placer un `requirements.txt` ou `pyproject.toml` à côté du script (ou dans un répertoire parent). `azd` crée automatiquement un environnement virtuel, installe les dépendances et exécute le script.

### JavaScript et TypeScript

Même principe — un `package.json` près du script, et `azd` exécute d'abord `npm install`. Pour TypeScript, il utilise `npx tsx` sans étape de compilation et sans `tsconfig.json`.

### .NET

Deux modes disponibles :

- **Mode projet** : Si un `.csproj` est présent à côté du script, `azd` exécute automatiquement `dotnet restore` et `dotnet build`.
- **Mode single-file** : Sur .NET 10+, les fichiers `.cs` autonomes s'exécutent directement via `dotnet run script.cs`. Aucun fichier de projet requis.

## Configuration par exécuteur

Chaque langage supporte un bloc `config` optionnel :

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## Pourquoi c'est important pour les développeurs .NET

Les hooks étaient le dernier endroit dans un projet azd qui forçait à changer de langage. Maintenant, l'intégralité du pipeline de déploiement peut vivre dans un seul langage. Il devient possible de réutiliser les utilitaires .NET existants dans les hooks, de référencer des bibliothèques partagées et d'abandonner la maintenance de scripts shell.

## Conclusion

Un de ces changements qui paraissent anodins mais qui réduisent concrètement la friction au quotidien avec azd. Le support multi-langages pour les hooks est disponible maintenant — tous les détails dans le [post officiel](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/).
