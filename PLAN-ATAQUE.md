# Plan de ataque — Portafolio orientado a que te contraten como arquitecto

Rama: `feat/portafolio-contratacion` · Base: [AUDITORIA-UX.md](AUDITORIA-UX.md)
Flujo de trabajo: se edita `src/pagina.html`, se ejecuta `python tools/build.py` y se revisa en local antes de publicar. Un commit por paso. Nada se publica en Vercel sin tu visto bueno.

**Objetivo único:** que un reclutador, constructora o cliente entienda en 10 segundos quién eres, vea prueba de que cumples y te pueda contactar con un clic.
**Métrica de éxito:** contacto encontrado en <10 s, contacto por WhatsApp/correo/teléfono a un toque, lectura cómoda en móvil, Lighthouse accesibilidad ≥ 95.

## Fase 1 — Conversión (contacto y mensaje) · prioridad máxima
- [x] 1.1 Contacto accionable: `mailto:`, `tel:`, WhatsApp y LinkedIn como enlaces reales; "Copiar" queda como secundario.
- [x] 1.2 Botón "Contactar" fijo en la cabecera, siempre visible, junto a "DEMOS / CÓDIGO".
- [x] 1.3 CV en PDF descargable (necesito tu PDF o los datos para generarlo).
- [x] 1.4 Frase de valor en la portada: qué resuelves y para quién (propongo 2–3 opciones y eliges).
- [x] 1.5 Verificar en el sitio local que todos los enlaces abren bien.

## Fase 2 — Legibilidad y accesibilidad básica
- [x] 2.1 Texto útil ≥ 13–14 px (hoy 51 nodos < 12 px); 11–12 px solo en decoración.
- [x] 2.2 Gris secundario más claro (de `#888` a ≈`#A8A8A8`) y menos mayúsculas en frases largas.
- [x] 2.3 Objetivos táctiles ≥ 44 px (menú, pestañas, "Probar", selectores de medidas).
- [x] 2.4 Enlace "saltar al contenido" y `noscript` con nombre, rol y contacto.
- [x] 2.5 Un solo color de acento para acciones primarias (CTA), el resto neutro.

## Fase 3 — Prueba de que cumples (contenido)
- [x] 3.1 Plantilla de caso de estudio por obra: problema → rol → proceso → resultado → 2–3 cifras reales.
- [ ] 3.2 Franja de confianza: años, empresas, formación/certificaciones, software (necesito tus datos reales).
- [ ] 3.3 Testimonio o carta de recomendación (solo si tienes y puedes publicarla).
- [x] 3.4 Decidir el papel del Dashboard Metric.arq: demostración de habilidad, no producto en competencia con el contacto.

## Fase 4 — Navegación y descubrimiento
- [x] 4.1 Menú persistente con nombres de las 4 obras + Contacto (sin depender solo del gesto horizontal).
- [ ] 4.2 Probar teclado (Tab, flechas) y orden de foco; anuncios al cambiar de pantalla.
- [ ] 4.3 Revisión móvil real en teléfono (390 px) y ajustes.

## Fase 5 — SEO y compartir
- [x] 5.1 Favicon + `apple-touch-icon`.
- [x] 5.2 `robots.txt`, `sitemap.xml`, `canonical`.
- [x] 5.3 Datos estructurados (`Person` + `ProfessionalService`) con "arquitecto en Morelia".
- [ ] 5.4 Contenido esencial en HTML estático (indexable sin JavaScript).

## Fase 6 — Rendimiento y seguridad
- [ ] 6.1 Imágenes a WebP/AVIF con `srcset`.
- [ ] 6.2 Three.js solo al abrir el visor y versión actualizada; panoramas 360° bajo demanda.
- [ ] 6.3 `Content-Security-Policy`, `Permissions-Policy` y SRI en scripts externos.
- [ ] 6.4 Limpiar archivos de respaldo (`src/pagina.antes_dashboard.html`) si ya no sirven.

## Fase 7 — Validación
- [ ] 7.1 Lighthouse y axe antes/después; capturas comparativas.
- [ ] 7.2 Prueba con 3–5 personas: ¿entienden qué haces? ¿encuentran el contacto?
- [ ] 7.3 Publicar en Vercel con tu aprobación.

## Datos que necesito de ti (bloquean pasos)
| Dato | Paso |
|---|---|
| Número de WhatsApp (¿el mismo teléfono +52 351 202 5030?) y enlace a LinkedIn | 1.1 |
| CV en PDF (o confirmar que lo generamos) | 1.3 |
| Años de experiencia, empresas donde trabajaste, formación y certificaciones | 3.2 |
| Cifras reales por obra (m², toneladas, plazos, ahorros) que se puedan publicar | 3.1 |
| Testimonios publicables | 3.3 |

## Orden de ejecución
Fase 1 → 2 → 3 → 4 → 5 → 6 → 7. Las fases 1 y 2 no dependen de datos tuyos (salvo WhatsApp/LinkedIn), así que arrancan de inmediato.

## Fase 8 — Correcciones del dashboard (de AUDITORIA-DASHBOARD.md)
- [ ] 8.1 U1/L2: mostrar presupuesto ejercido y % en la vista 4D móvil; textos mínimos de 11–12 px y menos marcas de semana.
- [ ] 8.2 P1: quitar la descarga duplicada de `pano-sala.jpg` (con y sin `?v=`).
- [ ] 8.3 A1/A2: `<main>`, enlace "saltar al contenido" y `tabindex`/`role`/`aria-label` en `#v-home` y `#v-panel`.
- [ ] 8.4 A3: objetivos táctiles ≥ 44 px (cerrar, Planta baja/Tapanco, modos 4D móvil, barra de avance).
- [ ] 8.5 A4/U2: botón de ventanal con nombre fijo + `aria-pressed`, fuera del centro del modelo en móvil.
- [ ] 8.6 U3: pista de manipulación del modelo (arrastrar/pellizcar).
- [ ] 8.7 U4/U8/A5: splash legible (velo o entrada automática) y botón de pausa del hero.
- [ ] 8.8 L1/L3/U5/U7: etiquetas ≥ 12 px, gris `#A8A8A8`, cifra de presupuesto con aire, aviso "datos de ejemplo" legible.
- [ ] 8.9 T1/T2: favicon y SRI de Pannellum.
- [ ] 8.10 P2/P3: panorámicas a WebP/AVIF y carga diferida; medir con Lighthouse antes y después.
- [ ] 8.11 Revisar vistas no cubiertas (2D, 3D, 5D, 360°, renders, contacto) con teclado y lector de pantalla.

## Fase 9 — Reestructura del dashboard con objetivo claro
- [x] 9.1 Cuestionario de objetivo, público y mensaje (en curso).
- [x] 9.2 Definir jerarquía: qué se ve primero, qué es secundario, qué se oculta.
- [ ] 9.3 Nueva portada/inicio con propuesta clara y una sola acción principal.
- [ ] 9.4 Reordenar o fusionar secciones (2D/3D/4D/5D/360°/renders) según el objetivo.
- [ ] 9.5 Pruebas en escritorio y móvil, correcciones de la Fase 8 integradas, publicación con tu visto bueno.
