---
title: "Foundry Local 1.1: Echtzeit-Transkription, Embeddings und die Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 fügt Live-Mikrofon-Transkription, Text-Embeddings und Unterstützung für die Responses API hinzu — alles lokal ausgeführt ohne Cloud-Abhängigkeit, ohne Netzwerklatenz, ohne Kosten pro Token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 hat das Konzept bewiesen: KI-Modelle lokal auf Windows, macOS (Apple Silicon) und Linux x64 mit einem entwicklerfreundlichen SDK ausführen. Version 1.1 fügt drei Fähigkeiten hinzu, die viele echte Produktionsanwendungsfälle abdecken.

## Live-Audio-Transkription

Die bedeutendste neue Funktion: Echtzeit-Sprache-zu-Text-Streaming direkt vom Mikrofon. Untertitel, Sprach-UIs, Meeting-Transkription, Barrierefreiheitswerkzeuge — alles lokal ohne jede Cloud-Abhängigkeit.

Die API ist sitzungsbasiert und überträgt Ergebnisse, sobald sie eintreffen, mit `is_final`-Markierungen zur Unterscheidung von vorläufigem und finalisiertem Text. Verfügbar für alle Sprachbindungen: JavaScript, C#, Python und Rust.

Laden Sie ein Streaming-Sprachmodell aus dem Katalog, erstellen Sie eine Sitzung mit Audio-Einstellungen (Abtastrate, Kanäle, Sprache), starten Sie sie, schieben Sie rohe PCM-Audio-Chunks und konsumieren Sie den asynchronen Stream von Ergebnissen. Der Post enthält vollständige Python- und C#-Beispiele.

## Text-Embeddings

Semantische Suche, RAG-Pipelines, Clustering, Ähnlichkeitsvergleich — all das erfordert Embeddings. Foundry Local 1.1 fügt Unterstützung für Embedding-Modelle hinzu, sodass Sie Vektoren lokal aus demselben SDK generieren können, ohne Daten an einen Cloud-Endpoint zu senden.

Für Anwendungen, bei denen die Datenresidenz wichtig ist oder bei denen Sie sensible Inhalte verarbeiten, ist die lokale Embedding-Generierung eine bedeutsame Fähigkeit.

## Responses API

Foundry Local unterstützt jetzt die [Responses API](https://platform.openai.com/docs/api-reference/responses) — die strukturierte Schnittstelle für agentische Interaktionen. Dies fügt hinzu:

- **Tool-Aufruf** — lassen Sie lokal ausgeführte Modelle von Ihnen definierte Werkzeuge aufrufen
- **Multimodale Vision-Sprach-Eingabe** — übergeben Sie Bild + Text an vision-fähige Modelle
- Kompatibel mit der Standard-API-Form, sodass vorhandene Agenten, die auf die Responses API von OpenAI abzielen, gegen lokale Modelle funktionieren

## Verbesserungen der Paketgröße

Zwei Änderungen reduzieren die JavaScript-Paketgröße:
- Die `koffi`-FFI-Schicht wurde durch ein benutzerdefiniertes Node-API-C-Addon ersetzt
- Der WebGPU-Ausführungsanbieter wird als separates Plugin geliefert, sodass Anwendungen ohne GPU-Beschleunigung keine Größenkosten tragen

Das C#-SDK zielt jetzt auf niedrigere Framework-Versionen für breitere .NET-Kompatibilität ab.

## Warum Das Wichtig Ist

Die drei Fähigkeiten zusammen — Transkription, Embeddings, Tool-Aufruf — decken die Kernbausteine vieler KI-Anwendungen ab. Sie lokal auszuführen bedeutet:
- Kein Internet erforderlich
- Keine Kosten pro Token
- Keine Daten verlassen die Maschine
- Konsistente Latenz unabhängig von Netzwerkbedingungen

Foundry Local ist die richtige Wahl für Edge-Szenarien, datenschutzsensible Workloads, Offline-Anwendungen oder alles, wo Sie Cloud-Abhängigkeit während der Entwicklung vermeiden möchten.

Originalbeitrag: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
