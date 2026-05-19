---
title: "Endpoints Privats, VNets, NSGs — Aspire Gestiona la Xarxa Ara"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "El nou suport de xarxa empresarial d'Azure per a Aspire permet modelar VNets, endpoints privats, passarel·les NAT, NSGs i perímetres de seguretat de xarxa directament al teu AppHost, sense deriva d'infraestructura."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

He vist aquest escenari massa vegades. L'aplicació està llesta. La demostració és fantàstica. Aleshores apareix la llista de verificació de seguretat: treu l'emmagatzematge d'internet públic, executa dins d'una VNet, proporciona IPs de sortida per a la llista d'autoritats del soci, demostra que només les subxarxes correctes parlen amb els serveis correctes.

En aquest punt, el model d'aplicació i el model d'infraestructura comencen a divergir d'una manera que és dolorosa de mantenir.

El nou suport de xarxa empresarial d'Azure per a Aspire aborda això directament. Describes la forma de la xarxa juntament amb els recursos que l'utilitzen, al teu AppHost.

## Els Blocs de Construcció

Aquí teniu per a què serveix cada concepte de xarxa d'Azure, resumit:

| Característica | Usa-la quan | Per què importa |
|---------|------------|----------------|
| Xarxa virtual | Necessites un espai d'adreces privat | El límit de xarxa per a subxarxes, endpoints privats i enrutament |
| Subxarxa | Cal separar càrregues de treball dins de la VNet | Cada part del sistema obté el seu propi rang d'adreces i superfície de política |
| Subxarxa delegada | Un servei de plataforma (com ACA) necessita gestionar una subxarxa | Permet que el servei col·loqui infraestructura gestionada a la teva VNet de manera segura |
| Passarel·la NAT | Necessites IPs públiques de sortida predictibles | Adreça estable per a llistes d'autoritats i auditoria |
| Endpoint privat | Vols un recurs PaaS accessible privadament | Posa una IP privada per a aquest servei dins de la teva VNet, elimina l'exposició pública |
| NSG | Necessites regles de tràfic a nivell de subxarxa | Permetre/denegar explícit per al tràfic entrant i sortint per subxarxa |

## Descrivint-ho al teu AppHost

El canvi clau aquí és que estàs modelant la xarxa *juntament* amb els recursos que l'utilitzen, no en un fitxer Bicep separat que es desvia del model d'aplicació amb el temps.

Des de l'AppHost, pots:

- Crear VNets i subxarxes amb `AddVirtualNetwork()` i `AddSubnet()`
- Adjuntar una passarel·la NAT a subxarxes per a IPs de sortida estables
- Crear endpoints privats per a emmagatzematge, Key Vault, SQL i altres serveis PaaS
- Definir NSGs amb regles de seguretat d'entrada i sortida
- Configurar Perímetres de Seguretat de Xarxa per a polítiques entre recursos

El resultat és que quan executes `azd up`, la infraestructura coincideix amb el que el model d'aplicació diu que necessita. No el que diu una plantilla mantinguda manualment.

## Per Què Importa per a Aplicacions Reals

Algunes coses que es tornen significativament més fàcils un cop la xarxa es modela a Aspire:

**Endpoints privats per a Key Vault i emmagatzematge** — describes `WithPrivateEndpoint()` en aquests recursos, i Aspire gestiona la configuració de zones DNS i la connexió d'endpoints. L'aplicació mai canvia.

**IPs de sortida consistents** — afegeix una passarel·la NAT a la subxarxa rellevant i cada sol·licitud de sortida de la teva aplicació passa per una IP coneguda i estable. Els socis poden autoritzar-la. Els auditors poden rastrejar-la.

**Regles NSG des del codi** — en lloc de fer clic al portal o mantenir un fragment Bicep, les teves regles de seguretat viuen a l'AppHost juntament amb els recursos que protegeixen.

Aquest és el tipus d'integració que no fa que les demos siguin emocionants però fa que els sistemes de producció siguin mantenibles.

## Resum

La seguretat de xarxa apareixent tard en el cicle de vida del projecte és un problema resolt si la models juntament amb l'aplicació des del principi. El suport de xarxa empresarial d'Aspire fa això possible sense requerir un seguiment d'infraestructura separat.

Detalls complets a la publicació original: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
