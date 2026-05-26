---
title: ".NET 11 finalment arregla l'API de Processos"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process rep la seva actualització més gran en anys. RunAndCaptureTextAsync, KillOnParentExit, APIs SafeProcessHandle i control total sobre la redirecció dels identificadors estàndard — sense més codi repetitiu per als bloqueigs morts."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Tot desenvolupador .NET que alguna vegada ha hagut de llançar un procés i capturar la seva sortida ha escrit alguna variació del mateix codi repetitiu perillós: lectura async de stdout, lectura async de stderr, `WaitForExitAsync`, sense oblidar buidar tots dos streams o causaràs un bloqueig mort. És una trampa ben coneguda que existeix des de fa anys.

.NET 11 finalment ho arregla correctament.

## RunAndCaptureTextAsync

L'addició principal: un únic mètode estàtic que inicia un procés, captura stdout i stderr, i espera la sortida sense bloqueig mort.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Una sola crida. Sense buidatge manual de streams. Sense un `WaitForExit` col·locat acuradament. Si simplement necessiteu executar alguna cosa i obtenir la seva sortida, aquesta és l'API que voleu.

Hi ha també `Process.RunAsync` per al cas en què voleu esperar la sortida sense capturar el resultat.

## KillOnParentExit

Un problema comú amb els processos llançats: si el pare falla o és acabat, els processos fill continuen executant-se com a orfes. `KillOnParentExit` us permet declarar en el moment d'iniciar el procés que el procés fill ha d'acabar quan el procés pare surti.

Aquesta és una funcionalitat que existia de maneres específiques per plataforma (job objects a Windows, prctl a Linux) però requeria p/invoke o biblioteques de tercers per ser usada des de .NET. Ara és una propietat de primera classe a `ProcessStartInfo`.

## APIs Basades en SafeProcessHandle

La nova superfície d'API lleugera es construeix al voltant de `SafeProcessHandle` en lloc de la classe `Process` completa. La classe `Process` completa porta molt d'estat i és difícil de retallar — el camí `SafeProcessHandle` és més amigable amb el trimmer per a aplicacions que necessiten minimitzar la mida de sortida (WASM, AOT natiu).

## Control Total Sobre l'Herència d'Identificadors

L'actualització també afegeix control detallat sobre quins identificadors hereda un procés fill i com es redireccionen els identificadors estàndard. Anteriorment podíeu redirigir stdin/stdout/stderr però no podíeu especificar exactament quins identificadors heretar a nivell de SO. Les noves APIs exposen aquest control.

## Per Què És Important

La classe `Process` s'usa en eines, sistemes de compilació, executors de proves i qualsevol aplicació que invoca altres executables. L'antiga superfície d'API datava de .NET Framework i estava mostrant la seva edat. No és un canvi que trenca la compatibilitat — les APIs antigues segueixen funcionant — però el nou codi hauria de preferir la nova superfície.

Per a aplicacions retallades o escenaris de compilació AOT, el camí `SafeProcessHandle` és especialment benvingut. L'antiga classe `Process` portava molt codi pesat en reflexió que complicava el retallat.

Publicació original: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
