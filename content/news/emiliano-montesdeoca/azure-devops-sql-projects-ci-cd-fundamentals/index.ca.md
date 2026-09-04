---
title: "Deixeu de Tractar les Bases de Dades com a Flocs de Neu Especials: Azure DevOps + SQL Projects Ben Fet"
date: 2026-07-15
author: Emiliano Montesdeoca
description: "El model de pipeline de SQL projects a Azure DevOps demostra que el lliurament de bases de dades pot ser repetible, segur i comprovable quan els equips adopten disciplina CI/CD code-first."
tags:
  - Azure DevOps
  - Azure SQL
  - CI/CD
  - SQL Projects
  - DevSecOps
  - Data Engineering
---

Molts equips diuen que fan DevOps, i després despleguen canvis de base de dades manualment des del portàtil d'algú. Aquesta contradicció és exactament el que aquesta guia d'Azure SQL corregeix. SQL projects més pipelines d'Azure DevOps fan que el lliurament de bases de dades sigui determinista, auditable i prou segur per a fluxos de treball de producció reals.

Font original: https://devblogs.microsoft.com/azure-sql/fundamentals-of-azure-devops-with-sql-projects/

La part més forta de l'enfocament no és la sintaxi YAML, sinó la seqüència de disciplina: construir primer, publicar segon, i assegurar el camí de desplegament amb privilegis mínims i identitat sense contrasenya. Construir un .sqlproj amb dotnet valida la compatibilitat amb la plataforma objectiu aviat i produeix un artifact DACPAC que es pot promocionar entre entorns.

La meva opinió és directa: si el vostre esquema no es construeix a CI, el vostre procés de qualitat de base de dades és sobretot esperança. L'èxit local a SSMS o VS Code no és una garantia de llançament.

El disseny de desplegament també és refrescantment pragmàtic. Utilitzeu connexions de servei lligades a identitats Entra, concediu rols de base de dades amb àmbit per a comparació d'esquemes i dades, i automatitzeu l'obertura temporal de firewall per a IPs de l'executor amb neteja garantida. Aquest és el tipus d'higiene operativa que els equips salten fins que una revisió de bretxa els força a revisar-ho tot.

Recomanacions pràctiques per aplicar immediatament:

Separeu els pipelines de compilació i desplegament. La compilació s'ha d'executar en canvis de branca i fallar ràpid. El desplegament ha de ser específic de l'entorn i amb comportes de política. Emmagatzemeu les cadenes de connexió objectiu i les metadades d'infraestructura en variables de pipeline assegurades, i feu rotacions de revisions de govern per a les assignacions de rols regularment. Mantingueu les versions de SqlPackage explícites i fixades a CI per evitar canvis de comportament sorpresa.

No sobreprivilegieu aviat. Començar amb db_ddladmin, db_datareader i db_datawriter és una millor línia base que donar db_owner a cada principal del pipeline "només per fer-ho funcionar." Escaleu només quan un requisit de desplegament concret demostri que és necessari.

Una altra conclusió important és la portabilitat. Com que els SQL projects funcionen amb la cadena d'eines del SDK de .NET, aquest patró no és exclusiu d'Azure DevOps. Els mateixos fonaments es tradueixen a GitHub Actions o altres orquestradors, cosa que fa que aquesta guia sigui estratègica, no lligada a una plataforma.

Si la vostra organització encara tracta el lliurament d'esquemes com un procés especial fora del CI/CD de l'aplicació, aquest és el vostre plànol de migració. No necessiteu enginyeria de plataforma heroica. Necessiteu consistència, seguretat basada en identitat i una voluntat de deixar d'enviar canvis de base de dades per camins de privilegis ad hoc.

Els equips que facin això lliuraran més ràpid amb menys incidents de retrocés. Els equips que ho retardin continuaran pagant l'impost ocult dels desplegaments de pla de dades manuals.