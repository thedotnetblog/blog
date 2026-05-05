---
title: "Quell'Impostazione delle Finestre Flottanti di Visual Studio Che Non Conoscevi (Ma Dovresti)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Un'impostazione nascosta di Visual Studio ti dà il pieno controllo sulle finestre flottanti — voci indipendenti nella barra delle applicazioni, comportamento corretto con più monitor e integrazione perfetta con FancyZones. Un menu a tendina cambia tutto."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "visual-studio-floating-windows-powertoys.md" >}}).*

Se usate più monitor con Visual Studio (e onestamente, chi non lo fa al giorno d'oggi?), probabilmente avete sperimentato la frustrazione: le finestre degli strumenti flottanti scompaiono quando minimizzate l'IDE principale, restano sempre sopra a tutto il resto, e non appaiono come pulsanti separati nella barra delle applicazioni. Funziona per alcuni workflow, ma per configurazioni multi-monitor è frustrante.

Mads Kristensen del team di Visual Studio [ha condiviso un'impostazione poco conosciuta](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) che cambia completamente il comportamento delle finestre flottanti. Un menu a tendina. Tutto qui.

## L'impostazione

**Tools > Options > Environment > Windows > Floating Windows**

Il menu a tendina "These floating windows are owned by the main window" ha tre opzioni:

- **None** — indipendenza totale. Ogni finestra flottante ha la propria voce nella barra delle applicazioni e si comporta come una normale finestra di Windows.
- **Tool Windows** (predefinito) — i documenti flottano liberamente, le finestre degli strumenti restano legate all'IDE.
- **Documents and Tool Windows** — comportamento classico di Visual Studio, tutto legato alla finestra principale.

## Perché "None" è la scelta giusta per configurazioni multi-monitor

Impostatelo su **None** e improvvisamente tutte le vostre finestre flottanti di strumenti e documenti si comportano come vere applicazioni Windows. Appaiono nella barra delle applicazioni, restano visibili quando minimizzate la finestra principale di Visual Studio, e smettono di forzarsi in primo piano.

Combinatelo con **PowerToys FancyZones** ed è un vero game changer. Create layout personalizzati sui vostri monitor, agganciate l'Esplora Soluzioni in una zona, il debugger in un'altra, e i file di codice dove volete. Tutto resta al suo posto, tutto è accessibile indipendentemente, e il vostro spazio di lavoro risulta organizzato invece che caotico.

## Raccomandazioni rapide

- **Utenti avanzati multi-monitor**: Impostate su **None**, abbinate con FancyZones
- **Utenti occasionali delle finestre flottanti**: **Tool Windows** (predefinito) è un buon compromesso
- **Workflow tradizionale**: **Documents and Tool Windows** mantiene tutto classico

Consiglio pro: **Ctrl + doppio clic** sulla barra del titolo di qualsiasi finestra degli strumenti per renderla flottante o agganciarla istantaneamente. Non serve riavviare dopo aver cambiato l'impostazione.

## Conclusione

È una di quelle impostazioni del tipo "non ci posso credere che non lo sapevo". Se le finestre flottanti in Visual Studio vi hanno mai infastidito, andate a cambiare questa impostazione adesso.

Leggete il [post completo](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) per i dettagli e gli screenshot.
