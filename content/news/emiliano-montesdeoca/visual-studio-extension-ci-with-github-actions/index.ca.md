---
title: "Els Equips d'Extensions de Visual Studio Haurien de Deixar de Publicar per Hàbit i Començar a Publicar per Pipeline"
date: 2026-07-23
author: "Emiliano Montesdeoca"
description: "Un flux de GitHub Actions repetible per al versionat i publicació de VSIX ara és prou simple que els passos manuals de publicació són difícils de justificar."
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Font original: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Si manteniu extensions de Visual Studio i encara feu parts significatives del llançament manualment, aquest és el vostre senyal per modernitzar-vos.

El flux de treball mostrat en aquest article és intencionadament pràctic: segellar versió, compilar, publicar artifacts de prova a una galeria, després publicar bits estables al Marketplace. Sense cerimònia pesada de plataforma, només comportament de llançament determinista.

El que més m'agrada és que el versionat es tracta com a estat del pipeline, no com un element de llista de verificació pre-llançament. Aquesta decisió elimina un nombre sorprenent d'errors: metadades desajustades, versions d'assembly obsoletes i notes de llançament inconsistents.

La divisió entre la publicació a galeria i la publicació a Marketplace també és operativament madura. Els equips necessiten un lloc per a compilacions de validació ràpides que no portin la semàntica de llançament oficial. Empènyer-ho tot directament al Marketplace és d'alta fricció i fomenta dreceres arriscades.

Un patró de llançament fort per als equips d'extensions és:

En pull requests i commits a main, produïu artifacts VSIX de CI i publiqueu-los a la galeria per a provadors.

En llançaments etiquetats, publiqueu paquets signats i validats al Marketplace.

Mantingueu la gestió de tokens al mínim amb secrets dedicats i àmbits de privilegi mínim.

La meva opinió: els ecosistemes d'extensions van endarrerits respecte als ecosistemes d'aplicacions en disciplina de CI perquè els equips petits assumeixen que els fluxos de treball manuals són gestionables. Ho són fins que no ho són. Un pedaç precipitat, un paquet trencat, una actualització de manifest oblidada, i la confiança cau.

Aquestes accions reutilitzables són útils perquè codifiquen la lògica de llançament repetida una vegada i permeten als equips centrar-se en la qualitat de l'extensió en lloc de la mecànica d'empaquetament.

Encara es requereix judici d'enginyeria. Hauríeu de posar comporta a la publicació al Marketplace darrere de comprovacions de qualitat, i hauríeu de tractar els manifests de publicació com a artifacts de llançament auditats. Però la complexitat del pipeline de base és ara prou baixa que els llançaments només manuals són sobretot deute tècnic.

Si dirigiu el desenvolupament d'extensions, estandarditzeu això ara entre repositoris. Obtindreu millor traçabilitat, incorporació més fàcil i menys colls d'ampolla de llançament d'una sola persona.

Desplegament suggerit:

Comenceu amb compilació més publicació a galeria per a una extensió.

Introduïu el segellat de versió després de validar les vostres convencions de manifest-font.

Afegiu la publicació al Marketplace només després que la gestió de secrets i les comportes de llançament estiguin al seu lloc.

Això no va de perseguir la moda DevOps. Va de fiabilitat per a les persones que instal·len les vostres eines i esperen que les actualitzacions funcionin.

Els ecosistemes d'extensions estables es construeixen de la mateixa manera que les aplicacions estables: amb automatització avorrida i repetible que elimina les suposicions humanes.