---
title: "El servei d'agents de Foundry és GA: el que realment importa per als constructors d'agents.NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "El servei d'agents de Foundry de Microsoft acaba d'arribar a GA amb xarxes privades, Voice Live, avaluacions de producció i un temps d'execució obert multimodel. Aquí teniu el que heu de saber."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Siguem sincers: construir un prototip d'agent d'IA és la part fàcil. La part difícil és que tot sigui després: posar-lo en producció amb un aïllament adequat de la xarxa, fer avaluacions que realment signifiquen alguna cosa, gestionar els requisits de compliment i no trencar les coses a les 2 del matí.

El [Foundry Agent Service acaba de passar a GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), i aquest llançament està centrat en aquest buit de "tot després".

## Creat a partir de l'API Responses

Aquí teniu el titular: el servei d'agent de Foundry de nova generació es basa en l'API de respostes d'OpenAI. Si ja esteu creant amb aquest protocol de cable, migrar a Foundry és un canvi de codi mínim. Què obteniu: seguretat empresarial, xarxes privades, Entra RBAC, seguiment complet i avaluació, a més de la vostra lògica d'agent existent.

L'arquitectura és oberta intencionadament. No esteu bloquejat a un proveïdor de models ni a un marc d'orquestració. Utilitzeu DeepSeek per a la planificació, OpenAI per a la generació, LangGraph per a l'orquestració: el temps d'execució gestiona la capa de coherència.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Si veniu del paquet `azure-ai-agents`, ara els agents són operacions de primera classe a `AIProjectClient` a `azure-ai-projects`. Deixeu anar el pin autònom i utilitzeu `get_openai_client()` per generar respostes.

## Xarxes privades: s'ha eliminat el bloquejador empresarial

Aquesta és la característica que desbloqueja l'adopció empresarial. Foundry ara admet xarxes privades d'extrem a extrem amb BYO VNet:

- **Sense sortida pública**: el trànsit d'agents no toca mai l'Internet pública
- **Injecció de contenidor/subxarxa** a la vostra xarxa per a la comunicació local
- **Connectivitat d'eines inclosa**: els servidors MCP, Azure AI Search i els agents de dades de Fabric operen per camins privats

Aquest darrer punt és crític. No només les trucades d'inferència es mantenen privades: totes les trucades d'invocació i recuperació d'eines també es mantenen dins dels límits de la vostra xarxa. Per als equips que operen sota polítiques de classificació de dades que prohibeixen l'encaminament extern, això és el que faltava.

## Autenticació MCP feta correctament

Les connexions del servidor MCP ara admeten l'espectre complet de patrons d'autenticació:

|Mètode d'autenticació|Quan s'ha d'utilitzar|
|-------------|-------------|
|Basat en claus|Accés compartit senzill per a eines internes de tota l'organització|
|Entra la identitat de l'agent|servei a servei; l'agent s'autentica com ell mateix|
|Entra a la identitat gestionada|Aïllament per projecte; cap gestió de credencials|
|Passthrough d'identitat OAuth|Accés delegat per l'usuari; agent actua en nom dels usuaris|

OAuth Identity Passthrough és l'interessant. Quan els usuaris han de concedir a un agent accés a les seves dades personals (el seu OneDrive, la seva organització de Salesforce, una API de SaaS definida per l'usuari), l'agent actua en nom seu amb els fluxos d'OAuth estàndard. No hi ha cap identitat de sistema compartida que pretengui ser tothom.

## Voice Live: veu a veu sense la fontaneria

Afegir veu a un agent solia significar unir STT, LLM i TTS: tres serveis, tres salts de latència, tres superfícies de facturació, tot sincronitzat a mà. **Voice Live** ho col·lapsa en una única API gestionada amb:

- Activitat de veu semàntica i detecció de final de torn (comprèn el significat, no només el silenci)
- Supressió de soroll del costat del servidor i cancel·lació d'eco
- Suport d'intrusió (els usuaris poden interrompre la resposta mitjana)

Les interaccions de veu passen pel mateix temps d'execució de l'agent que el text. Els mateixos avaluadors, els mateixos rastres, la mateixa visibilitat de costos. Per a escenaris d'assistència al client, servei de camp o accessibilitat, això substitueix el que abans requeria una canalització d'àudio personalitzada.

## Avaluacions: des de la casella de selecció fins al seguiment continu

Aquí és on Foundry es pren seriosament sobre la qualitat de la producció. El sistema d'avaluació té ara tres capes:

1. **Avaluadors fora de la caixa**: coherència, rellevància, fonamentació, qualitat de recuperació, seguretat. Connecta't a un conjunt de dades o trànsit en directe i recupera les puntuacions.

2. **Avaluadors personalitzats**: codifiqueu la vostra pròpia lògica empresarial, estàndards de to i regles de compliment específiques del domini.

3. **Avaluació contínua**: Foundry mostra el trànsit de producció en directe, executa la vostra suite d'avaluadors i mostra els resultats mitjançant taulers de control. Establiu alertes d'Azure Monitor per quan cau la connexió a terra o incompliment dels llindars de seguretat.

Tot es publica a Azure Monitor Application Insights. Qualitat de l'agent, salut de la infraestructura, cost i telemetria d'aplicacions, tot en un sol lloc.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Sis noves regions per als agents allotjats

Els agents allotjats ara estan disponibles a l'est dels EUA, al nord del centre dels EUA, a Suècia al centre, al sud-est asiàtic, al Japó oriental i més. Això és important per als requisits de residència de les dades i per comprimir la latència quan el vostre agent s'executa a prop de les seves fonts de dades.

## Per què això és important per als desenvolupadors de.NET

Tot i que les mostres de codi de l'anunci de GA són Python primer, la infraestructura subjacent és independent del llenguatge, i l'SDK.NET per a `azure-ai-projects` segueix els mateixos patrons. L'API Responses, el marc d'avaluació, la xarxa privada, l'autenticació MCP, tot això està disponible a.NET.

Si heu estat esperant que els agents d'IA passin de "demo fantàstica" a "Puc enviar-ho a la feina", aquest llançament de GA és el senyal. Les xarxes privades, l'autenticació adequada, l'avaluació contínua i el seguiment de la producció són les peces que faltaven.

## Tancant

El servei d'agent de Foundry ja està disponible. Instal·leu l'SDK, obriu [el portal](https://ai.azure.com) i comenceu a crear. La [guia d'inici ràpid](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) us porta de zero a un agent en execució en qüestió de minuts.

Per obtenir la informació tècnica completa amb totes les mostres de codi, consulteu l'[anunci de GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
