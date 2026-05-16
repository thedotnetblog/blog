---
title: "Atualização de abril do Visual Studio 2026: agente cloud, agentes personalizados e agente depurador"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "A atualização de abril do Visual Studio 2026 (18.5) traz integração de agente cloud, agentes personalizados em nível de usuário, ferramentas C++ em GA e um Agente Depurador que valida correções contra o comportamento real em tempo de execução."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[A atualização de abril do Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) inclui integração de agente cloud, agentes personalizados em nível de usuário, ferramentas C++ chegando à GA e um novo Agente Depurador.

## Agente cloud: delegar trabalho a uma sessão remota do Copilot

No seletor de agentes da janela Chat, selecionar **Cloud** permite delegar uma tarefa a um agente de codificação remoto do Copilot. Você descreve o trabalho, o agente cria uma issue no GitHub no seu repositório e abre um PR quando termina. Você recebe uma notificação com "View PR" / "Open in browser" — tudo funciona enquanto você continua codificando, ou mesmo com o IDE fechado.

## Agentes personalizados agora viajam com você

Agentes personalizados em nível de usuário armazenados em `%USERPROFILE%/.github/agents/` não são mais limitados ao repositório — seguem você entre projetos. O caminho de armazenamento é configurável em Tools > Options > GitHub > Copilot > Chat. O botão `+` no seletor de agentes permite criar novos agentes diretamente. Eles obtêm as mesmas capacidades que agentes com escopo de repositório: consciência do espaço de trabalho, ferramentas, seleção de modelo e conexões MCP.

Agentes integrados: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Ferramentas de edição de código C++ chegam à GA

Duas ferramentas — `get_symbol_call_hierarchy` e `get_symbol_class_hierarchy` — agora estão ativadas por padrão. Elas dão ao Copilot navegação com reconhecimento de linguagem em bases de código C++, cobrindo hierarquias de herança e cadeias de chamadas de funções. Ative pelo ícone Tools no Copilot Chat. Funciona melhor com modelos de chamada de ferramentas.

## Agente Depurador: correções validadas contra o comportamento real em tempo de execução

Comece a partir de uma issue do GitHub ou Azure DevOps (ou uma descrição em linguagem natural), mude para o modo Debugger, e o agente:

1. Cria um reprodutor mínimo
2. Gera hipóteses de falha
3. Instrumenta o aplicativo com tracepoints e breakpoints condicionais
4. Executa uma sessão de depuração real
5. Analisa telemetria ao vivo
6. Sugere uma correção precisa

Você permanece no loop durante todo o processo — é interativo, não completamente autônomo.

## Correção de prioridade do IntelliSense

O VS agora suprime as conclusões do Copilot enquanto a lista do IntelliSense está ativa. Uma sugestão de cada vez. Era um ponto de atrito frequente e agora está ativado por padrão.

Notas de versão completas e download em [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
