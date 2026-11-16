# Revisión editorial, clínica y visual

La voz y el encargo de storytelling pertenecen a [novaderm-copy](../../novaderm-copy/SKILL.md). Cárgala en el agente paralelo después de la elección de imagen; el principal evalúa el resultado. Si no está disponible, informa el fallo y aplica la guía de voz persistente de esa skill si se conserva; si faltan también las fuentes, usa solo los patrones documentados en el manual y registra la limitación, sin fingir una reproducción exacta.

`02_copy/copy.md` y `caption.txt` llevan solo el pie final publicable; la propuesta, alternativas y decisiones se guardan aparte. La copia exacta del caption debe coincidir con lo que se pega en Instagram. No pegar el informe interno ni la lista de claims.

## Afirmaciones médicas

Consultar fuentes primarias vigentes para mecanismos, eficacia, indicaciones, riesgos o recomendaciones. Registrar título, URL, fecha, afirmación y límites. Sin soporte, limitar mensaje y marcar pendiente. Productos: confirmar nombre y claims autorizados pertinentes; no inventar autorizaciones.

`04_revision/afirmaciones.json`:

```json
{
  "afirmaciones": [{"texto": "afirmación real", "fuente": "URL primaria real", "consultada": "fecha real", "alcance": "qué respalda y qué no"}],
  "revision_profesional": {"estado": "pendiente", "responsable": null, "fecha": null, "observaciones": ""}
}
```

Sin claims: lista vacía y justificar «no aplica». Un agente no es revisor médico. Con revisión pendiente se entrega PNG/maestro **para revisión**, sin llamarlo listo para publicar. No fabricar antes/después, histología, ampliaciones de lesiones inexistentes, resultados ni testimonios. Identificar bases sintéticas en procedencia; aclarar en pie si podrían confundirse con caso real.

Para registrar el handoff final, `revision_profesional` debe llevar `png_sha256` y `caption_sha256` de los archivos finales; estado `aprobada` con responsable/fecha reales si hay claims, o `no_aplica` con observaciones que lo justifiquen si no los hay. No completar automáticamente una aprobación clínica ni atribuírsela al agente. Los hashes vinculan la revisión a esa versión y evitan reutilizarla tras cambios.

## Controles de entrega

Guardar `04_revision/revision.md` con **cumple / corregir / pendiente / no aplica**, evidencia y acción; sin aprobar automáticamente. `check` solo verifica invariantes técnicos.

Después de abrir y revisar realmente la salida, el principal registra `04_revision/aprobacion-visual.json` con `estado: "aprobada"`, su responsable, fecha real, `png_sha256`, `caption_sha256` y observaciones. Es un registro de trabajo del principal, no una solicitud adicional de aprobación al usuario. Si algo falla, mantener pendiente y corregir. El helper `handoff` exige que las revisiones correspondan a los hashes actuales; ni autentica un revisor ni sustituye su evaluación.

| Control | Evidencia |
|---|---|
| Elección | Tres bases visibles, diferencias reales y mensaje del usuario. |
| Foto | Tema, textura, anatomía, derechos/consentimiento o condición sintética; sin alteración engañosa. |
| Composición | Ojos/lesión/producto despejados; logo discreto y adaptable. |
| Lectura | PNG al 100 % y 360 px abiertos; tildes, trazos finos, secundario legibles; aumentar/simplificar/mover si falla. |
| Contraste | Medir frente al fondo compuesto sin letras. Objetivo operativo ≥4,5:1 en secundario y ≥3:1 en título grande; no especificación de marca ni certificación normativa. Inspeccionar cada línea. |
| Logo | Reconstrucción declarada, alfa 0 en fondo/huecos, proporción intacta, opacidad interna/adicional registrada. |
| Capas | Grupos nombrados, texto nativo, foto/logo separados; editar texto y mover logo sin alterar foto; PNG coherente. |
| Producto | Alfa real y bordes revisados sobre claro/oscuro/ajedrezado; etiqueta/proporciones intactas. |
| Medicina | Fuentes por claim; responsable/fecha reales o pendiente explícito. |
| Formato | PNG RGB/RGBA sRGB con dimensiones acordadas; revisar recorte de perfil antes de usar sin asumir que Instagram no cambia. |
| Entrega | Maestro/layout/PNG/miniatura/copy/caption, fuente/licencia, procedencia y revisión visual; previsualización en Instagram solo si cuenta y contenido se verificaron. Sin publicación automática. |

`render-check.json` aporta límites y contraste conservador por caja; `fondo-sin-texto.png` permite inspección. Mínimo bajo exige mirar el punto concreto; media alta no aprueba la línea. Cajas incluyen huecos alrededor de letras: el mínimo es conservador. Repetir render tras mover texto o cambiar degradado.

## Feedback e iteración

Pedir feedback sobre foto, titular, composición y copy; no repetir datos conocidos. Guardar versión previa antes de reconstruir. Cambios invalidan revisión visual; claims nuevos invalidan revisión médica afectada. Base nueva exige elección/procedencia de nuevo. Mantener borrador mientras haya pendientes.
