# Motor SVG y comandos

## Elección del formato

Maestro SVG nativo: nueve grupos `inkscape:groupmode="layer"`, fotos embebidas como imágenes, textos `<text>` editables e isotipo como rutas vectoriales anidadas. Se puede abrir en Inkscape u otro editor SVG que conserve texto/grupos. Un PDF, PNG o HTML por sí solo no garantiza capas editables. El HTML generado es una previsualización auxiliar.

El renderer usa Chromium a escala 1 y perfil sRGB; espera imagen y fuente antes de capturar. La fuente también se entrega como TTF con licencia porque algunos editores ignoran `@font-face` embebido. En ellos hay que habilitar/instalar la fuente de trabajo o elegir conscientemente una sustituta antes de editar; el paquete no la instala en el sistema. No convertir el único maestro a contornos: perdería edición de texto.

El motor mantiene los trazos del logo separados de la foto. La corrección de color es tinte opcional editable; el degradado de contraste es vectorial. No hay capas de ajuste propietarias de Photoshop. Formatos PSD/Canva requieren reconstrucción/importación y comprobación propia; no afirmar compatibilidad fiel sin probarla.

## Preparación del entorno

Python 3.11 o posterior. Desde la raíz del repositorio ejecutar `python setup.py` una sola vez. Para continuar en PowerShell, desde esa raíz:

```powershell
$projectRoot = Join-Path (Get-Location).Path 'Grupo Novaderm'
$skillRoot = Join-Path (Split-Path $projectRoot -Parent) '.agents/skills/novaderm-instagram'
$envRoot = Join-Path $projectRoot '.herramientas/novaderm-python'
$py = Join-Path $envRoot 'Scripts/python.exe'
$tool = Join-Path $skillRoot 'scripts/novaderm.py'
& $py $tool verify-package
```

Si el entorno ya tiene dependencias compatibles, reutilizarlo; no reinstalar en cada pieza. En macOS/Linux el ejecutable es `bin/python`. No llamar a la skill-creator ni instalar esta skill para crear publicaciones. Las únicas instalaciones descritas aquí son dependencias de Python y navegador, nunca la activación de la skill. El primer render puede requerir red para instalar Chromium. `render --browser RUTA` permite usar un Chromium/Chrome existente si no se puede descargar el navegador.

## Estado y comandos

`new` requiere solo tema; detecta el proyecto por su ubicación o acepta `--project`. No solicita fecha ni programa la publicación. La fecha opcional `--date` es únicamente metadato de creación para compatibilidad con trabajos anteriores. La ruta que imprime es `$job`, persistente y única. Reanudar con esa ruta, no crear otro trabajo si ya hay uno abierto.

```powershell
& $py $tool paths
& $py $tool new --project $projectRoot --topic 'TEMA REAL RECIBIDO'
```

El tema es un ejemplo de sintaxis; usar el recibido. No pedir fecha de publicación. `brief.json` guarda supuestos iniciales y se completa sin pedir datos innecesarios. `layout.json` empieza sin texto y se completa solo después de la elección. Estado: `awaiting_base_choice` → `base_selected` → `copy_reviewed` → `built_for_review` → `rendered_for_review`; luego `ready_for_user` solo si existe evidencia del compositor real y sus controles. El campo `instagram.status` registra además `awaiting_login`, `preparing`, `blocked` o `ready_for_user`. No significa publicado ni programado.

Para cada imagen real obtenida, guardar copia con procedencia. `--source` puede contener URL permanente, identificador de generación y prompt guardado, o referencia al archivo autorizado; `--rights` debe describir la autorización o el pendiente, no inventarla. Usar `--synthetic` solo si corresponde.

```powershell
& $py $tool option --job $job --id A --image $imageA --description 'Descripción específica del encuadre A' --source $sourceA --rights $rightsA --synthetic
# Repetir B y C con archivos y descripciones realmente distintos.
```

Se conserva original y una copia PNG normalizada sRGB; sin perfil de origen se registra la suposición sRGB. Se rechazan imágenes con píxeles idénticos, pero diferencias visuales, letras accidentales y derechos requieren juicio del agente. Mostrar los tres archivos antes de detenerse.

Después del mensaje de elección, y solo entonces:

```powershell
& $py $tool select --job $job --choice B --evidence 'Cita del mensaje real del usuario'
```

El script no puede verificar que un mensaje sea auténtico: el agente no debe inventarlo. Seleccionar nueva base archiva resultados previos e invalida copy/build/render. Agregar nuevas opciones no elige automáticamente ninguna.

Tras agente paralelo, evaluación y ajustes del principal:

```powershell
& $py $tool copy --job $job --file $copyFile --mode agent --evidence $agentId --review 'Evaluación concreta del principal y cambios realizados'
```

Fallback honesto: `--mode sequential-unavailable --evidence 'Causa real de indisponibilidad'`; conservar las dos pasadas. No usar fallback por comodidad cuando agentes están disponibles.

## Layout editable

Este es el esquema de un bloque, no una publicación de ejemplo. Coordenadas en píxeles del lienzo y `y` es línea base; saltos de línea explícitos. Escribir líneas reales del copy elegido. Separar context/title/subtitle en bloques propios.

```json
{
  "role": "title",
  "lines": ["Primera línea del titular", "Segunda línea"],
  "x": 90, "y": 700, "size": 92, "line_height": 92,
  "weight": 400, "anchor": "start", "color": "#FFFFFF"
}
```

Campos de `layout.json`:

| Campo | Uso |
|---|---|
| `width`, `height` | Dimensiones acordadas; iniciales 1080/1350. |
| `photo_align` | Una de xMin/xMid/xMax + YMin/YMid/YMax, como `xMaxYMid`; recorte `slice`, sin deformar. |
| `text` | Bloques con role `context`, `title`, `subtitle`; font-weight 300–700, anchor start/middle/end. |
| `color_adjust` | `null` o `{ "color":"#765344", "opacity":0.06 }`; propuesta opcional. |
| `contrast` | `null` o `{ "x":0,"y":600,"width":1080,"height":750,"top":0,"bottom":0.4 }`; gradiente negro vertical editable. Ajustar rectángulo y extremos. |
| `product` | `null` o `{ "file":"recursos/producto-recortado.png","x":650,"y":650,"width":200 }`; ruta dentro de trabajo, PNG con alfa 0 real; alto conserva proporción. |
| `protected` | Lista `{ "label":"zona clínica", "x":... ,"y":... ,"width":... ,"height":... }` de regiones que texto/logo no deben invadir. |
| `logo` | variant blanco/gris/color, x/y del viewport, width y opacity adicional 0–1. Inicial 109 de viewport, alfa extra 1. |
| `notes` | Decisiones aproximadas, referencia, recorte, color, motivo de escala/posición/alfa. |

El helper soporta los tres SVG suministrados. Un maestro oficial de otra geometría requiere adaptar en una copia la carga y revisar proporción/espacio del viewBox, sin sobrescribir originales ni fingir compatibilidad automática.

```powershell
& $py $tool build --job $job
& $py $tool render --job $job
& $py $tool check --job $job
```

Build rechaza ausencia de tres opciones/elección/copy revisado, y copia recursos. Archiva versiones previas antes de reconstruir; las revisiones deben repetirse. Cada cambio en layout o copy exige build/render nuevos; un SVG editado directamente puede renderizarse con `--accept-edited-svg` (conserva dimensiones/capas nativas; layout deja de reproducir esos cambios manuales). Documentar esos cambios y entregar el SVG como autoridad visual.

`render` genera PNG, miniatura y fondo sin letras para contraste; registra Chromium, límites reales de texto y advertencias. `check` comprueba capas, texto, recursos embebidos, hashes, dimensiones y coherencia de entrega. Un PASS técnico no valida composición/derechos/medicina. Hay que abrir imágenes y completar revisión.

## Organización y entrega

```text
Publicaciones/tema_id/
  brief.json, estado.json, layout.json
  01_bases/A/ ... B/ ... C/  (originales y copias normalizadas)
  02_copy/                  (propuesta, decisión, copy final)
  03_diseno/                (post.svg, preview.html, procedencia.json)
  04_revision/              (render-check, fondo, revisión, afirmaciones)
  05_entrega/               (post.svg, post.png, miniatura, layout, copy)
  recursos/                 (base, logo, producto si aplica, TTF, OFL)
  versiones/                (copias anteriores, sin sobrescribir)
```

Entregar carpeta de trabajo o ZIP que incluya `recursos` y `04_revision`, no solo 05_entrega. Puede mantenerse la base y los prompts dentro del trabajo interno si incluyen contenido privado; preparar una copia depurada para compartir y explicar qué se excluyó. No borrar originales del usuario. No hay comando de publicación. La skill de carga usa exclusivamente UI soportada y se detiene antes del control final.

## Prueba técnica reproducible

`python scripts/self_test.py --workspace RUTA_DE_TRABAJO` ejecuta el flujo en un proyecto aislado con fondos abstractos y texto «PRUEBA TÉCNICA», sin modelos de imagen, agentes, datos clínicos ni contenido publicable. Comprueba pausas técnicas, recursos reubicados, exportación/capas, edición de texto y movimiento de logo sin alterar la foto, alfa, contraste y versionado. Es una prueba de software, no un ejemplo de publicación ni una validación de estilo o médica. No ejecutarla dentro de la carpeta de publicaciones reales.


## Skills de apoyo y preparación de Instagram

`paths` imprime rutas detectadas de proyecto, Python persistente y skills hermanas. No modifica nada. Si se reubicó el paquete y falta el proyecto, usar `--project` o identificar la carpeta equivalente. La habilidad de copy y la de carga son carpetas hermanas de esta skill en `.agents/skills`.

`copy` mantiene `caption.txt` idéntico a `copy.md`; ambos deben contener solo el pie final sin Markdown de informe. `render` los copia a `05_entrega`. `check` verifica su correspondencia. El agente editorial guarda titulares y notas aparte.

Tras observar una pantalla real, registrar evidencia (este comando **no navega ni sube archivos**):

```powershell
& $py $tool handoff --job $job --status ready_for_user --account grupo_novaderm --evidence $observedEvidence --screenshot $screenshotPath --tab-id $tabId --content-verified
```

La bandera solo se marca tras comprobar en la UI imagen, caption y control de publicación visible sin pulsarlo, no al generar archivos. `ready_for_user` requiere exportación vigente, caption intacto, `revision.md`, revisión visual en `aprobacion-visual.json` y revisión clínica aprobada o no aplicable justificada en `afirmaciones.json`, cuenta objetivo exacta y captura real. Ambas revisiones llevan hashes del PNG/caption actuales. Una revisión profesional aprobada requiere responsable y fecha reales; «no_aplica» requiere lista vacía y justificación.

Para bloqueos reales, `handoff --status awaiting_login|preparing|blocked --account CUENTA_OBSERVADA --evidence DETALLE` registra el punto alcanzado sin declarar éxito. No conservar contraseñas, cookies, OTP ni datos privados en evidencia. `--tab-id` es una pista de reanudación, no una URL permanente ni prueba de borrador guardado. `select`, `copy`, `build` y `render` invalidan la preparación previa; volver a verificar/cargar cuando corresponda.

El runtime y Chromium se preparan una sola vez. Si `paths` encuentra el entorno de `.herramientas`, usarlo directamente. No reinstalar ni ejecutar self_test por post; esas pruebas son de mantenimiento del paquete.
