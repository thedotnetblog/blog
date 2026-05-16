---
title: "VS Code 1.119: OpenTelemetry para Sessões de Agentes, Integração do Navegador e Segurança"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (maio de 2026) adiciona rastreamento OpenTelemetry para sessões de agentes, compartilhamento de abas do navegador, melhorias de confiança e segurança, e um patch de segurança 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) foi lançado em 6 de maio de 2026 (com um patch de segurança 1.119.1 logo em seguida). O lançamento se concentra em observabilidade de agentes, interação com o navegador e redução de interrupções.

## Rastreamento OpenTelemetry para sessões de agentes

Este é o recurso de destaque para quem executa agentes em produção ou depura fluxos de trabalho agênticos. Ative com duas configurações:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Os rastros seguem as convenções semânticas GenAI. Cada solicitação do agente produz um span raiz `invoke_agent` com spans filho aninhados: `chat`, `execute_tool` e `execute_hook`. O uso de tokens é relatado por solicitação — incluindo contagens de leitura e criação de cache.

Funciona com o agente local, o agente em segundo plano do Copilot CLI e o agente Claude. Qualquer backend compatível com OTLP aceita os rastros — o [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) funciona bem para desenvolvimento local.

## Agentes agora podem acessar abas do navegador

Os agentes podem solicitar acesso às abas do navegador integrado — mas não é automático. Você deve compartilhar explicitamente uma aba via seletor de contexto, arrastar e soltar, ou contexto sugerido. Há um botão de compartilhamento no navegador para revogar o acesso. Quando um agente tenta abrir uma nova aba no mesmo domínio que uma aba já aberta (não compartilhada), o VS Code solicita que você reutilize a aba existente.

## Uso otimizado de tokens

Um modelo leve experimental agora gerencia as listas de tarefas dos agentes, mantendo esse trabalho administrativo longe do modelo principal mais caro. Reduz o consumo de tokens para tarefas que não precisam de capacidade completa de raciocínio.

## Confiança e segurança

Menos interrupções: VS Code 1.119 reduz solicitações de acesso à rede e gravações em pastas temporárias por agentes. O patch 1.119.1 resolve problemas de segurança específicos — vale a pena atualizar se ainda não o fez.

## Troca rápida para pré-visualização Markdown

Pequeno mas útil: agora você pode trocar rapidamente o editor atual para a pré-visualização Markdown sem navegar.

## VS Code Agents (pré-visualização Insiders)

A interface de sessão de agentes redesenhada — novo seletor de repositórios (local/repos/remoto), melhorias de subsessões, refinamento web e mobile, animações de progresso — está disponível no Insiders em [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Changelog completo: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
