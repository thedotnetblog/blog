---
title: "azd-Hooks in Python, TypeScript und .NET: Schluss mit Shell-Skripten"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Die Azure Developer CLI unterstützt jetzt Hooks in Python, JavaScript, TypeScript und .NET. Kein Kontextwechsel zu Bash mehr nur für ein Migrations-Skript."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [hier klicken]({{< ref "index.md" >}}).*

Wer schon einmal ein vollständig in .NET geschriebenes Projekt hatte und trotzdem Bash-Skripte für azd-Hooks schreiben musste, kennt den Schmerz. Warum in Shell-Syntax wechseln für einen Pre-Provisioning-Schritt, wenn der Rest des Projekts C# ist?

Diese Frustration hat jetzt eine offizielle Lösung. Die Azure Developer CLI hat [Multi-Sprachen-Unterstützung für Hooks eingeführt](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), und es ist genauso gut wie es klingt.

## Was sind Hooks?

Hooks sind Skripte, die an wichtigen Punkten im `azd`-Lebenszyklus ausgeführt werden — vor dem Provisioning, nach dem Deployment und mehr. Sie werden in `azure.yaml` definiert und ermöglichen die Injektion von benutzerdefinierter Logik ohne Änderungen an der CLI.

Bisher wurden nur Bash und PowerShell unterstützt. Jetzt kann man **Python, JavaScript, TypeScript oder .NET** verwenden — und `azd` erledigt den Rest automatisch.

## Wie die Erkennung funktioniert

Man verweist den Hook auf eine Datei, und `azd` leitet die Sprache aus der Dateiendung ab:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Keine zusätzliche Konfiguration. Bei mehrdeutigen Endungen kann man `kind: python` (oder die entsprechende Sprache) explizit angeben.

## Sprachspezifische Details

### Python

Eine `requirements.txt` oder `pyproject.toml` neben dem Skript ablegen (oder in einem übergeordneten Verzeichnis). `azd` erstellt automatisch eine virtuelle Umgebung, installiert Abhängigkeiten und führt das Skript aus.

### JavaScript und TypeScript

Dasselbe Muster — eine `package.json` in der Nähe des Skripts, und `azd` führt zuerst `npm install` aus. Für TypeScript wird `npx tsx` verwendet, ohne Kompilierungsschritt und ohne `tsconfig.json`.

### .NET

Zwei Modi verfügbar:

- **Projektmodus**: Liegt eine `.csproj` neben dem Skript, führt `azd` automatisch `dotnet restore` und `dotnet build` aus.
- **Single-File-Modus**: Ab .NET 10+ können eigenständige `.cs`-Dateien direkt via `dotnet run script.cs` ausgeführt werden. Kein Projektdatei erforderlich.

## Executor-spezifische Konfiguration

Jede Sprache unterstützt einen optionalen `config`-Block:

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

## Warum das für .NET-Entwickler wichtig ist

Hooks waren der letzte Ort in einem azd-basierten Projekt, der einen Sprachwechsel erzwang. Jetzt kann die gesamte Deployment-Pipeline — App-Code, Infrastrukturskripte und Lifecycle-Hooks — in einer einzigen Sprache leben. Bestehende .NET-Utilities lassen sich in Hooks wiederverwenden, gemeinsame Bibliotheken referenzieren, und Shell-Skript-Pflege entfällt.

## Fazit

Einer dieser Änderungen, die klein klingen, aber täglich Reibung aus dem azd-Workflow nehmen. Multi-Sprachen-Hook-Unterstützung ist jetzt verfügbar — alle Details im [offiziellen Post](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/).
