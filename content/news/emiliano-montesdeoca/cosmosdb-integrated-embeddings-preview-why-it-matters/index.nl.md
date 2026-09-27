---
title: "Geïntegreerde embeddings in Cosmos DB verwijderen een van de vervelendste AI-bekabelingsklussen"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Integrated Embeddings in Azure Cosmos DB is nu in publieke preview. De grote winst is simpel: embeddings blijven gesynchroniseerd met je data zonder dat je een aparte updatepijplijn moet bouwen en onderhouden."
tags:
  - Azure Cosmos DB
  - AI
  - Embeddings
  - RAG
  - Azure
---

Iedereen die een RAG-achtig systeem heeft gebouwd bovenop operationele data, weet dat het vervelende deel vaak niet vectorzoeken zelf is.

Het is embeddings actueel houden.

Daarom is de **Integrated Embeddings**-preview in Azure Cosmos DB zo'n praktische aankondiging. Het verwijdert een van de minst leuke onderdelen van AI-applicatiebekabeling: de aparte pijplijn die wijzigingen in de gaten houdt, embeddings regenereert, retries afhandelt en vectoren correct terugschrijft.

## Het bronartikel benoemt de echte pijn direct

De originele post zegt: "**Ze gesynchroniseerd houden met je data is het moeilijke deel**."

Precies.

Dat is het probleem.

Het moeilijkste deel in veel AI-ondersteunde data-applicaties is niet het laten werken van de eerste semantische query. Het is ervoor zorgen dat het systeem een week later niet stilletjes uit sync raakt met de realiteit.

Daar begint de operationele last zich te tonen:

- wijzigingsdetectie
- retries
- throttling
- her-embedding-logica
- correctheid van terugschrijven
- het geheel monitoren

Dat is veel bekabeling alleen om retrieval eerlijk te houden.

## Dit is een feature die werk wegneemt, niet alleen mogelijkheden toevoegt

Als Cosmos DB nu automatisch embeddings kan genereren en onderhouden naarmate data verandert, zijn de voordelen direct:

- minder bewegende delen
- minder synchronisatiedrift
- minder aangepaste infrastructuur
- eenvoudigere RAG- en semantische retrieval-architecturen

Dat is het soort platformfeature dat ik waardeer omdat het operationele last vermindert, niet alleen conceptuele complexiteit.

En in echte teams is operationele last meestal het ding dat goede prototypes doodt.

## De praktische consequentie is groter dan het klinkt

Dit gaat niet alleen over gemak.

Het verandert welke soorten teams realistisch AI-ondersteunde data-apps kunnen bouwen zonder een heel side-systeem voor embeddingsonderhoud te moeten opzetten.

Dat is vooral belangrijk voor:

- productteams met beperkte platformbandbreedte
- interne app-teams die kennisgedreven tools bouwen
- kleinere engineeringgroepen die werkende retrieval nodig hebben zonder toegewijde ML-infra

## Mijn standpunt

Integrated Embeddings lijkt een van die features die AI-ondersteunde apps stilletjes makkelijker maken om uit te leveren.

Het is niet de meest glamoureuze aankondiging in de reeks, maar voor teams die met Cosmos DB plus retrieval- of semantische zoekpatronen werken, kan het veel repetitieve bekabeling wegnemen.

En eerlijk gezegd zijn dat vaak de meest waardevolle platformverbeteringen.

Oorspronkelijke post: [Announcing the Public Preview of Integrated Embeddings in Azure Cosmos DB: Build AI Apps With Embeddings That Stay in Sync](https://devblogs.microsoft.com/cosmosdb/announcing-the-public-preview-of-integrated-embeddings-in-azure-cosmos-db-build-ai-apps-with-embeddings-that-stay-in-sync/)