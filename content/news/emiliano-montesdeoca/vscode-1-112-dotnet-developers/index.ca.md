---
title: "VS Code 1.112: Què haurien de preocupar-se realment als desenvolupadors de.NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 acaba de caure i està ple d'actualitzacions d'agents, un depurador de navegador integrat, MCP sandboxing i suport monorepo. Això és el que realment importa si esteu creant amb.NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 acaba d'aterrar, i sincerament? Aquest és diferent si passeu els vostres dies a la terra.NET. Hi ha moltes coses a les [notes oficials de la versió](https://code.visualstudio.com/updates/v1_112), però permeteu-me que us estalviï una mica de desplaçament i que em concentri en allò que realment ens importa.

## Copilot CLI acaba de ser molt més útil

El gran tema d'aquest llançament és **autonomia de l'agent**, donant més espai a Copilot per fer les seves coses sense que facis de cangur a cada pas.

### Direcció i cua de missatges

Coneixes aquell moment en què Copilot CLI està a mig camí d'una tasca i t'adones que t'has oblidat d'esmentar alguna cosa? Abans, calia esperar. Ara només podeu enviar missatges mentre una sol·licitud encara s'està executant, ja sigui per dirigir la resposta actual o posar en cua les instruccions de seguiment.

Això és enorme per a aquelles tasques més llargues de bastida `dotnet` en què esteu veient Copilot configura un projecte i penseu "oh, espera, també necessito MassTransit".

### Nivells de permís

Aquest és el que m'emociona més. Les sessions de Copilot CLI ara admeten tres nivells de permís:

- **Permisos predeterminats**: el flux habitual on les eines demanen confirmació abans d'executar-se
- **Evita les aprovacions**: s'aprova tot automàticament i torna a provar els errors
- **Pilot automàtic**: és totalment autònom: aprova les eines, respon a les seves pròpies preguntes i continua fins que es fa la tasca

Si esteu fent alguna cosa com la bastida d'una nova API ASP.NET Core amb Entity Framework, migracions i una configuració de Docker, el mode Autopilot significa que descriu el que voleu i aneu a prendre un cafè. Ho descobrirà.

Podeu habilitar el pilot automàtic amb la configuració `chat.autopilot.enabled`.

### Previsualitza els canvis abans de la delegació

Quan delegueu una tasca a Copilot CLI, es crea un arbre de treball. Abans, si teníeu canvis no compromesos, havíeu de comprovar el control de fonts per veure què es veuria afectat. Ara, la vista de xat mostra els canvis pendents abans de decidir si els voleu copiar, moure o ignorar-los.

Poca cosa, però us salva d'aquell "espera, què he posat en escena?" moment.

## Depura les aplicacions web sense sortir de VS Code

El navegador integrat ara admet **depuració completa**. Podeu establir punts d'interrupció, passar pel codi i inspeccionar variables, tot dins de VS Code. No més canviar a Edge DevTools.

Hi ha un nou tipus de depuració `editor-browser` i si ja teniu configuracions de llançament de `msedge` o `chrome`, la migració és tan senzilla com canviar el camp `type` al vostre `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Per als desenvolupadors de Blazor, això és un canvi de joc. Ja esteu executant `dotnet watch` al terminal; ara la vostra depuració també es manté a la mateixa finestra.

El navegador també va obtenir nivells de zoom independents (finalment), menús contextuals adequats del clic dret i el zoom es recorda per lloc web.

## Sandboxing del servidor MCP

Aquest és més important del que podríeu pensar. Si utilitzeu servidors MCP (potser n'heu configurat un de personalitzat per als vostres recursos d'Azure o consultes de base de dades), s'han executat amb els mateixos permisos que el vostre procés de VS Code. Això significa un accés complet al vostre sistema de fitxers, xarxa, tot.

Ara els podeu sorrar. Al teu `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Quan un servidor amb caixa de sorra necessita accés a alguna cosa que no té, VS Code us demana que atorgueu permís. Molt millor que l'enfocament "Espero que ningú faci res estrany".

> **Nota:** Sandboxing està disponible per ara a macOS i Linux. Arriba el suport de Windows, però escenaris remots com WSL funcionen.

## Descobriment de personalitzacions de Monorepo

Si esteu treballant en un monorepo (i siguem sincers, moltes solucions empresarials.NET acaben com una), això resol un veritable problema.

Anteriorment, si obríeu una subcarpeta del vostre repositori, VS Code no trobaria les vostres habilitats `copilot-instructions.md`, `AGENTS.md` o personalitzades a l'arrel del dipòsit. Ara, amb la configuració `chat.useCustomizationsInParentRepositories`, puja a l'arrel `.git` i ho descobreix tot.

Això significa que el vostre equip pot compartir instruccions de l'agent, fitxers de sol·licitud i eines personalitzades en tots els projectes en un monorepo sense que tothom hagi d'obrir la carpeta arrel.

## /resolució de problemes per a la depuració de l'agent

Alguna vegada has configurat instruccions o habilitats personalitzades i t'has preguntat per què no les recullen? La nova habilitat `/troubleshoot` llegeix els registres de depuració de l'agent i us diu què va passar: quines eines s'han utilitzat o s'han omès, per què les instruccions no s'han carregat i què està causant respostes lentes.

Activa-ho amb:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

A continuació, només cal escriure `/troubleshoot why is my custom skill not loading?` al xat.

També podeu exportar i importar aquests registres de depuració ara, la qual cosa és ideal per compartir amb el vostre equip quan alguna cosa no funciona com s'esperava.

## Compatibilitat amb imatges i fitxers binaris

Els agents ara poden llegir fitxers d'imatge del disc i fitxers binaris de manera nativa. Els fitxers binaris es presenten en format hexdump i les sortides d'imatge (com les captures de pantalla del navegador integrat) es mostren en una vista de carrusel.

Per als desenvolupadors de.NET, penseu: enganxeu una captura de pantalla d'un error de la interfície d'usuari al xat i feu que l'agent entengui què passa, o feu que analitzi la sortida d'una representació de component Blazor.

## Referències de símbols automàtiques

Petita millora de la qualitat de vida: quan copieu un nom de símbol (una classe, un mètode, etc.) i l'enganxeu al xat, ara VS Code el converteix automàticament en una referència `#sym:Name`. Això proporciona a l'agent un context complet sobre aquest símbol sense que hàgiu d'afegir-lo manualment.

Si voleu text sense format, feu servir `Ctrl+Shift+V`.

## Els connectors ara es poden activar/desactivar

Abans, desactivar un servidor o connector MCP significava desinstal·lar-lo. Ara podeu activar-los i desactivar-los, tant a nivell global com per espai de treball. Feu clic amb el botó dret a la vista Extensions o a la vista Personalitzacions i ja heu acabat.

Els connectors de npm i pypi també es poden actualitzar automàticament ara, tot i que primer demanaran l'aprovació, ja que les actualitzacions signifiquen executar codi nou a la vostra màquina.

## Tancant

VS Code 1.112 està clarament empenyent l'experiència de l'agent: més autonomia, millor depuració, seguretat més estricta. Per als desenvolupadors de.NET, la depuració integrada del navegador i les millores de Copilot CLI són les característiques més destacades.

Si encara no heu provat d'executar una sessió CLI Copilot completa en mode Autopilot per a un projecte.NET, aquesta versió és un bon moment per començar. Només recordeu establir els vostres permisos i deixar-ho cuinar.

[Descarregueu VS Code 1.112](https://code.visualstudio.com/updates/v1_112) o actualitzeu-ho des de VS Code mitjançant **Ajuda > Comproveu actualitzacions**.
