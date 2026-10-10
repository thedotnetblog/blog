---
title: 'Caminhos Customizados do Data API Builder Permitem Projetar APIs para Humanos, Não para Tabelas'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Caminhos REST compostos no DAB são um pequeno recurso com grande impacto arquitetural no design de APIs orientado a domínio.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Fonte original: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

O novo suporte a caminhos REST compostos no Data API Builder pode parecer uma melhoria menor de configuração, mas na verdade resolve uma tensão de design de API de longa data: a topologia do banco de dados vazando para o design de endpoints públicos.

As rotas padrão baseadas em entidade são ótimas para começar rápido. Muitas vezes estão erradas para APIs de produto de longo prazo. Sistemas reais precisam de estruturas de rota que combinem com conceitos de negócio, limites de propriedade e modelos mentais dos consumidores.

É por isso que essa mudança do DAB importa. Você pode manter a conveniência da API gerada enquanto apresenta uma superfície mais limpa, orientada a domínio.

Minha opinião é simples: se a estrutura de caminhos da sua API espelha nomes de tabelas brutas em produção, você geralmente está otimizando para conveniência do back-end às custas da clareza do cliente.

Com caminhos customizados, as equipes podem modelar limites melhores, como vendas, faturamento, suporte ou superfícies específicas de parceiros. Isso não substitui a governança apropriada de API, mas dá aos usuários do DAB uma forma prática de alinhar o design de rotas com a linguagem do produto.

Orientação prática para equipes adotando este recurso:

Defina uma política de nomenclatura antes de adicionar caminhos de forma improvisada. Subsegmentos inconsistentes se tornam bagunça de longo prazo.

Mapeie endpoints para contextos delimitados, não para organogramas. Equipes mudam; a semântica de domínio deveria ser estável.

Trate a estrutura de caminhos como parte da sua estratégia de versionamento e documente mudanças que quebram compatibilidade explicitamente.

Valide o comportamento de autorização ao longo das estruturas de rota customizadas, para que a clareza de rota venha acompanhada de clareza de segurança.

O que eu aprecio no DAB de forma geral é o modelo de alavancagem: você obtém paginação, filtragem, projeção e outros mecanismos de endpoint sem escrever código repetitivo de controller. Caminhos customizados tornam essa alavancagem mais pronta para produção, reduzindo uma das maiores objeções dos arquitetos de API.

Há uma ressalva. Uma composição de caminhos melhor pode tentar as equipes a expor demais rápido demais, porque a geração parece fácil. Guardrails ainda importam: mantenha a exposição de entidades deliberada, aplique políticas centralmente e evite construir contratos públicos acidentais a partir de experimentos internos de schema.

Para organizações .NET sob pressão de entrega, este recurso é um destravador de produtividade se usado com disciplina. Você pode se mover mais rápido do que camadas de API feitas à mão, ainda preservando uma superfície de endpoint coerente e amigável ao negócio.

Resumindo: os caminhos customizados do DAB não são sobre enfeitar URLs. São sobre recuperar a intenção do design de API mantendo a eficiência operacional dos endpoints gerados.
