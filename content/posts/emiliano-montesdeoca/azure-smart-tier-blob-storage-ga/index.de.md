---
title: "Azure Smart Tier ist GA — Automatische Kostenoptimierung für Blob Storage ohne Lifecycle-Regeln"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Blob Storage Smart Tier ist jetzt allgemein verfügbar und verschiebt Objekte automatisch zwischen Hot-, Cool- und Cold-Tiers basierend auf tatsächlichen Zugriffsmustern — ganz ohne Lifecycle-Regeln."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azure-smart-tier-blob-storage-ga.md" >}}).*

Wenn du jemals Zeit damit verbracht hast, Azure Blob Storage Lifecycle-Richtlinien zu optimieren und dann zugesehen hast, wie sie auseinanderfallen, sobald sich die Zugriffsmuster geändert haben, ist das hier für dich. Microsoft hat gerade die [allgemeine Verfügbarkeit von Smart Tier](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) für Azure Blob und Data Lake Storage angekündigt — eine vollständig verwaltete Tiering-Funktion, die Objekte automatisch zwischen Hot-, Cool- und Cold-Tiers basierend auf der tatsächlichen Nutzung verschiebt.

## Was Smart Tier tatsächlich macht

Das Konzept ist einfach: Smart Tier wertet kontinuierlich die letzte Zugriffszeit jedes Objekts in deinem Speicherkonto aus. Häufig abgerufene Daten bleiben in Hot, inaktive Daten werden nach 30 Tagen nach Cool verschoben und nach weiteren 60 Tagen nach Cold. Wenn auf die Daten erneut zugegriffen wird, werden sie sofort wieder auf Hot hochgestuft. Der Zyklus beginnt von vorne.

Keine Lifecycle-Regeln zu konfigurieren. Keine Vorhersagen von Zugriffsmustern. Kein manuelles Tuning.

Während der Preview berichtete Microsoft, dass **über 50% der von Smart Tier verwalteten Kapazität automatisch in kühlere Tiers verschoben wurde** — basierend auf tatsächlichen Zugriffsmustern. Das ist eine deutliche Kostenreduzierung für große Speicherkonten.

## Warum das für .NET-Entwickler wichtig ist

Wenn du Anwendungen baust, die Logs, Telemetrie, Analysedaten oder irgendeine Art von wachsendem Datenbestand erzeugen — und mal ehrlich, wer tut das nicht? — summieren sich die Speicherkosten schnell. Der traditionelle Ansatz war, Lifecycle-Management-Richtlinien zu schreiben, sie zu testen und dann neu anzupassen, wenn sich die Zugriffsmuster deiner App geändert haben. Smart Tier eliminiert diesen gesamten Workflow.

Einige praktische Szenarien, in denen das hilft:

- **Anwendungstelemetrie und Logs** — Hot beim Debuggen, nach ein paar Wochen kaum noch abgerufen
- **Datenpipelines und ETL-Ausgaben** — während der Verarbeitung stark genutzt, danach meistens Cold
- **Benutzergenerierte Inhalte** — aktuelle Uploads sind Hot, ältere Inhalte kühlen allmählich ab
- **Backup- und Archivdaten** — gelegentlich für Compliance abgerufen, meistens inaktiv

## Einrichtung

Smart Tier zu aktivieren ist eine einmalige Konfiguration:

- **Neue Konten**: Wähle Smart Tier als Standard-Zugangstier während der Erstellung des Speicherkontos (zonale Redundanz erforderlich)
- **Bestehende Konten**: Wechsle den Blob-Zugangstier von deiner aktuellen Standardeinstellung zu Smart Tier

Objekte kleiner als 128 KiB bleiben in Hot und verursachen keine Überwachungsgebühr. Für alles andere zahlst du die Standard-Kapazitätstarife für Hot/Cool/Cold — ohne Tier-Übergangsgebühren, ohne Gebühren für vorzeitige Löschung und ohne Datenabrufkosten. Eine monatliche Überwachungsgebühr pro Objekt deckt die Orchestrierung ab.

## Der Kompromiss, den du kennen solltest

Die Tiering-Regeln von Smart Tier sind statisch (30 Tage → Cool, 90 Tage → Cold). Wenn du benutzerdefinierte Schwellenwerte brauchst — zum Beispiel nach 7 Tagen für eine bestimmte Workload nach Cool verschieben — sind Lifecycle-Regeln weiterhin der richtige Weg. Und mische nicht beides: Vermeide es, Lifecycle-Regeln auf von Smart Tier verwaltete Objekte anzuwenden, da sie in Konflikt geraten können.

## Fazit

Das ist nicht revolutionär, aber es löst ein echtes operatives Problem. Wenn du wachsende Blob-Storage-Konten verwaltest und es leid bist, Lifecycle-Richtlinien zu pflegen, [aktiviere Smart Tier](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) und lass Azure sich darum kümmern. Es ist heute in fast allen zonalen Public-Cloud-Regionen verfügbar.
