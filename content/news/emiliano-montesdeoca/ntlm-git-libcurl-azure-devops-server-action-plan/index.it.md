---
title: "NTLM Sta Finendo in Git/libcurl: I Team Azure DevOps Server Hanno Bisogno di un Vero Piano di Migrazione"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "La rimozione di NTLM a settembre 2026 non è un problema minore di compatibilità; è una scadenza di architettura dell'identità per ambienti Azure DevOps Server on-prem."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

La prossima rimozione di NTLM in libcurl è uno di quei cambiamenti che sembrano tecnici ma sono in realtà organizzativi. Se il tuo percorso Git su HTTPS verso Azure DevOps Server dipende ancora da NTLM, il tuo problema non è il tooling, è debito di identità.

Fonte originale: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft ha ragione a spingere forte qui. NTLM ha debolezze crittografiche note e non dovrebbe essere un'impostazione predefinita enterprise moderna. La parte pericolosa è che molti ambienti credono di usare Kerberos quando in realtà sopravvivono con il fallback silenzioso SPNEGO a NTLM. Quell'illusione scompare a settembre 2026.

La mia opinione: **non trattarlo come un problema di "versione client"**. Riabilitare i flag NTLM, bloccare vecchie build di Git o sperare che il fallback rimanga disponibile è una soluzione temporanea di breve durata con rischio a lungo termine. Se la tua strategia di remediation è downgrade-e-ritarda, stai attivamente aumentando la fragilità operativa.

Una sequenza di migrazione pratica dovrebbe essere diretta e misurabile.

- **Verifica il comportamento di autenticazione attuale ora.** Esegui controlli basati su trace e validazione della cache dei ticket in contesti reali di sviluppatori e build agent, inclusi percorsi off-domain e remote-network.
- **Ripara Kerberos end-to-end:** SPN, alias DNS, impostazioni del load balancer, delega e raggiungibilità del domain controller.
- **Identifica presto gli scenari non-domain-joined o workgroup** e progetta una corsia SSH dove Kerberos non può essere reso affidabile.

Hai anche bisogno di chiarezza di proprietà. I team di sicurezza dovrebbero definire le baseline di policy, ma la platform engineering deve possedere la prontezza dell'implementazione. Questo non può essere un compito secondario per singoli amministratori di repo. Richiede cambiamenti coordinati in IIS, AD, perimetro di rete, agenti CI e guida per workstation sviluppatore.

Un rischio sottile è l'automazione. Build agent e account di servizio spesso vengono eseguiti in contesti dove i ticket Kerberos mancano o non sono validi, anche quando gli utenti umani funzionano. Se testi solo i workflow interattivi degli sviluppatori, perderai i punti di rottura più critici.

Il lato positivo è reale. Passare pulitamente a Kerberos o SSH non solo evita la rottura, ma **riduce la superficie di attacco e allinea i controlli di identità** con le aspettative di conformità moderne. I team che iniziano questa transizione ora tratteranno settembre come un non-evento. I team che aspettano faranno debug di fallimenti di autenticazione sotto pressione di rilascio.

Questo non è un avviso da archiviare. **È una scadenza da eseguire.**