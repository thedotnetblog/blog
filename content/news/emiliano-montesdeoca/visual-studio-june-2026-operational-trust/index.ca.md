---
title: "Actualització de Visual Studio de Juny: La Visibilitat d'Ús i la Confiança MCP Són les Funcions que Més Importen"
date: 2026-07-24
author: "Emiliano Montesdeoca"
description: "Les parts més importants d'aquest llançament no són cosmètiques; milloren la governança i la confiança en els fluxos de treball assistits per IA."
tags:
  - visual-studio
  - github-copilot
  - mcp
  - cplusplus
  - developer-experience
---

Font original: [Visual Studio June Update – Track Your Usage, Trust Your Tools](https://devblogs.microsoft.com/visualstudio/visual-studio-june-update-track-your-usage-trust-your-tools/)

Aquest llançament de Visual Studio té moltes addicions agradables de qualitat de vida, però dues actualitzacions destaquen per sobre de la resta per als equips seriosos: la transparència d'ús de Copilot i la validació de confiança MCP.

A mesura que el desenvolupament assistit per IA canvia a facturació basada en ús, la visibilitat ja no és una mètrica de conveniència. És un requisit de planificació. Les finestres d'ús en temps real i les alertes de llindar ajuden els equips a evitar pics de cost sorpresa i crear normes d'ús més saludables. Sense aquesta visibilitat, les discussions sobre guanys de productivitat es converteixen ràpidament en suposicions.

El flux de validació de confiança MCP és encara més important estratègicament. Els ecosistemes d'eines s'estan tornant dinàmics, i els sistemes dinàmics necessiten límits de confiança explícits. Comparar la configuració d'inici i les empremtes de capacitat contra línies base de confiança és exactament la postura predeterminada correcta.

La meva opinió forta: tot IDE integrat amb IA hauria de fer això per defecte. La deriva silenciosa de capacitat als servidors d'eines és un risc inacceptable per a entorns empresarials.

L'agent de modernització de C++ GA per a actualitzacions de MSVC és un altre guany pràctic. El treball d'actualització normalment s'ajorna perquè és tediós i arriscat. Tenir camins guiats i automatitzats dins de l'IDE redueix la barrera per mantenir-se al dia, especialment per a bases de codi grans i heretades.

Les suggeriments d'edició de llarga distància són una bona millora de productivitat, però es tracten millor com a acceleració opcional. Les funcions de confiança i govern haurien d'estar habilitades i enteses primer; les funcions de conveniència poden seguir.

Recomanacions pràctiques per als equips que implementin aquest llançament:

Activeu les alertes d'ús de Copilot amb llindars alineats amb la propietat pressupostària interna.

Formeu els desenvolupadors sobre les indicacions de confiança MCP perquè les aprovacions siguin intencionals, no clics habituals.

Proveu els fluxos de treball de l'agent de modernització en una solució C++ representativa abans del desplegament ampli.

Recolliu comentaris sobre les suggeriments de rang estès, però poseu comporta a l'activació predeterminada en l'acceptació mesurable.

El suport per a emojis de color és menor sobre el paper, però millora la llegibilitat en contextos de text mixt com xat, markdown i panells de sortida. El poliment UX petit sí que es nota quan s'utilitza diàriament.

En general, aquest llançament reflecteix una filosofia d'eines que madura: l'assistència d'IA ja no és només de velocitat de generació. És de control, responsabilitat i confiança en el que s'executa dins del vostre entorn de desenvolupament.

Si la vostra organització està estandarditzant en fluxos de treball de Visual Studio millorats amb IA, prioritzeu les funcions de confiança operativa primer. Són la base que permet que la resta de l'stack de productivitat escali de manera segura.