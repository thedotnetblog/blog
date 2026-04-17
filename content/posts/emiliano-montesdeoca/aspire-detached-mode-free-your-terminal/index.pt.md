---
title: "Pare de ficar de olho no seu terminal: o modo desacoplado do Aspire muda o fluxo de trabalho"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "O Aspire 13.2 permite executar seu AppHost em segundo plano e recuperar seu terminal. Combinado com os novos comandos CLI e suporte a agentes, isso é mais importante do que parece."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Toda vez que você executa um AppHost do Aspire, seu terminal some. Travado. Ocupado até você pressionar Ctrl+C. Precisa rodar um comando rápido? Abra outra aba. Quer verificar os logs? Mais uma aba. É um pequeno atrito que se acumula rápido.

O Aspire 13.2 resolve isso. James Newton-King [escreveu todos os detalhes](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), e sinceramente, essa é uma daquelas funcionalidades que muda imediatamente a forma como você trabalha.

## Modo desacoplado: um comando, terminal de volta

```bash
aspire start
```

Esse é o atalho para `aspire run --detach`. Seu AppHost inicia em segundo plano e você recupera seu terminal imediatamente. Sem abas extras. Sem multiplexador de terminal. Apenas seu prompt, pronto para usar.

## Gerenciando o que está rodando

A questão é — rodar em segundo plano só é útil se você conseguir gerenciar o que está lá fora. O Aspire 13.2 traz um conjunto completo de comandos CLI para exatamente isso:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Isso transforma o CLI do Aspire em um verdadeiro gerenciador de processos. Você pode iniciar múltiplos AppHosts, verificar seus status, acompanhar seus logs e encerrá-los — tudo a partir de uma única sessão de terminal.

## Combine com o modo isolado

O modo desacoplado combina naturalmente com o modo isolado. Quer rodar duas instâncias do mesmo projeto em segundo plano sem conflitos de porta?

```bash
aspire start --isolated
aspire start --isolated
```

Cada uma recebe portas aleatórias, secrets separados e seu próprio ciclo de vida. Use `aspire ps` para ver ambas, `aspire stop` para encerrar a que você não precisa mais.

## Por que isso é enorme para agentes de código

É aqui que fica realmente interessante. Um agente de código trabalhando no seu terminal agora pode:

1. Iniciar a app com `aspire start`
2. Consultar seu estado com `aspire describe`
3. Verificar logs com `aspire logs` para diagnosticar problemas
4. Parar com `aspire stop` quando terminar

Tudo sem perder a sessão do terminal. Antes do modo desacoplado, um agente que executasse seu AppHost ficava preso no próprio terminal. Agora ele pode iniciar, observar, iterar e limpar — exatamente como você gostaria que um agente autônomo funcionasse.

A equipe do Aspire investiu nisso. Executar `aspire agent init` configura um arquivo de habilidades do Aspire que ensina esses comandos aos agentes. Assim, ferramentas como o agente de código do Copilot podem gerenciar suas cargas de trabalho do Aspire diretamente.

## Finalizando

O modo desacoplado é uma melhoria de fluxo de trabalho disfarçada de uma simples flag. Você para de alternar contexto entre terminais, agentes param de se bloquear, e os novos comandos CLI dão visibilidade real do que está rodando. É prático, é limpo, e torna o ciclo de desenvolvimento diário visivelmente mais fluido.

Leia o [post completo](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) para todos os detalhes e obtenha o Aspire 13.2 com `aspire update --self`.
