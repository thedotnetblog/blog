---
title: "Hooki azd w Python, TypeScript i .NET: koniec ze skryptami shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI obsługuje teraz hooki w Python, JavaScript, TypeScript i .NET. Koniec z przełączaniem się na Bash tylko po to, żeby uruchomić skrypt migracji."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Ten artykuł został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Jeśli kiedykolwiek miałeś projekt w całości napisany w .NET i mimo to musiałeś pisać skrypty Bash dla hooków azd — znasz ten ból. Po co przełączać się na składnię shell w kroku pre-provisioning, skoro reszta projektu to C#?

Ta frustracja ma teraz oficjalne rozwiązanie. Azure Developer CLI [właśnie wprowadził obsługę wielu języków dla hooków](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), i jest dokładnie tak dobre, jak brzmi.

## Czym są hooki

Hooki to skrypty wykonywane w kluczowych punktach cyklu życia `azd` — przed provisioningiem, po deploymencie i nie tylko. Definiuje się je w `azure.yaml` i pozwalają na wstrzyknięcie własnej logiki bez modyfikowania CLI.

Wcześniej obsługiwane były tylko Bash i PowerShell. Teraz można używać **Pythona, JavaScript, TypeScript lub .NET** — resztą zajmuje się `azd` automatycznie.

## Jak działa wykrywanie

Wystarczy wskazać hook na plik, a `azd` wywnioskuje język z rozszerzenia:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Bez dodatkowej konfiguracji. Jeśli rozszerzenie jest niejednoznaczne, można jawnie podać `kind: python` (lub odpowiedni język).

## Ważne szczegóły według języka

### Python

Umieść `requirements.txt` lub `pyproject.toml` obok skryptu (lub w dowolnym katalogu nadrzędnym). `azd` automatycznie tworzy środowisko wirtualne, instaluje zależności i uruchamia skrypt.

### JavaScript i TypeScript

Ten sam wzorzec — `package.json` blisko skryptu, a `azd` najpierw wykona `npm install`. Dla TypeScript używa `npx tsx` bez etapu kompilacji i bez `tsconfig.json`.

### .NET

Dwa dostępne tryby:

- **Tryb projektu**: jeśli obok skryptu jest `.csproj`, `azd` automatycznie uruchamia `dotnet restore` i `dotnet build`.
- **Tryb single-file**: na .NET 10+ samodzielne pliki `.cs` uruchamiają się bezpośrednio przez `dotnet run script.cs`. Plik projektu nie jest wymagany.

## Konfiguracja dla konkretnego executora

Każdy język obsługuje opcjonalny blok `config`:

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

## Dlaczego to ważne dla programistów .NET

Hooki były ostatnim miejscem w projekcie opartym na azd, które wymuszało zmianę języka. Teraz cały pipeline deploymentu — od kodu aplikacji po hooki cyklu życia — może żyć w jednym języku. Można ponownie wykorzystywać istniejące narzędzia .NET w hookach, referencować współdzielone biblioteki i porzucić utrzymywanie skryptów shell.

## Podsumowanie

Jedna z tych zmian, które wydają się drobne, ale naprawdę redukują codzienne tarcia w pracy z azd. Obsługa wielu języków dla hooków jest dostępna teraz — pełna dokumentacja w [oficjalnym poście](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/).
