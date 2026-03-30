---
title: "O Dashboard do Aspire 13.2 agora tem uma API de telemetria — e isso muda tudo"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 traz exportação inteligente de telemetria, uma API programática para traces e logs, e melhorias na visualização GenAI. Veja por que isso importa para o seu workflow de depuração."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "aspire-132-dashboard-export-telemetry.md" >}}).*

Se você tem desenvolvido aplicações distribuídas com .NET Aspire, já sabe que o dashboard é a melhor coisa de toda a experiência. Todos os seus traces, logs e métricas em um só lugar — sem Jaeger externo, sem configuração de Seq, sem momentos de "deixa eu verificar o outro terminal".

O Aspire 13.2 acabou de melhorar tudo significativamente. James Newton-King [anunciou a atualização](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), e honestamente? Os recursos de exportação de telemetria e a API sozinhos justificam o upgrade.

## Exportar telemetria de forma civilizada

Aqui está o cenário que todos já vivemos: você está depurando um problema distribuído, finalmente reproduz depois de vinte minutos de configuração, e agora precisa compartilhar o que aconteceu com o time. Antes? Screenshots. Copiar e colar IDs de traces. A bagunça de sempre.

O Aspire 13.2 adiciona um diálogo de **Gerenciar logs e telemetria** onde você pode:

- Limpar toda a telemetria (útil antes de tentar reproduzir)
- Exportar telemetria selecionada em um arquivo ZIP no formato padrão OTLP/JSON
- Reimportar esse ZIP em qualquer dashboard Aspire depois

Esse último ponto é o recurso matador. Você reproduz um bug, exporta a telemetria, anexa ao seu work item, e seu colega pode importar no próprio dashboard para ver exatamente o que você viu. Acabou o "consegue reproduzir na sua máquina?"

Traces, spans e logs individuais também têm uma opção "Export JSON" nos menus de contexto. Precisa compartilhar um trace específico? Clique direito, copiar JSON, colar na descrição do PR. Pronto.

## A API de telemetria é o verdadeiro divisor de águas

Isso é o que mais me empolga. O dashboard agora expõe uma API HTTP em `/api/telemetry` para consultar dados de telemetria programaticamente. Endpoints disponíveis:

- `GET /api/telemetry/resources` — listar recursos com telemetria
- `GET /api/telemetry/spans` — consultar spans com filtros
- `GET /api/telemetry/logs` — consultar logs com filtros
- `GET /api/telemetry/traces` — listar traces
- `GET /api/telemetry/traces/{traceId}` — obter todos os spans de um trace específico

Tudo retorna no formato OTLP JSON. Isso alimenta os novos comandos CLI `aspire agent mcp` e `aspire otel`, mas a implicação real é maior: agora você pode construir ferramentas, scripts e integrações com agentes de IA que consultam a telemetria da sua app diretamente.

Imagine um agente de IA que pode ver seus traces distribuídos reais enquanto você depura. Isso não é mais hipotético — é o que esta API possibilita.

## Telemetria GenAI fica prática

Se você está construindo apps com IA usando Semantic Kernel ou Microsoft.Extensions.AI, vai gostar do visualizador de telemetria GenAI melhorado. O Aspire 13.2 adiciona:

- Descrições de ferramentas IA renderizadas como Markdown
- Um botão dedicado de GenAI na página de traces para acesso rápido
- Melhor tratamento de erros para JSON de GenAI truncado ou não padrão
- Navegação click-to-highlight entre definições de ferramentas

O post menciona que VS Code Copilot chat, Copilot CLI e OpenCode suportam configurar um `OTEL_EXPORTER_OTLP_ENDPOINT`. Aponte-os para o dashboard Aspire e você pode literalmente assistir seus agentes IA pensando em tempo real pela telemetria. Essa é uma experiência de depuração que você não encontra em nenhum outro lugar.

## Conclusão

O Aspire 13.2 transforma o dashboard de "UI bonita de depuração" para "plataforma de observabilidade programável". O workflow de exportação/importação sozinho economiza tempo real na depuração distribuída, e a API de telemetria abre a porta para diagnósticos assistidos por IA.

Se você já usa Aspire, atualize. Se não — esta é uma boa razão para conhecer [aspire.dev](https://aspire.dev).
