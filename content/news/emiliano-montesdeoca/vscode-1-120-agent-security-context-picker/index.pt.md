---
title: "VS Code 1.120: Prompts de Senha Seguros, Seletor de Tamanho de Contexto, Metadados GitHub no Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 é uma versão focada para usuários do Copilot: tratamento seguro de prompts de senha, seletor de tamanho de contexto do modelo, metadados de PR do GitHub em sessões de agente e gerenciamento de arquivo de sessões."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 foi lançado com um conjunto de melhorias no agente Copilot que são pequenas individualmente, mas notavelmente melhores no uso diário.

## Detecção Segura de Prompts de Senha em Terminais do Agente

Quando um agente Copilot executa um comando de terminal que aciona um prompt de senha ou frase secreta, VS Code agora detecta isso e exibe um diálogo de confirmação. O diálogo foca o terminal para que você possa digitar o segredo diretamente — e crucialmente, segredos nunca são roteados através do modelo.

Esta é uma melhoria de segurança significativa. Anteriormente, agentes executando comandos que acionavam prompts de autenticação podiam criar situações onde os usuários poderiam inadvertidamente expor credenciais. O anúncio do leitor de tela significa que usuários de acessibilidade também recebem a notificação.

## Seletor de Tamanho de Contexto no Seletor de Modelo

Um novo seletor de tamanho de contexto permite selecionar quanto contexto o modelo usa para uma sessão. Diferentes modelos têm diferentes tamanhos de janela de contexto, e alguns fluxos de trabalho se beneficiam de limitá-lo (menor latência, menor custo) ou maximizá-lo (bases de código complexas, sessões de longa duração).

## Metadados de PR do GitHub em Sessões Agent Host

Para sessões respaldadas por um repositório GitHub, VS Code agora exibe metadados do GitHub — incluindo um botão de pull request — na interface do usuário do agent host. Menos troca de contexto para o navegador ou extensão GitHub quando você está trabalhando em uma PR.

## Gerenciamento do Arquivo de Sessões de Chat

Duas melhorias para o Quick Pick de sessões:
- Sessões arquivadas são ocultadas por padrão (menos bagunça visual)
- A pesquisa ainda corresponde às sessões arquivadas, para que você possa reviver uma por título

As sessões também são agrupadas por recência por padrão, facilitando encontrar trabalho recente.

## Descoberta de Plugins CLI do Copilot

VS Code agora descobre automaticamente os plugins Copilot CLI instalados pelo usuário de `~/.copilot/installed-plugins/`. Se você configurou WinUI ou outras habilidades de agente específicas do domínio, elas são detectadas sem configuração manual.

## API de Editor de Diff Personalizado (Visualização)

Para autores de extensões: uma nova API proposta `customDiffEditorProvider` permite que extensões renderizem um diff unificado em uma única webview com acesso a documentos originais e modificados, em vez de duas visualizações de editor personalizadas lado a lado.

Post original: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
