---
title: "Rozszerzenie WinApp dla VS Code: Uruchamiaj, Debuguj i Pakuj Aplikacje Windows Bez Opuszczania Edytora"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Rozszerzenie WinApp dla VS Code przynosi pełne CLI do Tworzenia Aplikacji Windows bezpośrednio do VS Code — uruchamiaj, debuguj z tożsamością pakietu, pakuj i podpisuj aplikacje Windows bez Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Ten post został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Jeśli kiedykolwiek próbowałeś tworzyć aplikację Windows w VS Code, znasz ten moment. Pracujesz w pełnym skupieniu, edytujesz kod w ulubionym edytorze — i nagle potrzebujesz tożsamości pakietu dla Windows API. Albo musisz utworzyć MSIX. Albo podpisać pakiet. I nagle otwierasz Visual Studio, albo o 23:00 szukasz w Google "msix packaging without visual studio".

To tarcie już nie istnieje. [Rozszerzenie WinApp dla VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) jest w publicznym podglądzie — i jest to pełne [CLI do Tworzenia Aplikacji Windows](https://github.com/microsoft/WinAppCli) zintegrowane bezpośrednio z VS Code. Bez osobnej instalacji, bez Visual Studio.

## Tożsamość Pakietu z F5

Problem z Windows API — powiadomienia, zadania w tle, funkcje AI na urządzeniu, share targets — wiele z nich wymaga, aby aplikacja miała **tożsamość pakietu**. Bez niej te API po prostu nie działają.

Tradycyjnie uzyskanie tożsamości pakietu oznaczało zbudowanie pełnego instalatora MSIX lub uruchomienie z Visual Studio. Rozszerzenie WinApp całkowicie to zmienia dzięki niestandardowemu typowi debugowania `winapp`.

Dodaj to do swojego `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Naciśnij F5. Rozszerzenie znajduje dane wyjściowe kompilacji i manifest, nadaje aplikacji tożsamość pakietu za pośrednictwem `winapp run` i dołącza debuger. Dla aplikacji .NET to `coreclr` (wymaga C# Dev Kit). C/C++ używa `cppvsdbg`. Node/Electron używa wbudowanego debugera.

Możesz skonfigurować `preLaunchTask`, aby projekt kompilował się automatycznie przed każdym naciśnięciem F5 — ten sam przepływ build-and-launch co w Visual Studio, tylko w VS Code.

## Wszystko w Palecie Poleceń

Otwórz `Ctrl+Shift+P`, wpisz `WinApp` — i masz pełny zestaw narzędzi:

- **Initialize Project** — skonfiguruj projekt z Windows SDK i/lub Windows App SDK
- **Run Application** — uruchom jako luźno spakowaną aplikację z tożsamością pakietu
- **Create MSIX Package** — spakuj aplikację z opcjami certyfikatu i środowiska uruchomieniowego
- **Update Manifest Assets** — automatycznie generuj wszystkie wymagane ikony aplikacji z jednego obrazu źródłowego
- **Generate / Install Certificate** — zarządzanie certyfikatami deweloperskimi
- **Sign Package** — podpisz MSIX lub plik wykonywalny
- **Run SDK Tool** — uruchamiaj `makeappx`, `signtool`, `mt` lub `makepri` bezpośrednio

CLI WinApp też nie trzeba instalować. Jest dołączone do rozszerzenia.

## Działa z Wieloma Frameworkami

To nie tylko narzędzie dla .NET WPF/WinUI. Rozszerzenie działa z:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Ta szerokość jest celowa. VS Code to miejsce, gdzie żyją deweloperzy webowi i cross-platform. Jeśli tworzysz aplikację Tauri lub Electron wymagającą pakietowania Windows, to rozszerzenie cię obsłuży bez konieczności przyjmowania Visual Studio.

## Dlaczego To Ważne dla Deweloperów .NET

Dużo pracuję w VS Code — to tam piszę Markdown, zarządzam konfiguracjami, edytuję małe projekty i uruchamiam terminale. Ale do pracy z .NET Windows Desktop, Visual Studio był jedyną realną opcją, gdy tylko cokolwiek dotyczyło pakietowania.

To rozszerzenie wypełnia tę lukę. Teraz można mieć pełny cykl deweloperski .NET Windows Desktop — edycja, kompilacja, uruchamianie z tożsamością pakietu, debugowanie, pakowanie, podpisywanie — bez opuszczania VS Code. To prawdziwa poprawa jakości pracy.

## Pierwsze Kroki

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Lub wyszukaj **WinApp** w widoku Extensions (`Ctrl+Shift+X`).

Wymagania:
- Windows 10 lub nowszy
- VS Code 1.109.0 lub nowszy
- Rozszerzenie debugera dla języka Twojej aplikacji

Przeczytaj [pełne ogłoszenie Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) po więcej szczegółów.

## Podsumowanie

Rozszerzenie WinApp dla VS Code to mile widziane uzupełnienie dla deweloperów .NET Windows Desktop, którzy żyją w VS Code, ale musieli przełączać się na Visual Studio do pracy z pakowaniem. Tożsamość pakietu z F5, pakowanie MSIX z palety poleceń, wbudowane zarządzanie certyfikatami — to właściwy zestaw funkcji.

Wypróbuj w swoim następnym projekcie WPF lub WinUI. Tarcie, które omijałeś, właśnie znacznie się zmniejszyło.
