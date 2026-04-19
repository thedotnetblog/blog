---
title: "VS Code 1.117: Os Agentes Estão Ganhando Suas Próprias Branches Git e Eu Tô Adorando"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 traz isolamento com worktree para sessões de agentes, modo Autopilot persistente e suporte a subagentes. O fluxo de trabalho com agentes de código ficou muito mais real."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

A linha entre "assistente de IA" e "colega de equipe de IA" continua ficando mais fina. O VS Code 1.117 acabou de sair e as [notas de versão completas](https://code.visualstudio.com/updates/v1_117) estão recheadas, mas a história é clara: os agentes estão se tornando cidadãos de primeira classe no seu fluxo de trabalho de desenvolvimento.

Aqui está o que realmente importa.

## O modo Autopilot finalmente lembra sua preferência

Antes, você tinha que reativar o Autopilot toda vez que iniciava uma nova sessão. Irritante. Agora seu modo de permissão persiste entre sessões, e você pode configurar o padrão.

O Agent Host suporta três configurações de sessão:

- **Default** — as ferramentas pedem confirmação antes de executar
- **Bypass** — aprova tudo automaticamente
- **Autopilot** — totalmente autônomo, responde suas próprias perguntas e segue em frente

Se você está montando um novo projeto .NET com migrations, Docker e CI — configure para Autopilot uma vez e esqueça. Essa preferência fica salva.

## Worktree e isolamento git para sessões de agentes

Essa é a grande novidade. Sessões de agentes agora suportam isolamento completo com worktree e git. Isso significa que quando um agente trabalha em uma tarefa, ele ganha sua própria branch e diretório de trabalho. Sua branch principal fica intocada.

Melhor ainda — o Copilot CLI gera nomes de branch significativos para essas sessões de worktree. Chega de `agent-session-abc123`. Você recebe algo que realmente descreve o que o agente está fazendo.

Para desenvolvedores .NET que gerenciam múltiplas branches de features ou corrigem bugs enquanto uma tarefa longa de scaffolding roda, isso é um divisor de águas. Você pode ter um agente construindo seus controllers de API em um worktree enquanto você depura um problema na camada de serviços em outro. Sem conflitos. Sem stashing. Sem bagunça.

## Subagentes e equipes de agentes

O Agent Host Protocol agora suporta subagentes. Um agente pode criar outros agentes para lidar com partes de uma tarefa. Pense nisso como delegar — seu agente principal coordena, e agentes especializados cuidam das partes.

Isso é cedo, mas o potencial para fluxos de trabalho .NET é óbvio. Imagine um agente cuidando das suas migrations do EF Core enquanto outro configura seus testes de integração. Ainda não chegamos totalmente lá, mas o suporte ao protocolo chegando agora significa que as ferramentas virão rápido.

## Saída do terminal incluída automaticamente quando agentes enviam input

Pequeno mas significativo. Quando um agente envia input para o terminal, a saída do terminal agora é automaticamente incluída no contexto. Antes, o agente precisava de um turno extra só para ler o que aconteceu.

Se você já viu um agente executar `dotnet build`, falhar, e depois precisar de mais uma ida e volta só para ver o erro — essa fricção acabou. Ele vê a saída imediatamente e reage.

## O app Agents no macOS se atualiza sozinho

O app independente Agents no macOS agora se atualiza sozinho. Chega de baixar novas versões manualmente. Ele simplesmente se mantém atualizado.

## As coisas menores que vale a pena saber

- Os **hovers do package.json** agora mostram tanto a versão instalada quanto a última disponível. Útil se você gerencia ferramentas npm junto com seus projetos .NET.
- **Imagens em comentários JSDoc** são renderizadas corretamente em hovers e completions.
- **Sessões do Copilot CLI** agora indicam se foram criadas pelo VS Code ou externamente — prático quando você está pulando entre terminais.
- **Copilot CLI, Claude Code e Gemini CLI** são reconhecidos como tipos de shell. O editor sabe o que você está executando.

## A conclusão

VS Code 1.117 não é um despejo de features chamativas. É infraestrutura. Isolamento com worktree, permissões persistentes, protocolos de subagentes — esses são os blocos de construção para um fluxo de trabalho onde agentes lidam com tarefas reais e paralelas sem pisar no seu código.

Se você está construindo com .NET e ainda não mergulhou no fluxo de trabalho com agentes, honestamente, agora é a hora de começar.
