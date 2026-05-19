---
title: "Prywatne Endpoints, VNets, NSG — Aspire Teraz Zarządza Siecią"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Nowa obsługa sieci korporacyjnych Azure w Aspire pozwala modelować VNety, prywatne punkty końcowe, bramy NAT, NSG i obwody bezpieczeństwa sieci bezpośrednio w AppHost — bez dryfu infrastruktury."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Widziałem ten scenariusz zbyt wiele razy. Aplikacja jest gotowa. Demo wygląda świetnie. Następnie pojawia się lista kontrolna bezpieczeństwa: wynieść storage z publicznego internetu, uruchomić w VNecie, dostarczyć wychodzące IP do listy dozwolonych partnera, udowodnić, że tylko właściwe podsieci komunikują się z właściwymi usługami.

W tym momencie model aplikacji i model infrastruktury zaczynają się rozchodzić w sposób, który jest bolesny w utrzymaniu.

Nowa obsługa sieci korporacyjnych Azure w Aspire rozwiązuje to bezpośrednio. Opisujesz kształt sieci w AppHost obok zasobów, które jej używają.

## Elementy składowe

Do czego służy każda koncepcja sieciowa Azure, w skrócie:

| Funkcja | Kiedy używać | Dlaczego jest ważna |
|---------|------------|----------------|
| Sieć wirtualna | Gdy potrzebujesz prywatnej przestrzeni adresowej | Granica sieci dla podsieci, prywatnych punktów końcowych i routingu |
| Podsieć | Gdy musisz oddzielić obciążenia w VNecie | Każda część systemu dostaje własny zakres adresów i powierzchnię polityki |
| Podsieć delegowana | Gdy usługa platformy (np. ACA) musi zarządzać podsiecią | Pozwala usłudze bezpiecznie umieścić zarządzaną infrastrukturę w Twoim VNecie |
| Brama NAT | Gdy potrzebujesz przewidywalnych wychodzących publicznych IP | Stabilny adres dla list dozwolonych i audytów |
| Prywatny punkt końcowy | Gdy chcesz prywatnego dostępu do zasobu PaaS | Umieszcza prywatne IP tej usługi w Twoim VNecie, usuwa publiczną ekspozycję |
| NSG | Gdy potrzebujesz reguł ruchu na poziomie podsieci | Jawne zezwolenie/odmowa dla ruchu przychodzącego i wychodzącego dla każdej podsieci |

## Opisywanie w AppHost

Kluczowa zmiana polega na tym, że modelujesz sieć *razem* z zasobami, które jej używają, a nie w osobnym pliku Bicep, który z czasem rozchodzi się z modelem aplikacji.

Z AppHost możesz:

- Tworzyć VNety i podsieci za pomocą `AddVirtualNetwork()` i `AddSubnet()`
- Dołączać bramę NAT do podsieci dla stabilnych wychodzących IP
- Tworzyć prywatne punkty końcowe dla storage, Key Vault, SQL i innych usług PaaS
- Definiować NSG z regułami bezpieczeństwa przychodzącymi i wychodzącymi
- Konfigurować obwody bezpieczeństwa sieci dla polityk między zasobami

Efektem jest to, że gdy uruchamiasz `azd up`, infrastruktura odpowiada temu, co model aplikacji mówi, że potrzebuje. Nie temu, co mówi ręcznie utrzymywany szablon.

## Dlaczego to ważne dla prawdziwych aplikacji

Kilka rzeczy, które stają się znacznie łatwiejsze, gdy sieć jest zamodelowana w Aspire:

**Prywatne punkty końcowe dla Key Vault i storage** — opisujesz `WithPrivateEndpoint()` na tych zasobach, a Aspire zajmuje się konfiguracją strefy DNS i dołączaniem punktu końcowego. Aplikacja nigdy się nie zmienia.

**Spójne wychodzące IP** — dodaj bramę NAT do odpowiedniej podsieci, a każde wychodzące żądanie z Twojej aplikacji przechodzi przez znany, stabilny adres IP. Partnerzy mogą go dodać do listy dozwolonych. Audytorzy mogą go śledzić.

**Reguły NSG z kodu** — zamiast klikać w portalu lub utrzymywać fragment Bicep, reguły bezpieczeństwa mieszkają w AppHost obok zasobów, które chronią.

To jest rodzaj integracji, który nie sprawia, że dema są ekscytujące, ale sprawia, że systemy produkcyjne są łatwe w utrzymaniu.

## Podsumowanie

Bezpieczeństwo sieciowe pojawiające się późno w cyklu życia projektu jest rozwiązanym problemem, jeśli modelujesz je razem z aplikacją od początku. Obsługa sieci korporacyjnych Aspire sprawia, że jest to możliwe bez potrzeby osobnej ścieżki infrastruktury.

Pełne szczegóły w oryginalnym wpisie: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
