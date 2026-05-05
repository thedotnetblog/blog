---
title: "azd update — Um único comando para todos os seus gerenciadores de pacotes"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "O Azure Developer CLI agora tem um comando de atualização universal que funciona independentemente de como você o instalou — winget, Homebrew, Chocolatey ou script de instalação."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azd-update-universal-upgrade-command.md" >}}).*

Sabe aquela mensagem "Uma nova versão do azd está disponível" que aparece a cada poucas semanas? Aquela que você ignora porque não lembra se instalou o `azd` via winget, Homebrew ou aquele script curl que rodou há seis meses? Pois é, isso finalmente foi resolvido.

A Microsoft acabou de lançar o [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — um único comando que atualiza o Azure Developer CLI para a versão mais recente, independentemente de como você o instalou originalmente. Windows, macOS, Linux — não importa. Um comando só.

## Como funciona

```bash
azd update
```

É isso. Se você quer acesso antecipado a novas funcionalidades, pode mudar para o build diário de insiders:

```bash
azd update --channel daily
azd update --channel stable
```

O comando detecta seu método de instalação atual e usa o mecanismo de atualização apropriado por baixo dos panos. Chega de "espera, eu usei winget ou choco nessa máquina?"

## O pequeno detalhe

`azd update` está disponível a partir da versão 1.23.x. Se você está em uma versão anterior, vai precisar fazer uma última atualização manual usando seu método de instalação original. Depois disso, o `azd update` cuida de tudo dali em diante.

Verifique sua versão atual com `azd version`. Se precisar de uma instalação do zero, a [documentação de instalação](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) te ajuda.

## Por que isso importa

É uma pequena melhoria de qualidade de vida, mas para quem usa `azd` diariamente para fazer deploy de agentes de IA e apps Aspire no Azure, estar atualizado significa menos momentos de "esse bug já tinha sido corrigido na última versão". Uma coisa a menos para se preocupar.

Leia o [anúncio completo](https://devblogs.microsoft.com/azure-sdk/azd-update/) e a [análise mais detalhada](https://blog.jongallant.com/2026/04/azd-update) do Jon Gallant para mais contexto.
