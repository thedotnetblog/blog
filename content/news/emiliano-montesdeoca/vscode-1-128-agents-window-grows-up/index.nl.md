---
title: "VS Code 1.128 Zet Duidelijk In: Het Agents Window Wordt Het Nieuwe Werkoppervlak"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 verandert agentworkflows van noviteit naar dagelijkse ergonomie met multi-chat sessies, GA vision-ondersteuning en diepere host/session-controles."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 is een betekenisvolle release, niet vanwege één killerfeature, maar omdat meerdere wijzigingen rond één richting samenkomen: agent-first ontwikkeling in de editor wordt gestructureerd, parallel en operationeel beheersbaar.

Originele bron: https://code.visualstudio.com/updates/v1_128

De blikvanger is de rijkere multi-chat functionaliteit in agent host sessies, inclusief peer chats, forks en gelijktijdige beurten onder één bovenliggende sessie. Dit is precies wat ervaren ontwikkelaars nodig hebben bij het verkennen van alternatieve implementaties of het splitsen van taken over validatiepaden. Het weerspiegelt echt engineeringwerk, dat zelden lineair is.

Mijn mening: dit is de eerste VS Code-release waarin het Agents Window minder aanvoelt als een chatpaneel en meer als een orchestration-oppervlak voor de werkruimte.

Snelle chats zonder geselecteerde werkruimte zijn ook belangrijker dan ze lijken. Ze verlagen de drempel voor conceptuele of architectuurvragen terwijl projectsessies apart blijven. Die scheiding kan rommel verminderen en contextintegriteit behouden voor code-wijzigende workflows.

Copilot Vision dat GA bereikt is een ander omslagpunt. Zodra afbeeldingen en PDF's normale invoer voor chat zijn, worden documentatie-intensieve en UI-intensieve taken aanzienlijk vloeiender. Teams moeten nu denken aan multimodale context als standaardmogelijkheid, niet als geavanceerde toevoeging.

Er zijn ook praktische platformimplicaties. BYOK-ondersteuning in agent host scenario's, configureerbare model sampling parameters en utility model standaardwaarden duiden op groeiende volwassenheid voor enterprise model governance. Organisaties met strikte providervereisten kunnen nu gedrag vormgeven met fijnere controle in plaats van one-size-fits-all standaardwaarden.

Aanbevelingen voor teams die 1.128 adopteren:

Definieer conventies voor chatvertakking en naamgeving in multi-chat sessies zodat parallelle verkenning geen conversationele ruis wordt. Moedig ontwikkelaars aan om één chat voor implementatie en één voor tests of foutanalyse te gebruiken. Gebruik snelle chats doelbewust voor niet-repo-vragen.

Als je BYOK-endpoints gebruikt, stel dan basistemperatuur/top_p profielen per werklastklasse vast en documenteer uitzonderingen. Bepaal ook of utility flows op Copilot-geleverde of BYOK-modellen moeten draaien om onbedoelde stille gedragsverschillen te voorkomen.

Overweeg tot slot OS-level sneltoetsen strategisch. De mogelijkheid om VS Code-commando's systeembreed te activeren kan de flow voor power users verbeteren, maar onbeheerde sneltoetsuitbreiding kan consistentie binnen teams schaden.

VS Code 1.128 voegt niet alleen functies toe. Het verfijnt de mechanica van agentsamenwerking in echte ontwikkelloops. De editors die winnen in de volgende cyclus zullen degenen zijn die agentinteracties behandelen als first-class workflow-primitieven, niet als zijbalkexperimenten. Deze release laat zien dat VS Code die race begrijpt.