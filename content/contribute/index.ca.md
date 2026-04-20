---
title: "Escriu per a The .NET Blog"
description: "Comparteix el teu coneixement amb la comunitat .NET. Aprèn com unir-te com a autor i enviar la teva primera publicació."
---

The .NET Blog és una publicació impulsada per la comunitat on els desenvolupadors comparteixen idees, tutorials i històries sobre .NET, Azure, IA i desenvolupament cloud-native. **Donem la benvinguda a les contribucions de desenvolupadors de tots els nivells** — tant si estàs escrivint la teva primera entrada tècnica com si ja ets un ponent veterà.

## Com unir-te

Tot viu a GitHub i segueix un flux de treball basat en pull requests. Així és com pots començar:

### 1. Fes un fork del repositori

Ves a [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) i fes-ne un fork al teu compte de GitHub.

### 2. Crea el teu perfil d'autor

Si aquesta és la teva primera contribució, afegeix-te com a autor creant una carpeta a `content/authors/el-teu-usuari/` amb un fitxer `index.md`:

```yaml
---
title: "El teu nom"
id: "el-teu-usuari"
role: "El teu càrrec o títol"
bio: "Una breu biografia sobre tu."
avatar: "/img/authors/el-teu-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/el-teu-usuari"
  - platform: "Twitter"
    url: "https://x.com/el-teu-usuari"
---
```

Afegeix la imatge del teu avatar (quadrada, com a mínim 200×200px) a `static/img/authors/`.

### 3. Escriu la teva publicació

Crea una carpeta nova a `content/posts/el-teu-usuari/el-teu-article/` i afegeix-hi un fitxer `index.md`:

```yaml
---
title: "Títol de la teva publicació"
date: 2025-01-01
author: "el-teu-usuari"
description: "Una descripció d'una sola frase de la teva publicació."
tags: ["dotnet", "azure"]
---

El contingut de la teva publicació en Markdown...
```

### 4. Obre un pull request

Puja els teus canvis al teu fork i obre un pull request contra la branca `main`. El nostre equip el revisarà i et donarà feedback en pocs dies.

## El que busquem

- **Tutorials** — guies pas a pas sobre .NET, Azure, IA, Blazor, Aspire i més
- **Anàlisis en profunditat** — exploracions detallades d'una tecnologia, patró o arquitectura
- **Històries de la comunitat** — la teva experiència construint amb .NET en producció
- **Resums d'esdeveniments** — resum de conferències, trobades o webinars

## Directrius

- El contingut ha de ser tècnic i rellevant per a l'ecosistema .NET
- Els exemples de codi han de ser correctes i provats en un projecte real
- Inclou una descripció significativa i almenys una etiqueta rellevant
- Les publicacions es tradueixen automàticament a tots els idiomes admesos

## Contacta amb nosaltres

Obre un issue a [GitHub](https://github.com/thedotnetblog/blog/issues) o escriu-nos a [X / Twitter](https://x.com/thedotnetblog). Ens encantaria comptar amb tu a la comunitat!
