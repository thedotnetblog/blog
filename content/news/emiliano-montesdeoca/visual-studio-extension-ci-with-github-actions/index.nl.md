---
title: 'Visual Studio-extensieteams moeten stoppen met uitbrengen uit gewoonte en beginnen met uitbrengen via pipeline'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: 'Een herbruikbare GitHub Actions-flow voor VSIX-versiebeheer en publiceren is nu eenvoudig genoeg dat handmatige releasestappen moeilijk te rechtvaardigen zijn.'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Originele bron: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Als je Visual Studio-extensies onderhoudt en nog steeds aanzienlijke delen van de release handmatig uitvoert, is dit je signaal om te moderniseren.

De workflow in dit bericht is bewust praktisch: versie stempelen, bouwen, testartefacten publiceren naar een galerij, en vervolgens stabiele bits publiceren naar Marketplace. Geen zware platformceremonie, alleen deterministisch releasegedrag.

Wat ik het meest waardeer is dat versiebeheer wordt behandeld als pipelinestatus, niet als een pre-release checklist-item. Die ene beslissing elimineert een verrassend aantal fouten: niet-overeenkomende metadata, verouderde assembly-versies en inconsistente releasenotities.

De splitsing tussen galerijpublicatie en Marketplace-publicatie is ook operationeel volwassen. Teams hebben een plek nodig voor snelle validatiebuilds die geen officiële-releasesemantiek dragen. Alles direct naar Marketplace pushen is hoogfrictie en moedigt risicovolle shortcuts aan.

Een sterk releasepatroon voor extensieteams is:

Bij pull requests en main-commits, produceer CI VSIX-artefacten en publiceer naar galerij voor testers.

Bij getagde releases, publiceer ondertekende en gevalideerde pakketten naar Marketplace.

Houd tokenbeheer minimaal met speciale geheimen en zo min mogelijk rechten.

Mijn uitgesproken mening: extensie-ecosystemen lopen achter op app-ecosystemen in CI-discipline omdat kleine teams aannemen dat handmatige workflows beheersbaar zijn. Ze zijn beheersbaar tot ze dat niet meer zijn. Een gehaaste patch, een kapot pakket, een vergeten manifest-update, en het vertrouwen daalt.

Deze herbruikbare acties zijn nuttig omdat ze herhaalde releaselogica eenmalig coderen en teams zich kunnen concentreren op extensiekwaliteit in plaats van verpakkingsmechanica.

Er is nog steeds technisch inzicht nodig. Je moet Marketplace-publicatie afschermen achter kwaliteitscontroles, en je moet publicatiemanifesten behandelen als gecontroleerde release-artefacten. Maar de basispijplijncomplexiteit is nu laag genoeg dat handmatige releases meestal technische schuld zijn.

Als je extensieontwikkeling leidt, standaardiseer dit dan nu in alle repositories. Je krijgt betere traceerbaarheid, eenvoudigere onboarding en minder eenpersoonsreleaseknelpunten.

Voorgestelde uitrol:

Begin met build plus galerijpublicatie voor één extensie.

Introduceer versiestempeling na het valideren van je manifest-bronconventies.

Voeg Marketplace-publicatie pas toe nadat geheimbeheer en releasepoorten zijn geïnstalleerd.

Dit gaat niet over het najagen van DevOps-mode. Het gaat over betrouwbaarheid voor de mensen die je tooling installeren en verwachten dat updates werken.

Stabiele extensie-ecosystemen worden op dezelfde manier gebouwd als stabiele applicaties: met saaie, herhaalbare automatisering die menselijk giswerk elimineert.