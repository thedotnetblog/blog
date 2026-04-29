---
title: "Aprilupdate van Azure DevOps MCP Server: WIQL-query's, PAT-authenticatie en experimentele MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Server krijgt WIQL-aangedreven work item-query's, Personal Access Token-authenticatie, MCP-annotaties en een experimentele MCP Apps-functie die veelvoorkomende workflows verpakt in herbruikbare tools."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "index.md" >}}).*

Azure DevOps MCP Server wordt steeds beter. De update van april van Dan Hellem behandelt zowel de lokale als de remote server, en er zitten een paar echt nuttige toevoegingen in — vooral als je Copilot gebruikt om door borden en repositories te navigeren.

## Ondersteuning voor WIQL-query's

De belangrijkste nieuwe functie: een nieuwe `wit_query_by_wiql` tool waarmee je Work Item Query Language-query's rechtstreeks vanuit je MCP-client kunt uitvoeren.

Als je Azure Boards al een tijdje gebruikt, ken je WIQL. Het is de SQL-achtige querysyntaxis voor work items: `SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.AssignedTo] = @Me AND [System.State] = 'Active'`. Dat beschikbaar hebben als MCP-tool betekent dat je Copilot-sessies nu nauwkeurige sets work items kunnen ophalen zonder handmatig te filteren of door board-weergaven te klikken.

Eén kanttekening: op de remote MCP Server vereist deze tool momenteel de **Insiders**-featureflag terwijl ze de queryprestaties op schaal valideren. Hij komt voor iedereen beschikbaar zodra de telemetrie er goed uitziet.

## Persoonlijke toegangstokens op de lokale server

De lokale MCP Server ondersteunt nu PAT-authenticatie. Dat klinkt misschien als een kleine verbetering, maar het is belangrijk voor integratiescenario's — vooral wanneer je de MCP-server in een context draait waarin geen interactieve authenticatie beschikbaar is, of wanneer je verbinding maakt vanaf externe clients en automatisering.

De configuratiestappen staan beschreven in de [Getting Started-guide](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md#-personal-access-token-pat).

## MCP-annotaties op de remote server

Annotaties zijn metadata-tags op MCP-tools die LLM's vertellen hoe ze deze veilig moeten gebruiken. De Azure DevOps MCP Server implementeert nu annotaties voor:

- **Alleen-lezen tools** — het model weet dat deze veilig zijn om aan te roepen zonder bevestiging van de gebruiker
- **Destructieve tools** — het model weet dat het voorzichtig moet zijn en eerst moet bevestigen voordat het doorgaat
- **Open-world tools** — het model begrijpt dat deze onvoorspelbare resultaten kunnen teruggeven

Dit is fundamenteel voor de betrouwbaarheid van agents. Zonder annotaties moet het model op basis van de toolnaam gokken of het veilig is om deze aan te roepen. Met annotaties is het gedrag expliciet en kan de agent betere beslissingen nemen.

## Consolidatie van wiki-tools

De remote server begint gerelateerde tools te consolideren tot minder, maar krachtigere tools. De wiki-tools zijn de eerste die deze behandeling krijgen:

| Nieuwe tool | Vervangt |
|----------|----------|
| `wiki` (alleen lezen) | `wiki_get_page`, `wiki_get_page_content`, `wiki_list_pages`, `wiki_list_wikis`, `wiki_get_wiki` |
| `wiki_upsert_page` | `wiki_create_or_update_page` |

Minder tools = betere modelprestaties. Dit is een vast patroon in MCP-serverontwerp — kleinere, meer gerichte toolsets werken beter omdat het model niet hoeft te kiezen tussen vijf vrijwel identieke tools.

## Experimenteel: MCP Apps

Dit is de interessantste toevoeging, en het is duidelijk experimenteel. MCP Apps zijn verpakte workflows die draaien binnen de MCP-serveromgeving:

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

Het eerste voorbeeld is `mcp_app_my_work_item` — een zelfstandige work item-ervaring waarmee je aan jou toegewezen work items kunt bekijken, filteren en bewerken, zonder handmatig meerdere toolcalls te hoeven koppelen.

Het idee is overtuigend: in plaats van dat je agent `wit_get_work_item` → `wit_list_work_items` → `wit_update_work_item` over meerdere beurten aanroept, biedt één MCP App de volledige workflow als één gestructureerde, herbruikbare eenheid. Minder insteltijd, consistent gedrag en minder losse onderdelen.

## Afronding

Azure DevOps MCP Server wordt snel volwassener. WIQL-ondersteuning en PAT-authenticatie zijn directe winst voor iedereen die Copilot met Azure Boards gebruikt. Het annotatiewerk maakt de remote server veiliger voor agentische use cases. En MCP Apps, hoewel experimenteel, laten zien waar dit naartoe gaat: van ruwe tools naar composeerbare workflows.

Het is de moeite waard om de [documentatie](https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server) in de gaten te houden terwijl de remote server verder evolueert.

Oorspronkelijk bericht van Dan Hellem: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).