---
title: "Azure DevOps MCP Server chega ao Microsoft Foundry: O que isso significa para seus agentes de IA"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "O Azure DevOps MCP Server agora está disponível no Microsoft Foundry. Conecte seus agentes de IA diretamente aos workflows de DevOps — work items, repos, pipelines — com poucos cliques."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) está tendo seu momento. Se você tem acompanhado o ecossistema de agentes de IA, provavelmente notou servidores MCP surgindo por todo lado — dando aos agentes a capacidade de interagir com ferramentas e serviços externos através de um protocolo padronizado.

Agora o [Azure DevOps MCP Server está disponível no Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), e essa é uma daquelas integrações que faz você pensar nas possibilidades práticas.

## O que está realmente acontecendo aqui

A Microsoft já lançou o Azure DevOps MCP Server como [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — esse é o servidor MCP em si. A novidade é a integração com o Foundry. Agora você pode adicionar o Azure DevOps MCP Server aos seus agentes Foundry diretamente do catálogo de ferramentas.

Para quem ainda não conhece o Foundry: é a plataforma unificada da Microsoft para construir e gerenciar aplicações e agentes alimentados por IA em escala. Acesso a modelos, orquestração, avaliação, deploy — tudo em um só lugar.

## Configurando

A configuração é surpreendentemente simples:

1. No seu agente Foundry, vá para **Add Tools** > **Catalog**
2. Busque "Azure DevOps"
3. Selecione o Azure DevOps MCP Server (preview) e clique em **Create**
4. Insira o nome da sua organização e conecte

Isso é tudo. Seu agente agora tem acesso às ferramentas do Azure DevOps.

## Controlando o que seu agente pode acessar

Essa é a parte que eu aprecio: você não está preso a uma abordagem de tudo-ou-nada. Você pode especificar quais ferramentas estão disponíveis para seu agente. Então se você quer que ele apenas leia work items mas não toque em pipelines, pode configurar isso. Princípio do menor privilégio, aplicado aos seus agentes de IA.

Isso importa para cenários enterprise onde você não quer que um agente acidentalmente dispare um pipeline de deploy porque alguém pediu para ele "ajudar com o release."

## Por que isso é interessante para equipes .NET

Pense no que isso possibilita na prática:

- **Assistentes de planejamento de sprint** — agentes que podem buscar work items, analisar dados de velocidade e sugerir capacidade de sprint
- **Bots de code review** — agentes que entendem o contexto do seu PR porque podem realmente ler seus repos e work items vinculados
- **Resposta a incidentes** — agentes que podem criar work items, consultar deploys recentes e correlacionar bugs com mudanças recentes
- **Onboarding de desenvolvedores** — "No que devo trabalhar?" recebe uma resposta real baseada em dados reais do projeto

Para equipes .NET que já usam Azure DevOps para seus pipelines de CI/CD e gerenciamento de projetos, ter um agente de IA que pode interagir diretamente com esses sistemas é um passo significativo em direção à automação útil.

## O panorama maior do MCP

Isso faz parte de uma tendência mais ampla: servidores MCP estão se tornando a forma padrão como agentes de IA interagem com o mundo exterior. Estamos vendo para GitHub, Azure DevOps, bancos de dados, APIs SaaS — e o Foundry está se tornando o hub onde todas essas conexões se encontram.

Se você está construindo agentes no ecossistema .NET, vale a pena prestar atenção ao MCP. O protocolo é padronizado, as ferramentas estão amadurecendo, e a integração com Foundry torna acessível sem precisar configurar manualmente conexões de servidor.

## Para finalizar

O Azure DevOps MCP Server no Foundry está em preview, então espere que ele evolua. Mas o workflow principal é sólido: conectar, configurar acesso às ferramentas e deixar seus agentes trabalharem com seus dados de DevOps. Se você já está no ecossistema Foundry, está a poucos cliques. Experimente e veja quais workflows você consegue construir.

Confira o [anúncio completo](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) para a configuração passo a passo e mais detalhes.
