---
title: "L'Accés a Cosmos DB Sense Secrets és la Nova Línia Base"
date: 2026-07-16
author: "Emiliano Montesdeoca"
description: "Si la teva aplicació de Cosmos DB encara depèn de claus, ja estàs endarrerit en seguretat operativa."
tags:
  - azure-cosmos-db
  - dotnet
  - managed-identity
  - rbac
  - cloud-security
---

Font original: [Which Azure Cosmos DB Role Does My App Need?](https://devblogs.microsoft.com/cosmosdb/which-azure-cosmos-db-role-does-my-app-need/)

La idea més important d'aquesta guia de Cosmos DB no és una ordre, un ID de rol o un truc de CLI. És arquitectònica: deixeu de tractar les credencials com a configuració de l'aplicació i comenceu a tractar la identitat com a estat d'execució.

Masses equips encara envien amb cadenes de connexió perquè sembla ràpid. No és ràpid. És risc ajornat. Cada clau en un fitxer de configuració es converteix en un incident esperant un commit precipitat, una variable de pipeline copiada o un log filtrat. Managed identity més RBAC del pla de dades elimina gairebé completament aquesta classe de fallades.

El repte pràctic és la confusió entre l'autorització del pla de control i del pla de dades. Aquí és on molts equips, fins i tot els forts, perden dies. Els rols d'Azure RBAC als recursos no atorguen automàticament accés als documents, i els rols del pla de dades de Cosmos DB no atorguen administració del compte. Si el vostre equip no documenta explícitament aquesta separació als runbooks, seguireu tenint desplegaments fràgils i errors 403 difícils de depurar.

La meva recomanació per als equips de producció és simple:

Comenceu amb Data Reader per a camins de lectura i Data Contributor només on els escriptoris siguin realment necessaris.

Amplieu l'abast només quan tingueu un sol límit d'aplicació per compte.

Si compartiu un compte entre serveis, reduïu l'abast aviat als límits de base de dades o contenidor en lloc d'esperar la pressió d'auditoria.

Aquesta és una d'aquestes decisions que es componen. Quan connecteu la vostra aplicació .NET amb DefaultAzureCredential i configuració només d'endpoint, cada entorn es torna més net: local, CI, staging i prod. També feu que la resposta a incidents sigui més ràpida perquè podeu raonar sobre els permisos a través d'assignacions de rols en lloc de caçar claus misterioses.

L'article també insinua una cosa que els equips madurs haurien d'adoptar: els permisos com a disseny iteratiu, no com a configuració única. Podeu començar prou ampli per lliurar, després reduir amb telemetria i revisions d'accés. El privilegi mínim no és un punt final filosòfic; és un hàbit de lliurament.

Si només adopteu una cosa d'aquest article, feu que sigui això: elimineu els secrets primer, optimitzeu els rols després. Els equips que inverteixen aquest ordre solen encallar-se en reunions. Els equips que eliminen secrets primer solen enviar, després endurir.

El 2026, l'accés a dades sense secrets no és un patró avançat. És l'estàndard mínim responsable per a sistemes .NET seriosos a Azure.