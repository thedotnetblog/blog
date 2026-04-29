---
title: "Actualització d'abril de Azure DevOps MCP Server: consultes WIQL, autenticació PAT i MCP Apps experimentals"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server incorpora consultes de work items impulsades per WIQL, autenticació amb Personal Access Token, anotacions MCP i una funció experimental de MCP Apps que empaqueta fluxos de treball habituals en eines reutilitzables."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Azure DevOps MCP Server continua millorant. L'actualització d'abril de Dan Hellem cobreix tant el servidor local com el remot, i hi ha algunes incorporacions realment útils aquí — sobretot si has fet servir Copilot per navegar per taulers i repositoris.

## Suport per a consultes WIQL

La novetat principal: una eina nova `wit_query_by_wiql` que et permet executar consultes Work Item Query Language directament des del client MCP.

Si has fet servir Azure Boards durant una temporada, coneixes WIQL. És la sintaxi de consulta semblant a SQL per a work items: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Tenir-la disponible com a eina MCP vol dir que les teves sessions de Copilot poden obtenir conjunts precisos de work items sense filtrar manualment ni navegar per les vistes del tauler.

Un advertiment: al servidor MCP remot, aquesta eina ara mateix requereix la bandera de funció **Insiders** mentre validen el rendiment de les consultes a escala. Arribarà a tothom quan les dades de telemetria siguin bones.

## Tokens d'accés personal al servidor local

El servidor MCP local ara admet autenticació PAT. Sona com una millora menor, però és important per a escenaris d'integració — especialment quan executes el servidor MCP en un context on no hi ha autenticació interactiva disponible, o quan et connectes des de clients externs i automatització.

Les passes de configuració es documenten a la [guia d'inici](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat).

## Anotacions MCP al servidor remot

Les anotacions són metadades als tools MCP que indiquen als models de llenguatge com utilitzar-los amb seguretat. Azure DevOps MCP Server ara implementa anotacions per a:

- **Eines de només lectura** — el model sap que són segures d'invocar sense confirmació de l'usuari
- **Eines destructives** — el model sap que ha de ser prudent i confirmar abans de continuar
- **Eines de món obert** — el model entén que poden retornar resultats imprevisibles

Això és fonamental per a la fiabilitat dels agents. Sense anotacions, el model ha d'endevinar pel nom de l'eina si és segur invocar-la. Amb anotacions, el comportament és explícit i l'agent pot prendre millors decisions.

## Consolidació d'eines Wiki

El servidor remot comença a consolidar eines relacionades en menys eines però més potents. Les eines wiki són les primeres a rebre aquest tractament:

| Nova eina | Substitueix |
|----------|----------|
| `wiki` (només lectura) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Menys eines = millor rendiment del model. És un patró constant en el disseny de servidors MCP — conjunts d'eines més petits i més enfocats funcionen millor perquè el model no ha de decidir entre cinc eines gairebé idèntiques.

## Experimental: MCP Apps

Aquest és l'afegit més interessant, i és clarament experimental. MCP Apps són fluxos de treball empaquetats que s'executen dins de l'entorn del servidor MCP:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "mcp-server-azuredevops",
      "args": ["contoso", "-d", "core", "work", "work-items", "mcp-apps"]
    }
  }
}
```

El primer exemple és `mcp_app_my_work_item` — una experiència de work item autònoma que et permet veure, filtrar i editar work items assignats a tu, sense haver d'encadenar manualment múltiples crides d'eines.

La idea és convincent: en lloc que el teu agent cridi `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` al llarg de diverses interaccions, una sola MCP App proporciona tot el flux de treball com una unitat estructurada i reutilitzable. Menys temps de configuració, comportament coherent i menys peces soltes.

## Tancant

Azure DevOps MCP Server madura ràpidament. El suport WIQL i l'autenticació PAT són guanys immediats per a qualsevol persona que faci servir Copilot amb Azure Boards. La feina d'anotacions fa que el servidor remot sigui més segur per a casos d'ús agentius. I MCP Apps, tot i ser experimentals, apunten cap on va això: d'eines en brut a fluxos de treball compostables.

Val la pena fer un cop d'ull a la [documentació](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) mentre el servidor remot continua evolucionant.

Publicació original de Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).