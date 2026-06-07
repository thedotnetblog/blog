---
title: "VS Code 1.121: Fixar Modelos Favoritos, Compressão de Saída de Terminal, SSH para Agent"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 adiciona modelos favoritos, compressão expandida da saída de terminal para executores de teste e ferramentas de compilação, temporizador de silêncio inativo para terminais em segundo plano e autenticação SSH interativa por teclado no agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continua as melhorias de qualidade do agente Copilot do 1.120, com foco no gerenciamento de modelos e comportamento do terminal.

## Fixar Modelos Favoritos

O seletor de modelos agora suporta fixação. Se você sempre usa o mesmo modelo ou dois, fixe-os no topo da lista. Reduz a rolagem quando você tem acesso a muitos modelos de vários provedores.

## Compressão Expandida da Saída de Terminal

A ferramenta de terminal do agente já comprimia a saída para comandos comuns. O 1.121 expande isso para cobrir executores de teste e ferramentas de compilação:

- **Executores de teste:** `pytest`, `jest`, `cargo test`
- **Ferramentas de compilação:** `tsc`, `cargo build`, `make`
- **Linters, Docker, gerenciadores de pacotes**

Saídas de compilação longas e relatórios de falhas de teste são comprimidos em trechos relevantes antes de serem passados ao modelo. Isso mantém o uso do contexto gerenciável quando o agente executa ciclos de compilação ou suites de testes, que podem produzir milhares de linhas de saída.

## Temporizador de Silêncio Inativo para Terminais em Segundo Plano

Um novo temporizador de silêncio inativo para a ferramenta `run_in_terminal`: se um comando síncrono não produzir saída por um período configurável, é automaticamente promovido para execução em segundo plano. Isso evita que comandos de longa duração bloqueiem o agente quando estão processando silenciosamente. Você obtém um ID de terminal para verificar mais tarde.

## Variável de Ambiente VSCODE_AGENT

Quando o Copilot Chat executa comandos no terminal, uma variável de ambiente `VSCODE_AGENT` é agora definida. Útil se você tem scripts ou ferramentas que se comportam de forma diferente quando chamados de uma sessão de agente versus interativamente.

## Adicionar ao Chat do Navegador

Clicar com o botão direito no navegador integrado agora mostra uma opção "Adicionar ao Chat". Selecione conteúdo de uma página web e adicione-o diretamente ao seu contexto do Copilot Chat sem copiar e colar.

## Corrigido: Comandos Shell de Múltiplas Linhas no Agent Host

Uma correção de bug esperada: comandos shell de múltiplas linhas na ferramenta terminal do Agent Host agora funcionam corretamente. Anteriormente, esses podiam falhar ou produzir comportamento incorreto.

## Autenticação SSH Interativa por Teclado

As conexões SSH do Agent Host agora suportam autenticação interativa por teclado — o método de autenticação fallback usado por alguns servidores SSH (incluindo algumas configurações corporativas mais antigas). Agentes trabalhando em hosts SSH remotos têm menos probabilidade de encontrar falhas de autenticação.

Post original: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
