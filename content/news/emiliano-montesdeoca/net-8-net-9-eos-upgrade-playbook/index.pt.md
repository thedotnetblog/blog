---
title: '.NET 8 e .NET 9 Fim de Suporte: Trate Isso como um Prazo de Entrega'
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: '10 de novembro de 2026 não é apenas uma data de suporte; é o ponto em que o risco de upgrade adiado se torna explícito.'
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Fonte original: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Este anúncio é direto, e as equipes deveriam responder com igual clareza: se você planeja continuar entregando no .NET 8 ou .NET 9 depois de 10 de novembro de 2026, você está tomando uma decisão intencional de usar um runtime sem suporte.

As aplicações vão continuar rodando. Esse não é o ponto. O ponto é que as atualizações de segurança e manutenção param. Uma vez que isso acontece, toda vulnerabilidade conhecida sem um caminho de backport se torna seu passivo operacional.

Minha opinião: as organizações costumam tratar upgrades de framework como manutenção opcional, e depois pagam por essa decisão em janelas de emergência, achados de auditoria e escalonamentos apressados de fornecedores. Planejamento de upgrade deveria ser um item do roadmap de produto, não uma missão secundária.

Uma postura prática de migração para equipes .NET:

Defina o retargeting para .NET 10 como um objetivo com data, não um item de backlog em aberto.

Rode testes de compatibilidade e regressão em paralelo com o trabalho de recursos agora, não no quarto trimestre.

Acompanhe a prontidão de dependências e hospedagem como fluxos de trabalho separados, porque muitas falhas acontecem fora do arquivo de projeto.

Use o Upgrade Assistant e a documentação de mudanças que quebram compatibilidade desde cedo para antecipar surpresas.

Se você é dono de bibliotecas compartilhadas usadas por vários produtos, publique seu cronograma de suporte ao .NET 10 publicamente dentro da sua organização. As equipes downstream precisam de tempo de antecedência.

A marcação de componentes fora de suporte no Visual Studio também importa operacionalmente. Ela cria um sinal claro de que a limpeza da toolchain faz parte de se manter em conformidade. Equipes que ignoram isso costumam derivar para estados mistos de SDK e comportamento inconsistente de build.

Um detalhe pouco discutido é que o .NET 8 e o .NET 9 convergem para a mesma data final. Isso comprime as janelas de upgrade para organizações que escalonaram a adoção esperando mais folga. Se você migrou para o .NET 9 por acesso a recursos, você ainda cai no mesmo precipício de suporte.

Para líderes de plataforma, a matriz de decisão é simples: migre antes do prazo, ou documente e aceite o risco de não ter suporte com controles compensatórios. Não existe uma terceira opção em que nada muda.

A boa notícia é que o .NET 10 é um alvo LTS até novembro de 2028, o que compra uma pista estável assim que você completar a mudança.

Não espere pela última terça de patches para começar. Trate isso como um prazo de entrega com implicações de segurança, porque é exatamente isso que é.
