---
title: "Do laptop à produção: implantando agentes de IA no Microsoft Foundry com dois comandos"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "O Azure Developer CLI agora tem comandos 'azd ai agent' que levam seu agente de IA do desenvolvimento local a um endpoint Foundry em produção em minutos. Aqui está o fluxo de trabalho completo."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

Você conhece aquela lacuna entre "funciona na minha máquina" e "está implantado e servindo tráfego"? Para agentes de IA, essa lacuna tem sido dolorosamente ampla. Você precisa provisionar recursos, implantar modelos, configurar identidade, montar monitoramento — e isso é antes de qualquer pessoa poder realmente chamar seu agente.

O Azure Developer CLI acabou de transformar isso em [uma questão de dois comandos](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## O novo fluxo de trabalho `azd ai agent`

Deixe-me mostrar como isso realmente se parece. Você tem um projeto de agente de IA — digamos um agente concierge de hotel. Funciona localmente. Você quer ele rodando no Microsoft Foundry.

```bash
azd ai agent init
azd up
```

Isso é tudo. Dois comandos. `azd ai agent init` gera a infraestrutura como código no seu repositório, e `azd up` provisiona tudo no Azure e publica seu agente. Você recebe um link direto para seu agente no portal Foundry.

## O que acontece por baixo dos panos

O comando `init` gera templates Bicep reais e inspecionáveis no seu repositório:

- Um **Foundry Resource** (contêiner de nível superior)
- Um **Foundry Project** (onde seu agente vive)
- Configuração de **implantação de modelo** (GPT-4o, etc.)
- **Identidade gerenciada** com atribuições de papéis RBAC apropriadas
- `azure.yaml` para o mapa de serviços
- `agent.yaml` com metadados do agente e variáveis de ambiente

O ponto chave: tudo isso é seu. É Bicep versionado no seu repositório. Você pode inspecioná-lo, customizá-lo e fazer commit junto com o código do seu agente. Sem caixas pretas mágicas.

## O ciclo interno de desenvolvimento

O que eu realmente gosto é a história de desenvolvimento local. Quando você está iterando na lógica do agente, não quer reimplantar toda vez que muda um prompt:

```bash
azd ai agent run
```

Isso inicia seu agente localmente. Combine com `azd ai agent invoke` para enviar prompts de teste, e você tem um ciclo de feedback apertado. Editar código, reiniciar, invocar, repetir.

O comando `invoke` também é inteligente no roteamento — quando um agente local está rodando, ele aponta automaticamente para ele. Quando não está, vai para o endpoint remoto.

## Monitoramento em tempo real

Esta é a funcionalidade que me convenceu. Uma vez que seu agente está implantado:

```bash
azd ai agent monitor --follow
```

Cada requisição e resposta fluindo pelo seu agente é transmitida para seu terminal em tempo real. Para depurar problemas em produção, isso é inestimável. Sem vasculhar log analytics, sem esperar métricas agregarem — você vê o que está acontecendo agora.

## O conjunto completo de comandos

Aqui a referência rápida:

| Comando | O que faz |
|---------|-----------|
| `azd ai agent init` | Gera um projeto de agente Foundry com IaC |
| `azd up` | Provisiona recursos Azure e implanta o agente |
| `azd ai agent invoke` | Envia prompts ao agente remoto ou local |
| `azd ai agent run` | Executa o agente localmente para desenvolvimento |
| `azd ai agent monitor` | Transmite logs em tempo real do agente publicado |
| `azd ai agent show` | Verifica saúde e status do agente |
| `azd down` | Limpa todos os recursos Azure |

## Por que isso importa para desenvolvedores .NET

Embora o exemplo do anúncio seja baseado em Python, a história de infraestrutura é agnóstica a linguagem. Seu agente .NET recebe o mesmo scaffolding Bicep, a mesma configuração de identidade gerenciada, o mesmo pipeline de monitoramento. E se você já usa `azd` para suas apps .NET Aspire ou implantações Azure, isso se encaixa direto no seu fluxo de trabalho existente.

A lacuna de implantação para agentes de IA tem sido um dos maiores pontos de fricção no ecossistema. Ir de um protótipo funcional a um endpoint de produção com identidade, rede e monitoramento adequados não deveria exigir uma semana de trabalho DevOps. Agora requer dois comandos e alguns minutos.

## Para finalizar

`azd ai agent` está disponível agora. Se você tem adiado a implantação dos seus agentes de IA porque a configuração de infraestrutura parecia trabalho demais, experimente. Confira o [tutorial completo](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) para o passo a passo completo incluindo integração de app de chat frontend.
