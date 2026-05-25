---
title: ".NET 11 Preview 4: Plantilla de Servidor MCP, Biblioteques Runtime-Async, API de Processos"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 ja és disponible. Aquí els punts destacats: la plantilla de servidor MCP al SDK, biblioteques de runtime compilades amb runtime-async, dotnet watch per a mòbil i una gran ampliació de l'API de Processos."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 ja és disponible. Cada versió de vista prèvia principal de .NET afegeix una llarga llista d'elements a través del runtime, SDK, biblioteques, ASP.NET Core, MAUI, C# i Entity Framework. En lloc de repetir la llista completa, aquí hi ha les coses que em van cridar l'atenció.

## La Plantilla de Servidor MCP Arriba al SDK de .NET

L'element més interessant: una plantilla de projecte de servidor MCP ara ve inclosa al SDK. Això significa que `dotnet new mcp-server` (o com s'anomeni finalment la comanda) funciona directament sense configuració addicional. Per a qualsevol persona que construeixi eines MCP a .NET, això redueix significativament la fricció inicial. La integració de MCP a la cadena d'eines de la plataforma indica la direcció que pren l'ecosistema.

## Biblioteques de Runtime Compilades amb Runtime-Async

El runtime mateix ara compila les seves biblioteques estàndard fent servir la característica runtime-async. Es tracta d'un canvi intern que afecta el rendiment — les màquines d'estat async al runtime es tornen més eficients. La importància aquí no rau en canvis d'API visibles per a l'usuari; és que runtime-async és prou madur per ser usat per al propi BCL, la qual cosa és un senyal significatiu sobre la preparació de la característica.

## Optimitzacions JIT i Intrínsecs de Maquinari

Preview 4 continua el treball de JIT. Les millores d'intrínsecs de maquinari i generació de codi arriben aquí — els detalls es troben a les notes de llançament del runtime. Aquest tipus de canvis normalment milloren el rendiment en bucles de computació densa sense cap canvi de codi per la vostra part.

## Ampliació de l'API de Processos

Una gran actualització per a `System.Diagnostics.Process` arriba a Preview 4:

- `Process.RunAndCaptureTextAsync` — inicia un procés, captura stdout/stderr, espera la sortida, tot en una sola trucada sense risc de bloqueig mort
- `KillOnParentExit` — acoblament lleuger del cicle de vida entre processos pare i fill
- APIs basades en `SafeProcessHandle` més amigables amb el trimmer

Si alguna vegada heu escrit codi repetitiu per capturar la sortida d'un procés sense provocar bloquejos morts (lectura async de stdout *i* stderr simultàniament), `RunAndCaptureTextAsync` és l'API que us faltava.

## dotnet watch per a Android i iOS

`dotnet watch` ara admet la selecció de dispositius per a projectes .NET MAUI Android i iOS. Iteració més ràpida en mòbil sense gestionar manualment les connexions de dispositius al bucle de compilació.

## APIs de Compressió Basades en Span

Noves APIs d'encoder/decoder Deflate, ZLib i GZip basades en span arriben a les biblioteques. Menys assignacions en treballar amb dades comprimides — rellevant si feu processament de dades d'alt rendiment.

## Proveu-ho

[Baixeu .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — és una vista prèvia, no llesta per a producció, però val la pena executar-la contra els vostres projectes per detectar problemes aviat abans del cicle RC.

Publicació original: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
