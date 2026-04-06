---
title: "VS Code 1.115 — Notificações de Terminal em Segundo Plano, Modo Agente SSH e Mais"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 traz notificações de terminal em segundo plano para agentes, hospedagem remota de agentes via SSH, colagem de arquivos em terminais e rastreamento de edições com reconhecimento de sessão. Veja o que importa para desenvolvedores .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "vscode-1-115-agent-improvements.md" >}}).*

VS Code 1.115 acabou de [ser lançado](https://code.visualstudio.com/updates/v1_115), e embora seja uma versão mais leve em termos de funcionalidades principais, as melhorias relacionadas a agentes são genuinamente úteis se você trabalha com assistentes de código com IA diariamente.

Deixa eu destacar o que realmente vale a pena saber.

## Terminais em segundo plano se comunicam com agentes

Essa é a funcionalidade destaque. Terminais em segundo plano agora notificam automaticamente os agentes quando comandos são concluídos, incluindo o código de saída e a saída do terminal. Prompts de entrada em terminais em segundo plano também são detectados e exibidos ao usuário.

Por que isso importa? Se você usou o modo agente do Copilot para executar comandos de build ou suítes de testes em segundo plano, você conhece a dor do "será que já terminou?" — terminais em segundo plano eram essencialmente disparar-e-esquecer. Agora o agente é notificado quando seu `dotnet build` ou `dotnet test` termina, vê a saída e pode reagir de acordo. É uma mudança pequena que torna os fluxos de trabalho orientados por agentes significativamente mais confiáveis.

Há também uma nova ferramenta `send_to_terminal` que permite aos agentes enviar comandos para terminais em segundo plano com confirmação do usuário, corrigindo o problema onde `run_in_terminal` com um timeout movia terminais para segundo plano e os deixava somente leitura.

## Hospedagem remota de agentes via SSH

VS Code agora suporta conexão a máquinas remotas via SSH, instalando automaticamente o CLI e iniciando-o em modo host de agentes. Isso significa que suas sessões de agentes de IA podem mirar ambientes remotos diretamente — útil para desenvolvedores .NET que compilam e testam em servidores Linux ou VMs na nuvem.

## Rastreamento de edições em sessões de agentes

Edições de arquivos feitas durante sessões de agentes agora são rastreadas e restauradas, com diffs, desfazer/refazer e restauração de estado. Se um agente faz alterações no seu código e algo dá errado, você pode ver exatamente o que mudou e reverter. Tranquilidade para deixar agentes modificarem sua codebase.

## Reconhecimento de abas do navegador e outras melhorias

Mais algumas adições de qualidade de vida:

- **Rastreamento de abas do navegador** — o chat agora pode rastrear e linkar abas do navegador abertas durante uma sessão, para que agentes possam referenciar páginas web que você está visualizando
- **Colagem de arquivos no terminal** — cole arquivos (incluindo imagens) no terminal com Ctrl+V, arrastar e soltar, ou clique direito
- **Cobertura de testes no minimap** — indicadores de cobertura de testes agora aparecem no minimap para uma visão visual rápida
- **Pinch-to-zoom no Mac** — o navegador integrado suporta gestos de pinch-to-zoom
- **Direitos do Copilot em Sessões** — a barra de status mostra informações de uso na visualização de Sessões
- **Favicon em Ir para Arquivo** — páginas web abertas mostram favicons na lista de seleção rápida

## Conclusão

VS Code 1.115 é uma versão incremental, mas as melhorias de agentes — notificações de terminal em segundo plano, hospedagem de agentes SSH e rastreamento de edições — somam-se a uma experiência notavelmente mais fluida para desenvolvimento assistido por IA. Se você está usando o modo agente do Copilot para projetos .NET, esses são o tipo de melhorias de qualidade de vida que reduzem o atrito no dia a dia.

Confira as [notas de versão completas](https://code.visualstudio.com/updates/v1_115) para todos os detalhes.
