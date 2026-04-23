---
title: "Hook azd in Python, TypeScript e .NET: basta script shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "La CLI di Azure Developer ora supporta hook in Python, JavaScript, TypeScript e .NET. Niente più switch di contesto verso Bash solo per uno script di migrazione."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Se hai mai avuto un progetto completamente in .NET e ti sei ritrovato a scrivere script Bash solo per gli hook di azd, conosci bene quella sensazione. Perché passare alla sintassi shell per un passaggio di pre-provisioning quando tutto il resto del progetto è in C#?

Quella frustrazione ha ora una soluzione ufficiale. La CLI di Azure Developer [ha appena introdotto il supporto multi-linguaggio per gli hook](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), ed è esattamente buono come sembra.

## Gli hook, in breve

Gli hook sono script eseguiti in punti chiave del ciclo di vita di `azd` — prima del provisioning, dopo il deployment, e altro ancora. Definiti in `azure.yaml`, permettono di iniettare logica personalizzata senza modificare la CLI.

Prima erano supportati solo Bash e PowerShell. Ora si può usare **Python, JavaScript, TypeScript o .NET** — e `azd` si occupa del resto automaticamente.

## Come funziona il rilevamento

Basta puntare l'hook verso un file e `azd` deduce il linguaggio dall'estensione:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Nessuna configurazione aggiuntiva. Se l'estensione è ambigua, si può aggiungere `kind: python` (o il linguaggio appropriato) per specificarlo esplicitamente.

## Dettagli per linguaggio

### Python

Inserire un `requirements.txt` o `pyproject.toml` vicino allo script (o in una directory padre). `azd` crea automaticamente un ambiente virtuale, installa le dipendenze ed esegue lo script.

### JavaScript e TypeScript

Stesso schema — un `package.json` vicino allo script e `azd` esegue prima `npm install`. Per TypeScript, usa `npx tsx` senza step di compilazione né `tsconfig.json`.

### .NET

Due modalità disponibili:

- **Modalità progetto**: Se c'è un `.csproj` vicino allo script, `azd` esegue automaticamente `dotnet restore` e `dotnet build`.
- **Modalità single-file**: Con .NET 10+, i file `.cs` autonomi vengono eseguiti direttamente via `dotnet run script.cs`. Nessun file di progetto richiesto.

## Configurazione per executor

Ogni linguaggio supporta un blocco `config` opzionale:

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

## Perché è importante per gli sviluppatori .NET

Gli hook erano l'ultimo posto in un progetto basato su azd che costringeva a cambiare linguaggio. Ora l'intera pipeline di deployment può vivere in un unico linguaggio. È possibile riutilizzare le utility .NET esistenti negli hook, referenziare librerie condivise ed eliminare la manutenzione di script shell.

## Conclusione

Uno di quei cambiamenti che sembrano piccoli ma che riducono concretamente la frizione quotidiana con azd. Il supporto multi-linguaggio per gli hook è disponibile ora — tutti i dettagli nel [post ufficiale](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/).
