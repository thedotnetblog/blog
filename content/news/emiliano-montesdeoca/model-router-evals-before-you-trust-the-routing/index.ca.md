---
title: "Les avaluacions del model router són el pas que massa equips es salten"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "El nou repositori d'avaluació del model router de Foundry és important perquè les decisions d'encaminament s'han de mesurar contra la qualitat, la latència i el cost abans que els equips tractin la selecció automàtica de models com si fos màgia."
tags:
  - Microsoft Foundry
  - AI
  - Evaluations
  - Model Router
  - Cost Optimization
---

> *Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "index.md" >}}).*

L'encaminament automàtic de models sembla fantàstic fins que t'adones que encara has de demostrar que és la millor opció per a la teva càrrega de treball.

Per això és útil el nou **repositori d'avaluació del model router**.

Ofereix als equips una manera més concreta de respondre a les preguntes que realment importen:

- l'encaminament preserva la qualitat?
- millora el cost?
- què fa amb la latència?
- què canvia si restrinyo el subconjunt de models?

## L'article original fa les preguntes correctes

Una de les coses que més m'agrada del post original és que no tracta el model router com si fos bo per defecte.

En lloc d'això, fa les preguntes incòmodes però correctes:

- "**Als meus prompts, el model seleccionat automàticament pel model router iguala o supera el model únic que jo triaria?**"
- "**Estic realment estalviant diners de punta a punta, o només estic movent la despesa d'un lloc a un altre?**"

Aquesta és exactament l'actitud correcta.

Perquè l'encaminament automàtic és atractiu, però continua sent una decisió de sistema. I les decisions de sistema s'han de mesurar, no pas admirar.

## Per què aquest repositori importa més del que sembla al principi

En un nivell, això és només un repositori d'avaluació.

En un altre, és un senyal de maduresa.

Diu: si vols adoptar l'encaminament automàtic, aquí tens una manera més disciplinada de provar:

- qualitat
- cost
- latència
- compensacions del subconjunt
- comportament de distribució de models

Això és molt millor que tractar l'encaminament com una caixa negra amb un bon màrqueting.

## La meva opinió

Aquest és un bon exemple del tipus d'eines que necessiten més les plataformes d'IA: no més màgia, sinó més maneres de validar la màgia abans de confiar-hi.

Així és com els equips eviten construir una confiança cara sobre supòsits no provats.

Article original: [How to run evals for the model router](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)
