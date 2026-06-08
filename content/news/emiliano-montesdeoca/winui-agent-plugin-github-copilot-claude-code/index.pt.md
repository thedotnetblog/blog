---
title: "Um Plugin de Agente WinUI para GitHub Copilot e Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft lançou habilidades de agente para o desenvolvimento WinUI: scaffold, compilar, executar, testar, iterar, tudo com GitHub Copilot CLI ou Claude Code. A inovação chave: ferramentas de propósito específico que fundamentam o agente em fatos específicos do WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft publicou um conjunto open source de habilidades de agente para o desenvolvimento de aplicações WinUI, disponível em [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Instalação e Configuração

Instale o plugin com `/plugin install winui@awesome-copilot`, depois execute a configuração inicial com `/winui:winui-setup`. O processo de setup verifica os pré-requisitos, instala as dependências necessárias e configura o ambiente para o desenvolvimento de aplicações WinUI.

## O Ciclo de Desenvolvimento End-to-End

As habilidades cobrem o ciclo de desenvolvimento completo:

- **Scaffold:** Gera o template de projeto correto usando `dotnet new WinUI` com os parâmetros apropriados — o agente conhece os templates corretos e os valores padrão de configuração.
- **Compilação:** Gerencia o modelo de execução empacotado que as aplicações WinUI requerem, incluindo assinatura de pacotes e configurações de manifesto.
- **Interação e validação:** Inicia a aplicação, interage com ela e valida o comportamento.
- **Correção de erros de compilação:** O agente entende as mensagens de erro específicas do WinUI e sabe como resolvê-las.

## Eficiência de Tokens por meio de Ferramentas de Propósito Específico

A inovação chave é que as habilidades incluem ferramentas de propósito específico que buscam dados de referência concretos sob demanda:

- Detalhes da API do WinUI e Fluent Design
- Padrões MVVM e melhores práticas
- Empacotamento MSIX, assinatura de código e envio para a Store
- Acessibilidade, temas e automação de UI

Em vez de injetar toda a documentação do WinUI no contexto, as ferramentas buscam exatamente o que o agente precisa no momento em que precisa. Isso mantém o uso do contexto eficiente e melhora a precisão em domínios especializados.

## Por Que Habilidades de Propósito Específico São Importantes

Modelos de linguagem de propósito geral têm conhecimento limitado sobre as nuances específicas do WinUI: o modelo de execução empacotado, as APIs do Fluent Design, a integração MSIX ou a forma específica como o Windows App SDK envolve a funcionalidade Win32. Ferramentas de propósito específico resolvem isso fundamentando o agente em fatos verificados do WinUI, em vez de no conhecimento do modelo potencialmente desatualizado ou incorreto.

O mesmo padrão se aplica a qualquer framework ou SDK especializado com suas próprias convenções e requisitos que diferem dos padrões de desenvolvimento geral.

Post original: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
