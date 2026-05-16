---
title: "Eliminant el Treball Repetitiu de la Migració amb Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape fa un recorregut per la migració d'un desplegament Terraform d'AWS real a Azure Bicep — extraient la intenció del desplegament i remapejant l'arquitectura en lloc de fer una conversió sintàctica 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — una guia pas a pas de Git-Ape (eina git d'enginyeria de plataformes agentiva) que migra un repositori Terraform d'AWS real a Azure, centrant-se en l'extracció d'intenció en lloc de la conversió línia per línia.

## L'entrada: contoso-migration

La font és un projecte Terraform real (`contoso-migration`) que desplega una aplicació Next.js a AWS — EC2 per al còmput, ALB per a l'equilibri de càrrega, S3 per als artefactes, i claus IAM per a la identitat. Cost: ~34$/mes. L'objectiu no és reproduir la mateixa infraestructura a Azure; és entendre el que el desplegament realment intenta fer i reconstruir-ho amb serveis natius d'Azure.

## Pas 1: Validació i autenticació

Git-Ape comença validant totes les eines CLI necessàries — `az`, `aws`, `gh`, `jq`, `git` — i confirmant les sessions d'autenticació actives abans de tocar res. Sense execucions parcials.

## Pas 2: Extracció d'intenció

L'agent llegeix el repositori font sencer a través de l'API de GitHub i extreu la intenció del desplegament: temps d'execució (Node.js), tipus de còmput, patró d'entrada, gestió d'artefactes, model d'identitat, xarxa i monitoratge. Aquest és el pas clau — està construint un model semàntic del que fa el desplegament, no quines paraules clau de Terraform utilitza.

## Pas 3: Mapatge de serveis

Els serveis AWS es mapegen als equivalents d'Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Equilibri de càrrega integrat d'App Service
- Rols/claus IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Pas 4: Agent de crítica

Abans de generar la sortida, s'executa un agent de crítica i detecta dos problemes bloquejants:

1. **Anti-patró de construcció a l'inici** — el Terraform original estava executant `npm install && npm run build` a EC2 a l'inici. Solució: construir a CI, desplegar un artefacte llest.
2. **Blob Storage innecessari** — S3 s'usava per a l'etapa d'artefactes que es podria eliminar amb un CI/CD adequat. L'agent de crítica el va eliminar completament.

## Pas 5: Sortida generada

El resultat és ~80 línies de Bicep en lloc de les 200+ línies originals de Terraform. L'agent va crear un nou repositori GitHub amb `infra/main.bicep` i `.github/workflows/deploy.yml` i va eliminar tots els arxius específics d'AWS.

## Comparació de postura de seguretat

La migració també va produir una millora de seguretat significativa:

| Original AWS | Sortida Azure |
|---|---|
| Només HTTP | Només HTTPS, TLS 1.2 |
| SSH obert a 0.0.0.0/0 | Sense exposició SSH |
| Claus d'accés IAM | OIDC + Managed Identity |
| Sense monitoratge | Application Insights |

Cost: ~13$/mes vs els 34$/mes originals.

## Què el diferencia d'un convertidor de sintaxi

El pas de l'agent de crítica és el que el separa d'una traducció mecànica. Va detectar patrons que haurien funcionat a AWS però haurien estat incorrectes a Azure — i els va corregir en lloc de replicar-los. La sortida no és "AWS en sintaxi d'Azure"; és un desplegament natiu d'Azure que aconsegueix el mateix objectiu de manera més neta.

Consulteu la [guia completa](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) per a la traça completa de l'agent i els arxius generats.
