---
title: "Windows App Development CLI és cada cop més útil per al treball real de paquetització"
date: 2026-06-19
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3.2 afegeix suport per a paquets MSIX, una inicialització més intel·ligent i un comportament d'automatització millor. Per a equips .NET centrats en Windows, això el fa més pràctic dins d'un flux real de paquetització."
tags:
  - Windows
  - .NET
  - WinUI
  - WPF
  - Developer Tools
---

> *Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "windows-app-development-cli-v032-msix-bundles.md" >}}).* 

M'agraden les actualitzacions d'eines que eliminen passos molestos que ningú no gaudeix fent manualment.

Bàsicament, aquesta és la història de **Windows App Development CLI v0.3.2**.

Aquesta versió afegeix millor empaquetament, una inicialització més intel·ligent, un suport de captura de pantalla més net i un comportament més fiable en mode no interactiu. Res d'això sona espectacular per separat, però plegat fa que el CLI sigui més creïble per als equips que fan treball real de paquetització i lliurament d'apps Windows.

## El suport per a paquets MSIX és el titular per un motiu

L'addició més forta aquí és el **suport per a paquets MSIX**.

Si publiques apps Windows per a diverses arquitectures, tenir un camí més simple cap a un `.msixbundle` correcte importa molt. La història de Microsoft Store, el flux de paquetització i el lliurament multiarquitectura es tornen molt menys incòmodes quan el CLI pot gestionar més d'aquest flux directament.

Això és el tipus de funció que fa passar una eina de "previsualització interessant" a "potser de veritat me la quedo a la cadena d'eines".

## `winapp init` més intel·ligent també és més important del que sembla

Les millores a `winapp init` són d'aquelles que la gent subestima fins que sent el dolor exactament ella mateixa.

Detectar automàticament projectes compatibles, gestionar amb més netedat diversos tipus de projectes i funcionar millor en shells no interactives fan que el CLI sigui molt més realista per a configuracions basades en scripts i CI.

Això importa per a equips seriosos.

## Per què això és rellevant per als desenvolupadors de .NET

Val especialment la pena seguir-ho si formes part de la banda de .NET que encara es preocupa molt per:

- WPF
- WinUI
- paquetització d'escriptori
- enviaments a la Store
- distribució nativa a Windows

Aquests àmbits no sempre reben el mateix soroll que les eines de cloud o d'IA, però continuen sent molt importants per als productes reals.

## La meva opinió

Windows App Development CLI encara és jove, però els llançaments com aquest són els que fan que les eines es guanyin la confiança.

Una millor paquetització, un millor comportament d'inicialització i un millor suport d'automatització són exactament el tipus de millores que fan que una eina de previsualització comenci a sentir-se realment útil.

Publicació original: [Windows App Development CLI v0.3.2 — suport de paquetització, inicialització més intel·ligent i més coses](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-2-bundling-support-smarter-initialization-and-more/)