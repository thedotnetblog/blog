---
title: "Agent Skills a Visual Studio: Ensenya a Copilot Com Treballa Realment el Teu Equip"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio ara admet Agent Skills — conjunts d'instruccions reutilitzables que ensenyen a Copilot els fluxos de treball, estàndards de codi i convencions específics del teu equip. Defineix-los una vegada, aplica'ls automàticament."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Una de les frustracions persistents amb els assistents de codificació d'IA: coneixen bé la programació general però no coneixen les convencions específiques del *teu* equip, les teves API internes o els teus patrons preferits. En cada sessió, tornes a explicar el context. Agent Skills a Visual Studio està dissenyat per solucionar-ho.

## Què Són els Agent Skills

Conjunts d'instruccions reutilitzables — definits en fitxers `SKILL.md` — que ensenyen als agents de Copilot com gestionar tasques específiques. Defineix un skill per a "com executar el nostre pipeline de build", "com generar boilerplate per a la nostra capa de servei" o "la nostra llista de verificació de revisió de codi". L'agent aplica el skill automàticament quan és rellevant.

Això no és un concepte nou (`.github/copilot-instructions.md` existeix des de fa un temps), però la integració de Visual Studio els converteix en objectes de primera classe amb una interfície de descobriment.

## Creació de Skills a Visual Studio

El flux d'interfície integrat: fes clic a la icona d'eines a Copilot Chat, obre el tauler de skills, fes clic a `+`. Tries l'àmbit global (personal) o a nivell de solució, tries un nom i Visual Studio genera una plantilla. El mode Agent de Copilot pot llavors ajudar-te a omplir la plantilla — utilitza l'agent per escriure el skill per a l'agent.

Actualment al canal Insiders, aviat disponible a Release.

També pots crear skills manualment:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Ubicacions de Descobriment

Els skills es descobreixen automàticament des de rutes estàndard:

**Nivell de solució (compartit via repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/personal (el teu perfil d'usuari, disponible a tot arreu):** `~/.copilot/skills/`, `~/.agents/skills/`

El suport multi-ubicació significa que la mateixa convenció funciona amb GitHub Copilot, Claude Code i altres frameworks d'agents — defineix els teus skills una vegada, utilitza'ls a tot arreu.

## El Format

Els skills segueixen el format [agentskills.io/specification](https://agentskills.io/specification) — una especificació basada en Markdown llegible tant per humans com per màquines. Pots incloure scripts, plantilles i exemples al costat del `SKILL.md`.

## Valor Pràctic

El poder real no està en les característiques individuals — sinó en la combinació de skills compartits per l'equip (via `.github/skills/`) i skills personals (via `~/.agents/skills/`). Els skills de l'equip codifiquen com fa les coses la teva organització. Els skills personals codifiquen com treballes tu específicament. L'agent obté tots dos contextos automàticament.

Per a les organitzacions que ja utilitzen Copilot intensivament, aquest és un pas significatiu cap a fer que l'eina sigui realment conscient de les convencions específiques de la teva base de codi en lloc de donar consells genèrics.

Post original: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
