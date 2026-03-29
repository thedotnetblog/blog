---
title: "Dal laptop alla produzione: deploy di agenti IA su Microsoft Foundry con due comandi"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI ora ha i comandi 'azd ai agent' che portano il tuo agente IA dallo sviluppo locale a un endpoint Foundry in produzione in pochi minuti. Ecco il workflow completo."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

Conosci quel divario tra "funziona sulla mia macchina" e "è in produzione e serve traffico"? Per gli agenti IA, quel divario è stato dolorosamente ampio. Devi provisionare risorse, fare il deploy dei modelli, configurare l'identità, impostare il monitoraggio — e questo è prima che qualcuno possa effettivamente chiamare il tuo agente.

L'Azure Developer CLI ha appena reso tutto questo una [questione di due comandi](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## Il nuovo workflow `azd ai agent`

Lascia che ti mostri come funziona nella pratica. Hai un progetto di agente IA — diciamo un agente concierge d'hotel. Funziona in locale. Vuoi farlo girare su Microsoft Foundry.

```bash
azd ai agent init
azd up
```

Tutto qui. Due comandi. `azd ai agent init` genera l'infrastructure-as-code nel tuo repo, e `azd up` provisiona tutto su Azure e pubblica il tuo agente. Ottieni un link diretto al tuo agente nel portale Foundry.

## Cosa succede sotto il cofano

Il comando `init` genera template Bicep reali e ispezionabili nel tuo repo:

- Una **Foundry Resource** (contenitore di livello superiore)
- Un **Foundry Project** (dove vive il tuo agente)
- Configurazione del **deployment del modello** (GPT-4o, ecc.)
- **Managed Identity** con assegnazioni di ruoli RBAC appropriate
- `azure.yaml` per la mappa dei servizi
- `agent.yaml` con metadati dell'agente e variabili d'ambiente

Il punto chiave: tutto questo è tuo. È Bicep versionato nel tuo repo. Puoi ispezionarlo, personalizzarlo e committarlo insieme al codice del tuo agente. Nessuna scatola nera magica.

## Il ciclo interno di sviluppo

Quello che mi piace davvero è l'esperienza di sviluppo locale. Quando stai iterando sulla logica dell'agente, non vuoi fare il redeploy ogni volta che cambi un prompt:

```bash
azd ai agent run
```

Questo avvia il tuo agente in locale. Combinalo con `azd ai agent invoke` per inviare prompt di test, e hai un ciclo di feedback stretto. Modificare codice, riavviare, invocare, ripetere.

Il comando `invoke` è anche intelligente nel routing — quando un agente locale è in esecuzione, lo punta automaticamente. Quando non lo è, va all'endpoint remoto.

## Monitoraggio in tempo reale

Questa è la funzionalità che mi ha convinto. Una volta che il tuo agente è in deploy:

```bash
azd ai agent monitor --follow
```

Ogni richiesta e risposta che passa attraverso il tuo agente viene trasmessa al tuo terminale in tempo reale. Per il debug di problemi in produzione, non ha prezzo. Niente ricerche in Log Analytics, niente attese per l'aggregazione delle metriche — vedi cosa sta succedendo adesso.

## Il set completo dei comandi

Ecco il riferimento rapido:

| Comando | Cosa fa |
|---------|---------|
| `azd ai agent init` | Scaffold di un progetto agente Foundry con IaC |
| `azd up` | Provisiona risorse Azure e fa il deploy dell'agente |
| `azd ai agent invoke` | Invia prompt all'agente remoto o locale |
| `azd ai agent run` | Esegue l'agente in locale per lo sviluppo |
| `azd ai agent monitor` | Streama log in tempo reale dall'agente pubblicato |
| `azd ai agent show` | Controlla salute e stato dell'agente |
| `azd down` | Pulisce tutte le risorse Azure |

## Perché è importante per gli sviluppatori .NET

Anche se l'esempio nell'annuncio è basato su Python, la storia dell'infrastruttura è language-agnostic. Il tuo agente .NET ottiene lo stesso scaffolding Bicep, lo stesso setup di managed identity, la stessa pipeline di monitoraggio. E se stai già usando `azd` per le tue app .NET Aspire o deployment Azure, si integra direttamente nel tuo workflow esistente.

Il divario di deployment per gli agenti IA è stato uno dei maggiori punti di attrito nell'ecosistema. Passare da un prototipo funzionante a un endpoint di produzione con identità, networking e monitoraggio appropriati non dovrebbe richiedere una settimana di lavoro DevOps. Ora richiede due comandi e qualche minuto.

## Per concludere

`azd ai agent` è disponibile ora. Se hai rimandato il deployment dei tuoi agenti IA perché il setup dell'infrastruttura sembrava troppo lavoro, provalo. Consulta il [walkthrough completo](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) per la guida passo per passo inclusa l'integrazione di un'app chat frontend.
