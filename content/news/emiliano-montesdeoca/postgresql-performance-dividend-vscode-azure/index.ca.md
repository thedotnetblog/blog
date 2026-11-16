---
title: "El Treball de Rendiment de PostgreSQL Hauria de Passar on Escrius Codi"
date: 2026-07-20
author: "Emiliano Montesdeoca"
description: "El millor flux de treball d'ajust de PostgreSQL no són més dashboards, sinó bucles de retroalimentació més ajustats dins de l'editor."
tags:
  - postgresql
  - azure
  - visual-studio-code
  - database-performance
  - devops
---

Font original: [The performance dividend: Optimizing PostgreSQL on Azure directly in Visual Studio Code](https://azure.microsoft.com/en-us/blog/the-performance-dividend-optimizing-postgresql-on-azure-directly-in-visual-studio-code/)

Estic d'acord amb la tesi central d'aquesta actualització d'Azure: el treball de rendiment falla menys per falta d'eines i més per context fragmentat. La majoria d'equips ja tenen monitorització, editors de consultes i dashboards d'operacions. El que els falta és continuitat des del senyal fins a l'acció.

La direcció de l'extensió PostgreSQL a VS Code importa perquè escurça aquest camí. Quan les mètriques del servidor, els plans de consulta i les recomanacions d'assessor apareixen al mateix lloc on els desenvolupadors ja editen SQL, els equips es mouen del diagnòstic a la correcció més ràpid. Això sembla obvi, però en organitzacions reals és un canvi estructural. Els canvis de context són on es perd la propietat.

Aquí teniu la part pràctica per als líders d'enginyeria. Si voleu guanys mesurables, no introduïu aquestes capacitats com a opcionals agradables de tenir. Feu-les part del vostre flux de revisió:

Requereixi una captura de pantalla o resum del pla de consulta per a cada canvi de consulta no trivial.

Feu un seguiment setmanal de les principals recomanacions de l'assessor i assigneu propietaris, no només alertes.

Tracteu l'IntelliSense conscient d'esquema i la correcció de search_path com a eines de prevenció, no com a comoditat.

L'article també posiciona Azure HorizonDB com a visió de futur mentre manté Azure Database for PostgreSQL com el valor predeterminat de producció d'avui. Aquest és exactament l'enfocament correcte. Els equips es fiquen en problemes quan converteixen l'emoció de la tecnologia en previsualització en compromisos operatius massa aviat. Estabilitat primer, després experimentació selectiva.

La meva opinió forta: la cultura de rendiment és un problema d'editor abans de ser un problema de núvol. Si l'ajust només passa en focs i sales de guerra, no esteu fent enginyeria de rendiment, esteu fent resposta a incidents de rendiment. La història d'integració de VS Code ajuda els equips a moure's a l'esquerra, on viuen les correccions més barates.

Hi ha un advertiment. Les recomanacions integrades poden crear excés de confiança si els equips deixen de validar suposicions contra el comportament de la càrrega de treball. L'ajust assistit per IA i els consells de l'assessor són acceleradors, no substituts de la disciplina de benchmarks. Encara necessiteu línies base, proves de càrrega repetibles i comportes de regressió.

Si la vostra organització executa PostgreSQL a Azure a escala, el moviment correcte ara és estandarditzar aquest flux de treball integrat, després instrumentar el temps de cicle des de la detecció d'incidències fins a la mitigació. El dividend de rendiment és real, però només si l'operacionalitzeu. En cas contrari, és només una altra demo de funcions.

Conclusió: no compreu més observabilitat. Col·lapseu la distància entre la informació i el canvi.