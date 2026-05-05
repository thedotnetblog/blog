---
title: "azd agora permite executar e depurar agentes IA localmente — O que mudou em março 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "O Azure Developer CLI lançou sete versões em março 2026. Destaques: loop local de execução e depuração para agentes IA, integração com GitHub Copilot na configuração de projetos, e suporte a Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}}).*

Sete versões em um mês. Foi isso que o time do Azure Developer CLI (`azd`) publicou em março 2026, e a funcionalidade principal é a que eu estava esperando: **um loop local de execução e depuração para agentes IA**.

PC Chan [publicou o resumo completo](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), e embora haja muito conteúdo, deixe-me filtrar o que realmente importa para desenvolvedores .NET construindo apps com IA.

## Executar e depurar agentes IA sem fazer deploy

Esta é a grande novidade. A nova extensão `azure.ai.agents` adiciona comandos que te dão uma experiência de loop interno adequada para agentes IA:

- `azd ai agent run` — inicia seu agente localmente
- `azd ai agent invoke` — envia mensagens (local ou em produção)
- `azd ai agent show` — mostra status e saúde do container
- `azd ai agent monitor` — transmite logs do container em tempo real

Antes, testar um agente IA significava fazer deploy no Microsoft Foundry toda vez que você fazia uma mudança. Agora você pode iterar localmente, testar o comportamento do seu agente, e só fazer deploy quando estiver pronto.

## GitHub Copilot configura seu projeto azd

`azd init` agora oferece uma opção "Set up with GitHub Copilot (Preview)". Em vez de responder prompts manualmente, um agente Copilot gera a configuração para você. Quando um comando falha, `azd` oferece troubleshooting assistido por IA — tudo sem sair do terminal.

## Container App Jobs e melhorias de deploy

- **Container App Jobs**: `azd` agora faz deploy de `Microsoft.App/jobs` pela config existente `host: containerapp`.
- **Timeouts configuráveis**: Nova flag `--timeout` no `azd deploy` e campo `deployTimeout` no `azure.yaml`.
- **Fallback de build remoto**: Quando o build ACR falha, `azd` faz fallback automático para Docker/Podman local.
- **Validação preflight local**: Parâmetros Bicep são validados localmente antes do deploy.

## Melhorias de DX

- **Detecção automática de pnpm/yarn** para projetos JS/TS
- **Suporte a pyproject.toml** para Python
- **Diretórios de templates locais** — `azd init --template` aceita caminhos do sistema de arquivos
- **Melhores mensagens de erro** no modo `--no-prompt`
- **Variáveis de ambiente de build** injetadas em todos os subprocessos de build (.NET, Node.js, Java, Python)

## Conclusão

O loop de depuração local de agentes IA é a estrela desta versão, mas o acúmulo de melhorias de deploy e refinamento de DX faz o `azd` parecer mais maduro do que nunca. Se você está fazendo deploy de apps .NET no Azure — especialmente agentes IA — esta atualização vale a pena.

Confira as [notas completas da versão](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) para todos os detalhes.
