---
title: ".NET 8 i .NET 9 Fi de Suport: Tracteu Això com a Data Límit de Lliurament"
date: 2026-07-19
author: "Emiliano Montesdeoca"
description: "El 10 de novembre de 2026 no és només una data de suport; és el punt on el risc d'actualització ajornat es torna explícit."
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Font original: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Aquest anunci és directe, i els equips haurien de respondre amb la mateixa claredat: si planifiqueu seguir enviant amb .NET 8 o .NET 9 després del 10 de novembre de 2026, esteu prenent una decisió intencional de runtime no suportat.

Les aplicacions seguiran funcionant. Aquest no és el punt. El punt és que les actualitzacions de seguretat i servei s'aturen. Un cop això passa, cada vulnerabilitat coneguda sense un camí de backport es converteix en la vostra responsabilitat operativa.

La meva opinió: les organitzacions sovint tracten les actualitzacions de framework com a manteniment opcional i després paguen per aquesta decisió en finestres d'emergència, troballes d'auditoria i escalacions de venedor precipitades. La planificació d'actualització hauria de ser un element del roadmap de producte, no una missió secundària.

Una postura de migració pràctica per als equips .NET:

Establiu el reorientament a .NET 10 com un objectiu datat, no com un element de backlog obert.

Executeu proves de compatibilitat i regressió en paral·lel amb el treball de funcions ara, no al Q4.

Feu un seguiment de la preparació de dependències i hostatjament com a fluxos de treball separats, perquè moltes fallades passen fora del fitxer de projecte.

Utilitzeu Upgrade Assistant i la documentació de canvis trencadors aviat per avançar-vos a les sorpreses.

Si teniu biblioteques compartides utilitzades per múltiples productes, publiqueu el vostre calendari de suport de .NET 10 públicament dins de la vostra organització. Els equips downstream necessiten temps de preparació.

El marcatge de components fora de suport de Visual Studio també importa operativament. Crea un senyal clar que la neteja de la cadena d'eines és part de mantenir-se compliant. Els equips que ignoren això solen derivar cap a estats de SDK mixts i comportament de compilació inconsistent.

Un detall poc discutit és que .NET 8 i .NET 9 convergeixen a la mateixa data de finalització. Això comprimeix les finestres d'actualització per a les organitzacions que van escalonar l'adopció esperant més marge. Si us vau moure a .NET 9 per accedir a funcions, encara aterreu al mateix penya-segat de suport.

Per als líders de plataforma, la matriu de decisió és simple: migrar abans de la data límit, o documentar i acceptar el risc no suportat amb controls compensatoris. No hi ha una tercera opció on res canviï.

La bona notícia és que .NET 10 és un objectiu LTS fins al novembre de 2028, cosa que compra una pista estable un cop completeu el moviment.

No espereu l'últim Patch Tuesday per començar. Tracteu això com una data límit de lliurament amb implicacions de seguretat, perquè això és exactament el que és.