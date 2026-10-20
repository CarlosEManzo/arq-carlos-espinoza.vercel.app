# Auditoría UX/UI y funcional — Portafolio Arq. Carlos Francisco Espinoza Manzo

Fecha: 2026-10-20 · Sitio: https://arq-carlos-espinoza.vercel.app/ · Fuente: `src/pagina.html` (→ `tools/build.py` → `index.html`)

## 0. Cómo se hizo y qué NO cubre
- **Hecho:** lectura del código fuente, `vercel.json`, README y 15 commits recientes; mediciones en el sitio publicado en escritorio (1920 px) con JavaScript (carga, encabezados, objetivos táctiles, tamaños de texto, alt); captura de la portada; análisis de 8 perfiles de Instagram de UX/UI.
- **No hecho:** prueba real en móvil (la emulación no cambió el viewport), Lighthouse/axe, prueba con lector de pantalla, recorrido completo de cada pantalla con capturas, pruebas en Safari/Firefox. Los hallazgos de móvil salen del código (media queries y commits) y deben verificarse en un teléfono.
- Severidad: **Alta** = afecta contratación o accesibilidad básica · **Media** = fricción notable · **Baja** = pulido.

## 1. Resumen ejecutivo
El portafolio tiene una identidad visual muy propia y un nivel técnico poco común para un arquitecto: recorrido horizontal, visor 3D con Three.js, visor 360°, dashboard de obra y una calculadora de instalaciones. Es memorable y demuestra habilidad real. La carga medida es rápida (DOMContentLoaded ~0.7 s en la visita medida) y el HTML tiene `lang="es"`, un solo `h1`, `main`/`nav`, `alt` en todas las imágenes, metadatos para compartir y cabeceras de seguridad.

Los puntos débiles están en lo que decide que te contacten:
1. **Contacto débil y sin enlaces:** correo y teléfono son texto con botón "Copiar"; no hay `mailto:`, `tel:`, WhatsApp, LinkedIn ni CV descargable. Es el hallazgo de mayor impacto.
2. **Texto pequeño y de bajo peso:** 51 elementos de texto bajo 12 px; la fuente mono en 11–12 px, en mayúsculas y con gris `#888`, cuesta leer.
3. **Descubribilidad:** el contenido principal vive dentro de un recorrido horizontal con scroll bloqueado (`overflow:hidden`); quien no entiende el gesto abandona. Hay que probarlo con visitantes reales.
4. **Cero señales de confianza:** sin testimonios, cifras de resultado, logos de empresas, formación o certificaciones visibles en la ruta principal.
5. **SEO y descubrimiento mínimos:** sin favicon, `robots.txt`, `sitemap.xml` ni datos estructurados; contenido pintado por JavaScript.

## 2. Qué hacen bien los referentes de UX/UI (insumos)
Perfiles revisados (datos públicos de Instagram, oct. 2026):

| Perfil | Seguidores | Enfoque | Lección aplicable |
|---|---|---|---|
| @uxui_howard.le | 516 mil | Game UI y Web UI; "ayudó a 100k+ diseñadores" | Prueba social con una cifra clara en la bio; enlace único a su sitio |
| @janm_ux | 364 mil | "Mejora 1 % al día en UX/UI" | Promesa corta y concreta; recurso descargable (componentes de Figma) como imán |
| @uiuxdailytips | 301 mil | Tips diarios, 1,926 publicaciones | Constancia y formato repetible; destacadas por tema (Usabilidad, Clientes) |
| @filatov.design | 278 mil | UX/UI + IA, prompts | Mezcla de herramientas/IA con ejemplos; enlace a recurso propio |
| @uiux.build | 59.7 mil | Estudio de diseño web | Cada pieza educativa cierra con llamado a la acción ("DM PROJECT"); mostrar servicios y "250+ trabajos" |
| @feuxui | 8.2 mil | Series numeradas "30 tips de diseño" | Una idea por pieza, antes/después ✗/✓, gancho "comenta X y te envío la guía" |
| @jaypee_ux | 217 | "Portfolio Journey" | Narrar el proceso en público; bio honesta |
| @uxtips.la | 97 | Notas de aprendiz | Cuentas pequeñas: el formato importa más que el tamaño |

Patrones comunes: bio que dice **quién eres + qué ganas el visitante + un solo enlace**; **prueba social cuantificada**; **una idea por pieza**; **recurso gratuito como imán**; **llamado a la acción explícito al final**. Limitación: son bios y publicaciones sueltas, no un estudio estadístico; las cifras de engagement vienen de pocas muestras.

## 3. Auditoría de diseño visual
**Fortalezas**
- Sistema de color coherente: fondo `#0D0D0D`, tarjetas `#1A1A1A`, bordes `#2A2A2A`, texto `#E6E6E6`, acento blanco. Cumple de sobra la regla 60/30/10 con acento neutro.
- Par tipográfico Inter (títulos, muy grandes y con `clamp()`) + Space Mono (etiquetas técnicas): refuerza el tono de plano/ingeniería.
- Concepto "Minimalismo monolítico" bien ejecutado en la portada: nombre enorme, mucho aire, un solo foco.

**Hallazgos**
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| V1 | 51 nodos de texto <12 px; 46 reglas CSS a 11–12 px en mono y mayúsculas | Alta | Mínimo 13–14 px para texto útil; reservar 11–12 px para decoración. Menos mayúsculas en frases largas |
| V2 | Gris `#888` sobre `#0D0D0D` (~5.6:1, pasa AA) y sobre `#1A1A1A` (~4.9:1, justo) a tamaños chicos | Media | Subir a `#A0A0A0`–`#B0B0B0` para texto secundario pequeño |
| V3 | Acento 100 % blanco: no hay color que guíe al CTA | Media | Un solo color de acento (≈10 %) para acciones primarias (contacto, abrir dashboard) |
| V4 | Portada: textos auxiliares (esquinas) casi ilegibles a escala 0.5 | Media | Revisar jerarquía: solo 3 niveles (nombre, rol, acción) |
| V5 | Tres sistemas de interfaz a la vez (portafolio, dashboard, calculadora) con densidad distinta | Baja | Documentar tokens (espacios, radios, tamaños) y compartirlos |
| V6 | Sin favicon ni ícono de app | Baja | Añadir `favicon.ico`/SVG y `apple-touch-icon` |

## 4. Auditoría de experiencia de usuario
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| U1 | **Contacto no accionable:** correo/teléfono son `<span>` con "Copiar"; sin `mailto:`, `tel:`, WhatsApp ni LinkedIn | Alta | Convertir en enlaces reales + botón WhatsApp + LinkedIn + CV en PDF. Mantener "Copiar" como secundario |
| U2 | **Contacto solo al final** del recorrido (pantalla Z) | Alta | Botón "Contactar" fijo en la cabecera, junto a "DEMOS / CÓDIGO" |
| U3 | Navegación horizontal con `overflow:hidden` en body: el visitante no ve cuánto hay ni dónde está salvo la barra `04 / 04` | Media | Menú persistente con nombres de las 4 obras + Contacto; mantener puntos clicables (ya existen) |
| U4 | Sin propuesta de valor en la portada más allá de "Arquitecto · estructuras metálicas y coordinación BIM · Morelia" | Media | Una frase de resultado: qué problema resuelves y para quién (p. ej. "Coordino obra y BIM para que el proyecto llegue a tiempo y sin retrabajo") |
| U5 | Sin caso de estudio estructurado (problema → proceso → resultado → métricas) | Alta | Plantilla fija por obra, con 2–3 cifras (m², toneladas, semanas, ahorro) |
| U6 | Sin testimonios, empresas ni formación visibles | Media | Franja de confianza: empresas, años, certificaciones, software (Revit, etc.) |
| U7 | Dashboard y calculadora muestran "datos de ejemplo" | Baja | Está bien etiquetado; añadir un aviso breve de por qué existen y qué demuestran |
| U8 | Promoción cruzada Dashboard/portafolio puede diluir el mensaje principal (el commit log muestra varias idas y vueltas) | Media | Definir un solo objetivo de la página: ¿que te contraten como arquitecto o vender el dashboard? |
| U9 | Texto de pantalla final del recorrido eliminado y vuelto a añadir: señales de indecisión de IA | Baja | Congelar el flujo y probar con 3–5 personas |

## 5. Accesibilidad (WCAG 2.2 AA, revisión parcial)
Bien: `lang="es"`, 1 `h1` + 5 `h2`, `alt` en las 6 imágenes del DOM inicial, `aria-label` en secciones, `aria-hidden` en decoración (37), `aria-live` (5), `prefers-reduced-motion` respetado (4 reglas), `:focus-visible` presente, handlers de teclado (5).

| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| A1 | 16 de 58 elementos interactivos miden menos de 44 px (p. ej. "DEMOS / CÓDIGO" 165×40, pestañas 40 px de alto, "Probar" 68×36, "3 × 3 m" 77×38) | Media | Objetivo mínimo 44×44 (WCAG 2.2 pide 24×24 como mínimo y 44 como buena práctica en móvil) |
| A2 | Contenido principal en un carrusel horizontal gestionado con JS: riesgo para teclado y lectores de pantalla | Alta | Probar con Tab, flechas y NVDA; asegurar orden de foco y anuncios al cambiar de pantalla |
| A3 | Sin `noscript` y todo el contenido se genera con JS | Media | Mensaje `noscript` y contenido esencial (nombre, rol, contacto) en HTML estático |
| A4 | Sin enlace "saltar al contenido" | Baja | Añadirlo (útil con el menú fijo) |
| A5 | Texto <12 px y mayúsculas mono | Media | Ver V1 |
| A6 | Visor 3D y 360°: sin alternativa textual documentada | Media | Descripción corta y controles por teclado documentados |

## 6. Rendimiento
- Medido: DOMContentLoaded ≈ 717 ms, load ≈ 771 ms, 10 recursos, 1 canvas (visita con caché; no es Lighthouse).
- `index.html` pesa ~194 KB y `dashboard/index.html` ~183 KB; `dashboard/modelo.html` ~746 KB; panoramas 360° de hasta 1.4 MB y fotos de 0.4–1.1 MB; carpeta `photos/` ≈ 30 MB en total.
- Three.js r128 desde cdnjs (versión de 2021) en dos páginas; Pannellum 2.5.6 en el dashboard.

| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| P1 | Imágenes en JPG pesadas | Media | Convertir a WebP/AVIF con `srcset`; ya hay miniaturas `photos/t/` |
| P2 | Three.js 0.128 sin versión mínima moderna ni carga diferida | Media | Cargar solo al abrir el visor; actualizar versión o usar módulo |
| P3 | `loading="lazy"` solo en 2 sitios del HTML estático (el resto se pinta por JS) | Baja | Verificar que las imágenes inyectadas también lo usen |
| P4 | Panoramas 360° sin precarga controlada | Baja | Cargar al entrar en la pantalla, no antes |
| P5 | Caché de 1 año con `immutable` en fotos y frames | — | Correcto; si cambias una foto, cambia el nombre de archivo |

## 7. SEO y compartir
Bien: `title`, `description`, Open Graph y Twitter Card con imagen 1200×630, `theme-color`, `og:locale es_MX`.
Falta: favicon, `robots.txt`, `sitemap.xml`, `canonical`, datos estructurados (`Person` + `ProfessionalService`), contenido indexable sin JS. Para un arquitecto local, añade "arquitecto en Morelia" en `h1`/`h2` visible y una ficha de Google Business.

## 8. Seguridad y mantenimiento
- `vercel.json` incluye `X-Content-Type-Options`, `Referrer-Policy` y `X-Frame-Options`. Falta `Content-Security-Policy` y `Permissions-Policy`.
- Scripts externos (cdnjs, Google Fonts) sin `integrity` (SRI) en las etiquetas revisadas.
- El correo y teléfono aparecen en texto claro en el HTML: es un riesgo normal de spam. Si te preocupa, usa un formulario.
- Código fuente en un solo archivo de ~190 KB (`src/pagina.html`): difícil de mantener; separar CSS/JS en archivos.
- Existe `src/pagina.antes_dashboard.html` (respaldo) dentro del repositorio.

## 9. Funciones revisadas
| Función | Estado observado | Nota |
|---|---|---|
| Portada con nombre, rol y fondo animado | Funciona | Revisar legibilidad de textos pequeños |
| Recorrido horizontal por 4 obras | Funciona según commits recientes (flecha, puntos clicables, móvil) | Probar teclado y rueda del mouse |
| Monografías (Información) | Funciona | Falta formato de caso de estudio con métricas |
| Maqueta 3D (Three.js) | Funciona | Peso y carga diferida |
| Planos e instalaciones | Funciona | — |
| Calculadora de instalaciones | Funciona (botones "Probar", "Cómo funciona") | Objetivos táctiles <44 px |
| Dashboard Metric.arq (360°, 3D, calendario) | Funciona (datos de ejemplo) | Definir su papel frente al portafolio |
| Copiar correo/teléfono | Funciona | No hay enlace directo |
| Compartir en redes | Configurado | Verificar la tarjeta con el depurador de Facebook/LinkedIn |

No probé de forma manual cada interacción ni los flujos en móvil.

## 10. Plan de acción priorizado
**Semana 1 (alto impacto, poco esfuerzo)**
1. Contacto: `mailto:`, `tel:`, botón WhatsApp, LinkedIn y CV en PDF; botón "Contactar" fijo en la cabecera.
2. Subir tamaños: texto útil ≥13–14 px, objetivos táctiles ≥44 px, gris secundario más claro.
3. Frase de valor en la portada (qué haces y para quién).
4. Favicon, `robots.txt`, `sitemap.xml`, `noscript` y datos estructurados.

**Semana 2–3**
5. Plantilla de caso de estudio (problema, proceso, resultado, 2–3 cifras) para las 4 obras.
6. Franja de confianza: empresas, años, certificaciones, software, testimonio.
7. Menú persistente con nombres de obra; probar teclado y lector de pantalla.

**Mes 1–2**
8. Optimizar imágenes (WebP/AVIF), cargar Three.js solo bajo demanda, actualizar versión.
9. CSP y SRI; separar CSS/JS del HTML.
10. Prueba de usabilidad con 3–5 personas (¿entienden el gesto horizontal? ¿encuentran el contacto en <10 s?) y Lighthouse/axe para medir antes/después.

## 11. Preguntas abiertas para ti
- ¿El objetivo principal es que te contraten (empleo/freelance de arquitectura) o promocionar Metric.arq?
- ¿Quién es el visitante ideal (reclutador de constructora, cliente residencial, estudio BIM)?
- ¿Tienes cifras reales de obra y testimonios que se puedan publicar?
