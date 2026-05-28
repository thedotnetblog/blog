---
title: "Foundry Local 1.1: Realtime Transcriptie, Embeddings en de Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 voegt live microfoon-transcriptie, tekst-embeddings en Responses API-ondersteuning toe — allemaal lokaal uitgevoerd zonder cloudafhankelijkheid, zonder netwerklatentie, zonder kosten per token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 bewees het concept: AI-modellen lokaal uitvoeren op Windows, macOS (Apple Silicon) en Linux x64 met een ontwikkelaarsvriendelijke SDK. Versie 1.1 voegt drie mogelijkheden toe die veel echte productie-gebruiksscenario's dekken.

## Live Audiotranscriptie

De meest significante nieuwe functie: realtime spraak-naar-tekst streaming rechtstreeks van de microfoon. Ondertiteling, spraakinterfaces, vergadertranscriptie, toegankelijkheidshulpmiddelen — alles lokaal uitgevoerd zonder enige cloudafhankelijkheid.

De API is sessiegebaseerd en streamt resultaten zodra ze binnenkomen, met `is_final`-markeringen om tussentijdse van definitieve tekst te onderscheiden. Beschikbaar voor alle taalbindingen: JavaScript, C#, Python en Rust.

Laad een streaming spraakmodel uit de catalogus, maak een sessie met audio-instellingen (samplerate, kanalen, taal), start hem, stuur ruwe PCM-audiobrokken en verbruik de asynchrone stroom resultaten. De post bevat volledige Python- en C#-voorbeelden.

## Tekst-Embeddings

Semantisch zoeken, RAG-pijplijnen, clustering, overeenkomstenmatching — dit alles vereist embeddings. Foundry Local 1.1 voegt ondersteuning voor embedding-modellen toe zodat u lokaal vectoren kunt genereren via dezelfde SDK, zonder gegevens naar een cloud-endpoint te sturen.

Voor toepassingen waar gegevensresidentie belangrijk is of waarbij u gevoelige inhoud verwerkt, is lokale embedding-generatie een betekenisvolle mogelijkheid.

## Responses API

Foundry Local ondersteunt nu de [Responses API](https://platform.openai.com/docs/api-reference/responses) — de gestructureerde interface ontworpen voor agentische interacties. Dit voegt toe:

- **Tool-aanroepen** — laat lokaal draaiende modellen door u gedefinieerde tools aanroepen
- **Multimodale vision-taalinvoer** — geef afbeelding + tekst door aan vision-geschikte modellen
- Compatibel met de standaard API-vorm, zodat bestaande agents gericht op OpenAI's Responses API werken met lokale modellen

## Verbeteringen Pakketgrootte

Twee wijzigingen verkleinen de JavaScript-pakketgrootte:
- De `koffi` FFI-laag is vervangen door een aangepaste Node-API C-addon
- De WebGPU-uitvoeringsprovider wordt als afzonderlijke plugin meegeleverd, zodat toepassingen zonder GPU-versnelling geen groottekosten betalen

De C# SDK richt zich nu op lagere frameworkversies voor bredere .NET-compatibiliteit.

## Waarom Dit Belangrijk Is

De drie mogelijkheden samen — transcriptie, embeddings, tool-aanroepen — dekken de kernbouwstenen van veel AI-toepassingen. Ze lokaal uitvoeren betekent:
- Geen internet vereist
- Geen kosten per token
- Geen gegevens die de machine verlaten
- Consistente latentie ongeacht netwerkomstandigheden

Foundry Local is de juiste keuze voor edge-scenario's, privacygevoelige workloads, offline toepassingen, of alles waarbij u cloudafhankelijkheid wilt vermijden tijdens ontwikkeling.

Originele post: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
