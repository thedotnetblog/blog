---
title: "azd update — Één Opdracht voor Al je Package Managers"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "De Azure Developer CLI heeft nu een universele updateopdracht die werkt ongeacht hoe je het hebt geïnstalleerd — winget, Homebrew, Chocolatey of installatiescript."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azd-update-universal-upgrade-command" >}}).*

Ken je dat bericht "Een nieuwe versie van azd is beschikbaar" dat elke paar weken verschijnt? De boodschap die je wegklikt omdat je niet meer weet of je `azd` via winget, Homebrew of dat curl-script van zes maanden geleden hebt geïnstalleerd? Dat is eindelijk opgelost.

Microsoft heeft zojuist [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) uitgebracht — één opdracht die de Azure Developer CLI bijwerkt naar de nieuwste versie, ongeacht hoe je het oorspronkelijk hebt geïnstalleerd.

## Hoe het werkt

```bash
azd update
```

Dat is alles. Voor vroege toegang tot nieuwe functies:

```bash
azd update --channel daily
azd update --channel stable
```

De opdracht detecteert je huidige installatiemethode en gebruikt het juiste updatemechanisme.

## De kleine vangst

`azd update` wordt geleverd vanaf versie 1.23.x. Als je een oudere versie hebt, moet je één laatste handmatige update uitvoeren. Daarna regelt `azd update` alles.

## Waarom het uitmaakt

Dit is een kleine kwaliteitsverbetering, maar voor degenen onder ons die `azd` dagelijks gebruiken voor het implementeren van AI-agents en Aspire-apps naar Azure, is het bijblijven belangrijk.

Lees de [volledige aankondiging](https://devblogs.microsoft.com/azure-sdk/azd-update/).
