---
title: "Azure DevOps Server April 2026 Patch — PR-afrondingsoplossing en Beveiligingsupdates"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server krijgt Patch 3 met een oplossing voor PR-afrondingsfouten, verbeterde afmeldvalidatie en herstelde GitHub Enterprise Server PAT-verbindingen."
tags:
  - azure-devops
  - devops
  - patches
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-devops-server-april-2026-patch" >}}).*

Snel bericht voor teams die zelf gehoste Azure DevOps Server draaien: Microsoft heeft [Patch 3 voor april 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) uitgebracht met drie gerichte fixes.

## Wat er opgelost is

- **Pull request-afrondingsfouten** — een null reference exception bij automatisch afronden van werkitems kon PR-merges laten mislukken
- **Afmeldomleidingsvalidatie** — verbeterde validatie bij afmelden om potentieel kwaadaardige omleidingen te voorkomen
- **GitHub Enterprise Server PAT-verbindingen** — het aanmaken van Personal Access Token-verbindingen is hersteld

## Hoe te updaten

Download [Patch 3](https://aka.ms/devopsserverpatch3) en voer het installatieprogramma uit. Controleer of de patch is toegepast:

```bash
<patch-installer>.exe CheckInstall
```

Microsoft raadt sterk aan om op de nieuwste patch te blijven voor zowel veiligheid als betrouwbaarheid.
