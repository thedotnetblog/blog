---
title: "El mode aïllat d'Aspire soluciona el malson del conflicte del port per al desenvolupament paral·lel"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introdueix el mode --isolated: ports aleatoris, secrets separats i zero col·lisions quan s'executen diverses instàncies del mateix AppHost. Perfecte per a agents d'IA, arbres de treball i fluxos de treball paral·lels."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

Si alguna vegada has provat d'executar dues instàncies del mateix projecte al mateix temps, saps el dolor. El port 8080 ja està en ús. S'ha pres el port 17370. Matar alguna cosa, reiniciar, fer malabars amb les variables d'entorn: és un assassí de la productivitat.

Aquest problema empitjora, no millora. Els agents d'IA creen arbres de treball git per treballar de manera independent. Els agents de fons generen entorns separats. Els desenvolupadors comproven el mateix repositori dues vegades per a les branques de funcions. Cadascun d'aquests escenaris toca el mateix mur: dues instàncies de la mateixa aplicació lluitant pels mateixos ports.

Aspire 13.2 soluciona això amb una sola bandera. James Newton-King de l'equip d'Aspire [va escriure tots els detalls](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), i és una d'aquestes característiques de "per què no vam tenir això abans".

## La correcció: `--isolated`

```bash
aspire run --isolated
```

Això és tot. Cada cursa obté:

- **Ports aleatoris**: no hi ha més col·lisions entre instàncies
- **Secrets d'usuari aïllats**: les cadenes de connexió i les claus API es mantenen separades per instància

No hi ha reasignació manual del port. Sense malabars amb variables d'entorn. Cada cursa obté un entorn fresc i lliure de col·lisions automàticament.

## Escenaris reals on això brilla

**Múltiples pagaments.** Tens una branca de funcions en un directori i una correcció d'errors en un altre:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Tots dos funcionen sense conflictes. El tauler mostra què s'està executant i on.

**Agents de fons a VS Code.** Quan l'agent de fons de Copilot Chat crea un arbre de treball git per treballar amb el vostre codi de manera independent, pot ser que hagi d'executar l'Aspire AppHost. Sense `--isolated`, això és una col·lisió de port amb el vostre arbre de treball principal. Amb ell, ambdues instàncies només funcionen.

L'habilitat d'Aspire que s'envia amb `aspire agent init` indica automàticament als agents que utilitzin `--isolated` quan treballen en arbres de treball. Per tant, l'agent de fons de Copilot hauria de gestionar-ho des de la caixa.

**Proves d'integració juntament amb el desenvolupament.** Necessites fer proves amb un AppHost en directe mentre continues creant funcions? El mode aïllat dóna a cada context els seus propis ports i configuració.

## Com funciona sota el capó

Quan passeu `--isolated`, la CLI genera un ID d'instància únic per a l'execució. Això provoca dos comportaments:

1. **Aleatoria de ports**: en lloc d'unir-se a ports previsibles definits a la configuració de l'AppHost, el mode aïllat tria els ports disponibles aleatòriament per a tot: el tauler de control, els punts finals del servei, tot això. El descobriment de serveis s'ajusta automàticament, de manera que els serveis es troben entre ells independentment dels ports on aterren.

2. **Aïllament secret**: cada execució aïllada obté el seu propi magatzem de secrets d'usuari, clau per l'ID de la instància. Les cadenes de connexió i les claus API d'una execució no es filtren a una altra.

El vostre codi no necessita cap canvi. El descobriment de serveis d'Aspire resol els punts finals en temps d'execució, de manera que tot es connecta correctament independentment de l'assignació del port.

## Quan utilitzar-lo

Utilitzeu `--isolated` quan executeu diverses instàncies del mateix AppHost simultàniament, tant si es tracta de desenvolupament paral·lel, proves automatitzades, agents d'IA o arbres de treball de git. Per al desenvolupament d'una sola instància on preferiu ports previsibles, `aspire run` normal encara funciona bé.

## Tancant

El mode aïllat és una petita característica que resol un problema real i cada cop més comú. A mesura que el desenvolupament assistit per IA ens empeny cap a fluxos de treball més paral·lels (múltiples agents, múltiples arbres de treball, múltiples contextos), la capacitat de fer girar una altra instància sense lluitar pels ports és essencial.

Llegiu la [publicació completa](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) per obtenir tots els detalls tècnics i proveu-ho amb `aspire update --self` per obtenir 13.2.
