---
title: "Foundry Local 1.1: Transcripció en Temps Real, Embeddings i la Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 afegeix transcripció en directe des del micròfon, embeddings de text i suport per a la Responses API — tot funcionant localment sense dependència del núvol, sense latència de xarxa, sense cost per token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 va provar el concepte: executar models d'IA localment a Windows, macOS (Apple Silicon) i Linux x64 amb un SDK amigable per als desenvolupadors. La versió 1.1 afegeix tres capacitats que cobreixen molts casos d'ús de producció reals.

## Transcripció d'Àudio en Directe

La nova característica més significativa: transmissió de veu a text en temps real directament des del micròfon. Subtítols, interfícies de veu, transcripció de reunions, eines d'accessibilitat — tot funcionant localment sense cap dependència del núvol.

L'API és basada en sessions i transmet els resultats a mesura que arriben, amb marcadors `is_final` per distingir el text provisional del finalitzat. Disponible per a totes les vinculacions de llenguatge: JavaScript, C#, Python i Rust.

Carregueu un model de veu per a transmissió del catàleg, creeu una sessió amb la configuració d'àudio (taxa de mostreig, canals, idioma), inicieu-la, envieu fragments d'àudio PCM en brut i consumiu el flux asíncron de resultats. La publicació té exemples complets en Python i C#.

## Embeddings de Text

Cerca semàntica, pipelines RAG, agrupació, coincidència de similitud — tot això necessita embeddings. Foundry Local 1.1 afegeix suport per a models d'embedding perquè pugeu generar vectors localment des del mateix SDK sense enviar dades a un punt final al núvol.

Per a aplicacions on la residència de dades és important o on es processa contingut sensible, la generació local d'embeddings és una capacitat significativa.

## Responses API

Foundry Local ara suporta la [Responses API](https://platform.openai.com/docs/api-reference/responses) — la interfície estructurada dissenyada per a interaccions agèntiques. Això afegeix:

- **Crida d'eines** — permeteu que els models que s'executen localment invokin les eines que heu definit
- **Entrada multimodal de visió i llenguatge** — passeu imatge + text als models amb capacitat de visió
- Compatible amb la forma estàndard de l'API, de manera que els agents existents que apunten a la Responses API d'OpenAI funcionen amb models locals

## Millores de Mida del Paquet

Dos canvis redueixen la mida del paquet JavaScript:
- La capa FFI `koffi` s'ha substituït per un addon C personalitzat de Node-API
- El proveïdor d'execució WebGPU s'inclou com a connector separat, de manera que les aplicacions que no necessiten acceleració GPU no paguen el cost de mida

L'SDK de C# ara apunta a versions inferiors del framework per a una compatibilitat .NET més àmplia.

## Per Què Importa

Les tres capacitats juntes — transcripció, embeddings, crida d'eines — cobreixen els blocs de construcció fonamentals de moltes aplicacions d'IA. Executar-les localment significa:
- No es necessita internet
- Sense costos per token
- Cap dada surt de la màquina
- Latència consistent independentment de les condicions de xarxa

Foundry Local és la millor elecció per a escenaris edge, càrregues de treball sensibles a la privadesa, aplicacions fora de línia, o qualsevol cosa en la qual vulgueu evitar la dependència del núvol durant el desenvolupament.

Publicació original: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
