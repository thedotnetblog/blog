---
title: "KubeCon Europe 2026: què haurien de preocupar-se realment als desenvolupadors.NET"
date: 2026-03-29
author: "Emiliano Montesdeoca"
description: "Microsoft va deixar caure un mur d'anuncis de Kubernetes a KubeCon Europe 2026. Aquí teniu la versió filtrada: només les actualitzacions AKS i natives del núvol que importen si envieu aplicacions.NET."
tags:
  - kubernetes
  - aks
  - azure
  - dotnet
  - cloud-native
  - ai
---

Coneixes aquesta sensació quan cau una publicació d'anunci massiva i t'estàs desplaçant per ella pensant "genial, però què canvia això realment per a mi"? Soc jo cada temporada de la KubeCon.

Microsoft acaba de publicar [el seu resum complet de KubeCon Europe 2026](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/), escrit pel mateix Brendan Burns, i sincerament? Aquí hi ha substància real. No només inclouen les caselles de selecció, sinó també el tipus de millores operatives que canvien la manera d'executar les coses en producció.

Permeteu-me desglossar el que realment importa per als desenvolupadors de.NET.

## mTLS sense l'impost de malla de servei

Això és el que passa amb les malles de servei: tothom vol les garanties de seguretat, ningú vol la sobrecàrrega operativa. AKS finalment està tancant aquesta bretxa.

[Azure Kubernetes Application Network](https://aka.ms/aks/application-network) us ofereix TLS mutu, autorització conscient de l'aplicació i telemetria de trànsit, sense desplegar una malla plena de sidecars. Combinat amb [Cilium mTLS a Advanced Container Networking Services](https://aka.ms/acns/cilium-mtls), obteniu una comunicació xifrada de pod a pod mitjançant certificats X.509 i SPIRE per a la gestió d'identitats.

Què significa això a la pràctica: les vostres API ASP.NET Core parlen amb treballadors en segon pla, els vostres serveis gRPC es trucen entre ells, tot xifrat i verificat per la identitat a nivell de xarxa, sense canvis en el codi de l'aplicació. Això és enorme.

Per als equips que migren des de `ingress-nginx`, també hi ha [Application Routing with Meshless Istio](https://aka.ms/aks/app-routing/gateway-api) amb suport complet de l'API de Kubernetes Gateway. Sense sidecars. Basat en estàndards. I van enviar eines `ingress2gateway` per a la migració incremental.

## Observabilitat de la GPU que no és una idea posterior

Si utilitzeu una inferència d'IA juntament amb els vostres serveis.NET (i siguem sincers, qui no comença a fer-ho?), probablement heu arribat al punt cec de supervisió de la GPU. Obtindreu grans taulers de CPU/memòria i després... res per a les GPU sense una fontaneria d'exportació manual.

[AKS ara mostra les mètriques de la GPU de manera nativa](https://aka.ms/aks/managed-gpu-metrics) a Prometheus i Grafana gestionats. Mateixa pila, mateixos taulers de comandament, mateix canal d'alertes. Sense exportadors personalitzats, ni agents de tercers.

Al costat de la xarxa, van afegir visibilitat per flux per al trànsit HTTP, gRPC i Kafka amb una [experiència d'Azure Monitor amb un sol clic](https://learn.microsoft.com/en-us/azure/aks/container-network-observability-logs). IP, ports, càrregues de treball, direcció del flux, decisions polítiques, tot en taulers integrats.

I aquesta és la que m'ha fet fer una doble presa: [xarxa de contenidors agent](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview) afegeix una interfície d'usuari web on podeu fer preguntes en llenguatge natural sobre l'estat de la xarxa del vostre clúster. "Per què el pod X no arriba al servei Y?" → diagnòstics de només lectura de la telemetria en directe. Això és realment útil a les 2 del matí.

## Xarxes entre clústers que no requereixen un doctorat

Històricament, Kubernetes multiclúster ha estat una experiència de "porta la teva pròpia cola de xarxa". Azure Kubernetes Fleet Manager ara s'envia [xarxes entre clústers](https://aka.ms/kubernetes-fleet/networking/cross-cluster) mitjançant la malla de clúster de Cilium gestionada:

- Connectivitat unificada entre clústers AKS
- Registre global de serveis per a la descoberta entre clústers
- Configuració gestionada de manera centralitzada, no repetida per clúster

Si utilitzeu microserveis.NET en diferents regions per a la seva resiliència o compliment, això substitueix una gran quantitat de fontaneria personalitzada fràgil. El servei A a l'oest d'Europa pot descobrir i trucar al servei B a l'est dels EUA a través de la malla, amb polítiques d'encaminament i seguretat coherents.

## Actualitzacions que no requereixen valentia

Siguem sincers: les actualitzacions de Kubernetes en producció són estressants. "Actualitzar i esperar" ha estat l'estratègia de facto per a massa equips, i és el principal motiu pel qual els clústers es queden endarrerits en les versions.

Dues noves capacitats canvien això:

**Les actualitzacions del grup d'agents blau-verd** creen un grup de nodes paral·lels amb la nova configuració. Valideu el comportament, canvieu el trànsit gradualment i manteniu un camí de retrocés net. No més mutacions in situ als nodes de producció.

**La recuperació de l'agrupació d'agents** us permet revertir una agrupació de nodes a la seva versió anterior de Kubernetes i a la imatge de node després d'una actualització de costat, sense haver de reconstruir el clúster.

En conjunt, finalment donen als operadors un control real sobre el cicle de vida de l'actualització. Per als equips.NET, això és important perquè la velocitat de la plataforma controla directament la rapidesa amb què podeu adoptar nous temps d'execució, pedaços de seguretat i capacitats de xarxa.

## Les càrregues de treball d'IA s'estan convertint en ciutadans de primer nivell de Kubernetes

El treball de codi obert amunt és igual d'important. L'assignació dinàmica de recursos (DRA) acaba de passar a GA a Kubernetes 1.36, fent que la programació de la GPU sigui una funció adequada de primera classe en lloc d'una solució alternativa.

Alguns projectes que val la pena veure:

|Projecte|Què fa|
|---------|-------------|
|[AI Runway](https://github.com/kaito-project/kubeairunway)|API comuna de Kubernetes per a la inferència: implementeu models sense conèixer els K8, amb el descobriment d'HuggingFace i les estimacions de costos|
|[HolmesGPT](https://www.cncf.io/blog/2026/01/07/holmesgpt-agentic-troubleshooting-built-for-the-cloud-native-era/)|Resolució de problemes d'agent per als nadius del núvol: ara un projecte Sandbox CNCF|
|[Dalec](https://github.com/project-dalec/dalec)|La imatge de contenidor declarativa es construeix amb la generació SBOM: menys CVE en l'etapa de creació|

La direcció és clara: la vostra API.NET, la vostra capa d'orquestració del nucli semàntic i les vostres càrregues de treball d'inferència s'han d'executar en un model de plataforma coherent. Hi arribem.

## Per on començaria aquesta setmana

Si esteu avaluant aquests canvis per al vostre equip, aquí teniu la meva llista de prioritats honesta:

1. **Observabilitat primer**: activeu les mètriques de la GPU i els registres de flux de xarxa en un clúster que no sigui de producte. Mira què t'has perdut.
2. **Proveu les actualitzacions blau-verd**: proveu el flux de treball de retrocés abans de la propera actualització del clúster de producció. Generar confiança en el procés.
3. **Pilota de xarxes conscients de la identitat**: trieu una ruta de servei interna i activeu mTLS amb Cilium. Mesureu la sobrecàrrega (spoiler: és mínim).
4. **Avalueu el gestor de flotes**: si executeu més de dos clústers, la xarxa entre clústers es compensa amb una cola personalitzada reduïda.

Petits experiments, feedback ràpid. Aquest és sempre el moviment.

## Tancant

Els anuncis de KubeCon poden ser aclaparadors, però aquest lot realment mou l'agulla dels equips.NET a AKS. Millor seguretat de xarxes sense sobrecàrrega de malla, observabilitat real de la GPU, actualitzacions més segures i bases d'infraestructura d'IA més sòlides.

Si ja esteu a AKS, aquest és un bon moment per endurir la vostra línia de base operativa. I si teniu previst traslladar les càrregues de treball.NET a Kubernetes, la plataforma s'acaba de preparar molt més per a la producció.
