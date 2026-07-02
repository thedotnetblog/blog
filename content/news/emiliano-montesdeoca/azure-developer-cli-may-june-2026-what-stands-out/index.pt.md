---
title: "O Azure Developer CLI continua se tornando uma ferramenta melhor de inner loop"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "As versões de maio e junho de 2026 do Azure Developer CLI adicionam muita coisa, mas o maior valor está em como melhoram o ciclo diário: melhor gerenciamento de ferramentas, provisionamento mais seguro, suporte mais forte para extensões e fluxos de execução mais práticos."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Grandes resumões de CLI podem ser cansativos de ler porque misturam grandes melhorias de workflow com pequenos ajustes em uma única parede de texto.

Então aqui vai minha versão curta: as últimas atualizações do **Azure Developer CLI** importam porque `azd` continua se tornando uma **ferramenta de inner loop melhor**, e não apenas um wrapper de deployment.

Essa é a mudança importante.

## O gerenciamento de ferramentas está virando parte do produto, não uma tarefa lateral

Uma das minhas adições favoritas são os novos comandos `azd tool`.

Tudo o que reduz atrito de setup vale a pena observar, especialmente em projetos onde um ambiente funcional depende de uma mistura de SDKs, CLIs, Docker, Bicep e extensões.

Se a ferramenta agora pode ajudar a descobrir, instalar, verificar e atualizar essas dependências diretamente, isso elimina muitos dos modos de falha irritantes que costumam atingir primeiro os novos usuários.

Isso é valor real.

## `azd exec` também parece mais importante do que soa

À primeira vista, `azd exec` pode parecer um recurso pequeno de conveniência.

Eu não acho que seja.

Executar comandos com todo o contexto do ambiente `azd`, incluindo resolução de secrets, é exatamente o tipo de capacidade que deixa a automação local e o scripting muito mais limpos.

Isso reduz a necessidade de scripts de cola extras e ajuda a manter a execução consistente entre ambientes.

Isso é um ganho prático.

## Provisionamento mais seguro e melhor comportamento de cancelamento são melhorias subestimadas

A release também traz mudanças em dependências de provisionamento, tratamento de cancelamento e comportamento de deployment, coisas que talvez não pareçam glamorosas, mas são muito bem-vindas.

Prompts interativos de cancelamento, melhor modelagem de dependências e um estado de deployment mais claro são exatamente o tipo de melhoria que faz um CLI parecer confiável ao trabalhar com recursos reais do Azure.

E confiança é um assunto grande para ferramentas como essa.

## A minha leitura

Quanto mais `azd` melhora em setup, scripting, segurança de deployment e suporte a extensões, mais ele parece algo que você pode manter no seu ciclo diário em vez de tocar só imediatamente antes do deployment.

Essa é a direção certa.

Para equipes que constroem apps cloud-native ou movidos por IA no Azure, isso torna o CLI mais útil no lugar que realmente importa: durante o desenvolvimento de verdade.

Post original: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)