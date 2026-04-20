---
title: "VS Code 1.117: Agenten Krijgen Hun Eigen Git-branches en Ik Ben Er Helemaal Voor"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 brengt worktree-isolatie voor agentsessies, persistente Autopilot-modus en subagentondersteuning. De agentische coderingworkflow is een stuk reëler geworden."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

De grens tussen "AI-assistent" en "AI-teamlid" wordt steeds dunner. VS Code 1.117 is zojuist geland en de [volledige releasenotes](https://code.visualstudio.com/updates/v1_117) zijn gevuld, maar het verhaal is duidelijk: agenten worden eerste klas burgers in je workflow.

Dit is wat er echt toe doet.

## Autopilot-modus onthoudt eindelijk je voorkeur

Eerder moest je Autopilot opnieuw inschakelen elke keer dat je een nieuwe sessie startte. Vervelend. Nu blijft je machtigingsmodus bewaard tussen sessies, en je kunt de standaard instellen.

De Agent Host ondersteunt drie sessieconfiguraties:

- **Default** — tools vragen om bevestiging voordat ze worden uitgevoerd
- **Bypass** — keurt alles automatisch goed
- **Autopilot** — volledig autonoom, beantwoordt zijn eigen vragen en gaat door

Als je een nieuw .NET-project scaffoldt met migraties, Docker en CI — stel het eén keer in op Autopilot en vergeet het. Die voorkeur blijft.

## Worktree- en git-isolatie voor agentsessies

Dit is de grote. Agentsessies ondersteunen nu volledige worktree- en git-isolatie. Dat betekent dat wanneer een agent aan een taak werkt, het zijn eigen branch en werkmap krijgt. Je hoofdbranch blijft onaangetast.

Nog beter — Copilot CLI genereert betekenisvolle branchnamen voor deze worktree-sessies. Geen `agent-session-abc123` meer. Je krijgt iets dat daadwerkelijk beschrijft wat de agent doet.

Voor .NET-ontwikkelaars die meerdere feature-branches uitvoeren of bugs oplossen terwijl een lange scaffoldingtaak loopt, is dit een game changer.

## Subagenten en agentteams

Het Agent Host Protocol ondersteunt nu subagenten. Een agent kan andere agenten starten om delen van een taak te verwerken. De hoofdagent coördineert en gespecialiseerde agenten verwerken de stukken.

## Terminaluitvoer automatisch inbegrepen wanneer agenten invoer sturen

Klein maar betekenisvol. Wanneer een agent invoer naar de terminal stuurt, wordt de terminaluitvoer nu automatisch opgenomen in de context. Als je ooit een agent `dotnet build` hebt zien uitvoeren, zien mislukken en dan nog een ronde nodig had alleen om de fout te zien — die wrijving is weg.

## Zelfupdatende Agents-app op macOS

De standalone Agents-app op macOS werkt zichzelf nu automatisch bij. Geen handmatig downloaden van nieuwe versies meer.

## De conclusie

VS Code 1.117 is infrastructuur. Worktree-isolatie, persistente machtigingen, subagentprotocollen — dit zijn de bouwstenen voor een workflow waarbij agenten echte, parallelle taken uitvoeren zonder je code aan te raken. Als je met .NET bouwt en je nog niet in de agentische workflow hebt verdiept, is dit eerlijk gezegd het moment om te beginnen.
