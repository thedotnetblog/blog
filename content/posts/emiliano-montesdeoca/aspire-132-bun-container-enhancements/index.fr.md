---
title: "Aspire 13.2 : Support Bun, Meilleurs Conteneurs et Moins de Friction de Debug"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 ajoute le support Bun de première classe pour les apps Vite, corrige la fiabilité de Yarn et apporte des améliorations aux conteneurs qui rendent le comportement local plus prévisible."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Si vous construisez des backends .NET avec des frontends JavaScript dans Aspire, la 13.2 est la mise à jour qui améliore silencieusement votre quotidien. Des améliorations solides à des choses légèrement agaçantes.

## Bun est Maintenant Citoyen de Première Classe

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Si votre équipe utilise déjà Bun, Aspire ne vous force plus à aller à contre-courant.

## Yarn Plus Fiable

Les utilisateurs de Yarn bénéficient de moins d'échecs mystérieux avec `withYarn()` et `addViteApp()`.

## Améliorations des Conteneurs

Pull policy explicite avec `ImagePullPolicy.Never` pour utiliser l'image locale sans aller au registry. PostgreSQL 18+ avec des volumes de données fonctionne maintenant correctement.

## Améliorations du Débogage

- `DebuggerDisplayAttribute` sur les types core
- Meilleurs messages d'erreur pour `WaitFor`
- `BeforeResourceStartedEvent` se déclenche au bon moment

## Conclusion

Post original de David Pine : [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
