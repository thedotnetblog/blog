---
title: "Mission Control para Agentes de Codificação: Uma Experiência Unificada no VS Code"
description: "O VS Code reúne agentes de codificação locais, na nuvem, CLI e de terceiros em Sessões de Agentes, permitindo que os desenvolvedores acompanhem, interrompam e coordenem trabalhos autônomos."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

# Mission Control para Agentes de Codificação: Uma Experiência Unificada no VS Code

Um único assistente de codificação é fácil de entender. Vários agentes trabalhando em lugares diferentes não são.

Um agente é executado localmente no VS Code. Outro trabalha em uma issue do GitHub na nuvem. Um agente CLI vive no terminal. Um agente de codificação de terceiros pode ter um modelo de sessão diferente e limites diferentes. Sem uma visão compartilhada, os desenvolvedores gastam mais tempo rastreando o trabalho do que supervisionando-o.

A experiência unificada de agentes do VS Code aborda esse problema de coordenação com Sessões de Agentes: um lugar para lançar agentes, ver seu status, abrir suas conversas e intervir quando o plano muda.

Trata-se menos de adicionar outro agente e mais de tornar múltiplos agentes gerenciáveis.

## Uma Visão para Diferentes Tipos de Trabalho

O artigo de origem descreve quatro participantes distintos: GitHub Copilot local, Agente de Codificação Copilot na nuvem, GitHub Copilot CLI e OpenAI Codex para assinantes Copilot elegíveis.

Eles têm pontos fortes diferentes:

- Um agente local pode inspecionar o workspace atual e fazer mudanças rápidas.
- Um agente de codificação na nuvem pode trabalhar de forma assíncrona em uma issue e abrir um pull request.
- Um agente CLI se encaixa bem em workflows pesados de terminal e comandos operacionais.
- Outro provedor pode oferecer um modelo ou estilo de raciocínio diferente.

As Sessões de Agentes oferecem um lar comum para essas tarefas. Você pode ver o que está em execução, o que está fazendo e onde continuar a conversa.

Essa visibilidade é importante porque o trabalho autônomo não remove a coordenação. Torna a coordenação uma tarefa de engenharia de primeira classe.

## Interrupções Fazem Parte do Fluxo de Trabalho

A fonte faz uma observação simples: "É comum enviar um prompt e perceber que você esqueceu algo importante." Anteriormente, a escolha era frequentemente esperar ou cancelar. Com editores de chat, você pode abrir uma sessão ativa e adicionar informações enquanto o agente está trabalhando.

Isso é mais próximo de uma verdadeira colaboração. Os requisitos mudam. Um teste revela uma suposição. Um revisor percebe que uma API deve permanecer compatível com versões anteriores. O agente útil não é aquele que nunca precisa de correção; é aquele que pode absorver a correção sem perder toda a tarefa.

Para trabalhos em .NET, uma interrupção pode ser tão simples quanto:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

A instrução é breve porque o repositório já carrega o contexto maior. A sessão é o lugar para corrigir a direção, não para reafirmar todo o sistema.

## Agentes Personalizados Transformam Hábitos de Equipe em Funções

O VS Code também introduz agentes especializados, como Plan. Em vez de implementar imediatamente, um agente de planejamento faz perguntas sobre escopo, componentes, bibliotecas e restrições antes de produzir uma especificação de implementação.

Esse padrão é útil além de um agente integrado. Uma equipe pode definir funções focadas:

- **Research** reúne evidências e escreve um registro de decisão breve.
- **Review** verifica uma mudança em relação às convenções do repositório.
- **Testing** identifica casos ausentes e propõe um plano de testes.
- **Architecture** compara opções sem modificar arquivos.

Uma pequena definição de agente personalizado pode parecer assim:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

A parte útil não é o YAML. É a separação explícita de responsabilidades. Um agente de planejamento não deve editar silenciosamente código de produção. Um agente de revisão não deve reescrever o design que deveria avaliar.

## Subagentes Reduzem Colisões de Contexto

Conversas longas acumulam contexto não relacionado. Subagentes fornecem um workspace isolado para uma tarefa de pesquisa limitada e retornam o resultado para a sessão principal.

Isso é um bom ajuste para perguntas como:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

O agente principal permanece focado em implementação enquanto o agente de pesquisa lida com uma questão mais estreita. O mesmo princípio se aplica a equipes: delegação clara produz melhores resultados do que lançar vários agentes com autoridade sobreposta.

## A Ressalva: Mais Agentes Significam Mais Coordenação

Sessões de Agentes podem mostrar atividade, mas não podem resolver propriedade conflitante. Dois agentes editando a mesma área ainda podem criar um problema de merge. Um agente na nuvem e um agente local podem fazer suposições incompatíveis. Um agente personalizado pode produzir uma recomendação que outro agente ignora.

Defina limites:

1. Um agente é proprietário da implementação para um determinado branch.
2. Agentes de pesquisa retornam artefatos, não edições não rastreadas.
3. Solicitações de pull permanecem o limite de revisão.
4. Nomes de agentes e prompts declaram o que eles podem alterar.
5. A saída da sessão é retida quando explica uma decisão importante.

## Minha Opinião

O futuro multi-agente não é uma fila de janelas de chat. É uma pequena equipe com funções, handoffs e responsabilidade.

Sessões de Agentes é valioso porque reconhece essa realidade. Oferece aos desenvolvedores uma superfície de controle para trabalhos que já estão acontecendo no editor, terminal e nuvem. O próximo ganho de produtividade virá menos de ter mais agentes e mais de tornar seus limites legíveis.

Para uma equipe .NET, eu começaria com um agente de planejamento e um agente de implementação. Use a saída de planejamento como a especificação de issue ou pull request, então deixe o agente de implementação trabalhar dentro desse limite. Meça retrabalhação antes de adicionar mais funções.

O melhor mission control ainda é aquele que torna a propriedade óbvia.
