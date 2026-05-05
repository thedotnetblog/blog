---
title: "Servidor Azure DevOps d'abril de 2026: correcció de finalització de relacions públiques i actualitzacions de seguretat"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "L'Azure DevOps Server obté el Pedaç 3 amb una solució per a errors de finalització de relacions públiques, una validació de tancament de sessió millorada i connexions PAT restaurades de GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

Informació ràpida per als equips que executen Azure DevOps Server: Microsoft va llançar [el pegat 3 per a l'abril de 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) amb tres solucions específiques.

## Què s'ha solucionat

- **Errores de finalització de la sol·licitud d'extracció**: una excepció de referència nul·la durant la compleció automàtica d'elements de treball podria provocar que les combinacions de PR fallin. Si heu trobat errors de finalització de PR aleatòries, és probable que aquesta sigui la causa
- **Validació de la redirecció de tancament de la sessió**: validació millorada durant la tancament de la sessió per evitar possibles redireccions malicioses. Aquesta és una solució de seguretat que val la pena aplicar ràpidament
- **Connexions PAT del servidor GitHub Enterprise**: la creació de connexions de testimoni d'accés personal al servidor GitHub Enterprise es va trencar, ara s'ha restaurat

## Com actualitzar

Baixeu [Pedaç 3](https://aka.ms/devopsserverpatch3) i executeu l'instal·lador. Per verificar que s'ha aplicat el pegat:

```bash
<patch-installer>.exe CheckInstall
```

Si esteu executant Azure DevOps Server localment, Microsoft us recomana fermament mantenir-vos en l'últim pedaç tant per seguretat com per fiabilitat. Consulteu les [notes de la versió](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) per a tots els detalls.
