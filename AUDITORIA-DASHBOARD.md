# Auditoría UX/UI — Dashboard Metric.arq (Loft 6 × 15)

Fecha: 2026-10-21 · Archivo: `dashboard/index.html` (183 KB) + `dashboard/modelo.html` (746 KB, visor 3D) + `dashboard/datos.js`
Sitio: https://arq-carlos-espinoza.vercel.app/dashboard/ (revisado en local, mismo código)

## 0. Cómo se hizo y qué NO cubre
- **Hecho:** lectura del código; mediciones con JavaScript y capturas en escritorio (1440 × 900) y móvil (390 × 844) de la portada (splash), el inicio y la vista 4D; conteo de peticiones y peso de la primera carga; revisión de consola.
- **No hecho:** recorrido completo de cada vista (2D planos, 3D, 5D costos, 360°, renders, contacto), prueba con teclado real y lector de pantalla, verificación de contraste con herramienta (solo estimé con los colores del CSS), Lighthouse/axe, conexión lenta, Safari/Firefox, uso de los controles táctiles en un teléfono real. Lo que dependa de eso está marcado como "por verificar".
- Severidad: **Alta** (afecta la lectura de datos clave o el acceso) · **Media** (fricción notable) · **Baja** (pulido).

## 1. Resumen
El dashboard es la pieza técnica más sólida del portafolio: una portada cinematográfica, un inicio con 6 cifras clave, una vista 4D donde se ve el modelo, el diagrama de Gantt y el costo avanzando por semana, y un menú claro de 7 secciones (2D, 3D, 4D, 5D, 360°, renders, contacto). Está en español, etiquetado como "datos de ejemplo", sin desbordes horizontales en móvil y con las imágenes con texto alternativo.

Lo más importante a corregir:
1. **En móvil la vista 4D no muestra el presupuesto ejercido ni el porcentaje**, que sí aparecen en escritorio. Es el dato central de esa pantalla.
2. **Textos demasiado pequeños:** en 4D móvil, 22 elementos de texto miden menos de 11 px y el mínimo es 8 px.
3. **La misma panorámica se descarga dos veces** (`pano-sala.jpg?v=11` y `pano-sala.jpg`, 1.2 MB cada una), y la primera carga pesa 4.4 MB en 31 peticiones.
4. **Teclado y lectores de pantalla:** sin zona `main`, sin enlace "saltar al contenido" y con contenedores de scroll sin `tabindex`.
5. **Botón "Cerrar/Abrir ventanal"** cambia de texto y además usa `aria-pressed`, lo que confunde a los lectores de pantalla; en móvil flota sobre el modelo.

## 2. Qué funciona bien
- **Jerarquía:** título enorme, una frase, tres acciones (Recorrido 360°, Ver planos 2D, Obra 4D) y una tira de cifras (52 m², 2 niveles, 8 recintos, 6 redes, 26 semanas, $506,707).
- **Vista 4D:** muy legible; el control de semanas, el Gantt con el marcador "HOY" y el presupuesto avanzando enseñan el valor de BIM de forma inmediata. En móvil el Gantt cabe y se entiende.
- **Navegación:** menú lateral con 7 secciones, selector de vista arriba a la derecha, botón de pantalla completa y botón para volver al portafolio.
- **Accesibilidad base:** `lang="es"`, un solo `h1`, 40 `aria-label`, 32 `aria-pressed`, 17 `aria-current`, 16 imágenes y todas con `alt`, el título de la página cambia por vista ("4D · Obra · Loft 6 × 15"), `:focus-visible` definido y reglas para `prefers-reduced-motion`.
- **Honestidad del contenido:** "presupuesto de ejemplo", "semana · ejemplo", "datos de ejemplo" visibles.
- **Móvil:** sin desbordes horizontales (ancho de página 390 = ancho de pantalla) en portada, inicio y 4D.
- **Rendimiento parcial:** el visor 3D se carga en un `iframe` diferido (`loading="lazy"`) y hay miniaturas `t-*.jpg`.

## 3. Hallazgos

### 3.1 UX y contenido
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| U1 | En móvil (390 px) la tarjeta de 4D no muestra "Presupuesto ejercido" ni el porcentaje (en escritorio: $326,133 y 64 %) | Alta | Mostrar el total y el % en una línea compacta sobre el Gantt, o en la cabecera de la tarjeta |
| U2 | "Cerrar ventanal / Abrir ventanal" flota en el centro del modelo en móvil y tapa parte de la maqueta; en escritorio queda pegado bajo las pestañas | Media | Moverlo a la barra de modos o a un menú de ajustes; nombre fijo: "Ventanal" |
| U3 | No vi ninguna indicación de cómo manipular el modelo (arrastrar para girar, pellizcar para acercar) | Media | Pista breve de 3 s la primera vez, con ícono |
| U4 | La portada (splash) obliga a pulsar "Entrar" antes de ver contenido; el párrafo cae sobre ventanas iluminadas de la foto y pierde contraste | Media | Entrar automático tras 2–3 s o poner el texto sobre un velo; subir el tamaño del botón |
| U5 | La cifra "$506,707" toca el borde derecho de la tira de cifras en 1440 px | Baja | Más espacio interno o reducir el tamaño de la cifra a 28 px |
| U6 | "Volver al portafolio" es solo una flecha (con `aria-label`) | Baja | Añadir el texto "Portafolio" en escritorio |
| U7 | El aviso "datos de ejemplo" en la portada es el texto más pequeño de la pantalla (10–11 px) | Baja | Subirlo a 12–13 px, es un dato de honestidad importante |
| U8 | El hero cambia de imagen automáticamente cada pocos segundos sin botón de pausa | Media | Botón "Pausar" y detener al enfocar o pasar el cursor |

### 3.2 Legibilidad
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| L1 | Inicio en escritorio: 21 de 43 textos < 12 px, 6 < 11 px; mínimo 10.5 px | Media | Piso de 12 px para etiquetas y 13–14 px para texto de lectura |
| L2 | Vista 4D en móvil: 22 textos < 11 px, mínimo 8 px (marcas de semana, "SEMANA · EJEMPLO", importes) | Alta | Piso de 11–12 px; mostrar menos marcas de semana (1, 10, 20, 26) |
| L3 | Colores: `--muted:#8a8a8a` sobre `#0D0D0D` ≈ 5.6:1 (pasa AA para texto normal) pero a 8–10 px y sobre fotos no es fiable | Media | Subir a `#A8A8A8` y poner velo bajo texto sobre imagen (por verificar con herramienta) |
| L4 | Uso masivo de mayúsculas con espaciado ancho en etiquetas | Baja | Reservar mayúsculas para etiquetas cortas |

### 3.3 Accesibilidad (WCAG 2.2 AA, revisión parcial)
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| A1 | Sin `<main>` ni enlace "saltar al contenido" | Media | Marcar el contenedor principal y añadir el salto |
| A2 | `#v-home` y `#v-panel` (contenedores con scroll interno) sin `tabindex` ni `role` | Media | `tabindex="0"`, `role="region"` y `aria-label`; probar flechas y AvPág |
| A3 | Objetivos táctiles < 44 px: cerrar (40×40), pestañas "Planta baja / Tapanco" (33 px de alto), modos de 4D en móvil (40 px), "Cerrar ventanal" (42 px) y la barra de avance (3 px de alto en la medición) | Media | Mínimo 44 × 44, y un área táctil de 44 px alrededor del control de la barra |
| A4 | Botón de ventanal con texto cambiante y `aria-pressed` a la vez | Media | Un nombre fijo + `aria-pressed`, o texto cambiante sin `aria-pressed` |
| A5 | Hero con cambio automático sin pausa (WCAG 2.2.2) | Media | Ver U8 |
| A6 | Visor 3D y panorámicas 360°: sin alternativa por teclado ni descripción textual documentada | Media | Describir el contenido y ofrecer los renders como alternativa; por verificar el teclado |
| A7 | Panorámica y visor 3D dentro de `iframe`: título presente ("Modelo 3D del loft"), pero sin resumen de lo que muestra | Baja | Añadir `aria-describedby` con una frase |

### 3.4 Rendimiento
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| P1 | `pano-sala.jpg` se pide dos veces (con y sin `?v=11`), 1.2 MB cada vez | Alta | Unificar la URL (un solo parámetro de versión) |
| P2 | Primera carga: 31 peticiones, 4.4 MB; carpeta de imágenes 9.7 MB; panorámicas de 0.7–1.4 MB | Media | Panoramas a WebP/AVIF y carga solo al abrir 360°; `srcset` en renders |
| P3 | Evento `load` ≈ 11.7 s en la medición local (incluye iframe y panorámica) | Media | Diferir la panorámica y el iframe hasta su vista; medir con Lighthouse en producción |
| P4 | `setInterval` cada 120 ms para posicionar el cono y la miniatura | Baja | Pausar cuando la pestaña no está visible o usar `requestAnimationFrame` |
| P5 | `modelo.html` pesa 746 KB y repite Three.js r128 | Baja | Compartir librería con el portafolio y actualizar versión |

### 3.5 Técnico
| # | Hallazgo | Sev. | Recomendación |
|---|---|---|---|
| T1 | Error de consola: `favicon.ico` no encontrado | Baja | Añadir `<link rel="icon">` como en el portafolio |
| T2 | Pannellum 2.5.6 desde cdnjs sin SRI | Baja | Añadir `integrity` o alojarlo en el proyecto |
| T3 | Sin `canonical` ni datos estructurados propios en el dashboard (por verificar `<meta>`) | Baja | Añadir canonical y Open Graph propios |

## 4. Plan de acción
**Rápido (media jornada)**
1. U1/L2: mostrar el presupuesto y el % en móvil y subir los textos mínimos en 4D.
2. P1: quitar la descarga duplicada de `pano-sala.jpg`.
3. A1/A2/A3/A4: `main`, enlace de salto, `tabindex` en los contenedores, objetivos de 44 px y arreglar el botón de ventanal.
4. T1: favicon.

**Siguiente**
5. U2/U3/U4/U8: reubicar el ventanal, pista de manipulación, contraste del splash y pausa del hero.
6. L1/L3/U5/U7: tamaños y contraste de etiquetas.

**Después**
7. P2/P3: WebP/AVIF y carga diferida de panorámicas; medir con Lighthouse antes/después.
8. Probar teclado, lector de pantalla y teléfono real; recorrer 2D, 3D, 5D, 360° y renders (no revisados aquí).

## 5. Preguntas abiertas
- ¿Quieres que el splash siga siendo una pantalla de entrada o prefieres que se abra directo en el inicio?
- ¿El dashboard debe ser un demostrador técnico para reclutadores (mensaje breve y datos claros) o un producto para clientes (más funciones)?
