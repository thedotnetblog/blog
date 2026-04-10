---
title: "VS Code 1.116 — App de Agentes Ganha Navegação por Teclado e Autocompletação de Contexto de Arquivos"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 foca no polimento da app de Agentes — atalhos de teclado dedicados, melhorias de acessibilidade, autocompletação de contexto de arquivos e resolução de links CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "vscode-1-116-agents-app-updates.md" >}}).*

VS Code 1.116 é a versão de abril de 2026, e embora seja mais leve que algumas atualizações recentes, as mudanças são focadas e significativas — especialmente se você está usando a app de Agentes diariamente.

Aqui está o que chegou, baseado nas [notas de versão oficiais](https://code.visualstudio.com/updates/v1_116).

## Melhorias na app de Agentes

A app de Agentes continua amadurecendo com polimento de usabilidade que faz uma diferença real nos fluxos de trabalho diários:

**Atalhos de teclado dedicados** — agora você pode focar a visualização de Mudanças, a árvore de arquivos dentro de Mudanças e a visualização de Personalizações do Chat com comandos e atalhos de teclado dedicados. Se você estava clicando pela app de Agentes para navegar, isso traz fluxos de trabalho totalmente controlados por teclado.

**Diálogo de ajuda de acessibilidade** — pressionar `Alt+F1` na caixa de entrada do chat agora abre um diálogo de ajuda de acessibilidade mostrando comandos e atalhos disponíveis. Usuários de leitores de tela também podem controlar a verbosidade dos anúncios. Boa acessibilidade beneficia a todos.

**Autocompletação de contexto de arquivos** — digite `#` no chat da app de Agentes para ativar autocompletação de contexto de arquivos no seu workspace atual. Esta é uma daquelas pequenas melhorias de qualidade de vida que aceleram cada interação — chega de digitar caminhos completos de arquivos ao referenciar código.

## Resolução de links CSS `@import`

Uma boa para desenvolvedores frontend: VS Code agora resolve referências CSS `@import` que usam caminhos de node_modules. Você pode fazer `Ctrl+clique` através de imports como `@import "some-module/style.css"` ao usar bundlers. Pequeno, mas elimina um ponto de atrito nos fluxos de trabalho CSS.

## Conclusão

VS Code 1.116 é sobre refinamento — tornar a app de Agentes mais navegável, mais acessível e mais amigável ao teclado. Se você passa tempo significativo na app de Agentes (e suspeito que muitos de nós passamos), essas mudanças se acumulam.

Confira as [notas de versão completas](https://code.visualstudio.com/updates/v1_116) para a lista completa.
