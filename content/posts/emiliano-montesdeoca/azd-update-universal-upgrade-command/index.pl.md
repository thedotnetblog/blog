---
title: "azd update — Jedno Polecenie do Wszystkich Menedżerów Pakietów"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ma teraz uniwersalne polecenie aktualizacji, które działa niezależnie od metody instalacji — winget, Homebrew, Chocolatey lub skrypt instalacyjny."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azd-update-universal-upgrade-command" >}}).*

Znasz ten komunikat "Dostępna jest nowa wersja azd", który pojawia się co kilka tygodni? Ten, który odrzucasz, bo nie pamiętasz, czy zainstalowałeś `azd` przez winget, Homebrew czy ten skrypt curl z sześciu miesięcy temu? To jest w końcu naprawione.

Microsoft właśnie dostarczył [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — pojedyncze polecenie, które aktualizuje Azure Developer CLI do najnowszej wersji niezależnie od tego, jak go pierwotnie zainstalowałeś.

## Jak to działa

```bash
azd update
```

To wszystko. Dla wczesnego dostępu do nowych funkcji:

```bash
azd update --channel daily
azd update --channel stable
```

Polecenie wykrywa Twoją aktualną metodę instalacji i używa odpowiedniego mechanizmu aktualizacji.

## Mały haczyk

`azd update` jest dostarczany od wersji 1.23.x. Jeśli jesteś na starszej wersji, będziesz musiał wykonać jedną ostatnią ręczną aktualizację. Potem `azd update` zajmuje się wszystkim.

## Dlaczego to ważne

To małe ulepszenie jakości życia, ale dla tych z nas, którzy używają `azd` na co dzień do wdrażania agentów AI i aplikacji Aspire do Azure, bycie na bieżąco ma znaczenie.

Przeczytaj [pełne ogłoszenie](https://devblogs.microsoft.com/azure-sdk/azd-update/).
