---
title: "On hauríeu d'allotjar els vostres agents d'IA a Azure? Una guia pràctica de decisions"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure ofereix sis maneres d'allotjar agents d'IA: des de contenidors en brut fins a agents allotjats de Foundry totalment gestionats. A continuació s'explica com triar l'adequat per a la vostra càrrega de treball.NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

Si esteu creant agents d'IA amb.NET ara mateix, probablement heu notat alguna cosa: hi ha * moltes * maneres d'allotjar-los a Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents, i tots semblen raonables fins que realment n'has de triar un. Microsoft acaba de publicar una [guia completa per a l'allotjament d'agents d'Azure AI](https://devblogs.microsoft.com/all-things-azure/hostedagent/) que ho aclareix, i vull desglossar-ho des d'una perspectiva pràctica del desenvolupador.NET.

## Les sis opcions d'un cop d'ull

Així és com resumiria el paisatge:

|Opció|El millor per|Tu gestiones|
|--------|----------|------------|
|**Aplicacions de contenidors**|Control total del contenidor sense complexitat K8s|Observabilitat, estat, cicle de vida|
|**AKS**|Compliment empresarial, multi-clúster, xarxes personalitzades|Tot (aquest és el punt)|
|**Funcions d'Azure**|Tasques d'agent de curta durada i impulsades per esdeveniments|No gaire, veritat sense servidor|
|**Servei d'aplicacions**|Agents HTTP simples, trànsit previsible|Desplegament, configuració d'escalat|
|**Agents de foneria**|Agents opcionals de codi a través del portal/SDK|Gairebé res|
|**Agents allotjats de la foneria**|Agents de marc personalitzats amb infraestructures gestionades|Només el vostre codi d'agent|

Els quatre primers són càlculs de propòsit general: *podeu* executar-hi agents, però no estaven dissenyats per a això. Els dos últims són nadius dels agents: entenen les converses, les trucades d'eines i els cicles de vida dels agents com a conceptes de primera classe.

## Foundry Hosted Agents: el lloc ideal per als desenvolupadors d'agents.NET

Aquí és el que em va cridar l'atenció. Els agents allotjats de Foundry se situen al centre: teniu la flexibilitat d'executar el vostre propi codi (nucli semàntic, marc d'agents, LangGraph, el que sigui), però la plataforma gestiona la infraestructura, l'observabilitat i la gestió de converses.

La peça clau és l'**Adaptador d'allotjament**: una capa d'abstracció fina que connecta el vostre marc d'agent amb la plataforma Foundry. Per a Microsoft Agent Framework, té aquest aspecte:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Aquesta és tota la vostra història d'allotjament. L'adaptador gestiona la traducció del protocol, la transmissió mitjançant esdeveniments enviats pel servidor, l'historial de converses i el seguiment d'OpenTelemetry, tot automàticament. Sense programari intermedi personalitzat, sense fontaneria manual.

## El desplegament és realment senzill

Abans he desplegat agents a Container Apps i funciona, però acabeu escrivint molt codi de cola per a la gestió de l'estat i l'observabilitat. Amb Hosted Agents i `azd`, el desplegament és:

```bash
# Install the AI agent extension
azd ext install azure.ai.agents

# Init from a template
azd ai agent init

# Build, push, deploy — done
azd up
```

Aquest únic `azd up` crea el vostre contenidor, l'envia a ACR, subministra el projecte Foundry, desplega els punts finals del model i inicia el vostre agent. Cinc passos es van col·lapsar en una ordre.

## Gestió de converses integrada

Aquesta és la peça que estalvia més temps en la producció. En lloc de crear el vostre propi magatzem d'estat de conversa, els agents allotjats ho gestionen de manera nativa:

```python
# Create a persistent conversation
conversation = openai_client.conversations.create()

# First turn
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Second turn — context is preserved
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

No Redis. No hi ha botiga de sessions de Cosmos DB. No hi ha programari intermediari personalitzat per a la serialització de missatges. La plataforma només ho gestiona.

## El meu marc de decisió

Després de revisar les sis opcions, aquí teniu el meu model mental ràpid:

1. **Necessites zero infraestructura?** → Agents de fundició (portal/SDK, sense contenidors)
2. **Tens un codi d'agent personalitzat però vols un allotjament gestionat?** → Agents allotjats de Foundry
3. **Necessiteu tasques d'agent de curta durada i basades en esdeveniments?** → Azure Functions
4. **Necessites el màxim control dels contenidors sense K8?** → Aplicacions de contenidors
5. **Necessites un compliment estricte i múltiples clústers?** → AKS
6. **Teniu un agent HTTP senzill amb trànsit previsible?** → Servei d'aplicacions

Per a la majoria de desenvolupadors de.NET que creen amb Semantic Kernel o Microsoft Agent Framework, Hosted Agents és probablement el punt de partida adequat. Obteniu una escala a zero, OpenTelemetry integrada, gestió de converses i flexibilitat de marc, sense gestionar Kubernetes ni connectar la vostra pròpia pila d'observabilitat.

## Tancant

El paisatge d'allotjament d'agents a Azure està madurant ràpidament. Si inicieu un nou projecte d'agent d'IA avui, m'agradaria considerar seriosament els agents allotjats de Foundry abans d'arribar a Container Apps o AKS per costum. La infraestructura gestionada estalvia temps real i el patró de l'adaptador d'allotjament us permet mantenir la vostra elecció de marc.

Consulteu la [guia completa de Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) i el [repositori de mostres de Foundry](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) per obtenir exemples de treball.
