---
title: "NTLM Kończy Się w Git/libcurl: Zespoły Azure DevOps Server Potrzebują Prawdziwego Planu Migracji"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "Wrześniowe 2026 usunięcie NTLM to nie drobny problem kompatybilności; to termin architektury tożsamości dla lokalnych środowisk Azure DevOps Server."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

Nadchodzące usunięcie NTLM w libcurl to jedna z tych zmian, która wygląda technicznie, ale jest organizacyjna. Jeśli twoja ścieżka Git przez HTTPS do Azure DevOps Server wciąż polega na NTLM, twój problem to nie narzędzia, to dług tożsamościowy.

Oryginalne źródło: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft ma rację, naciskając mocno w tym obszarze. NTLM ma znane słabości kryptograficzne i nie powinien być domyślnym standardem korporacyjnym. Niebezpieczną częścią jest to, że wiele środowisk wierzy, że używa Kerberos, podczas gdy w rzeczywistości przetrwają na cichym SPNEGO fallback do NTLM. Ta iluzja znika we wrześniu 2026.

Moja opinia: **nie traktuj tego jako problemu „wersji klienta"**. Ponowne włączanie flag NTLM, przypinanie starych wersji Git lub liczenie, że fallback pozostanie dostępny, to krótkotrwałe obejście z długoterminowym ryzykiem. Jeśli twoja strategia naprawcza to degradacja i opóźnienie, aktywnie zwiększasz kruchość operacyjną.

Praktyczna sekwencja migracji powinna być bezpośrednia i mierzalna.

- **Zweryfikuj obecne zachowanie auth teraz.** Przeprowadź kontrolę opartą na śledzeniu i walidację pamięci podręcznej biletów w prawdziwych kontekstach programistów i agentów kompilacji, w tym ścieżek poza domeną i zdalnej sieci.
- **Napraw Kerberos end-to-end:** SPN, aliasy DNS, ustawienia load balancera, delegacja i osiągalność kontrolera domeny.
- **Zidentyfikuj scenariusze poza domeną i workgroup wcześnie** i zaprojektuj pas SSH tam, gdzie Kerberos nie może być niezawodny.

Potrzebujesz też jasności własności. Zespoły bezpieczeństwa powinny definiować bazowe polityki, ale inżynieria platformowa musi być odpowiedzialna za gotowość implementacyjną. To nie może być poboczne zadanie dla indywidualnych adminów repozytoriów. Wymaga skoordynowanych zmian w IIS, AD, krawędzi sieciowej, agentach CI i wskazówkach dla stacji roboczych programistów.

Jednym subtelnym ryzykiem jest automatyzacja. Agenci kompilacji i konta usługowe często działają w kontekstach, w których bilety Kerberos są nieobecne lub nieprawidłowe, nawet gdy użytkownicy ludzie działają dobrze. Jeśli testujesz tylko interaktywne przepływy programistów, przeoczysz najbardziej krytyczne punkty awarii.

Korzyść jest realna. Czyste przejście na Kerberos lub SSH nie tylko unika awarii, ale **redukuje powierzchnię ataku i dopasowuje kontrole tożsamości** do nowoczesnych oczekiwań zgodności. Zespoły, które rozpoczną tę transformację teraz, będą traktować wrzesień jako nie-wydarzenie. Zespoły, które będą czekać, będą debugować awarie uwierzytelniania pod presją wydania.

To nie jest ostrzeżenie do zarchiwizowania. **To termin do wykonania.**