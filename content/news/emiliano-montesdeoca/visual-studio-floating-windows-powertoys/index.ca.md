---
title: "Aquella configuració de Windows flotant de Visual Studio que no sabíeu (però hauríeu)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Una configuració oculta de Visual Studio us ofereix un control total sobre les finestres flotants: entrades independents de la barra de tasques, un comportament adequat de diversos monitors i una perfecta integració de FancyZones. Un desplegable ho canvia tot."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

Si utilitzeu diversos monitors amb Visual Studio (i sincerament, qui no ho fa en aquests dies), probablement heu experimentat la molèstia: les finestres d'eines flotants desapareixen quan minimitzeu l'IDE principal, sempre es mantenen al capdavant de tota la resta i no apareixen com a botons separats de la barra de tasques. Funciona per a alguns fluxos de treball, però per a configuracions de diversos monitors és frustrant.

Mads Kristensen de l'equip de Visual Studio [ha compartit una configuració poc coneguda](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) que canvia completament el comportament de les finestres flotants. Un desplegable. Això és tot.

## La configuració

**Eines > Opcions > Entorn > Windows > Finestres flotants**

El menú desplegable "Aquestes finestres flotants són propietat de la finestra principal" té tres opcions:

- **Cap** — total independència. Cada finestra flotant té la seva pròpia entrada a la barra de tasques i es comporta com una finestra normal de Windows.
- **Tool Windows** (per defecte): els documents floten lliurement, les finestres d'eines es mantenen lligades a l'IDE.
- **Finestres de documents i eines**: comportament clàssic de Visual Studio, tot lligat a la finestra principal.

## Per què "Cap" és el moviment per a les configuracions de diversos monitors

Estableix-lo a **Cap** i, de sobte, totes les teves finestres i documents d'eines flotants es comporten com aplicacions de Windows reals. Apareixen a la barra de tasques, es mantenen visibles quan minimitzeu la finestra principal de Visual Studio i deixen de forçar-se al davant de tot.

Combineu-ho amb **PowerToys FancyZones** i és un canvi de joc. Creeu dissenys personalitzats als vostres monitors, col·loqueu el vostre Explorador de solucions a una zona, depureu a una altra i codifiqueu fitxers allà on vulgueu. Tot es manté, tot és accessible de manera independent i el vostre espai de treball se sent organitzat en lloc de caòtic.

## Recomanacions ràpides

- **Usuaris avançats amb monitors múltiples**: s'estableix en **Cap**, s'acobla amb FancyZones
- **Flotants ocasionals**: **Tool Windows** (per defecte) és un sòlid terme mitjà
- **Flux de treball tradicional**: **Documents i Windows Tool** manté tot el clàssic

Consell professional: **Ctrl + feu doble clic** a la barra de títol de qualsevol finestra d'eina per flotar o acoblar-la a l'instant. No cal reiniciar després de canviar la configuració.

## Tancant

És una d'aquestes configuracions "No em puc creure que no sabia sobre això". Si alguna vegada les finestres flotants a Visual Studio us han molestat, aneu a canviar-ho ara mateix.

Llegiu la [publicació completa](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) per obtenir els detalls i les captures de pantalla.
