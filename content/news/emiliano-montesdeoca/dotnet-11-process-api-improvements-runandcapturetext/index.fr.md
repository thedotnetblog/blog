---
title: ".NET 11 règle enfin l'API Processus"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process reçoit sa plus grande mise à jour depuis des années. RunAndCaptureTextAsync, KillOnParentExit, API SafeProcessHandle et contrôle total sur la redirection des handles standard — plus de code répétitif de deadlock."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Tout développeur .NET qui a eu besoin de lancer un processus et de capturer sa sortie a écrit une variation du même code boilerplate dangereux : lecture async de stdout, lecture async de stderr, `WaitForExitAsync`, sans oublier de drainer les deux flux sinon vous aurez un deadlock. C'est un piège bien connu qui existe depuis des années.

.NET 11 règle enfin cela correctement.

## RunAndCaptureTextAsync

L'ajout principal : une seule méthode statique qui démarre un processus, capture stdout et stderr, et attend la sortie sans deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Un seul appel. Pas de drainage manuel des flux. Pas de `WaitForExit` soigneusement positionné. Si vous avez juste besoin d'exécuter quelque chose et d'obtenir sa sortie, c'est l'API qu'il vous faut.

Il y a aussi `Process.RunAsync` pour le cas où vous voulez attendre la sortie sans capturer le résultat.

## KillOnParentExit

Un problème courant avec les processus lancés : si le parent plante ou est tué, les processus enfants continuent de tourner comme des orphelins. `KillOnParentExit` vous permet de déclarer au démarrage du processus que le processus enfant doit se terminer quand le processus parent se termine.

C'est une fonctionnalité qui existait de manières spécifiques à chaque plateforme (job objects sur Windows, prctl sur Linux) mais nécessitait p/invoke ou des bibliothèques tierces pour être utilisée depuis .NET. Désormais, c'est une propriété de premier rang sur `ProcessStartInfo`.

## APIs Basées sur SafeProcessHandle

La nouvelle surface d'API légère est construite autour de `SafeProcessHandle` plutôt que de la classe `Process` complète. La classe `Process` complète contient beaucoup d'état et est difficile à éliminer — le chemin `SafeProcessHandle` est plus adapté au trimmer pour les applications qui doivent minimiser la taille de sortie (WASM, AOT natif).

## Contrôle Total sur l'Héritage des Handles

La mise à jour ajoute également un contrôle précis sur les handles qu'un processus enfant hérite et comment les handles standard sont redirigés. Auparavant, vous pouviez rediriger stdin/stdout/stderr mais ne pouviez pas spécifier exactement quels handles hériter au niveau du système d'exploitation. Les nouvelles APIs exposent ce contrôle.

## Pourquoi C'est Important

La classe `Process` est utilisée dans les outils, les systèmes de build, les exécuteurs de tests et toute application qui invoque d'autres exécutables. L'ancienne surface d'API datait de .NET Framework et montrait son âge. Ce n'est pas un changement cassant — les anciennes APIs fonctionnent toujours — mais le nouveau code devrait préférer la nouvelle surface.

Pour les applications avec trimming ou les scénarios de compilation AOT, le chemin `SafeProcessHandle` est particulièrement bienvenu. L'ancienne classe `Process` amenait beaucoup de code lourd en réflexion qui compliquait le trimming.

Post original : [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
