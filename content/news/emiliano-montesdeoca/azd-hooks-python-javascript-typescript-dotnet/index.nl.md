---
title: "azd-hooks in Python, TypeScript en .NET: genoeg van shell-scripts"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "De Azure Developer CLI ondersteunt nu hooks in Python, JavaScript, TypeScript en .NET. Geen contextswitch meer naar Bash alleen voor een migratieScript."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Als je ooit een volledig .NET-project had en toch Bash-scripts moest schrijven voor azd-hooks, dan ken je dat gevoel maar al te goed. Waarom overstappen naar shell-syntax voor een pre-provisioning stap wanneer de rest van het project C# is?

Die frustratie heeft nu een officiële oplossing. De Azure Developer CLI heeft [multi-taalondersteuning voor hooks uitgebracht](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), en het is precies zo goed als het klinkt.

## Wat zijn hooks

Hooks zijn scripts die worden uitgevoerd op cruciale momenten in de `azd`-levenscyclus — voor provisioning, na deployment, en meer. Ze worden gedefinieerd in `azure.yaml` en maken het mogelijk om aangepaste logica te injecteren zonder de CLI aan te passen.

Voorheen werden alleen Bash en PowerShell ondersteund. Nu kun je **Python, JavaScript, TypeScript of .NET** gebruiken — en `azd` regelt de rest automatisch.

## Hoe detectie werkt

Wijs de hook naar een bestand en `azd` leidt de taal af uit de extensie:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Geen extra configuratie nodig. Als de extensie onduidelijk is, kun je `kind: python` (of de betreffende taal) expliciet toevoegen.

## Taalspecifieke details

### Python

Plaats een `requirements.txt` of `pyproject.toml` naast het script (of in een bovenliggende map). `azd` maakt automatisch een virtuele omgeving, installeert afhankelijkheden en voert het script uit.

### JavaScript en TypeScript

Hetzelfde patroon — een `package.json` bij het script en `azd` voert eerst `npm install` uit. Voor TypeScript wordt `npx tsx` gebruikt, zonder compilatiestap en zonder `tsconfig.json`.

### .NET

Twee beschikbare modi:

- **Projectmodus**: Als er een `.csproj` naast het script staat, voert `azd` automatisch `dotnet restore` en `dotnet build` uit.
- **Single-file modus**: Op .NET 10+ kunnen zelfstandige `.cs`-bestanden direct worden uitgevoerd via `dotnet run script.cs`. Geen projectbestand vereist.

## Executor-specifieke configuratie

Elke taal ondersteunt een optioneel `config`-blok:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Hooks waren de laatste plek in een azd-gebaseerd project die een taalwissel afdwong. Nu kan de volledige deployment pipeline — van applicatiecode tot lifecycle-hooks — in één taal leven. Bestaande .NET-utilities zijn herbruikbaar in hooks, gedeelde bibliotheken kunnen worden gerefereerd en shell-scriptonderhoud is verleden tijd.

## Conclusie

Een van die veranderingen die klein lijken maar dagelijks veel wrijving uit de azd-workflow halen. Multi-taalondersteuning voor hooks is nu beschikbaar — bekijk de [officiële post](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) voor de volledige documentatie.
