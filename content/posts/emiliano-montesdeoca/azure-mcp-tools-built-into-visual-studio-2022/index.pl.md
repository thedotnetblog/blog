---
title: "Narzędzia Azure MCP Są Teraz Wbudowane w Visual Studio 2022 — Żadnego Rozszerzenia"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Narzędzia Azure MCP są dostarczane jako część obciążenia deweloperskiego Azure w Visual Studio 2022. Ponad 230 narzędzi, 45 usług Azure, zero rozszerzeń do zainstalowania."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

Jeśli korzystałeś z narzędzi Azure MCP w Visual Studio przez oddzielne rozszerzenie, znasz procedurę — zainstaluj VSIX, zrestartuj, miej nadzieję, że nie popsuje, zarządzaj niezgodnościami wersji. To tarcie zniknęło.

Yun Jung Choi [ogłosiła](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/), że narzędzia Azure MCP są teraz dostarczane bezpośrednio jako część obciążenia deweloperskiego Azure w Visual Studio 2022. Żadnego rozszerzenia. Żadnego VSIX.

## Co to faktycznie oznacza

Ponad 230 narzędzi w 45 usługach Azure — dostępnych bezpośrednio z okna czatu. Wylistuj swoje konta pamięci masowej, wdróż aplikację ASP.NET Core, diagnostykuj problemy App Service — wszystko bez otwierania karty przeglądarki.

## Jak włączyć

1. Zaktualizuj do Visual Studio 2022 **17.14.30** lub nowszego
2. Upewnij się, że obciążenie **Azure development** jest zainstalowane
3. Otwórz GitHub Copilot Chat
4. Kliknij przycisk **Wybierz narzędzia** (ikona dwóch kluczy)
5. Włącz **Azure MCP Server**

Pozostaje włączone między sesjami.

## Zastrzeżenie

Narzędzia są domyślnie wyłączone — musisz je włączyć. Dla .NET deweloperów korzystających z Visual Studio oznacza to jeszcze mniej powodów do przełączania kontekstu do portalu Azure.
