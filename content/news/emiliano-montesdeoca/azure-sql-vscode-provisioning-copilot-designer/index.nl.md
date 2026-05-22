---
title: "De MSSQL-extensie voor VS Code wordt stilletjes een veel groter platform"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "De nieuwste update van de MSSQL-extensie voegt Azure SQL-provisioning, Copilot-ondersteund schemaontwerp, Data API Builder en notebooks toe. Het interessante is hoeveel databasewerk nu binnen VS Code kan blijven."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Dit artikel is automatisch vertaald. Voor de oorspronkelijke versie, [klik hier]({{< ref "index.md" >}}).*

De MSSQL-extensie voor VS Code groeit al een tijd, maar deze nieuwste update maakt de richting veel duidelijker.

Het is niet meer alleen «verbinden en een paar queries draaien».

Met **Azure SQL-provisioning**, **Schema Designer met Copilot**, **SQL Notebooks** en **Data API Builder** die allemaal in één release worden doorontwikkeld, wordt de extensie een veel completere werkruimte voor databasegerichte ontwikkeling.

## De praktische haak is provisioning direct vanuit de editor

De bronpost zegt dat je nu een volledig beheerde cloud-database «direct vanuit je editor en zonder kosten» kunt maken met de gratis tier.

Dat is het soort functie dat klein lijkt totdat je beseft hoeveel setup-frictie het wegneemt.

Voor veel ontwikkelaars zit het vervelende deel van data-zware experimenten niet in SQL zelf. Het zit in de omgevingskloof tussen:

- idee
- database
- schema
- API
- testbare backend

Als die kloof kleiner wordt binnen één tool, wordt de hele workflow aantrekkelijker.

## Dit is hoe een sterkere inner loop voor datawerk eruitziet

Wat ik aan deze release waardeer, is dat meer van de databaseworkflow op één plek blijft:

- database provisioneren
- schema ontwerpen
- wijzigingen beoordelen
- ORM-scripts genereren
- API's exposen
- endpoints testen
- documenteren en queryen via notebooks

Dat is een veel overtuigender verhaal dan SQL behandelen als een los zijgereedschap in de stack.

## De Copilot-ondersteunde schemaworkflow is waar de AI-waarde echt voelbaar wordt

De toevoegingen aan de schema-designer zijn vooral interessant omdat ze een goed evenwicht lijken te treffen.

De waarde is niet «AI ontwerpt je datamodel en jij vertrouwt er blind op».

De waarde is:

- snellere startpunten
- visuele review
- wijzigingstracking
- migratiegerichte output
- expliciete accept/undo-controles

Dat is een veel gezondere AI-workflow dan volledige auto-generatie zonder inspectiepad.

En voor databasewerk is reviewbaarheid heel belangrijk.

## Data API Builder is een stille vermenigvuldiger

De andere functie die ik niet zou negeren is de Data API Builder-integratie.

Als je binnen dezelfde omgeving van schema naar:

- REST
- GraphQL
- MCP-endpoints

kunt gaan, ontstaat een zeer efficiënt pad voor backendprototypes en interne tools.

Dat vervangt geen diepere backend engineering. Maar het verkort de weg van database-idee naar werkende interface absoluut.

## Mijn visie

Deze release laat de MSSQL-extensie meer aanvoelen als een klein platform in VS Code dan als een simpel add-on.

Voor ontwikkelaars die API's, datatools, beheertools of SQL-gestuurde prototypes bouwen, is dat een betekenisvolle verschuiving.

En als Microsoft deze loop blijft aanscherpen, wordt de extensie veel strategischer nuttig dan veel mensen nu nog aannemen.

Originele post: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)