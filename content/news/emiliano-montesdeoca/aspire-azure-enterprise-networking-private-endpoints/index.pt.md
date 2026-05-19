---
title: "Endpoints Privados, VNets, NSGs — Aspire Gerencia a Rede Agora"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "O novo suporte de rede empresarial do Azure para Aspire permite modelar VNets, endpoints privados, gateways NAT, NSGs e perímetros de segurança de rede diretamente no seu AppHost, sem deriva de infraestrutura."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Já vi esse cenário muitas vezes. A aplicação está pronta. A demonstração é ótima. Então aparece a lista de verificação de segurança: tire o armazenamento da internet pública, execute dentro de uma VNet, forneça IPs de saída para a lista de permissões do parceiro, prove que apenas as sub-redes corretas falam com os serviços corretos.

Nesse ponto o modelo de aplicação e o modelo de infraestrutura começam a divergir de maneiras que são dolorosas de manter.

O novo suporte de rede empresarial do Azure para Aspire aborda isso diretamente. Você descreve a forma da rede ao lado dos recursos que a usam, no seu AppHost.

## Os Blocos de Construção

Aqui está para que serve cada conceito de rede do Azure, destilado:

| Recurso | Use quando | Por que é importante |
|---------|------------|----------------|
| Rede virtual | Você precisa de um espaço de endereçamento privado | O limite de rede para sub-redes, endpoints privados e roteamento |
| Sub-rede | Você precisa separar cargas de trabalho dentro da VNet | Cada parte do sistema obtém seu próprio intervalo de endereços e superfície de política |
| Sub-rede delegada | Um serviço de plataforma (como ACA) precisa gerenciar uma sub-rede | Permite que o serviço coloque infraestrutura gerenciada em sua VNet com segurança |
| Gateway NAT | Você precisa de IPs públicos de saída previsíveis | Endereço estável para listas de permissões e auditoria |
| Endpoint privado | Você quer um recurso PaaS acessível privatamente | Coloca um IP privado para esse serviço dentro da sua VNet, remove a exposição pública |
| NSG | Você precisa de regras de tráfego no nível da sub-rede | Permitir/negar explícito para tráfego de entrada e saída por sub-rede |

## Descrevendo no seu AppHost

A mudança chave aqui é que você está modelando a rede *junto* com os recursos que a usam, não em um arquivo Bicep separado que se afasta do modelo de aplicação com o tempo.

Do AppHost, você pode:

- Criar VNets e sub-redes com `AddVirtualNetwork()` e `AddSubnet()`
- Anexar um gateway NAT às sub-redes para IPs de saída estáveis
- Criar endpoints privados para armazenamento, Key Vault, SQL e outros serviços PaaS
- Definir NSGs com regras de segurança de entrada e saída
- Configurar Perímetros de Segurança de Rede para políticas entre recursos

O resultado é que quando você executa `azd up`, a infraestrutura corresponde ao que o modelo de aplicação diz que precisa. Não o que diz um template mantido manualmente.

## Por Que Isso Importa para Aplicações Reais

Algumas coisas que se tornam significativamente mais fáceis quando a rede é modelada no Aspire:

**Endpoints privados para Key Vault e armazenamento** — você descreve `WithPrivateEndpoint()` nesses recursos, e o Aspire lida com a configuração da zona DNS e o anexo de endpoints. A aplicação nunca muda.

**IPs de saída consistentes** — adicione um gateway NAT à sub-rede relevante e cada solicitação de saída da sua aplicação passa por um IP conhecido e estável. Os parceiros podem incluí-lo na lista de permissões. Os auditores podem rastreá-lo.

**Regras NSG do código** — em vez de clicar no portal ou manter um trecho Bicep, suas regras de segurança vivem no AppHost ao lado dos recursos que protegem.

Este é o tipo de integração que não torna as demonstrações emocionantes, mas torna os sistemas de produção manuteníveis.

## Conclusão

A segurança de rede aparecendo tarde no ciclo de vida do projeto é um problema resolvido se você a modelar junto com a aplicação desde o início. O suporte de rede empresarial do Aspire torna isso possível sem exigir um rastreamento de infraestrutura separado.

Detalhes completos na publicação original: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
