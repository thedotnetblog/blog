---
title: ".NET 11 Preview 5: Què Provaria Primer Realment"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 inclou millores al SDK, runtime, C#, ASP.NET Core i EF Core. Aquí teniu les actualitzacions que crec que val més la pena provar aviat si construïu aplicacions .NET reals."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

Les publicacions de previsualització de .NET sempre estan plenes.

Això és una bona notícia per a la plataforma, però també significa que la pregunta pràctica queda enterrada: **què hauríeu de provar primer realment?**

.NET 11 Preview 5 porta molt al SDK, runtime, llibreries, ASP.NET Core, C#, MAUI i EF Core. En lloc de convertir-ho en un gegant recull de registre de canvis, vull centrar-me en les parts que crec que mereixen atenció real dels desenvolupadors ara.

## La plantilla de servidor MCP a `dotnet new` és un senyal

Aquesta és probablement l'opció més estratègica de la secció del SDK.

Quan una plantilla de projecte arriba directament al SDK, significa que la plataforma ja no tracta l'escenari com a nínxol. Tenir una **plantilla de servidor MCP** integrada a `dotnet new` redueix el cost de provar el patró i envia un missatge clar sobre cap a on va l'ecosistema.

Si esteu construint eines per a agents, assistents interns o utilitats de desenvolupament integrades amb IA a .NET, aquesta és una de les primeres coses que provaria.

## Les comprovacions de vulnerabilitat i final de vida en temps de compilació són exactament el tipus de valors predeterminats que m'agraden

La seguretat i la consciència del cicle de vida són molt millors quan la plataforma t'ajuda **durant la compilació**, no després dels fets en un informe separat que ningú llegeix.

Les noves comprovacions del SDK per a vulnerabilitats i paquets en final de vida durant la compilació són el tipus de funció que m'encanta perquè fan que el millor comportament sigui el predeterminat.

No són cridaneres, però són el tipus de millores que envelleixen molt bé.

## C# continua tornant-se més expressiu als llocs correctes

Els elements de C# de Preview 5 són interessants, especialment:

- jerarquies de classes tancades
- declaracions d'unió i patrons d'unió
- treball contínu d'evolució d'unsafe

No adoptaria tot això cegament en codi de producció encara, perquè les funcions de llenguatge en previsualització sempre mereixen un cicle de proves sobri. Però la direcció és bona. C# continua movent-se cap a un modelatge més ric sense perdre la seva identitat.

## ASP.NET Core i EF Core tenen actualitzacions pràctiques que val la pena provar aviat

Dues àrees que definitivament posaria a prova:

### Millores de Blazor

La validació client-side per a Blazor SSR i les millores de QuickGrid sense interactivitat són ambdós el tipus de funcions de qualitat de vida que poden simplificar aplicacions reals.

### Valors predeterminats i avisos d'EF Core

EF Core movent la compatibilitat de SQL Server 2022 al valor predeterminat i afegint avisos per a consultes EF asíncrones que s'executen sincronament són exactament el tipus de canvis que poden descobrir problemes ocults en bases de codi reals.

Això significa que val la pena provar-ho aviat en lloc de tard.

## La meva llista curta per a una primera passada

Si tingués mig dia per explorar Preview 5, faria això:

1. provar la plantilla de servidor MCP
2. executar compilacions i inspeccionar les noves comprovacions de vulnerabilitat/EOL
3. provar qualsevol base de codi que pogués beneficiar-se de les noves funcions de modelatge de C#
4. validar escenaris de Blazor SSR si esteu en aquest stack
5. executar camins intensius d'EF Core i vigilar els canvis d'avisos o diferències SQL

Aquí és on crec que està el valor inicial.

## La meva opinió

.NET 11 Preview 5 se sent com un d'aquells llançaments on la plataforma continua impulsant en dues direccions alhora:

- capacitats de desenvolupador més ambicioses
- millors valors predeterminats per a equips orientats a producció

Aquesta combinació és el que vull d'un cicle de previsualització.

Proveu-ho, però proveu-ho amb propòsit.

Article original: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)