---
title: "Azure DevOps Server Patch Aprile 2026 — Fix per il Completamento delle PR e Aggiornamenti di Sicurezza"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server riceve la Patch 3 con un fix per i fallimenti nel completamento delle PR, validazione migliorata al logout e ripristino delle connessioni PAT con GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Avviso rapido per i team che eseguono Azure DevOps Server in self-hosting: Microsoft ha rilasciato la [Patch 3 di aprile 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) con tre fix mirati.

## Cosa è stato corretto

- **Fallimenti nel completamento delle pull request** — un'eccezione di riferimento null durante l'auto-completamento dei work item poteva causare il fallimento dei merge delle PR. Se hai riscontrato errori casuali nel completamento delle PR, questa è probabilmente la causa
- **Validazione del redirect al logout** — validazione migliorata durante il logout per prevenire potenziali redirect malevoli. Questo è un fix di sicurezza che vale la pena applicare tempestivamente
- **Connessioni PAT con GitHub Enterprise Server** — la creazione di connessioni con Personal Access Token verso GitHub Enterprise Server era rotta, ora è stata ripristinata

## Come aggiornare

Scarica la [Patch 3](https://aka.ms/devopsserverpatch3) e avvia l'installer. Per verificare che la patch sia stata applicata:

```bash
<patch-installer>.exe CheckInstall
```

Se esegui Azure DevOps Server on-premises, Microsoft raccomanda fortemente di restare sempre sull'ultima patch sia per sicurezza che per affidabilità. Consulta le [note di rilascio](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) per tutti i dettagli.
