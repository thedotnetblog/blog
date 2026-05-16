---
title: "Azure Developer CLI (azd) april 2026 updates"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd bracht in april 2026 vijf releases uit, met als highlight ondersteuning voor meertalige hooks voor Python, JavaScript, TypeScript en .NET — plus een publieke preview van azd update, AI-quotacontroles vooraf en meer."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[Azure Developer CLI (azd) bracht in april 2026 vijf releases uit](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 tot en met 1.24.2), met als groot thema hooks die nu draaien in Python, JavaScript, TypeScript en .NET — niet meer alleen in Bash en PowerShell.

## Meertalige hooks in azure.yaml

Hooks kunnen nu naast shellscripts verwijzen naar `.py`-, `.js`-, `.ts`- of `.cs`-bestanden. Elke taal krijgt automatische afhankelijkheidsresolutie:

- **Python** — detecteert `requirements.txt` of `pyproject.toml`, maakt een virtualenv aan en installeert afhankelijkheden vóór uitvoering. Configureer de env-naam met `virtualEnvName`.
- **JavaScript / TypeScript** — detecteert `package.json` en voert automatisch `npm install` uit. TypeScript wordt uitgevoerd via `npx tsx` zonder compilatiestap. Kies je pakketbeheerder met het configuratieblok `packageManager`.
- **.NET** — voert `.cs`-bestanden uit met `dotnet run`. Single-file scripts worden ondersteund op .NET 10+. Configureer het doelframework via het blok `configuration/framework`.

Dit betekent dat teams die al in een van deze talen werken, geen aparte Bash- of PowerShell-hook meer hoeven bij te houden alleen om provisioning-lifecycle-events te verbinden.

## azd update naar publieke preview

`azd update` is nu in publieke preview op alle platforms. Eén commando handelt de update af ongeacht hoe azd oorspronkelijk werd geïnstalleerd — niet meer afzonderlijk Homebrew-, WinGet- of MSI-paden volgen.

## Niet-interactieve modus via AZD_NON_INTERACTIVE

Het instellen van `AZD_NON_INTERACTIVE=true` (of het gebruik van `--non-interactive` / `--no-prompt`) levert nu consistente, deterministische fouten op in CI/CD-pipelines wanneer een vereiste invoer niet automatisch kan worden opgelost. Voorheen was het gedrag inconsistent tussen commando's.

## Voorafgaande controle van AI-modelquota

`azd provision` valideert Azure Cognitive Services-quota voordat er AI-modelresources worden ingericht. Deployments die zouden mislukken door quotalimieten tonen de fout nu vroeg in het proces in plaats van halverwege het inrichten.

## "Herstel deze fout" in Copilot-probleemoplossing

De Copilot-probleemoplossingintegratie in azd krijgt de mogelijkheid om een voorgestelde oplossing direct toe te passen — niet alleen te beschrijven. Wanneer de agent een herstelbaar probleem identificeert, kan het de wijziging ter plekke doorvoeren.

## Aangepaste provisioningproviders en Key Vault-geheimresolver

Extensieauteurs kunnen nu alternatieve infrastructuurbackends registreren met `WithProvisioningProvider()`. Afzonderlijk lost azd `@Microsoft.KeyVault(...)`-verwijzingen automatisch op voordat de configuratie aan extensies wordt doorgegeven, waardoor handmatige geheimresolutie in aangepaste providers niet meer nodig is.

## Uitsluitingen voor sjablonen en watch-modus

Twee nieuwe ignore-bestanden bieden nauwkeurigere controle over bestandsverwerking:
- **`.azdignore`** — sluit bijdrager-specifieke bestanden (documentatie, CI-configuraties) uit van sjabloonkopieën zodat eindgebruikers een schone projectscaffold krijgen.
- **`.azdxignore`** — sluit mappen uit van het activeren van rebuilds tijdens `azd x watch`, wat ruis vermindert tijdens iteratieve ontwikkeling.

## Preflight voor gereserveerde namen en docker.network-optie

azd waarschuwt nu wanneer voorspelde resourcenamen Azure-gereserveerde woorden (`MICROSOFT`, `WINDOWS` of het voorvoegsel `LOGIN`) bevatten voordat het inrichten begint. Een nieuwe `docker.network`-optie geeft `--network` door aan `docker build`, wat handig is in bedrijfsproxyomgevingen die een specifiek Docker-netwerk vereisen.

## Beveiligingsoplossingen

Het Windows MSI-pakket bevat nu codeondertekeningsverificatie. Een afzonderlijke oplossing sluit een omgevingsvariabelenlek dat waarden over extensiecommandobegrenzingen heen kon blootstellen.

---

Een drukke maand — de meertalige hooksupport elimineert met name een echt knelpunt voor teams die niet voornamelijk in Bash werken. Zie de [volledige release notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) voor het complete changelog van alle vijf releases.
