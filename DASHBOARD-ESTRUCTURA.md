# Dashboard Metric.arq — nueva estructura (borrador para aprobar)

Base: cuestionario del 2026-10-21 + [AUDITORIA-DASHBOARD.md](AUDITORIA-DASHBOARD.md)

## 1. Objetivo, público, mensaje y acción
| Pregunta | Decisión |
|---|---|
| **Objetivo** | Vender un proyecto: mostrar el proyecto entero a inversionistas o compradores antes de construirlo |
| **Visitante** | Mixto: comprador (quiere ver y sentir el espacio) e inversionista (quiere saber cuánto y cuándo) |
| **Mensaje en 10 s** | «Veo el proyecto antes de construirlo» |
| **Única acción final** | «Pedir un tablero para su obra», por cotización en WhatsApp con mensaje prellenado, sin precios públicos |
| **Estructura** | Un solo recorrido guiado en scroll, una idea por pantalla |
| **Peso mayor** | Renders y recorrido 360° |
| **Datos para inversionistas** | Presupuesto por capítulo y total, y calendario por fases (siempre marcados "ejemplo"; no se inventan precios de venta ni retornos) |

## 2. Principios
1. **Una pantalla = una pregunta del visitante** y una sola acción posible.
2. **Primero lo emocional (ver), luego lo racional (entender), luego lo financiero (cuánto y cuándo), al final la acción.**
3. **Lo técnico se pliega:** planos 2D y modelo 3D quedan como apoyo ("Ver el detalle técnico"), no como secciones al mismo nivel.
4. **Honestidad:** "Datos de ejemplo" visible en cada cifra económica.
5. Las correcciones de la Fase 8 (accesibilidad, móvil, rendimiento) se integran desde el inicio.

## 3. Recorrido propuesto
| # | Pantalla | Pregunta que responde | Contenido (activos existentes) | Peso |
|---|---|---|---|---|
| 0 | **Portada** | ¿Qué es esto? | Render de fachada de noche; título «Ve tu proyecto antes de construirlo»; subtítulo «Loft 6 × 15 · ejemplo de tablero Metric.arq»; botón «Empezar» (o entrada automática) | Alto |
| 1 | **Míralo** | ¿Cómo se verá? | Galería de los 9 renders (fachada, sala, cocina, patio, tapanco, TV, café, medio baño) a pantalla completa, con pie descriptivo | Muy alto |
| 2 | **Recórrelo** | ¿Cómo se siente estar dentro? | Panorámicas 360° (cochera, sala, cocina, jardín, tapanco) con hotspots; pista «arrastra para mirar» | Muy alto |
| 3 | **Entiéndelo** | ¿Qué es exactamente? | Cifras clave: 52 m², 2 niveles, 8 recintos, 6 redes; maqueta 3D como una sola vista; «Ver planos 2D» plegado | Medio |
| 4 | **¿Cuánto?** | ¿Cuánto cuesta construirlo? | Presupuesto por capítulo y total ($506,707, **ejemplo**); gráfica simple de barras por capítulo | Medio |
| 5 | **¿Cuándo?** | ¿Cuánto tarda? | Calendario por 6 fases / 26 semanas con barra de avance (4D) y total ejercido (visible también en móvil) | Medio |
| 6 | **Pide tu tablero** | ¿Qué hago ahora? | Frase «Te armo un tablero como este para tu proyecto»; botón único «Pedir cotización por WhatsApp» con mensaje prellenado; enlaces secundarios al portafolio y CV | Alto |

**Se pliega o se baja de nivel:** planos 2D, modelo 3D completo, redes de instalaciones, panel de costos detallado, "Obra 4D" interactiva avanzada (queda como detalle dentro de «¿Cuándo?»).

## 4. Navegación
- Barra superior mínima: logo Metric.arq · puntos de progreso (7) · botón «Pedir tablero» (ámbar, siempre visible).
- Teclado: flechas y AvPág; `main` y enlace «saltar al contenido».
- Botón «Volver al portafolio» con texto.

## 5. Mensaje de WhatsApp (prellenado)
«Hola Carlos, vi el tablero Metric.arq del Loft 6×15 y quiero uno para mi proyecto. Tipo de proyecto: __ · Ubicación: __ · m² aproximados: __.»

## 6. Qué cambia respecto a hoy
| Hoy | Nueva versión |
|---|---|
| 7 secciones al mismo nivel (2D, 3D, 4D, 5D, 360°, renders, contacto) | 7 pasos con orden narrativo y peso distinto |
| Inicio con 6 cifras sin explicar para qué sirven | Cada cifra vive junto a la pregunta que responde |
| Contacto al final con WhatsApp, Llamar, Correo | Una sola acción: pedir cotización por WhatsApp |
| 4D y 5D como paneles técnicos | «Cuánto» y «cuándo» como respuestas simples; el detalle queda plegado |
| El visitante debe descubrir qué hacer | Una acción por pantalla y siempre un botón visible |

## 7. Criterios de éxito
- Un visitante nuevo dice qué es el dashboard después de 10 s (probar con 3–5 personas).
- La cifra de presupuesto y el calendario se leen en móvil sin zoom.
- Clic al botón de WhatsApp desde cualquier pantalla.
- Lighthouse accesibilidad ≥ 95 y primera carga < 2 MB (hoy 4.4 MB).

## 8. Plan de construcción
1. Crear la nueva versión en `dashboard/` conservando `modelo.html`, `datos.js` e imágenes; el archivo actual se respalda como `dashboard/index.anterior.html` (no se borra).
2. Portada, Míralo y Recórrelo (renders + 360°) con la carga diferida de panorámicas.
3. Entiéndelo, ¿Cuánto? y ¿Cuándo? con los datos de `datos.js`.
4. Pide tu tablero + barra superior.
5. Fase 8 integrada: accesibilidad, 44 px, textos ≥ 12 px, favicon, imágenes sin duplicar.
6. Pruebas en escritorio y móvil, capturas para tu revisión y publicación con tu sí.

## 9. Dudas que quedan
- ¿La portada mantiene «Entrar» o se abre directo en «Míralo»? (recomiendo directo)
- ¿Conservo «Loft 6 × 15» como ejemplo o lo cambio por un proyecto inmobiliario más grande (si tienes uno con renders)?
- ¿Precio de venta/renta y retorno: se omiten por ahora?
