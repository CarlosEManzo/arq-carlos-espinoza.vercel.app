# Portafolio · Arq. Carlos Francisco Espinoza Manzo

Sitio estático (HTML + CSS + JS, sin build en el servidor). Diseño «Minimalismo monolítico»: recorrido horizontal por cuatro obras, monografías con información, maqueta 3D (Three.js) y planos, y un panel DEMOS / CÓDIGO con una calculadora de instalaciones.

## Estructura

| Ruta | Qué es |
|---|---|
| `src/pagina.html` | Fuente de la página (estilos, contenido y scripts). Aquí se edita. |
| `tools/build.py` | Genera `index.html` (cabecera, metadatos para compartir) y revisa que estén todas las fotos. |
| `index.html` | Página final que se publica. No se edita a mano. |
| `photos/` | Fotos usadas (`photos/t/` son las miniaturas). |
| `og.jpg` | Imagen que se ve al compartir el enlace. |
| `vercel.json` | Cabeceras de seguridad y caché. |

## Editar y publicar

```bash
python tools/build.py          # regenera index.html
npx vercel --prod              # publica en Vercel
```

`.vercelignore` deja fuera `src/` y `tools/` del despliegue.
