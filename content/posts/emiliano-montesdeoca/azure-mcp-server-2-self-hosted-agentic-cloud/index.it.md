---
title: "Azure MCP Server 2.0 è Arrivato — L'Automazione Agentica Self-Hosted nel Cloud È Qui"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 è stabile con deployment remoti self-hosted, 276 tool su 57 servizi Azure, e sicurezza di livello enterprise — ecco cosa conta per gli sviluppatori .NET che costruiscono workflow agentici."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}}).*

Se hai costruito qualcosa con MCP e Azure di recente, probabilmente sai già che l'esperienza locale funziona bene. Connetti un server MCP, lascia che il tuo agente AI parli alle risorse Azure, e vai avanti. Ma nel momento in cui hai bisogno di condividere questa configurazione con un team? Ecco dove le cose si complicavano.

Non più. Azure MCP Server [ha appena raggiunto la versione 2.0 stabile](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), e la feature principale è esattamente quello che i team enterprise chiedevano: **supporto per server MCP remoti self-hosted**.

## Che cos'è Azure MCP Server?

Un rapido ripasso. Azure MCP Server implementa la specifica [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) ed espone le capacità di Azure come tool strutturati e scopribili che gli agenti AI possono invocare. Pensalo come un ponte standardizzato tra il tuo agente e Azure — provisioning, deployment, monitoring, diagnostica, tutto attraverso un'interfaccia coerente.

I numeri parlano da soli: **276 tool MCP su 57 servizi Azure**. È una copertura seria.

## Il grande affare: deployment remoti self-hosted

Ecco il punto. Eseguire MCP localmente sulla tua macchina va bene per lo sviluppo e gli esperimenti. Ma in uno scenario di team reale, hai bisogno di:

- Accesso condiviso per sviluppatori e sistemi agentici interni
- Configurazione centralizzata (contesto tenant, impostazioni di sottoscrizione predefinite, telemetria)
- Limiti di rete e policy aziendali
- Integrazione nelle pipeline CI/CD

Azure MCP Server 2.0 affronta tutto questo. Puoi deployarlo come servizio interno gestito centralmente con trasporto basato su HTTP, autenticazione adeguata e governance coerente.

Per l'autenticazione, hai due solide opzioni:

1. **Managed Identity** — quando eseguito insieme a [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **On-Behalf-Of (OBO) flow** — delegazione OpenID Connect che chiama le API Azure usando il contesto dell'utente autenticato

Quel flusso OBO è particolarmente interessante per noi sviluppatori .NET. Significa che i tuoi workflow agentici possono operare con i permessi effettivi dell'utente, non con un account di servizio sovra-privilegiato. Principio del minimo privilegio, integrato fin dall'inizio.

## Hardening della sicurezza

Non è solo un rilascio di feature — è anche uno di sicurezza. Il rilascio 2.0 aggiunge:

- Validazione endpoint più forte
- Protezioni contro i pattern di injection negli strumenti orientati alle query
- Controlli di isolamento più rigidi per gli ambienti di sviluppo

Se stai per esporre MCP come servizio condiviso, questi salvaguardi contano. Molto.

## Dove puoi usarlo?

La storia della compatibilità client è ampia. Azure MCP Server 2.0 funziona con:

- **IDE**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **Agenti CLI**: GitHub Copilot CLI, Claude Code
- **Standalone**: server locale per configurazioni semplici
- **Self-hosted remote**: la nuova stella del 2.0

Inoltre c'è il supporto per sovereign cloud per Azure US Government e Azure gestito da 21Vianet, che è critico per i deployment regolamentati.

## Perché questo conta per gli sviluppatori .NET

Se stai costruendo applicazioni agentiche con .NET — che sia Semantic Kernel, Microsoft Agent Framework, o la tua orchestrazione personalizzata — Azure MCP Server 2.0 ti dà un modo production-ready per lasciare che i tuoi agenti interagiscano con l'infrastruttura Azure. Nessun wrapper REST personalizzato. Nessun pattern di integrazione specifico per il servizio. Solo MCP.

Combinato con l'[API fluent per MCP Apps](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) uscito pochi giorni fa, l'ecosistema .NET MCP sta maturando velocemente.

## Per iniziare

Scegli il tuo percorso:

- **[GitHub Repo](https://aka.ms/azmcp)** — codice sorgente, documentazione, tutto
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — deployment containerizzato
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — integrazione IDE
- **[Self-hosting guide](https://aka.ms/azmcp/self-host)** — la feature principale del 2.0

## Per concludere

Azure MCP Server 2.0 è esattamente il tipo di upgrade infrastrutturale che non sembra vistoso in una demo ma cambia tutto nella pratica. MCP remoto self-hosted con autenticazione appropriata, hardening della sicurezza e supporto per sovereign cloud significa che MCP è pronto per team reali che costruiscono workflow agentici reali su Azure. Se stavi aspettando il segnale "enterprise-ready" — questo è.
