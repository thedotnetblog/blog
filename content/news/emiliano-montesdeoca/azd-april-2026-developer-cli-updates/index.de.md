---
title: "Azure Developer CLI (azd) April 2026 Updates"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd veröffentlichte fünf Releases im April 2026 – Highlight ist der mehrsprachige Hook-Support für Python, JavaScript, TypeScript und .NET, dazu öffentliche Vorschau von azd update, KI-Quota-Preflight-Check und mehr."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) veröffentlichte fünf Releases im April 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 bis 1.24.2). Das große Thema: Hooks, die jetzt in Python, JavaScript, TypeScript und .NET ausgeführt werden – nicht mehr nur in Bash und PowerShell.

## Mehrsprachige Hooks in azure.yaml

Hooks können nun neben Shell-Skripten auf `.py`-, `.js`-, `.ts`- oder `.cs`-Dateien verweisen. Jede Sprache erhält eine automatische Abhängigkeitsauflösung:

- **Python** — erkennt `requirements.txt` oder `pyproject.toml`, erstellt ein Virtualenv und installiert Abhängigkeiten vor der Ausführung. Den Namen der Umgebung konfiguriert man mit `virtualEnvName`.
- **JavaScript / TypeScript** — erkennt `package.json` und führt automatisch `npm install` aus. TypeScript wird über `npx tsx` ausgeführt, ohne Compile-Schritt. Den Paketmanager wählt man über den Konfigurationsblock `packageManager`.
- **.NET** — führt `.cs`-Dateien mit `dotnet run` aus. Single-File-Skripte werden auf .NET 10+ unterstützt. Das Ziel-Framework wird über den Block `configuration/framework` konfiguriert.

Teams, die bereits in einer dieser Sprachen arbeiten, müssen keinen separaten Bash- oder PowerShell-Hook mehr pflegen, nur um Lifecycle-Events des Provisionierens zu verbinden.

## azd update geht in die öffentliche Vorschau

`azd update` ist jetzt auf allen Plattformen in der öffentlichen Vorschau. Ein einzelner Befehl übernimmt das Update, unabhängig davon, wie azd ursprünglich installiert wurde – kein manuelles Nachverfolgen von Homebrew-, WinGet- oder MSI-Pfaden mehr.

## Nicht-interaktiver Modus via AZD_NON_INTERACTIVE

Das Setzen von `AZD_NON_INTERACTIVE=true` (oder `--non-interactive` / `--no-prompt`) erzeugt nun konsistente, deterministische Fehler in CI/CD-Pipelines, wenn eine erforderliche Eingabe nicht automatisch aufgelöst werden kann. Zuvor war das Verhalten befehlsübergreifend inkonsistent.

## KI-Modell-Quota-Preflight-Check

`azd provision` validiert die Azure Cognitive Services Quota, bevor KI-Modellressourcen bereitgestellt werden. Deployments, die aufgrund von Quota-Grenzen scheitern würden, zeigen den Fehler jetzt früh im Prozess an – nicht erst in der Mitte des Provisionierens.

## „Diesen Fehler beheben" in der Copilot-Fehlerbehebung

Die azd-Copilot-Integration zur Fehlerbehebung gewinnt die Fähigkeit, einen vorgeschlagenen Fix direkt anzuwenden – nicht nur zu beschreiben. Wenn der Agent ein behebbares Problem erkennt, kann er die Änderung direkt vornehmen.

## Benutzerdefinierte Provisionierungsanbieter und Key Vault Secret Resolver

Erweiterungsautoren können nun alternative Infrastruktur-Backends mit `WithProvisioningProvider()` registrieren. Außerdem löst azd `@Microsoft.KeyVault(...)`-Referenzen automatisch auf, bevor die Konfiguration an Erweiterungen übergeben wird – manuelle Secret-Auflösung in benutzerdefinierten Anbietern entfällt.

## Ausschlüsse für Templates und Watch-Modus

Zwei neue Ignore-Dateien bieten feinere Kontrolle über die Dateiverarbeitung:
- **`.azdignore`** — schließt beitragerspezifische Dateien (Dokumentation, CI-Konfigurationen) aus Template-Kopien aus, damit Endnutzer ein sauberes Projektgerüst erhalten.
- **`.azdxignore`** — schließt Verzeichnisse aus, die während `azd x watch` Rebuilds auslösen, und reduziert so Lärm bei der iterativen Entwicklung.

## Reserved-Name-Preflight und docker.network-Option

azd warnt nun, wenn vorhergesagte Ressourcennamen reservierte Azure-Wörter (`MICROSOFT`, `WINDOWS` oder das Präfix `LOGIN`) enthalten – bevor die Provisionierung beginnt. Eine neue `docker.network`-Option übergibt `--network` an `docker build`, was in Unternehmens-Proxy-Umgebungen nützlich ist, die ein bestimmtes Docker-Netzwerk erfordern.

## Sicherheitsfixes

Das Windows-MSI-Paket enthält jetzt eine Code-Signing-Verifizierung. Ein weiterer Fix schließt ein Environment-Variable-Leak, das Werte über Erweiterungsbefehlsgrenzen hinweg hätte offenlegen können.

---

Ein intensiver Monat – der mehrsprachige Hook-Support beseitigt insbesondere einen echten Reibungspunkt für Teams, die nicht hauptsächlich in Bash arbeiten. Die [vollständigen Release Notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) enthalten das komplette Changelog aller fünf Releases.
