---
title: "La Còpia de Seguretat Immutable per a Cosmos DB és el Tipus de Funció que Aprecies Massa Tard"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Backup per a Azure Cosmos DB ara afegeix còpies de seguretat immutables i retenció a llarg termini en previsualització pública. El punt clau no és només la recuperació, sinó millorar la resiliència i la preservació d'evidències per a càrregues de treball regulades o d'alt risc."
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

Les funcions de còpia de seguretat són fàcils d'ignorar fins al moment en què es converteixen en la cosa més important de la sala.

Per això crec que la nova previsualització d'**Azure Backup per a Azure Cosmos DB** mereix atenció.

La part interessant aquí no és merament "una altra opció de còpia de seguretat." És l'addició de **punts de recuperació immutables** i **retenció a llarg termini** en un model que està molt més alineat amb la preparació contra ransomware, l'auditabilitat i els requisits de recuperació regulats.

## La immutabilitat canvia la conversa

Quan els atacants ataquen sistemes de producció, la següent pregunta ja no és només "tenim una còpia de seguretat?"

És:

- es pot confiar en la còpia de seguretat?
- es pot alterar o eliminar?
- encara tenim un punt de recuperació protegit després que comenci l'incident?

Per això importen les còpies de seguretat immutables. Milloren el camí de recuperació quan l'entorn al seu voltant ja no pot ser fiable.

## La meva opinió

Aquest no és el tipus d'anunci que emociona a tothom.

Però per als equips que executen càrregues de treball crítiques a Cosmos DB, és exactament el tipus de capacitat que es torna central durant el pitjor dia del trimestre.

I sovint aquestes són les funcions més importants de seguir.

Article original: [Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)