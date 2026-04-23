---
title: "Applica subito la patch: aggiornamento di sicurezza OOB .NET 10.0.7 per ASP.NET Core Data Protection"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 è una release fuori banda che corregge una vulnerabilità di sicurezza in Microsoft.AspNetCore.DataProtection — l'encryptor autenticato gestito calcolava HMAC sui byte sbagliati, con possibile escalation dei privilegi. Aggiorna immediatamente."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Questo aggiornamento non è facoltativo. Se la tua applicazione usa `Microsoft.AspNetCore.DataProtection`, devi aggiornare a 10.0.7.

## Cosa È Successo

Dopo la release Patch Tuesday di `.NET 10.0.6`, alcuni utenti hanno iniziato a segnalare che la decrittazione falliva nelle loro applicazioni. Durante l'analisi di quella regressione, il team ha scoperto anche una vulnerabilità di sicurezza: **CVE-2026-40372**.

Nelle versioni `10.0.0` fino a `10.0.6` di `Microsoft.AspNetCore.DataProtection`, l'encryptor autenticato gestito calcolava il proprio tag di validazione HMAC sui **byte sbagliati** del payload e poi scartava l'hash calcolato. Questo poteva causare un'escalation dei privilegi.

In parole semplici: il controllo di integrità non faceva ciò che doveva. Data Protection usa la crittografia autenticata per impedire la manomissione — l'HMAC è il controllo "questo è stato modificato?". Se l'HMAC viene calcolato sui dati sbagliati, perdi quella garanzia.

## Chi È Interessato

Qualsiasi applicazione .NET 10 che usa `Microsoft.AspNetCore.DataProtection` — versioni da 10.0.0 a 10.0.6. La buona notizia è che questo pacchetto è specifico di .NET 10. Se sei ancora su .NET 8 o 9, non sei interessato da questa CVE specifica.

Usi comuni di Data Protection: crittografia dei cookie, token antiforgery, temp data in MVC e qualsiasi altro uso di `IDataProtector` nella tua applicazione.

## Come Risolvere Il Problema

Aggiorna il pacchetto NuGet `Microsoft.AspNetCore.DataProtection` a **10.0.7**:

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Oppure aggiorna il tuo SDK/runtime: [scarica .NET 10.0.7](https://dotnet.microsoft.com/download/dotnet/10.0).

Verifica di essere sulla versione corretta:

```bash
dotnet --info
```

Poi **ricompila e ridistribuisci** la tua applicazione. La correzione non entra in vigore finché non stai eseguendo il pacchetto aggiornato.

## Il Quadro Generale

Le release di sicurezza fuori banda sono rare — arrivano quando la vulnerabilità è abbastanza grave da non poter aspettare il Patch Tuesday successivo. Questa è una conseguenza diretta di una regressione in 10.0.6 che ha creato un varco di sicurezza. Il fatto che sia stata scoperta tramite segnalazioni di bug è un buon segno: il processo ha funzionato. La correzione è rapida e l'ambito è ristretto.

Se stai eseguendo .NET 10 in produzione con qualsiasi framework per applicazioni web, questa è una situazione da aggiornare nello stesso giorno.

Annuncio originale di Rahul Bhandari: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).