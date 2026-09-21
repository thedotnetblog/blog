---
title: "Unveränderliches Backup für Cosmos DB ist die Art von Funktion, die man zu spät schätzt"
date: 2026-06-27
author: "Emiliano Montesdeoca"
description: "Azure Backup für Azure Cosmos DB fügt jetzt unveränderliche Backups und Langzeitaufbewahrung in der öffentlichen Vorschau hinzu. Der Kernpunkt ist nicht nur die Wiederherstellung, sondern die Verbesserung der Resilienz und Beweiserhaltung für regulierte oder risikoreiche Workloads."
tags:
  - Azure Cosmos DB
  - Azure
  - Backup
  - Security
  - Resilience
---

Backup-Funktionen sind leicht zu ignorieren, bis zu dem Moment, in dem sie das Wichtigste im Raum werden.

Deshalb verdient die neue **Azure Backup für Azure Cosmos DB**-Vorschau Aufmerksamkeit.

Der interessante Teil hier ist nicht nur "eine weitere Backup-Option". Es ist die Hinzufügung von **unveränderlichen Wiederherstellungspunkten** und **Langzeitaufbewahrung** in einem Modell, das viel besser auf Ransomware-Bereitschaft, Auditierbarkeit und regulierte Wiederherstellungsanforderungen abgestimmt ist.

## Unveränderlichkeit ändert das Gespräch

Wenn Angreifer Produktionssysteme angreifen, ist die nächste Frage nicht mehr nur "haben wir ein Backup?"

Sie lautet:

- kann dem Backup vertraut werden?
- kann es geändert oder gelöscht werden?
- haben wir noch einen geschützten Wiederherstellungspunkt, nachdem der Vorfall begonnen hat?

Deshalb sind unveränderliche Backups wichtig. Sie verbessern den Wiederherstellungspfad, wenn die Umgebung um sie herum nicht mehr vertrauenswürdig sein könnte.

## Meine Meinung

Dies ist nicht die Art von Ankündigung, die alle begeistert.

Aber für Teams, die kritische Workloads auf Cosmos DB betreiben, ist es genau die Art von Fähigkeit, die am schlechtesten Tag des Quartals zentral wird.

Und das sind oft die wichtigsten Funktionen, die man im Auge behalten sollte.

Originalquelle: [Azure Backup for Azure Cosmos DB Public Preview Adds Immutable Backups and Long-Term Retention](https://devblogs.microsoft.com/cosmosdb/azure-backup-for-azure-cosmos-db-public-preview-adds-immutable-backups-and-long-term-retention/)