---
title: "Como o Copilot Studio Migrou para .NET 10 WebAssembly e Ficou 20% Mais Rápido"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "As melhorias do .NET 10 WASM não são apenas para novos projetos. Aqui está o que o Copilot Studio mediu após a atualização do .NET 8: fingerprinting automático, WasmStripILAfterAOT por padrão e números reais de desempenho de execução."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

A equipe do Copilot Studio fez algo sobre o qual todos os desenvolvedores Blazor WASM estavam curiosos: eles realmente atualizaram uma aplicação de produção do .NET 8 para o .NET 10 e mediram os resultados. O post compartilha números específicos, o que é raro e genuinamente útil.

## A Migração Foi Chata (Isso é Positivo)

Atualizar o framework de destino, atualizar as referências de pacotes, corrigir as alterações breaking. É isso. O build do .NET 10 agora está rodando em produção. A migração em si não foi a parte interessante — as mudanças no .NET 10 são.

## Fingerprinting Automático de Assets

Anteriormente, distribuir um app WASM significava escrever scripts personalizados para renomear os assets publicados com hashes SHA256 para invalidação de cache. O Copilot Studio tinha um script PowerShell fazendo exatamente isso — renomear arquivos, injetar atributos `integrity` no loader JavaScript, gerenciar tudo manualmente.

No .NET 10, tudo isso está integrado. Os assets publicados são automaticamente marcados com fingerprint, importados diretamente de `dotnet.js` e validados com integridade sem intervenção manual. A equipe deletou o script de renomeação.

Pequena mudança em escopo, redução significativa de complexidade.

## WasmStripILAfterAOT Agora Está Ativado por Padrão

No .NET 8, remover IL de assemblies compiladas AOT era opt-in. No .NET 10 é o padrão. Após a compilação AOT, o bytecode IL original é removido da saída — não é necessário em tempo de execução, e mantê-lo inflava o tamanho do pacote sem razão.

O Copilot Studio usa uma otimização específica: ele distribui tanto um motor JIT (inicialização rápida) quanto um motor AOT (desempenho máximo em estado estável), carregando ambos em paralelo e transferindo de JIT para AOT quando estiver pronto. Também deduplica arquivos idênticos entre os dois motores.

O novo comportamento de stripping do IL significa que os assemblies AOT não correspondem mais bit a bit com seus equivalentes JIT, então menos arquivos são deduplicados:
- .NET 8: 59 arquivos compartilhados
- .NET 10: 22 arquivos compartilhados

Resultado líquido: tamanho do pacote aproximadamente 15% maior para o motor AOT. O download AOT é ~6% mais lento em LAN rápida, ~17% mais lento em 4G. Mas tudo acontece em segundo plano depois que o app já está interativo.

## Os Números de Desempenho

Esta é a parte que importa:

- **~20% mais rápido** na primeira chamada (caminho frio)
- **~5% mais rápido** nas chamadas subsequentes (caminho quente)

As melhorias são mais visíveis em "bots grandes" — agentes grandes e complexos onde o código compilado AOT domina. Para fluxos de trabalho mais simples o ganho é menor.

## Se Você Ainda Está no .NET 8

A história de migração é genuinamente simples: atualize `<TargetFramework>`, atualize as referências de pacotes, remova quaisquer scripts de fingerprinting personalizados, e você se beneficiará automaticamente do `WasmStripILAfterAOT`. Se você estiver compilando AOT, espere ganhos de desempenho similares.

Uma nota do post: se você carregar o runtime .NET WASM dentro de um `WebWorker`, defina `dotnetSidecar = true` ao inicializar.

Post original: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
