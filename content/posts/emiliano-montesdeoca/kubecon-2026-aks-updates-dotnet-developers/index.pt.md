---
title: "KubeCon Europe 2026: O que os desenvolvedores .NET realmente precisam saber"
date: 2026-03-29
author: "Emiliano Montesdeoca"
description: "A Microsoft soltou uma enxurrada de anúncios de Kubernetes na KubeCon Europe 2026. Aqui está a versão filtrada — só as atualizações de AKS e cloud-native que importam se você está entregando apps .NET."
tags:
  - kubernetes
  - aks
  - azure
  - dotnet
  - cloud-native
  - ai
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "kubecon-2026-aks-updates-dotnet-developers" >}}).*

Sabe aquela sensação quando cai um post gigante de anúncios e você fica scrollando pensando "legal, mas o que isso muda pra mim na prática"? É assim que me sinto toda temporada de KubeCon.

A Microsoft acabou de publicar o [resumo completo da KubeCon Europe 2026](https://opensource.microsoft.com/blog/2026/03/24/whats-new-with-microsoft-in-open-source-and-kubernetes-at-kubecon-cloudnativecon-europe-2026/) — escrito pelo próprio Brendan Burns — e sinceramente? Tem conteúdo real aqui. Não são apenas checklists de features, mas melhorias operacionais que mudam como você gerencia as coisas em produção.

Deixa eu explicar o que realmente importa para nós desenvolvedores .NET.

## mTLS sem o imposto do service mesh

A coisa com service meshes é: todo mundo quer as garantias de segurança, ninguém quer a carga operacional. O AKS finalmente está fechando essa lacuna.

[Azure Kubernetes Application Network](https://aka.ms/aks/application-network) te dá TLS mútuo, autorização com reconhecimento de aplicação e telemetria de tráfego — sem implantar um mesh pesado com sidecars. Combinado com [Cilium mTLS no Advanced Container Networking Services](https://aka.ms/acns/cilium-mtls), você tem comunicação criptografada pod-a-pod usando certificados X.509 e SPIRE para gerenciamento de identidade.

Na prática: suas APIs ASP.NET Core conversando com workers em background, seus serviços gRPC chamando uns aos outros — tudo criptografado e verificado por identidade no nível de rede, sem nenhuma alteração no código. Isso é enorme.

Para times migrando do `ingress-nginx`, também tem [Application Routing com Meshless Istio](https://aka.ms/aks/app-routing/gateway-api) com suporte completo à Kubernetes Gateway API. Sem sidecars. Baseado em padrões. E lançaram ferramentas `ingress2gateway` para migração incremental.

## Observabilidade de GPU que não é secundária

Se você está rodando inferência de IA junto com seus serviços .NET (e sejamos honestos, quem não está começando?), provavelmente já se deparou com o ponto cego do monitoramento de GPU. Tinha dashboards ótimos de CPU/memória e depois... nada para GPUs sem configuração manual de exportadores.

[AKS agora expõe métricas de GPU nativamente](https://aka.ms/aks/managed-gpu-metrics) no Prometheus e Grafana gerenciados. Mesmo stack, mesmos dashboards, mesmo pipeline de alertas. Sem exportadores custom, sem agentes de terceiros.

No lado de rede, adicionaram visibilidade por fluxo para tráfego HTTP, gRPC e Kafka com uma [experiência one-click no Azure Monitor](https://learn.microsoft.com/en-us/azure/aks/container-network-observability-logs). IPs, portas, workloads, direção do fluxo, decisões de policy — tudo em dashboards integrados.

E aqui vem a que me fez olhar duas vezes: [agentic container networking](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview) adiciona uma UI web onde você pode fazer perguntas em linguagem natural sobre o estado de rede do seu cluster. "Por que o pod X não alcança o serviço Y?" → diagnósticos read-only a partir de telemetria ao vivo. Genuinamente útil às 2 da manhã.

## Networking cross-cluster que não exige doutorado

Multi-cluster em Kubernetes historicamente foi uma experiência de "traga sua própria cola de rede". Azure Kubernetes Fleet Manager agora entrega [networking cross-cluster](https://aka.ms/kubernetes-fleet/networking/cross-cluster) através de Cilium cluster mesh gerenciado:

- Conectividade unificada entre clusters AKS
- Registro global de serviços para descoberta cross-cluster
- Configuração gerenciada centralmente, não repetida por cluster

Se você roda microsserviços .NET em várias regiões para resiliência ou compliance, isso substitui muita cola custom frágil. O Serviço A no West Europe pode descobrir e chamar o Serviço B no East US através do mesh, com políticas de roteamento e segurança consistentes.

## Upgrades que não exigem coragem

Sejamos honestos — upgrades de Kubernetes em produção são estressantes. "Atualizar e torcer" tem sido a estratégia de facto para muitos times, e é a razão principal pela qual clusters ficam defasados nas versões.

Duas novas capacidades mudam isso:

**Blue-green agent pool upgrades** criam um pool de nós paralelo com a nova configuração. Valide o comportamento, mova tráfego gradualmente e mantenha um caminho limpo de rollback. Nada mais de mutações in-place em nós de produção.

**Agent pool rollback** permite reverter um pool de nós para a versão anterior do Kubernetes e imagem de nó quando um upgrade dá errado — sem reconstruir o cluster.

Juntos, finalmente dão aos operadores controle real sobre o ciclo de vida de upgrades. Para times .NET, isso importa porque a velocidade da plataforma controla diretamente quão rápido você pode adotar novos runtimes, patches de segurança e capacidades de rede.

## Workloads de IA se tornam cidadãos de primeira classe no Kubernetes

O trabalho upstream em open-source é igualmente importante. Dynamic Resource Allocation (DRA) acabou de chegar em GA no Kubernetes 1.36, tornando o scheduling de GPU uma feature de primeira classe ao invés de um workaround.

Alguns projetos que vale a pena acompanhar:

| Projeto | O que faz |
|---------|-----------|
| [AI Runway](https://github.com/kaito-project/kubeairunway) | API Kubernetes comum para inferência — deploy de modelos sem saber K8s, com descoberta HuggingFace e estimativas de custo |
| [HolmesGPT](https://www.cncf.io/blog/2026/01/07/holmesgpt-agentic-troubleshooting-built-for-the-cloud-native-era/) | Troubleshooting agêntico para cloud-native — agora projeto CNCF Sandbox |
| [Dalec](https://github.com/project-dalec/dalec) | Builds declarativos de imagens de container com geração de SBOM — menos CVEs na fase de build |

A direção é clara: sua API .NET, sua camada de orquestração com Semantic Kernel e seus workloads de inferência deveriam todos rodar em um modelo de plataforma consistente. Estamos chegando lá.

## Por onde eu começaria esta semana

Se você está avaliando essas mudanças para seu time, aqui vai minha lista honesta de prioridades:

1. **Observabilidade primeiro** — habilite métricas de GPU e logs de fluxo de rede em um cluster não-prod. Veja o que você andou perdendo.
2. **Teste blue-green upgrades** — experimente o workflow de rollback antes do seu próximo upgrade de cluster em produção. Construa confiança no processo.
3. **Pilote networking com identidade** — escolha um caminho de serviço interno e habilite mTLS com Cilium. Meça o overhead (spoiler: é mínimo).
4. **Avalie Fleet Manager** — se você roda mais de dois clusters, networking cross-cluster se paga sozinho em redução de cola custom.

Experimentos pequenos, feedback rápido. Essa é sempre a jogada.

## Finalizando

Anúncios de KubeCon podem ser avassaladores, mas essa leva realmente move a agulha para times .NET no AKS. Melhor segurança de rede sem overhead de mesh, observabilidade real de GPU, upgrades mais seguros e fundações mais fortes para infraestrutura de IA.

Se você já está no AKS, é um ótimo momento para reforçar sua baseline operacional. E se está planejando mover workloads .NET para Kubernetes — a plataforma ficou significativamente mais pronta para produção.
