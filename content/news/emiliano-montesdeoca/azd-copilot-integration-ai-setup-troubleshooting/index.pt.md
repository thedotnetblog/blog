---
title: "azd + GitHub Copilot: Configuração de projeto com IA e resolução inteligente de erros"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "O Azure Developer CLI agora se integra com o GitHub Copilot para gerar a infraestrutura do seu projeto e resolver erros de deploy — sem sair do terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Este artigo foi traduzido automaticamente. Para ver a versão original em inglês, [clique aqui]({{< ref "index.md" >}}).*

Você conhece aquele momento em que quer fazer o deploy de uma app existente no Azure e se vê olhando para um `azure.yaml` em branco, tentando lembrar se sua API Express deveria usar Container Apps ou App Service? Esse momento acabou de ficar muito mais curto.

O Azure Developer CLI (`azd`) agora se integra com o GitHub Copilot de duas formas concretas: scaffolding assistido por IA durante o `azd init`, e resolução inteligente de erros quando os deploys falham. Ambas as funcionalidades ficam completamente no terminal — exatamente onde eu quero que estejam.

## Configuração com Copilot durante azd init

Quando você executa `azd init`, agora aparece a opção "Set up with GitHub Copilot (Preview)". Selecione-a e o Copilot analisa sua base de código para gerar o `azure.yaml`, os templates de infraestrutura e os módulos Bicep — com base no seu código real.

```
azd init
# Selecione: "Set up with GitHub Copilot (Preview)"
```

Pré-requisitos:

- **azd 1.23.11 ou superior** — verifique com `azd version` ou atualize com `azd update`
- **Assinatura ativa do GitHub Copilot** (Individual, Business ou Enterprise)
- **GitHub CLI (`gh`)** — o `azd` pedirá login se necessário

O que acho genuinamente útil: funciona nos dois sentidos. Construindo do zero? O Copilot ajuda a configurar os serviços Azure certos desde o início. Tem uma app existente que você queria fazer deploy faz tempo? Aponte o Copilot para ela e ele gera a configuração sem você precisar reestruturar nada.

### O que ele faz de verdade

Digamos que você tem uma API Express em Node.js com dependência do PostgreSQL. Em vez de decidir manualmente entre Container Apps e App Service, e depois escrever Bicep do zero, o Copilot detecta sua stack e gera:

- Um `azure.yaml` com as configurações corretas de `language`, `host` e `build`
- Um módulo Bicep para Azure Container Apps
- Um módulo Bicep para Azure Database for PostgreSQL

E ele faz verificações prévias antes de tocar em qualquer coisa — verifica se seu diretório git está limpo, pede consentimento para as ferramentas do servidor MCP. Nada acontece sem que você saiba exatamente o que vai mudar.

## Resolução de erros com Copilot

Erros de deploy são inevitáveis. Parâmetros faltando, problemas de permissão, disponibilidade de SKUs — e a mensagem de erro raramente diz a única coisa que você realmente precisa saber: *como resolver*.

Sem Copilot, o ciclo é: copiar o erro → pesquisar na documentação → ler três respostas irrelevantes do Stack Overflow → executar alguns comandos `az` CLI → tentar de novo e torcer. Com o Copilot integrado ao `azd`, esse ciclo colapsa. Quando qualquer comando `azd` falha, ele imediatamente oferece quatro opções:

- **Explain** — descrição em linguagem natural do que deu errado
- **Guidance** — instruções passo a passo para corrigir
- **Diagnose and Guide** — análise completa + Copilot aplica a correção (com sua aprovação) + nova tentativa opcional
- **Skip** — resolver você mesmo

O ponto crucial: o Copilot já tem contexto sobre seu projeto, o comando que falhou e a saída do erro. Suas sugestões são específicas para *sua situação*, não documentação genérica.

### Configurar comportamento padrão

Se você sempre escolhe a mesma opção, pule o prompt interativo:

```
azd config set copilot.errorHandling.category troubleshoot
```

Valores: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Você também pode habilitar auto-fix e retry:

```
azd config set copilot.errorHandling.fix allow
```

Voltar ao modo interativo a qualquer momento:

```
azd config unset copilot.errorHandling.category
```

## Conclusão

Esta é exatamente o tipo de integração do Copilot que agrega valor real. Experimente executando `azd update` para obter a versão mais recente e use `azd init` no seu próximo projeto.

Leia o [anúncio original aqui](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
