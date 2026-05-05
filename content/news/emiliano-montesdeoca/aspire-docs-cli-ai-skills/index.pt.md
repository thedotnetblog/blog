---
title: "Aspire 13.2 traz uma CLI de documentação — e seu agente de IA também pode usá-la"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 adiciona aspire docs — uma CLI para pesquisar, navegar e ler documentação oficial sem sair do terminal. Também funciona como ferramenta para agentes de IA. Veja por que isso importa."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "aspire-docs-cli-ai-skills.md" >}}).*

Você conhece aquele momento quando está mergulhado num Aspire AppHost, conectando integrações, e precisa verificar exatamente quais parâmetros a integração Redis espera? Você faz alt-tab pro navegador, procura pelo aspire.dev, aperta os olhos nos docs da API, e volta pro seu editor. Contexto perdido. Flow quebrado.

Aspire 13.2 acabou de [lançar uma solução pra isso](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). A CLI `aspire docs` permite que você pesquise, navegue e leia documentação oficial do Aspire diretamente do seu terminal. E como é respaldada por serviços reutilizáveis, agentes de IA e skills podem usar os mesmos comandos para consultar docs em vez de alucinar APIs que não existem.

## O problema que isso realmente resolve

David Pine acerta em cheio no post original: agentes de IA eram *terríveis* em ajudar desenvolvedores a construir apps com Aspire. Recomendavam `dotnet run` em vez de `aspire run`, referenciavam learn.microsoft.com para docs que vivem no aspire.dev, sugeriam pacotes NuGet desatualizados, e — meu favorito pessoal — alucinavam APIs que não existem.

Por quê? Porque Aspire foi específico de .NET por muito mais tempo do que é poliglota, e os LLMs trabalham com dados de treinamento que antecedem os recursos mais recentes. Quando você dá a um agente de IA a capacidade de consultar os docs atuais, ele para de adivinhar e começa a ser útil.

## Três comandos, zero abas do navegador

A CLI é refrescantemente simples:

### Listar todos os docs

```bash
aspire docs list
```

Retorna cada página de documentação disponível no aspire.dev. Precisa de saída legível por máquina? Adicione `--format Json`.

### Pesquisar um tópico

```bash
aspire docs search "redis"
```

Pesquisa tanto em títulos quanto em conteúdo com pontuação de relevância ponderada. O mesmo motor de busca que alimenta a ferramenta de documentação internamente. Você obtém resultados ranqueados com títulos, slugs e scores de relevância.

### Ler uma página inteira (ou apenas uma seção)

```bash
aspire docs get redis-integration
```

Transmite a página completa como markdown pro seu terminal. Precisa de apenas uma seção?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Precisão cirúrgica. Sem rolar por 500 linhas. Só a parte que você precisa.

## O ângulo do agente de IA

Aqui é onde fica interessante pra nós desenvolvedores que construímos com ferramentas de IA. Os mesmos comandos `aspire docs` funcionam como ferramentas para agentes de IA — através de skills, servidores MCP, ou wrappers simples de CLI.

Em vez do seu assistente de IA inventar APIs do Aspire baseadas em dados de treinamento desatualizados, ele pode chamar `aspire docs search "postgres"`, encontrar os docs oficiais de integração, ler a página certa, e te dar a abordagem documentada. Documentação em tempo real e atualizada — não o que o modelo memorizou seis meses atrás.

A arquitetura por trás disso é intencional. O time do Aspire construiu serviços reutilizáveis (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) em vez de uma integração pontual. Isso significa que o mesmo motor de busca funciona para humanos no terminal, agentes de IA no seu editor, e automação no seu pipeline de CI.

## Cenários do mundo real

**Consultas rápidas no terminal:** Você está três arquivos de profundidade e precisa dos parâmetros de configuração do Redis. Dois comandos, noventa segundos, de volta ao trabalho:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**Desenvolvimento assistido por IA:** Seu skill do VS Code encapsula os comandos da CLI. Você pergunta "Adicione um banco de dados PostgreSQL ao meu AppHost" e o agente consulta os docs reais antes de responder. Sem alucinações.

**Validação CI/CD:** Seu pipeline valida configurações de AppHost contra documentação oficial programaticamente. A saída `--format Json` conecta-se limpo com `jq` e outras ferramentas.

**Bases de conhecimento personalizadas:** Construindo suas próprias ferramentas de IA? Envie a saída JSON estruturada direto pra sua base de conhecimento:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Sem web scraping. Sem chaves de API. Os mesmos dados estruturados que a ferramenta de documentação usa internamente.

## A documentação está sempre atualizada

Esta é a parte que mais aprecio. A CLI não baixa um snapshot — ela consulta o aspire.dev com cache baseado em ETag. No momento em que os docs são atualizados, sua CLI e qualquer skill construído sobre ela reflete isso. Sem cópias desatualizadas, sem momentos de "mas o wiki dizia...".

## Pra fechar

`aspire docs` é uma daquelas funcionalidades pequenas que resolve um problema real de forma limpa. Humanos ganham acesso à documentação direto no terminal. Agentes de IA ganham uma forma de parar de adivinhar e começar a referenciar docs reais. E tudo é sustentado pela mesma fonte de verdade.

Se você está construindo com .NET Aspire e ainda não experimentou a CLI, execute `aspire docs search "seu-topico-aqui"` e veja como é. Depois considere envolver esses comandos em qualquer skill de IA ou configuração de automação que está usando — seus agentes vão agradecer.

Confira o [mergulho profundo de David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) sobre como a ferramenta de documentação foi construída, e a [referência oficial da CLI](https://aspire.dev/reference/cli/commands/aspire-docs/) para todos os detalhes.
