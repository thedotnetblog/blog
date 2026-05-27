---
title: "La reducció de paquets NuGet a .NET 10 és el tipus de millora que notes a tot arreu"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "La nova reducció de paquets NuGet a .NET 10 disminueix els informes de vulnerabilitats falsos positius, simplifica el gràfic de restauració i millora el rendiment de la restauració. És una d'aquelles canvis de plataforma que milloren el treball diari en silenci."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

*Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "index.md" >}}).*

Algunes millores de plataforma entusiasmen perquè obren nous escenaris.

D'altres entusiasmen perquè fan que els fluxos de treball existents siguin menys sorollosos, menys fràgils i menys molestos.

**La reducció de paquets NuGet a .NET 10** encaixa clarament en la segona categoria, i ho dic com un elogi.

## Per què això importa

Si has hagut d'afrontar soroll de vulnerabilitats transitives, gràfics de restauració innecessàriament grans o paquets que tècnicament hi són però que en realitat no són rellevants per al runtime que fa servir la teva app, aquest canvi toca un punt de dolor real.

La reducció ajuda eliminant del gràfic efectiu de dependències els paquets proporcionats per la plataforma quan el runtime ja els subministra.

Això vol dir:

- menys informes de vulnerabilitats falsos positius
- gràfics de dependències transitives més nets
- menys sobrecàrrega de restauració
- resultats d'auditoria més accionables

## La meva opinió

Això és exactament el tipus de millora de .NET que m'encanta.

Fa que els valors per defecte siguin millors, redueix la càrrega mental i millora tant la qualitat del senyal de seguretat com el comportament diari del tooling.

Això és una victòria encara que no arribi mai a una diapositiva de keynote.

Article original: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
