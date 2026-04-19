---
title: "Azure Smart Tier és GA: optimització automàtica de costos d'emmagatzematge de blob sense regles de cicle de vida"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "El nivell intel·ligent d'Azure Blob Storage ara està disponible en general, movent els objectes automàticament entre els nivells calents, freds i freds en funció dels patrons d'accés reals; no calen regles de cicle de vida."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

Si alguna vegada heu passat temps ajustant les polítiques de cicle de vida d'Azure Blob Storage i després heu vist com es van trencar quan els patrons d'accés canviaven, aquesta és la vostra. Microsoft acaba d'anunciar la [disponibilitat general del nivell intel·ligent](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) per a Azure Blob i Data Lake Storage: una capacitat de nivells totalment gestionada que mou automàticament objectes entre nivells calents, freds i freds en funció de l'ús real.

## Què fa realment el nivell intel·ligent

El concepte és senzill: el nivell intel·ligent avalua contínuament el darrer temps d'accés de cada objecte al vostre compte d'emmagatzematge. Les dades a les quals s'accedeix amb freqüència es mantenen en calent, les dades inactives es mouen per refredar-se després de 30 dies i després a fred després de 60 dies més. Quan s'accedeix de nou a les dades, es torna a activar immediatament. El cicle es reinicia.

No hi ha regles de cicle de vida per configurar. No hi ha prediccions de patrons d'accés. Sense sintonització manual.

Durant la previsualització, Microsoft va informar que **més del 50% de la capacitat gestionada per nivells intel·ligents es va canviar automàticament a nivells més freds** en funció dels patrons d'accés reals. Això suposa una reducció de costos significativa per als comptes d'emmagatzematge grans.

## Per què això és important per als desenvolupadors de.NET

Si esteu creant aplicacions que generen registres, telemetria, dades analítiques o qualsevol tipus de fons de dades en creixement, i sincerament, qui no, els costos d'emmagatzematge s'acumulen ràpidament. L'enfocament tradicional era escriure polítiques de gestió del cicle de vida, provar-les i tornar-les a ajustar quan canviaven els patrons d'accés de la vostra aplicació. El nivell intel·ligent elimina tot aquest flux de treball.

Alguns escenaris pràctics on això ajuda:

- **Telemetria i registres d'aplicacions**: calent durant la depuració, rarament s'hi accedeix després d'unes setmanes
- **Conductes de dades i sortides d'ETL**: s'hi accedeix molt durant el processament, després principalment en fred
- **Contingut generat per l'usuari**: les càrregues recents són interessants, el contingut més antic es refreda gradualment
- **Còpia de seguretat i dades d'arxiu**: s'accedeix de tant en tant per complir-ho, principalment inactiu

## Configurant-lo

Habilitar el nivell intel·ligent és una configuració única:

- **Comptes nous**: seleccioneu el nivell intel·ligent com a nivell d'accés predeterminat durant la creació del compte d'emmagatzematge (es requereix redundància zonal)
- **Comptes existents**: canvieu el nivell d'accés a blob del nivell predeterminat actual al nivell intel·ligent

Els objectes de menys de 128 KiB es mantenen en calent i no incorren en la taxa de supervisió. Per a la resta, pagueu tarifes estàndard de capacitat calenta/fresca/fred sense càrrecs de transició de nivell, sense despeses d'eliminació anticipada i sense costos de recuperació de dades. Una quota de seguiment mensual per objecte cobreix l'orquestració.

## La compensació a conèixer

Les regles de classificació del nivell intel·ligent són estàtiques (30 dies → fred, 90 dies → fred). Si necessiteu llindars personalitzats (per exemple, passar a la refrigeració després de 7 dies per a una càrrega de treball específica), les regles del cicle de vida encara són el camí a seguir. I no barregeu les dues coses: eviteu utilitzar regles de cicle de vida en objectes gestionats per nivell intel·ligent, ja que poden entrar en conflicte.

## Tancant

Això no és revolucionari, però soluciona un autèntic mal de cap operatiu. Si gestioneu comptes d'emmagatzematge de blobs en creixement i esteu cansat de mantenir polítiques de cicle de vida, [habilita el nivell intel·ligent](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) i deixeu que Azure s'encarregui. Actualment està disponible a gairebé totes les regions de núvol públic de zona.
