---
title: "Aspire 13.3: Suport de Kubernetes, Registres del Navegador i la Habilitat Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Cinc setmanes després del 13.2, Aspire 13.3 arriba amb 45 noves funcions incloent desplegament AKS de primera classe, una habilitat d'incorporació assistida per IA, captura de registres del navegador i resultats d'ordres estructurats."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Cinc setmanes no és molt de temps per a una versió, però Aspire 13.3 no ho sembla. Els elements principals són significatius: desplegament de Kubernetes i AKS de primera classe amb Helm, una habilitat d'incorporació assistida per agent anomenada Aspireify, captura de registres del navegador directament al dashboard i resultats d'ordres estructurats. A més, 45 noves funcions, 134 millores i 93 correccions d'errors.

Anem als punts destacats.

## Aspireify: Incorporació Assistida per Agent

Afegir Aspire a un projecte existent sona senzill — afegeix un AppHost, llest. En la pràctica implica molta arqueologia: quins ports importen, quines variables d'entorn són dependències reals, quins serveis de Docker Compose s'han de mapejar a integracions d'Aspire.

La nova **habilitat Aspireify** ofereix al teu agent de codi un flux de treball guiat exactament per a això. Quan `aspire init` crea un AppHost esquelet, la habilitat Aspireify ajuda l'agent a inspeccionar el repositori, entendre com ja s'executa i connectar l'AppHost per adaptar-se a l'aplicació — no al revés.

La postura predeterminada és "minimitzar els canvis al teu codi." Si la teva aplicació ja llegeix `DATABASE_URL`, l'agent ho mapeja amb `WithEnvironment()` en lloc de demanar-te que reescriguis la teva configuració. Si un port està codificat de forma fixa, l'habilitat indica a l'agent quan preservar-lo.

Aquest és el tipus d'eines d'IA que realment estalvien temps en lloc de generar més feina per revisar.

## Desplegament de Kubernetes i AKS de Primera Classe

Aquesta és una que ha estat a la llista de desitjos durant un temps. Aspire 13.3 inclou **suport de desplegament de Kubernetes i AKS de primera classe amb Helm**. Ara pots apuntar a AKS com a destí de desplegament directament des de les eines d'Aspire.

Per als equips que ja executen càrregues de treball de producció a AKS, això tanca una bretxa significativa. El teu model d'aplicació d'Aspire ara té un camí net des del desenvolupament local fins a Kubernetes sense necessitat d'escriure manualment gràfics Helm.

## Registres del Navegador al Dashboard

Aquesta és una de les funcions que semblen petites fins que estàs depurant un problema de frontend.

La nova API `WithBrowserLogs()` adjunta un recurs de navegador rastrejat a qualsevol recurs capaç d'endpoints. Aspire llança Chromium usant un pipe CDP privat i transmet registres de consola, sol·licituds de xarxa i errors directament al flux de registres del recurs:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

L'AppHost de TypeScript admet el mateix:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Errors de consola, sol·licituds de xarxa fallides, excepcions del costat del client — tot visible al mateix dashboard on ja estàs observant traces i mètriques. Sense haver de canviar de pestanya a les DevTools del navegador per les coses bàsiques.

## Resultats d'Ordres Estructurats

Les ordres de recursos han rebut una millora significativa. Fins ara, les ordres retornaven èxit/fracàs. Ara retornen resultats estructurats: text, JSON o markdown que flueix a través del model, la interfície del dashboard, la CLI i les eines MCP.

El dashboard lliga tot això amb un nou centre de notificacions a la capçalera. Els resultats de les ordres apareixen com a notificacions amb marca de temps amb renderització de markdown i una acció "Veure resposta".

Això fa que les ordres de recursos siguin veritablement composables. Una integració ara pot exposar una ordre que retorna una sortida significativa — com ara una URL de túnel — en lloc de simplement canviar l'estat en algun lloc.

## Conclusió

Aspire 13.3 val l'actualització encara que sigui només pel suport de Kubernetes. Els registres del navegador i els resultats d'ordres estructurats semblen el tipus de millores de qualitat de vida que s'acumulen ràpidament en el flux de treball de desenvolupament quotidià.

Notes de versió completes: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
