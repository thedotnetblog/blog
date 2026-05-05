---
title: "Azure MCP Server jest Teraz .mcpb — Instaluj bez Żadnego Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server jest teraz dostępny jako MCP Bundle (.mcpb) — pobierz, przeciągnij do Claude Desktop i gotowe. Bez Node.js, Python czy .NET."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Wiesz, co było irytujące w konfiguracji serwerów MCP? Potrzebowałeś runtime. Node.js dla wersji npm, Python dla pip/uvx, .NET SDK dla wariantu dotnet.

[Azure MCP Server właśnie to zmienił](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Jest teraz dostępny jako `.mcpb` — MCP Bundle — a konfiguracja to przeciągnij i upuść.

## Czym jest MCP Bundle?

Pomyśl o tym jak o rozszerzeniu VS Code (`.vsix`) lub rozszerzeniu przeglądarki (`.crx`), ale dla serwerów MCP. Plik `.mcpb` to samodzielne archiwum ZIP zawierające binarny plik serwera i wszystkie jego zależności.

## Jak zainstalować

**1. Pobierz bundle dla swojej platformy**

Przejdź na [stronę GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) i pobierz plik `.mcpb` dla swojego OS i architektury.

**2. Zainstaluj w Claude Desktop**

Najłatwiej: przeciągnij plik `.mcpb` do okna Claude Desktop na stronie ustawień Rozszerzeń (`☰ → Plik → Ustawienia → Rozszerzenia`). Przejrzyj szczegóły serwera, kliknij Zainstaluj, potwierdź.

**3. Uwierzytelnij się w Azure**

```bash
az login
```

## Na początek

- **Pobieranie**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repozytorium**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Dokumentacja**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Sprawdź [pełny post](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
