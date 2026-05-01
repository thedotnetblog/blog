---
title: "O Azure MCP Server Agora é um .mcpb — Instale-o sem Nenhum Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "O Azure MCP Server está disponível como MCP Bundle (.mcpb) — baixe, arraste para o Claude Desktop e pronto. Sem Node.js, Python ou .NET necessários."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Sabe o que era chato na configuração de servidores MCP? Você precisava de um runtime. Node.js para a versão npm, Python para pip/uvx, .NET SDK para a variante dotnet.

O [Azure MCP Server acabou de mudar isso](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Agora está disponível como `.mcpb` — um MCP Bundle — e a configuração é arrastar e soltar.

## O que é um MCP Bundle?

Pense como uma extensão do VS Code (`.vsix`) ou extensão de navegador (`.crx`), mas para servidores MCP. Um arquivo `.mcpb` é um arquivo ZIP independente que inclui o binário do servidor e todas as suas dependências.

## Como instalar

**1. Baixe o bundle para sua plataforma**

Vá para a [página de GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) e baixe o arquivo `.mcpb` para seu OS e arquitetura.

**2. Instale no Claude Desktop**

O mais fácil: arraste e solte o arquivo `.mcpb` na janela do Claude Desktop na página de configurações de Extensões (`☰ → Arquivo → Configurações → Extensões`). Revise os detalhes, clique em Instalar, confirme.

**3. Autentique no Azure**

```bash
az login
```

Só isso. O Azure MCP Server usa suas credenciais Azure existentes.

## O que você pode fazer

Mais de 100 ferramentas de serviços Azure diretamente do seu cliente IA:
- Consultar e gerenciar Cosmos DB, Storage, Key Vault, App Service, Foundry
- Gerar comandos `az` CLI para qualquer tarefa
- Criar templates Bicep e Terraform

## Para começar

- **Download**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Repositório**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Docs**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Veja o [post completo](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
