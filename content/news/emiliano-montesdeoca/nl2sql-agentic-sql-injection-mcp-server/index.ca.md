---
title: "NL2SQL és la Injecció SQL de l'Era dels Agents"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Abans de deixar que un agent consulti la teva base de dades amb llenguatge natural, llegeix això. NL2SQL sembla senzill fins que penses en la completesa de l'esquema, el no-determinisme i el que SQL MCP Server realment resol."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Hi ha una versió del pitch de NL2SQL que sona perfecta: els usuaris fan preguntes en llenguatge natural, els agents generen SQL, les dades tornen. Menys pantalles, menys consultes, menys codi. Senzill.

Llavors hi penses cinc minuts més.

## Els Problemes de Què Ningú Parla en la Demo

**Els esquemes no van ser dissenyats per explicar coses.** Noms de taules críptics, noms de columnes inconsistents, relacions tècnicament vàlides que són semànticament invàlides sense predicats addicionals — això és normal en bases de dades empresarials. No són errors, és simplement la història acumulada de canvis de negoci. Però quan demanes a un model que infereixi la intenció d'un esquema que no va ser dissenyat per transmetre intenció, el model ho intentarà de totes formes. No es rendirà. Generarà la seva millor consulta i retornarà els resultats amb confiança.

**Els models no són deterministes.** Fes la mateixa pregunta a la mateixa base de dades dues vegades i podries obtenir SQL diferent. El model calcula probabilitats, i petites variacions en el context produeixen sortides diferents. No pots aconseguir una garantia a través de proves que l'agent sempre generi la consulta correcta.

**La revisió d'usuari no escala.** "Simplement revisa cada consulta abans de l'execució" sembla segur. Però assumeix que els usuaris són experts tant en el model de dades com en SQL — exactament les persones que no necessitaven una interfície de llenguatge natural. També introdueix sobrecàrrega cognitiva i una nova classe de biaix de confirmació, on els usuaris aclaparats per la complexitat de la consulta aproven consultes invàlides en lloc d'investigar-les.

**I llavors hi ha la injecció.** En el desenvolupament SQL tradicional, la parametrització resolia la injecció perquè l'entrada de l'usuari omplia paràmetres, no l'estructura SQL. Amb NL2SQL, el model genera el propi SQL. El prompt, el context de l'esquema, l'historial de la conversa i les dades recuperades influeixen en el que s'executa. Si algú elabora un prompt que canvia el que genera el model, això és injecció — no a nivell de paràmetre, sinó a nivell de generació de consulta. I a diferència de DROP TABLE (obvi, recuperable), la injecció NL2SQL produeix consultes que retornen resultats incorrectes sense cap error visible. Les decisions de negoci es prenen sobre dades incorrectes.

## El Que SQL MCP Server Realment Resol

Aquí l'article fa el seu punt pràctic més útil. En lloc de donar a l'agent accés arbitrari a l'esquema i esperar el millor, SQL MPC Server exposa una **superfície API curada** construïda sobre [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

La diferència importa: l'agent no genera SQL. Crida endpoints nomenats que retornen formes de resultat predefinides. El SQL s'escriu una vegada, per un desenvolupador, i és determinista. El no-determinisme de l'agent es limita a triar *quin* endpoint cridar, no a compondre consultes arbitràries.

Això és anàleg al que va fer la parametrització per a la injecció SQL en el model d'aplicació tradicional — elimina la capacitat de compondre consultes arbitràries a partir d'entrades no fiables.

## La Pregunta Correcta

L'article no diu "mai facis servir NL2SQL." Diu: sigues deliberat sobre *on* l'apliques i *què* exposes. Per a anàlisis exploratòries en un entorn controlat, amb un esquema d'abast limitat i accés de només lectura, NL2SQL pot estar bé. Per a sistemes de producció on les decisions de negoci depenen dels resultats, una capa API curada és considerablement més segura.

Honestament: alguns problemes es resolen veritablement millor amb consultes estructurades darrere d'endpoints nomenats que amb llenguatge natural a SQL. SQL MCP Server et dona aquesta opció sense abandonar completament la interfície agèntica.

Post original: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
