---
title: "Atualização de março do Visual Studio permite criar agentes Copilot personalizados — e o find_symbol é revolucionário"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "A atualização de março 2026 do Visual Studio traz agentes Copilot personalizados, skills reutilizáveis, a ferramenta find_symbol com reconhecimento de linguagem, e profiling com Copilot do Test Explorer."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}}).*

O Visual Studio acabou de receber sua atualização Copilot mais significativa. Mark Downie [anunciou a versão de março](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), e o destaque são os agentes personalizados — mas honestamente, a ferramenta `find_symbol` pode ser a que mais muda seu workflow.

## Agentes Copilot personalizados no seu repo

Quer que o Copilot siga os padrões de código do seu time? Agentes personalizados são definidos como arquivos `.agent.md` em `.github/agents/`. Cada agente tem acesso completo ao workspace, compreensão de código, ferramentas, seu modelo preferido e conexões MCP.

## Agent skills: pacotes de instruções reutilizáveis

Skills são carregados automaticamente de `.github/skills/` no seu repo ou `~/.copilot/skills/` no seu perfil.

## find_symbol: navegação com reconhecimento de linguagem

A nova ferramenta `find_symbol` dá ao modo agente do Copilot navegação de símbolos baseada em serviços de linguagem. Em vez de buscar texto, o agente pode encontrar todas as referências de um símbolo e acessar informações de tipo e escopo.

Para desenvolvedores .NET, é uma melhoria enorme — bases de código C# com hierarquias de tipos profundas se beneficiam enormemente.

## Perfilar testes com Copilot

Há um novo **Profile with Copilot** no menu de contexto do Test Explorer. O Profiling Agent executa o teste e analisa performance automaticamente.

## Perf tips durante debugging ao vivo

A otimização de performance agora acontece durante o debug. O Visual Studio mostra tempo de execução inline. Linha lenta? Clique no Perf Tip e peça sugestões ao Copilot.

## Corrigir vulnerabilidades NuGet do Solution Explorer

Um link **Fix with GitHub Copilot** aparece diretamente no Solution Explorer quando uma vulnerabilidade é detectada.

## Conclusão

Agentes personalizados e skills são o destaque, mas `find_symbol` é a joia escondida — muda fundamentalmente a precisão do Copilot ao refatorar código .NET. Baixe o [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) para experimentar.
