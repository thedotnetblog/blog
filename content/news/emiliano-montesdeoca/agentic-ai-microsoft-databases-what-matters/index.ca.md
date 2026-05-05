---
title: "Servidor SQL MCP, Copilot a SSMS i un concentrador de bases de dades amb agents d'IA: el que realment importa de SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft va deixar caure una pila d'anuncis de bases de dades a SQLCon 2026. Aquí teniu les coses que realment importen si esteu creant aplicacions basades en IA a Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft acaba de començar [SQLCon 2026 juntament amb FabCon a Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/), i hi ha molt per desempaquetar. L'anunci original cobreix des de plans d'estalvi fins a funcions de compliment empresarial. Vaig a ometre les diapositives de preus empresarials i em centraré en les peces que importen si sou un desenvolupador que construeix coses amb Azure SQL i AI.

## El servidor SQL MCP està en previsualització pública

Aquest és el titular per a mi. L'Azure SQL Database Hyperscale ara té un **SQL MCP Server** en previsualització pública que us permet connectar de manera segura les vostres dades SQL a agents d'IA i Copilots mitjançant el [Model Context Protocol](https://modelcontextprotocol.io/).

Si heu estat seguint l'onada MCP, i sincerament, és difícil perdre's ara mateix, això és un gran problema. En lloc de crear canalitzacions de dades personalitzades per alimentar el context dels vostres agents d'IA des de la vostra base de dades, obteniu un protocol estandarditzat per exposar les dades SQL directament. Els vostres agents poden consultar, raonar i actuar sobre la informació de la base de dades en directe.

Per a aquells de nosaltres que creem agents d'IA amb Semantic Kernel o Microsoft Agent Framework, això obre un camí d'integració net. El vostre agent necessita comprovar l'inventari? Busqueu un registre de client? Validar una comanda? MCP li ofereix una manera estructurada de fer-ho sense que escriviu codi d'obtenció de dades a mida per a cada escenari.

## GitHub Copilot a SSMS 22 ara és GA

Si passeu algun temps a SQL Server Management Studio (i siguem sincers, la majoria de nosaltres encara ho fem), GitHub Copilot ara està disponible generalment a SSMS 22. La mateixa experiència Copilot que ja feu servir a VS Code i Visual Studio, però per a T-SQL.

El valor pràctic aquí és senzill: assistència basada en xat per escriure consultes, refactoritzar procediments emmagatzemats, resoldre problemes de rendiment i gestionar tasques d'administració. No hi ha res revolucionari en concepte, però tenir-lo allà mateix a SSMS significa que no cal que canvieu de context a un altre editor només per obtenir ajuda d'IA amb el treball de la vostra base de dades.

## Els índexs vectorials han rebut una actualització seriosa

L'Azure SQL Database ara té índexs vectorials més ràpids i capaços amb suport complet per a la inserció, l'actualització i la supressió. Això vol dir que les vostres dades vectorials es mantenen actuals en temps real, sense necessitat de reindexació per lots.

Aquí teniu les novetats:
- **Quantització** per a mides d'índex més petites sense perdre massa precisió
- **Filtratge iteratiu** per obtenir resultats més precisos
- **Integració més estreta de l'optimitzador de consultes** per a un rendiment previsible

Si esteu fent la generació augmentada per la recuperació (RAG) amb Azure SQL com a magatzem de vectors, aquestes millores són directament útils. Podeu mantenir els vostres vectors al costat de les vostres dades relacionals a la mateixa base de dades, cosa que simplifica significativament la vostra arquitectura en comparació amb l'execució d'una base de dades vectorial separada.

Les mateixes millores vectorials també estan disponibles a la base de dades SQL a Fabric, ja que totes dues s'executen amb el mateix motor SQL a sota.

## Database Hub in Fabric: gestió agentica

Aquest és més avançat, però és interessant. Microsoft va anunciar el **Database Hub a Microsoft Fabric** (accés anticipat), que us ofereix un únic panell de vidre a Azure SQL, Cosmos DB, PostgreSQL, MySQL i SQL Server mitjançant Arc.

L'angle interessant no és només la visió unificada, sinó l'enfocament agent de la gestió. Els agents d'IA controlen contínuament el patrimoni de la vostra base de dades, evidencien què ha canviat, expliquen per què és important i suggereixen què fer a continuació. És un model human-in-the-loop on l'agent fa el treball i tu fas les trucades.

Per als equips que gestionen més d'un grapat de bases de dades, això podria reduir realment el soroll operatiu. En lloc de saltar entre portals i comprovar manualment les mètriques, l'agent us porta el senyal.

## Què significa això per als desenvolupadors de.NET

El fil que connecta tots aquests anuncis és clar: Microsoft està incorporant agents d'IA a cada capa de la pila de bases de dades. No com un truc, sinó com una capa d'eines pràctica.

Si esteu creant aplicacions.NET amb el suport d'Azure SQL, això és el que faria realment:

1. **Proveu el servidor SQL MCP** si esteu creant agents d'IA. És la manera més neta de donar accés a la base de dades dels vostres agents sense fontaneria personalitzada.
2. **Activa Copilot a SSMS** si encara no ho has fet: guanys de productivitat gratuïts per al treball SQL diari.
3. **Mira els índexs vectorials** si estàs fent RAG i actualment tens una botiga de vectors independent. La consolidació a Azure SQL significa un servei menys per gestionar.

## Tancant

L'anunci complet té més: plans d'estalvi, assistents de migració, funcions de compliment, però la història del desenvolupador es troba al servidor MCP, les millores vectorials i la capa de gestió agent. Aquestes són les peces que canvien la manera de construir, no només el pressupost.

Fes una ullada a l'[anunci complet de Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) per obtenir la imatge completa i [inscriu-te a l'accés anticipat al centre de bases de dades](https://aka.ms/database-hub) si vols provar la nova experiència de gestió.
