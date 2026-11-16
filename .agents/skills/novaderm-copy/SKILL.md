---
name: novaderm-copy
description: Redactar storytelling, titulares y pies de Instagram en español con la voz editorial de Grupo Novaderm. Usar como apoyo de novaderm-instagram o para revisar su copy; no diseña, controla el navegador ni publica.
---

# Voz editorial de Grupo Novaderm

Skill de apoyo textual. En el flujo completo, el agente principal la carga en un agente de copy **después de la elección explícita de una de las tres imágenes base**, mientras prepara el diseño. El principal es el único responsable del navegador y de la carga en Instagram. Esta skill no abre sesiones, rellena formularios, sube archivos ni pulsa «Publicar».

Para separar contexto con `collaboration.spawn_agent`, el principal usa `fork_turns: "none"` y proporciona únicamente la ruta de esta skill, brief mínimo y carpeta de salida; el agente lee su guía editorial y no hereda el historial completo por defecto.

## Entradas mínimas

Recibe tema, objetivo, imagen base elegida (archivo o descripción), fuentes clínicas disponibles, CTA autorizado o preferencia de cierre y ruta del trabajo. Reutiliza público y restricciones del brief si existen. Si ya hay tema, no vuelvas a pedirlo. Si una ausencia cambia el mensaje, devuelve al principal la pregunta concreta; no envíes un segundo cuestionario al usuario.

Si falta el tema en un encargo exclusivamente textual, pide solo el tema. En el flujo de diseño, sin elección de base registrada no cierres el copy: informa al principal y conserva la pausa de [novaderm-instagram](../novaderm-instagram/SKILL.md). Si esa skill hermana no está disponible, realiza únicamente el encargo textual expresamente pedido y declara que no puedes verificar el estado de elección ni continuar el flujo visual. No simules una invocación o una elección.

## Redactar sin cargar contexto ajeno

Lee [voz-editorial.md](references/voz-editorial.md). Esa guía reúne las observaciones editoriales necesarias; no cargues el manual visual ni todas las portadas. No vuelvas a visitar Instagram en cada encargo: usa la evidencia congelada, salvo que el usuario pida actualizar la voz o aporte nuevas referencias.

1. Define una sola idea y el movimiento emocional adecuado: reconocimiento → comprensión → criterio individual → invitación. No conviertas cada tema en una venta ni inventes una historia de paciente.
2. Propón dos titulares distintos, breves y específicos, y recomienda uno según tema y base. Orientación: 2–9 palabras; no es una medida original. Añade secundario solo si aporta algo nuevo.
3. Escribe un pie original que desarrolle el titular con párrafos breves y lenguaje cotidiano. Adapta profundidad, cierre y emojis al objetivo; no copies el orden exacto ni frases distintivas de un post previo.
4. Identifica afirmaciones de titular, secundario y pie. Usa las fuentes clínicas suministradas o verifica fuentes primarias vigentes cuando haga falta. No atribuyas a la cuenta evidencia de eficacia. Con soporte insuficiente, limita o retira la afirmación y registra el pendiente; no inventes citas ni aprobación profesional.
5. Relee para evaluar voz, naturalidad, coherencia con imagen, precisión, CTA y ausencia de repetición. Ajusta antes de devolver la propuesta. No añadas fechas de publicación ni programación si no se han solicitado.

## Archivos de salida y devolución al principal

Dentro de `02_copy/` del trabajo indicado, entrega:

- `propuesta-agente.md`: dos titulares, recomendado y motivo, secundario opcional, intención narrativa y autoevaluación con **cumple / corregir / pendiente**. Explica los pendientes concretos, sin aprobar medicina.
- `copy.md`: **solo el pie propuesto para Instagram**, con sus saltos de línea y hashtags opcionales; sin encabezados de informe, alternativas, Markdown decorativo, notas internas ni marcadores por completar. El principal lo revisa antes de usarlo.
- `claims.json`: inventario de afirmaciones propuestas y revisión pendiente. El principal puede incorporarlo a `04_revision/afirmaciones.json` y actualizarlo si modifica el texto.

Esquema de `claims.json` (completar con contenido real; no usar una fuente ficticia):

```json
{
  "afirmaciones": [
    {
      "texto": "afirmación incluida en la propuesta",
      "ubicacion": "titular | secundario | pie",
      "fuentes": [{"titulo": "fuente primaria consultada", "url": "URL real", "consultada": "fecha real", "alcance": "qué respalda y qué no"}],
      "estado": "sustentada_pendiente_revision_profesional | pendiente_soporte",
      "accion": "revisión o cambio necesario"
    }
  ],
  "revision_profesional": {"estado": "pendiente", "responsable": null, "fecha": null},
  "notas": []
}
```

Si no hay afirmaciones clínicas, usa lista vacía, estado profesional `no_aplica` y justificación en notas. Una fuente no consultada no se registra como consultada. No rellenes responsable/fecha de aprobación con el nombre de un agente. Si la base es sintética y podría confundirse con un caso real, incorpora una aclaración adecuada en el pie y en las notas.

Devuelve al principal las rutas y un resumen de la recomendación y los pendientes. El principal evalúa y ajusta el resultado, registra su decisión y gestiona toda interacción con Instagram; el subagente no declara que el post ya está cargado o listo para publicar.

## Si no hay agentes paralelos

El principal puede leer esta skill y hacer una primera pasada de escritura y una segunda de evaluación, registrando `sequential-unavailable` y la causa real en el flujo principal. Debe informar que no hubo agente paralelo; no simular independencia ni sustituir revisión clínica. Reutiliza las mismas entradas y salidas, sin volver a preguntar datos conocidos.
