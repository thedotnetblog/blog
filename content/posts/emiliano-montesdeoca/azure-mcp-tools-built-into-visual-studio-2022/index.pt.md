---
title: "As ferramentas Azure MCP agora vêm integradas no Visual Studio 2022 — Sem extensão necessária"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "As ferramentas Azure MCP são distribuídas como parte da carga de trabalho de desenvolvimento Azure no Visual Studio 2022. Mais de 230 ferramentas, 45 serviços Azure, zero extensões para instalar."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}}).*

Se você tem usado as ferramentas Azure MCP no Visual Studio através da extensão separada, já conhece o processo — instalar o VSIX, reiniciar, torcer para não quebrar, gerenciar incompatibilidades de versão. Essa fricção acabou.

Yun Jung Choi [anunciou](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) que as ferramentas Azure MCP agora são distribuídas diretamente como parte da carga de trabalho de desenvolvimento Azure no Visual Studio 2022. Sem extensão. Sem VSIX. Sem a dança do reiniciar.

## O que isso realmente significa

A partir do Visual Studio 2022 versão 17.14.30, o Azure MCP Server vem incluído na carga de trabalho de desenvolvimento Azure. Se você já tem essa carga de trabalho instalada, basta ativá-lo no GitHub Copilot Chat e pronto.

Mais de 230 ferramentas em 45 serviços Azure — acessíveis diretamente pela janela de chat. Liste suas contas de armazenamento, faça deploy de uma app ASP.NET Core, diagnostique problemas no App Service, consulte o Log Analytics — tudo sem abrir uma aba do navegador.

## Por que isso importa mais do que parece

A questão com ferramentas de desenvolvimento é a seguinte: cada passo extra é fricção, e fricção mata a adoção. Ter o MCP como extensão separada significava incompatibilidades de versão, falhas na instalação e mais uma coisa para manter atualizada. Integrá-lo na carga de trabalho significa:

- **Um único caminho de atualização** pelo Visual Studio Installer
- **Sem divergência de versões** entre a extensão e a IDE
- **Sempre atualizado** — o MCP Server é atualizado com os releases regulares do VS

Para equipes que padronizam no Azure, isso é muito relevante. Você instala a carga de trabalho uma vez, ativa as ferramentas, e elas estão lá para cada sessão.

## O que você pode fazer com isso

As ferramentas cobrem todo o ciclo de vida do desenvolvimento através do Copilot Chat:

- **Aprender** — pergunte sobre serviços Azure, boas práticas, padrões de arquitetura
- **Projetar e desenvolver** — obtenha recomendações de serviços, configure o código da sua aplicação
- **Fazer deploy** — provisione recursos e faça deploy diretamente pela IDE
- **Solucionar problemas** — consulte logs, verifique a saúde dos recursos, diagnostique problemas em produção

Um exemplo rápido — digite isso no Copilot Chat:

```
List my storage accounts in my current subscription.
```

O Copilot chama as ferramentas Azure MCP por trás dos panos, consulta suas assinaturas e retorna uma lista formatada com nomes, localizações e SKUs. Sem precisar do portal.

## Como ativar

1. Atualize para o Visual Studio 2022 **17.14.30** ou superior
2. Certifique-se de que a carga de trabalho **Azure development** está instalada
3. Abra o GitHub Copilot Chat
4. Clique no botão **Select tools** (o ícone das duas chaves)
5. Ative o **Azure MCP Server**

É isso. Fica ativado entre sessões.

## Um detalhe

As ferramentas vêm desativadas por padrão — você precisa ativá-las manualmente. E as ferramentas específicas do VS 2026 não estão disponíveis no VS 2022. A disponibilidade das ferramentas também depende das permissões da sua assinatura Azure, assim como no portal.

## O cenário geral

Isso faz parte de uma tendência clara: o MCP está se tornando o padrão para expor ferramentas de nuvem nas IDEs de desenvolvimento. Já vimos o [lançamento estável do Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) e integrações MCP no VS Code e em outros editores. Tê-lo integrado no sistema de cargas de trabalho do Visual Studio é a evolução natural.

Para nós desenvolvedores .NET que vivemos no Visual Studio, isso elimina mais um motivo para trocar de contexto para o portal Azure. E sinceramente, quanto menos troca de abas, melhor.
