---
title: "Servidor SQL MCP: la manera correcta de donar accés a la base de dades d'AI Agents"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "El servidor SQL MCP del creador d'API de dades ofereix als agents d'IA un accés segur i determinista a la base de dades sense exposar esquemes ni confiar en NL2SQL. RBAC, emmagatzematge en memòria cau, suport multibase de dades, tot integrat."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

Siguem sincers: la majoria dels servidors MCP de bases de dades disponibles avui dia són aterridors. Prenen una consulta en llenguatge natural, generen SQL sobre la marxa i l'executen amb les dades de producció. Què podria sortir malament? (Tot. Tot podria sortir malament.)

L'equip d'Azure SQL acaba de [introduir SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), i té un enfocament fonamentalment diferent. Creat com a característica del Data API Builder (DAB) 2.0, ofereix als agents d'IA un accés estructurat i determinista a les operacions de la base de dades, sense NL2SQL, sense exposar el vostre esquema i amb RBAC complet a cada pas.

## Per què no NL2SQL?

Aquesta és la decisió de disseny més interessant. Els models no són deterministes i les consultes complexes tenen més probabilitats de produir errors subtils. Les consultes exactes que els usuaris esperen que l'IA pugui generar són també les que necessiten més escrutini quan es produeixen de manera no determinista.

En lloc d'això, SQL MCP Server utilitza un enfocament **NL2DAB**. L'agent treballa amb la capa d'abstracció d'entitats del creador de l'API de dades i el creador de consultes integrat per produir un T-SQL precís i ben format de manera determinista. Mateix resultat per a l'usuari, però sense risc de JOIN al·lucinats o exposició accidental de dades.

## Set eines, no set-centes

SQL MCP Server exposa exactament set eines DML, independentment de la mida de la base de dades:

- `describe_entities` — descobreix entitats i operacions disponibles
- `create_record` — inserir files
- `read_records` — consulteu taules i vistes
- `update_record` — modifica les files
- `delete_record` — elimina les files
- `execute_entity` — executa procediments emmagatzemats
- `aggregate_records` — consultes d'agregació

Això és intel·ligent perquè les finestres de context són l'espai de pensament de l'agent. Inundar-los amb centenars de definicions d'eines deixa menys espai per al raonament. Set eines fixes mantenen l'agent centrat a *pensar* en lloc de *navegar*.

Cada eina es pot activar o desactivar individualment:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Com començar en tres ordres

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Això és un servidor SQL MCP en execució que exposa la vostra taula de clients. La capa d'abstracció d'entitats significa que podeu aliar noms i columnes, limitar camps per rol i controlar exactament el que veuen els agents, sense exposar els detalls de l'esquema intern.

## La història de seguretat és sòlida

Aquí és on la maduresa del creador de l'API de dades té els seus fruits:

- **RBAC a cada capa**: cada entitat defineix quins rols poden llegir, crear, actualitzar o suprimir i quins camps són visibles
- **Integració d'Azure Key Vault**: cadenes de connexió i secrets gestionats de manera segura
- **Microsoft Entra + OAuth personalitzat**: autenticació de grau de producció
- **Política de seguretat de contingut**: els agents interactuen mitjançant un contracte controlat, no SQL brut

L'abstracció de l'esquema és especialment important. Els noms de les vostres taules i columnes internes mai s'exposen a l'agent. Definiu entitats, àlies i descripcions que tinguin sentit per a la interacció de l'IA, no la vostra base de dades ERD.

## Multibase de dades i multiprotocol

SQL MCP Server és compatible amb Microsoft SQL, PostgreSQL, Azure Cosmos DB i MySQL. I com que és una funció DAB, obteniu punts finals REST, GraphQL i MCP simultàniament des de la mateixa configuració. Les mateixes definicions d'entitat, les mateixes regles RBAC, la mateixa seguretat, als tres protocols.

La configuració automàtica a DAB 2.0 pot fins i tot inspeccionar la vostra base de dades i crear la configuració de manera dinàmica, si us sentiu còmode amb menys abstracció per a la creació de prototips ràpids.

## La meva opinió

Així és com hauria de funcionar l'accés a la base de dades empresarial per als agents d'IA. No "hey LLM, escriu-me una mica d'SQL i YOLO contra la producció". En lloc d'això: una capa d'entitat ben definida, generació de consultes deterministes, RBAC a cada pas, memòria cau, monitorització i telemetria. És avorrit de la millor manera possible.

Per als desenvolupadors de.NET, la història d'integració és neta: DAB és una eina.NET, el servidor MCP s'executa com a contenidor i funciona amb Azure SQL, que la majoria de nosaltres ja estem utilitzant. Si esteu creant agents d'IA que necessiten accés a dades, comenceu aquí.

## Tancant

SQL MCP Server és gratuït, de codi obert i s'executa a qualsevol lloc. És l'enfocament prescriptiu de Microsoft per oferir als agents d'IA un accés segur a la base de dades. Consulteu la [publicació completa](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) i la [documentació](https://aka.ms/sql/mcp) per començar.
