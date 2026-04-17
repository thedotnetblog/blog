---
title: "Escribe para The .NET Blog"
description: "Comparte tu conocimiento con la comunidad .NET. Aprende cómo unirte como autor y enviar tu primer artículo."
---

The .NET Blog es una publicación impulsada por la comunidad donde los desarrolladores comparten ideas, tutoriales e historias sobre .NET, Azure, IA y desarrollo cloud-native. **Damos la bienvenida a contribuciones de desarrolladores de todos los niveles** — tanto si es tu primer artículo técnico como si eres un ponente con experiencia.

## Cómo Unirse

Todo vive en GitHub y sigue un flujo de trabajo de pull requests. Así puedes empezar:

### 1. Haz un Fork del Repositorio

Ve a [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) y haz un fork a tu cuenta de GitHub.

### 2. Crea tu Perfil de Autor

Si es tu primera contribución, añádete como autor creando una carpeta en `content/authors/tu-usuario/` con un archivo `index.md`:

```yaml
---
title: "Tu Nombre"
id: "tu-usuario"
role: "Tu cargo o título"
bio: "Una breve biografía sobre ti."
avatar: "/img/authors/tu-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/tu-usuario"
  - platform: "Twitter"
    url: "https://x.com/tu-usuario"
---
```

Añade tu imagen de avatar (cuadrada, mínimo 200×200px) en `static/img/authors/`.

### 3. Escribe tu Artículo

Crea una nueva carpeta en `content/posts/tu-usuario/slug-de-tu-articulo/` y añade un archivo `index.md`:

```yaml
---
title: "Título de tu Artículo"
date: 2025-01-01
author: "tu-usuario"
description: "Una descripción breve de tu artículo."
tags: ["dotnet", "azure"]
---

El contenido de tu artículo en Markdown...
```

### 4. Abre un Pull Request

Sube tus cambios a tu fork y abre un pull request contra la rama `main`. Nuestro equipo lo revisará y te dará feedback en unos días.

## Qué Buscamos

- **Tutoriales** — guías paso a paso sobre .NET, Azure, IA, Blazor, Aspire y más
- **Análisis profundos** — exploraciones detalladas de una tecnología, patrón o arquitectura
- **Historias de la comunidad** — tu experiencia construyendo con .NET en producción
- **Resúmenes de eventos** — resúmenes de conferencias, meetups o webinars

## Directrices

- El contenido debe ser técnico y relevante para el ecosistema .NET
- Los ejemplos de código deben ser precisos y probados en un proyecto real
- Incluye una descripción significativa y al menos una etiqueta relevante
- Los artículos se traducen automáticamente a todos los idiomas disponibles

## Contacto

Abre un issue en [GitHub](https://github.com/thedotnetblog/blog/issues) o contáctanos en [X / Twitter](https://x.com/thedotnetblog). ¡Nos encantaría tenerte en la comunidad!
