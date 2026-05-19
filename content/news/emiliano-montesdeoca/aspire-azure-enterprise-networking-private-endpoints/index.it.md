---
title: "Endpoint Privati, VNet, NSG — Aspire Gestisce la Rete Ora"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Il nuovo supporto per le reti aziendali Azure di Aspire consente di modellare VNet, endpoint privati, gateway NAT, NSG e perimetri di sicurezza di rete direttamente nell'AppHost, senza deriva dell'infrastruttura."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Ho visto questo scenario troppe volte. L'app è pronta. La demo è fantastica. Poi arriva la checklist di sicurezza: porta lo storage fuori da internet pubblico, esegui all'interno di un VNet, fornisci IP in uscita per l'allowlist del partner, dimostra che solo le subnet giuste parlano con i servizi giusti.

A quel punto il modello dell'applicazione e il modello dell'infrastruttura iniziano a divergere in modi che sono dolorosi da mantenere.

Il nuovo supporto per le reti aziendali Azure di Aspire affronta questo direttamente. Descrivi la forma della rete accanto alle risorse che la usano, nel tuo AppHost.

## I Blocchi di Costruzione

Ecco a cosa serve ogni concetto di rete Azure, sintetizzato:

| Funzionalità | Usala quando | Perché è importante |
|---------|------------|----------------|
| Rete virtuale | Hai bisogno di uno spazio di indirizzi privato | Il confine di rete per subnet, endpoint privati e routing |
| Subnet | Devi separare i carichi di lavoro all'interno del VNet | Ogni parte del sistema ottiene il proprio intervallo di indirizzi e superficie di policy |
| Subnet delegata | Un servizio di piattaforma (come ACA) deve gestire una subnet | Consente al servizio di posizionare infrastruttura gestita nel tuo VNet in modo sicuro |
| Gateway NAT | Hai bisogno di IP pubblici in uscita prevedibili | Indirizzo stabile per allowlist e auditing |
| Endpoint privato | Vuoi una risorsa PaaS raggiungibile privatamente | Inserisce un IP privato per quel servizio nel tuo VNet, rimuove l'esposizione pubblica |
| NSG | Hai bisogno di regole di traffico a livello di subnet | Permetti/nega esplicito per il traffico in entrata e in uscita per subnet |

## Descrivendolo nel tuo AppHost

Il cambiamento chiave qui è che stai modellando la rete *insieme* alle risorse che la usano, non in un file Bicep separato che si allontana dal modello dell'applicazione nel tempo.

Dall'AppHost puoi:

- Creare VNet e subnet con `AddVirtualNetwork()` e `AddSubnet()`
- Allegare un gateway NAT alle subnet per IP in uscita stabili
- Creare endpoint privati per storage, Key Vault, SQL e altri servizi PaaS
- Definire NSG con regole di sicurezza in entrata e in uscita
- Configurare Perimetri di Sicurezza di Rete per policy tra risorse

Il risultato è che quando esegui `azd up`, l'infrastruttura corrisponde a ciò che il modello dell'applicazione dice di cui ha bisogno. Non quello che dice un template mantenuto manualmente.

## Perché Questo è Importante per le Applicazioni Reali

Alcune cose che diventano significativamente più facili una volta che la rete è modellata in Aspire:

**Endpoint privati per Key Vault e storage** — descrivi `WithPrivateEndpoint()` su quelle risorse, e Aspire gestisce la configurazione delle zone DNS e l'allegato degli endpoint. L'app non cambia mai.

**IP in uscita coerenti** — aggiungi un gateway NAT alla subnet pertinente e ogni richiesta in uscita dalla tua app passa attraverso un IP noto e stabile. I partner possono aggiungerlo all'allowlist. I revisori possono tracciarlo.

**Regole NSG dal codice** — invece di cliccare nel portale o mantenere un frammento Bicep, le tue regole di sicurezza vivono nell'AppHost accanto alle risorse che proteggono.

Questo è il tipo di integrazione che non rende le demo eccitanti ma rende i sistemi di produzione manutenibili.

## Conclusione

La sicurezza di rete che appare tardi nel ciclo di vita del progetto è un problema risolto se la modelli insieme all'app fin dall'inizio. Il supporto per le reti aziendali di Aspire rende ciò possibile senza richiedere una traccia di infrastruttura separata.

Dettagli completi nel post originale: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
