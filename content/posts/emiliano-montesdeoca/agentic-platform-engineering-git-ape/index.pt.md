---
title: "A Engenharia de Plataformas Agêntica Está se Tornando Real — Git-APE Mostra Como"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "O projeto Git-APE da Microsoft coloca a engenharia de plataformas agêntica em prática — usando agentes do GitHub Copilot e Azure MCP para transformar solicitações em linguagem natural em infraestrutura cloud validada."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Engenharia de plataformas tem sido um daqueles termos que soam ótimos em conferências, mas que normalmente significam "construímos um portal interno e um wrapper de Terraform." A verdadeira promessa — infraestrutura self-service que seja realmente segura, governada e rápida — sempre esteve a alguns passos de distância.

O time Azure acaba de publicar a [Parte 2 da série sobre engenharia de plataformas agêntica](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), e esta é toda sobre a implementação prática. Eles chamam de **Git-APE** (sim, a sigla é intencional), e é um projeto open source que usa agentes do GitHub Copilot mais servidores Azure MCP para transformar solicitações em linguagem natural em infraestrutura validada e implantada.

## O que o Git-APE realmente faz

A ideia central: em vez de desenvolvedores aprenderem módulos Terraform, navegarem por UIs de portais ou abrirem tickets para o time de plataforma, eles conversam com um agente Copilot. O agente interpreta a intenção, gera Infrastructure-as-Code, valida contra políticas e implanta — tudo dentro do VS Code.

Aqui está a configuração:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Abra o workspace no VS Code, e os arquivos de configuração do agente são descobertos automaticamente pelo GitHub Copilot. Você interage diretamente com o agente:

```
@git-ape deploy a function app with storage in West Europe
```

O agente usa o Azure MCP Server por baixo dos panos para interagir com os serviços Azure. A configuração MCP nas opções do VS Code habilita capacidades específicas:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Por que isso importa

Para nós que construímos no Azure, isso muda a conversa de engenharia de plataformas de "como construímos um portal" para "como descrevemos nossas guardrails como APIs." Quando a interface da sua plataforma é um agente de IA, a qualidade das suas restrições e políticas se torna o produto.

O blog da Parte 1 apresentou a teoria: APIs bem descritas, schemas de controle e guardrails explícitas tornam as plataformas agent-ready. A Parte 2 prova que funciona entregando ferramentas reais. O agente não gera recursos cegamente — valida contra melhores práticas, respeita convenções de nomenclatura e aplica as políticas da sua organização.

A limpeza é igualmente simples:

```
@git-ape destroy my-resource-group
```

## Minha opinião

Vou ser honesto — aqui é mais sobre o padrão do que sobre a ferramenta específica. O Git-APE em si é uma demo/arquitetura de referência. Mas a ideia subjacente — agentes como a interface da sua plataforma, MCP como protocolo, GitHub Copilot como host — é para onde a experiência do desenvolvedor enterprise está caminhando.

Se você é um time de plataforma procurando como tornar seu ferramental interno amigável para agentes, não há melhor ponto de partida. E se você é um desenvolvedor .NET se perguntando como isso se conecta ao seu mundo: o Azure MCP Server e os agentes do GitHub Copilot funcionam com qualquer workload Azure. Sua API ASP.NET Core, seu stack .NET Aspire, seus microsserviços em containers — tudo pode ser alvo de um fluxo de deploy agêntico.

## Concluindo

Git-APE é um olhar inicial mas concreto sobre engenharia de plataformas agêntica na prática. Clone o [repo](https://github.com/Azure/git-ape), experimente a demo e comece a pensar em como as APIs e políticas da sua plataforma precisariam ser para que um agente as use com segurança.

Leia o [post completo](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) para o walkthrough e vídeos de demonstração.
