---
title: "Hooks d'azd en Python, TypeScript i .NET: adéu als scripts de shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "La CLI d'Azure Developer ara permet escriure hooks en Python, JavaScript, TypeScript o .NET. S'ha acabat canviar de context a Bash per executar un script de migració."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [feu clic aquí]({{< ref "index.md" >}}).*

Si alguna vegada has tingut un projecte completament en .NET i tot i així has hagut d'escriure scripts Bash per als hooks d'azd, coneixes bé aquell dolor. Per què canviar a sintaxi de shell en un pas de pre-provisioning quan tota la resta del projecte és C#?

Aquesta frustració té ara solució oficial. L'Azure Developer CLI [acaba de llançar suport multi-llenguatge per a hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), i és exactament tan bo com sona.

## Hooks, breument

Els hooks són scripts que s'executen en punts clau del cicle de vida d'`azd` — abans del provisioning, després del desplegament, i més. Es defineixen a `azure.yaml` i permeten injectar lògica personalitzada sense modificar la CLI.

Abans només s'admetien Bash i PowerShell. Ara pots usar **Python, JavaScript, TypeScript o .NET** — i `azd` s'encarrega de la resta automàticament.

## Com funciona la detecció

Simplement apuntes el hook a un fitxer i `azd` infereix el llenguatge per l'extensió:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Sense configuració addicional. Si l'extensió és ambigua, pots afegir `kind: python` (o el que correspongui) per especificar-ho explícitament.

## Detalls importants per llenguatge

### Python

Col·loca un `requirements.txt` o `pyproject.toml` al costat del script (o en qualsevol directori pare) i `azd` crea un entorn virtual, instal·la dependències i executa l'script.

### JavaScript i TypeScript

El mateix patró — posa un `package.json` a prop del script i `azd` executarà `npm install` primer. Per a TypeScript, usa `npx tsx` sense pas de compilació ni `tsconfig.json`.

### .NET

Dos modes disponibles:

- **Mode projecte**: Si hi ha un `.csproj` al costat del script, `azd` executa `dotnet restore` i `dotnet build` automàticament.
- **Mode single-file**: En .NET 10+, pots posar un fitxer `.cs` independent i s'executa directament amb `dotnet run script.cs`. Sense fitxer de projecte.

## Configuració per executor

Cada llenguatge admet un bloc `config` opcional:

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

## Per què importa per a desenvolupadors .NET

Els hooks eren l'últim lloc d'un projecte basat en azd que t'obligava a usar un altre llenguatge. Ara tot el pipeline de desplegament pot viure en un sol llenguatge. Pots reutilitzar les teves utilitats .NET existents als hooks, referenciar llibreries compartides i evitar el manteniment de scripts de shell.

## Conclusió

És un d'aquells canvis que semblen petits però que eliminen molta fricció del dia a dia amb azd. El suport multi-llenguatge per a hooks ja està disponible — consulta el [post oficial](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) per a la documentació completa.
