---
title: "L'Azure MCP Server 2.0 s'acaba de caure: l'automatització del núvol agent autoallotjada és aquí"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 es manté estable amb desplegaments remots autoallotjats, 276 eines en 57 serveis Azure i seguretat de nivell empresarial: això és el que importa per als desenvolupadors de.NET que creen fluxos de treball agents."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

Si darrerament heu estat creant alguna cosa amb MCP i Azure, probablement ja sabeu que l'experiència local funciona bé. Connecteu un servidor MCP, deixeu que el vostre agent d'IA parli amb els recursos d'Azure, seguiu endavant. Però, en el moment que necessiteu compartir aquesta configuració amb un equip? Allà va ser on les coses es van complicar.

Ja no. Servidor MCP d'Azure [acaba d'aconseguir 2.0 estable](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), i la funció de titular és exactament el que els equips empresarials han demanat: **suport del servidor MCP remot autoallotjat**.

## Què és Azure MCP Server?

Actualització ràpida. Azure MCP Server implementa l'especificació [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) i exposa les capacitats d'Azure com a eines estructurades i detectables que els agents d'IA poden invocar. Penseu en això com un pont estandarditzat entre el vostre agent i Azure: subministrament, desplegament, supervisió, diagnòstic, tot mitjançant una interfície coherent.

Les xifres parlen per si soles: **276 eines MCP en 57 serveis Azure**. Això és una cobertura seriosa.

## El gran problema: desplegaments remots autoallotjats

Aquí està la cosa. Executar MCP localment a la vostra màquina està bé per a desenvolupament i experiments. Però en un escenari d'equip real, necessiteu:

- Accés compartit per a desenvolupadors i sistemes d'agents interns
- Configuració centralitzada (context de l'arrendatari, valors predeterminats de subscripció, telemetria)
- Xarxa empresarial i límits polítics
- Integració en pipelines CI/CD

Azure MCP Server 2.0 aborda tot això. Podeu implementar-lo com a servei intern gestionat de manera centralitzada amb transport basat en HTTP, autenticació adequada i govern coherent.

Per a l'autenticació, obteniu dues opcions sòlides:

1. **Identitat gestionada**: quan s'executa al costat de [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **Flux en nom de (OBO)**: delegació d'OpenID Connect que crida a les API d'Azure mitjançant el context de l'usuari iniciat

Aquest flux OBO és especialment interessant per als desenvolupadors de.NET. Vol dir que els vostres fluxos de treball d'agent poden funcionar amb els permisos reals de l'usuari, no amb un compte de servei amb privilegis excessius. Principi del mínim privilegi, integrat.

## Enduriment de la seguretat

Això no és només una versió de funcions, també és una de seguretat. La versió 2.0 afegeix:

- Validació de punt final més forta
- Proteccions contra patrons d'injecció en eines orientades a la consulta
- Controls d'aïllament més estrictes per a entorns de desenvolupament

Si voleu exposar MCP com a servei compartit, aquestes garanties són importants. Molts.

## On el pots utilitzar?

La història de la compatibilitat del client és àmplia. Azure MCP Server 2.0 funciona amb:

- **IDEs**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **Agents CLI**: GitHub Copilot CLI, Claude Code
- **Autònom**: servidor local per a configuracions senzilles
- **Control remot autoallotjat**: la nova estrella de la 2.0

A més, hi ha suport sobirà al núvol per al govern d'Azure dels Estats Units i Azure operat per 21Vianet, que és fonamental per als desplegaments regulats.

## Per què això és important per als desenvolupadors de.NET

Si esteu creant aplicacions agents amb.NET, ja sigui el nucli semàntic, el Microsoft Agent Framework o la vostra pròpia orquestració, Azure MCP Server 2.0 us ofereix una manera preparada per a la producció de permetre que els vostres agents interactuïn amb la infraestructura Azure. No hi ha embolcalls REST personalitzats. No hi ha patrons d'integració específics del servei. Només MCP.

Combinat amb l'[API fluida per a aplicacions MCP](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) que va caure fa uns dies, l'ecosistema.NET MCP està madurant ràpidament.

## Primers passos

Tria el teu camí:

- **[GitHub Repo](https://aka.ms/azmcp)** — codi font, documents, tot
- **[Imatge Docker](https://aka.ms/azmcp/download/docker)** — desplegament en contenidors
- **[Extensió de codi VS](https://aka.ms/azmcp/download/vscode)** — Integració IDE
- **[Guia d'allotjament personal](https://aka.ms/azmcp/self-host)**: la funció insígnia 2.0

## Tancant

Azure MCP Server 2.0 és exactament el tipus d'actualització d'infraestructura que no sembla cridaner en una demostració, però que ho canvia tot a la pràctica. MCP remot autoallotjat amb autenticació adequada, reforç de la seguretat i suport sobirà del núvol significa que MCP està preparat per a equips reals que creen fluxos de treball reals a l'Azure. Si heu estat esperant el senyal "preparat per a l'empresa", això és tot.
