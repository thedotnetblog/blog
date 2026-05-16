---
title: "Aggiornamenti di Azure Developer CLI (azd) per aprile 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd ha rilasciato cinque versioni ad aprile 2026, guidate dal supporto hooks multi-linguaggio per Python, JavaScript, TypeScript e .NET — oltre alla preview pubblica di azd update, controlli preliminari della quota AI e altro ancora."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) ha rilasciato cinque versioni ad aprile 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (dalla 1.23.14 alla 1.24.2), con il grande tema degli hook che ora si eseguono in Python, JavaScript, TypeScript e .NET — non solo in Bash e PowerShell.

## Hook multi-linguaggio in azure.yaml

Gli hook possono ora puntare a file `.py`, `.js`, `.ts` o `.cs` oltre agli script shell. Ogni linguaggio ottiene la risoluzione automatica delle dipendenze:

- **Python** — rileva `requirements.txt` o `pyproject.toml`, crea un virtualenv e installa le dipendenze prima dell'esecuzione. Configura il nome dell'ambiente con `virtualEnvName`.
- **JavaScript / TypeScript** — rileva `package.json` ed esegue `npm install` automaticamente. TypeScript viene eseguito tramite `npx tsx` senza necessità di un passaggio di compilazione. Scegli il tuo package manager con il blocco di configurazione `packageManager`.
- **.NET** — esegue file `.cs` con `dotnet run`. Gli script single-file sono supportati su .NET 10+. Configura il framework di destinazione tramite il blocco `configuration/framework`.

Questo significa che i team che già lavorano in uno di questi linguaggi non hanno più bisogno di mantenere un hook Bash o PowerShell separato solo per collegare gli eventi del ciclo di vita del provisioning.

## azd update arriva in preview pubblica

`azd update` è ora in preview pubblica su tutte le piattaforme. Un singolo comando gestisce l'aggiornamento indipendentemente da come azd è stato installato originalmente — non è più necessario tracciare separatamente i percorsi di Homebrew, WinGet o MSI.

## Modalità non interattiva tramite AZD_NON_INTERACTIVE

Impostare `AZD_NON_INTERACTIVE=true` (o usare `--non-interactive` / `--no-prompt`) produce ora fallimenti coerenti e deterministici nelle pipeline CI/CD quando un input richiesto non può essere risolto automaticamente. In precedenza il comportamento era inconsistente tra i comandi.

## Verifica preliminare della quota dei modelli AI

`azd provision` valida la quota di Azure Cognitive Services prima di tentare di effettuare il provisioning delle risorse dei modelli AI. I deployment che fallirebbero a causa dei limiti di quota ora mostrano l'errore all'inizio del processo anziché a metà del provisioning.

## "Correggi questo errore" nella risoluzione dei problemi di Copilot

L'integrazione per la risoluzione dei problemi di Copilot in azd ottiene la capacità di applicare direttamente una correzione suggerita — non solo di descriverla. Quando l'agente identifica un problema risolvibile, può apportare la modifica in loco.

## Provider di provisioning personalizzati e resolver di segreti Key Vault

Gli autori di estensioni possono ora registrare backend di infrastruttura alternativi con `WithProvisioningProvider()`. Separatamente, azd risolve automaticamente i riferimenti `@Microsoft.KeyVault(...)` prima di passare la configurazione alle estensioni, eliminando la necessità di una risoluzione manuale dei segreti nei provider personalizzati.

## Esclusioni per template e modalità watch

Due nuovi file ignore offrono un controllo più preciso sulla gestione dei file:
- **`.azdignore`** — esclude i file riservati ai contributori (documentazione, configurazioni CI) dalle copie dei template affinché gli utenti finali ottengano uno scaffold di progetto pulito.
- **`.azdxignore`** — esclude le directory dal trigger di ricostruzioni durante `azd x watch`, riducendo il rumore durante lo sviluppo iterativo.

## Verifica preliminare dei nomi riservati e opzione docker.network

azd avverte ora quando i nomi di risorse previsti conterrebbero parole riservate di Azure (`MICROSOFT`, `WINDOWS` o il prefisso `LOGIN`) prima che inizi il provisioning. Una nuova opzione `docker.network` passa `--network` a `docker build`, utile negli ambienti proxy aziendali che richiedono una rete Docker specifica.

## Correzioni di sicurezza

Il pacchetto MSI di Windows ora include la verifica della firma del codice. Una correzione separata chiude una perdita di variabili d'ambiente che poteva esporre valori attraverso i confini dei comandi delle estensioni.

---

Un mese intenso — il supporto degli hook multi-linguaggio in particolare elimina un vero punto di attrito per i team che non lavorano principalmente in Bash. Consulta le [note di rilascio complete](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) per il changelog completo di tutte e cinque le versioni.
