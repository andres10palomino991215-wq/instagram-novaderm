# NovaDerm — Especificación de reconstrucción gráfica

**Documento de trabajo | 16 de noviembre de 2026**

Este documento permite construir una publicación de imagen para un tema nuevo conservando el lenguaje observado en [@grupo_novaderm](https://www.instagram.com/grupo_novaderm/). Complementa el [análisis de las últimas 20 semanas](Manual_NovaDerm_20_semanas.md) e incluye una reconstrucción vectorial provisional del símbolo.

## 0. Estado de precisión

| Parámetro | Lo observado o medido | Grado de certeza |
|---|---|---|
| Fotografía | Predominan fotografías a sangre con piel, rostro, manos, zonas afectadas y procedimientos en primer plano. | Alto para las piezas revisadas. |
| Tipografía | Serif editorial de alto contraste, combinando tamaños y pesos. La fuente está rasterizada dentro de las publicaciones. | Categoría visual: alta. Nombre y versión exactos: no verificados. |
| Color | Blanco muy claro en letras y símbolo, sobre fotografías en tonos naturales. Se registran valores de píxeles de archivos concretos en la sección 4. | Los píxeles citados son mediciones exactas de esas copias; no identifican el color oficial original. |
| Logo | Símbolo blanco de perfil femenino y formas curvas. Se ha trazado desde una publicación real. | Forma aproximada; no es el archivo maestro. |
| Transparencia | La publicación es una fotografía JPEG aplanada: no conserva un canal alfa independiente para el símbolo. El SVG de trabajo tiene fondo y espacios interiores transparentes de verdad. | Propiedad del JPEG y del SVG: verificada. Opacidad original del logo en el archivo de diseño: desconocida. |
| Formato | Dos archivos visibles medidos: 1088 × 1344 px y 1350 × 1688 px. | Medida de esas copias descargadas de Instagram, no necesariamente del archivo exportado por el diseñador. |

**Regla de uso:** una medición de un píxel no equivale a una especificación oficial de marca. No afirmar que una fuente candidata, el SVG trazado o los colores de referencia son los originales hasta compararlos con una plantilla editable o el manual de marca.

## 1. Objetivo visual

La pieza debe parecer una portada de revista de dermatología: imagen íntima y convincente, información breve, estructura editorial y acabado cuidado. Su jerarquía es:

1. La fotografía identifica de inmediato el área de piel, la preocupación o el tratamiento.
2. Un título de una idea plantea la pregunta, condición o beneficio prudente.
3. Una línea secundaria añade contexto si hace falta.
4. El símbolo identifica la cuenta sin competir con el mensaje.
5. El pie de foto desarrolla la información que no cabe en la portada.

**No** usar como regla una plantilla corporativa azul brillante, grandes bloques de información, un marco blanco o iconos decorativos. No aparecen como base predominante en las piezas recientes examinadas. La cuadrícula combina fotos muy cálidas con imágenes más grises o clínicas; no necesita una tonalidad idéntica en todas.

## 2. Análisis comparativo de referencias

| Pieza y vínculo | Imagen | Organización de texto | Distintivo |
|---|---|---|---|
| [Facial, 9 nov.](https://www.instagram.com/p/DfhpukJOpCA/) | Vista superior, rostro acostado, manos y toalla; piel cálida y blancos textiles. | Dos niveles centrados arriba; palabra principal muy grande en mayúsculas. | Símbolo blanco abajo, centrado. |
| [Piel y estructura, 5 nov.](https://www.instagram.com/p/DfX_MQfuKoJ/) | Perfil cercano de mujer y piel cálida. | Enunciado centrado sobre la imagen y subtítulo más pequeño. | Marca en zona inferior. |
| [Radiesse, 31 oct.](https://www.instagram.com/p/DfK_sMtOwcV/) | Perfil y cuello de mujer mayor, colores claros; producto y jeringa visibles. | Titular en la mitad inferior y una aclaración debajo. | Marca pequeña cerca de la parte superior; el símbolo no tiene posición fija universal. |
| [Labios, 19 oct.](https://www.instagram.com/p/DesJ9Lius5Z/) | Macro cálido de labios y mejilla. | Línea fina y texto de mayor peso, alineados a la izquierda. | Símbolo bajo, a la izquierda. |
| [Psoriasis, 6 oct.](https://www.instagram.com/p/DeK3pxoO6vQ/) | Lesiones en un brazo; imagen clínica explícita y fondo gris. | Pregunta centrada con la condición como palabra de mayor tamaño. | Símbolo blanco inferior. |
| [Acné, 25 sept.](https://www.instagram.com/p/Ddt6imAO_by/) | Primer plano de rostro con lesiones y mano aplicando producto. | Bloque blanco a la izquierda; alternancia entre serif delgada y texto grueso. | Símbolo a la izquierda, sobre mejilla. Es la fuente del SVG provisional. |
| [Telangiectasias, 17 sept.](https://www.instagram.com/p/DdaMEkGOqiG/) | Primer plano de ojo y mejilla con visualización ampliada de vasos. | Titular en varios niveles alineado a la izquierda. | Lupa y líneas como recurso específico de explicación. |
| [Azúcar y piel, 4 ago.](https://www.instagram.com/p/DbnnJ7_OkPN/) | Imagen dividida entre azúcar y textura de piel. | Título centrado grande y subtítulo menor. | Comparación de dos campos visuales. |
| [Tipos de piel, 9 jul.](https://www.instagram.com/p/DalyYGTuI4D/) | Bandas de texturas cutáneas. | Título superior y etiquetas en las franjas. | Estructura informativa distinta del retrato. |

Estas plantillas son familias de solución observadas, no reglas de que todas las piezas deban llevar exactamente los mismos elementos.

## 3. Fotografía: criterio de selección y tratamiento

### 3.1 Según el tema

| Objetivo | Imagen sugerida | Encuadre | Qué comprobar |
|---|---|---|---|
| Problema dermatológico | Zona afectada reconocible, con textura real. | Primer plano o detalle. | La zona relevante debe ser visible, sin manipular el diagnóstico ni exagerar lesiones. |
| Prevención o autocuidado | Rostro, mano, piel o rutina cotidiana. | Retrato cercano o detalle. | Gesto natural y espacio para texto. |
| Tratamiento profesional | Paciente y manos de profesional, instrumental o producto real. | Medio corto o primer plano. | Que el procedimiento y el producto correspondan al tema y sean identificables. |
| Educación comparativa | Dos texturas, elementos o una zona con ampliación. | Composición partida o imagen con llamada visual. | Que la comparación ayude a explicar, no sugiera un resultado clínico inexistente. |
| Bienestar y empatía | Persona real o imagen de la condición tratada con respeto. | Cercano, expresivo, sin dramatización innecesaria. | Consentimiento y lenguaje sin estigma. |

### 3.2 Dirección de imagen

- Llenar el lienzo con fotografía; mantener la cara o el área protagonista suficientemente grande para identificarse en una pantalla de teléfono.
- Escoger un encuadre con una región de contraste donde pueda ir el titular. En algunas piezas se superpone a la piel; en otras se utiliza un fondo más neutro.
- Buscar luz suave y sombras naturales; evitar piel artificialmente lisa o una saturación excesiva. Conservar poros, arrugas, pigmentación y textura pertinente.
- Tratar los colores con moderación: piel melocotón o marrón, beige, gris y blancos. Un fondo frío o una foto clínica son compatibles si el tema lo requiere.
- Mantener detalles anatómicos y características reales; nunca alterar una imagen de resultado para hacer una afirmación médica.
- Si hay un producto de referencia, utilizar su forma y etiqueta correctas. Para un montaje, aislar el producto con transparencia auténtica y conservar sus proporciones; no mostrar un rectángulo de fondo salvo que sea parte del diseño.
- Asegurar que se dispone de autorización y derechos de uso de la fotografía antes de publicarla.

### 3.3 Control de contraste

Primero probar el texto blanco sobre la fotografía sin efectos. Si se pierde, mover el bloque, escoger otra foto o aplicar un degradado/sombra localizada y suave. La intensidad debe decidirse visualmente: no se pudo medir el ajuste original de cada pieza. Comprobar al 100 %, en miniatura y sobre versiones claras y oscuras.

## 4. Color: mediciones y propuestas separadas

### 4.1 Muestras verificadas de píxeles

Origen A: [facial del 9 de noviembre](https://www.instagram.com/p/DfhpukJOpCA/), copia JPEG visible de **1088 × 1344 px**. Origen B: [acné recurrente del 25 de septiembre](https://www.instagram.com/p/Ddt6imAO_by/), copia JPEG visible de **1350 × 1688 px**. Coordenadas en píxeles desde la esquina superior izquierda; las copias y compresión pueden cambiar según Instagram.

| Medición | Posición o método | RGB | HEX |
|---|---|---:|---|
| A: píxel claro en zona superior de la composición | x=550, y=200 | 246, 248, 245 | `#F6F8F5` |
| A: zona cálida de piel | x=500, y=900 | 175, 122, 82 | `#AF7A52` |
| A: zona cálida rojiza | x=600, y=500 | 170, 90, 83 | `#AA5A53` |
| A: zona gris clara junto al símbolo | x=550, y=1190 | 220, 220, 220 | `#DCDCDC` |
| B: mediana RGB de la selección de píxeles claros usada para el símbolo | Recorte x=140–270, y=752–889; máscara por luminosidad y diferencia de canales | 213, 202, 199 | `#D5CAC7` |
| A: píxeles blancos presentes en región del titular | x=250–849, y=180–409; selección de canales >245 | 255, 255, 255 aparece 9.544 veces en esa región | `#FFFFFF` |

La región del titular contiene también fotografía clara: esta última medición confirma que el blanco existe en la región, pero por sí sola no demuestra que ese fuese el relleno original de la fuente. Las cifras de piel son muestras de esas fotografías, **no colores de marca**. `#D5CAC7` describe el aspecto resultante del logo sobre esa piel, no su alfa ni su color de origen.

### 4.2 Valores para iniciar un diseño nuevo — propuestos

- Texto y símbolo: **`#FFFFFF` al 100 % de opacidad de capa**, salvo que el archivo maestro indique otra cosa; es el punto de partida del SVG provisional.
- Blanco cálido opcional: `#F7F3EF` para comprobar suavidad sobre una imagen concreta.
- Los beige, café, gris y piel se deben obtener de la fotografía elegida, no aplicar como un filtro obligatorio.
- El azul de las comunicaciones de la marca puede usarse en el copy o en otra familia de piezas, pero no se confirmó un código azul oficial a partir de estas fotografías.

## 5. Tipografía: identificación, comparación y ajuste

### 5.1 Rasgos observables

La tipografía principal tiene remates, contrastes marcados entre trazos gruesos y finos y proporciones editoriales elegantes. Se ven mayúsculas muy grandes, líneas finas en caja mixta y énfasis en un peso más grueso. El encaje entre letras es relativamente apretado en algunos titulares. Las piezas muestran distintas jerarquías; no se puede confirmar si todos los pesos pertenecen a una sola familia.

### 5.2 Qué está identificado y qué falta

El nombre exacto de la fuente, el archivo y su licencia **no son recuperables de manera fiable de un JPEG**. El nombre de archivo de una publicación no contiene la fuente. Candidatas de prueba: **Cormorant Garamond** y **Bodoni Moda**; son comparadores posibles, no una identificación. Debe comprobarse la disponibilidad, licencia y uso comercial antes de elegir una.

**Método de identificación:**

1. Conseguir el archivo editable del post o una exportación vectorial con texto y consultar las propiedades de fuente. Esta es la mejor evidencia.
2. Si no existe, obtener un recorte nítido de una palabra larga con mayúsculas, una frase en minúsculas, acentos y signos. Registrar la publicación y resolución.
3. Comparar como mínimo las formas de `A`, `R`, `G`, `S`, `a`, `e`, `g`, la tilde, `¿` y `?`; observar terminales, serifas, proporción del ojo y grosor fino.
4. Componer exactamente la misma cadena en cada candidata, a igual altura visual, sin deformar horizontalmente los glifos.
5. Comparar letra por letra y ajustar tamaño, interletrado y peso. Guardar una hoja de comparación y señalar que sigue siendo una atribución tentativa.
6. Solo llamar «fuente exacta» a una familia y estilo que se confirmen en el archivo o documentación de marca.

### 5.3 Escala propuesta para producir en 1080 × 1350 px

Las cifras siguientes son **rangos operativos iniciales**, no valores extraídos del editable:

| Elemento | Tamaño inicial | Interlínea y uso |
|---|---:|---|
| Palabra protagonista | 105–180 px | 0,85–1,0 veces el tamaño; adaptar al ancho y a la longitud. |
| Título en frase | 68–110 px | 0,95–1,08; preferir 2–4 líneas. |
| Contexto o subtítulo | 30–48 px | 1,05–1,2; aumentar si se pierde en móvil. |
| Microtexto | Evitar por debajo de 28 px en un archivo de 1080 px de ancho. | Recomendación para legibilidad, no medición de los posts. |

Centrar o alinear a la izquierda según la zona tranquila de la foto. Evitar justificar. No aplastar o estirar la fuente para llenar una caja. El ajuste final se hace por legibilidad, no por un valor fijo de tracking.

## 6. Isotipo: extracción, SVG y transparencia

### 6.1 Archivo disponible

**[SVG provisional con fondo transparente](../Logos/Referencias%20anteriores/isotipo_novaderm_reconstruccion_provisional.svg).**

Se trazó el símbolo visible en [acné recurrente, 25 de septiembre](https://www.instagram.com/p/Ddt6imAO_by/). La copia examinada mide 1350 × 1688 px. Se utilizó un recorte de x=140 a 270 y y=752 a 889; la selección del símbolo mediante umbral produjo una forma aproximada de unos 119 × 126 px. Su anchura visible corresponde a aproximadamente **8,8 % del ancho de esa copia**. Es una medición de esa pieza, no un tamaño universal.

El SVG tiene un `viewBox` de `0 0 131 138`, relleno blanco `#FFFFFF`, tres regiones trazadas y espacio exterior transparente. Los espacios entre curvas dejan ver el fondo. El archivo es editable y escalable; la fidelidad geométrica está limitada por la resolución del logo visible, la compresión, la mezcla con la fotografía y el umbral de extracción. **No es el símbolo maestro ni una reproducción certificada.** Al ampliar se pueden observar irregularidades. Conservarlo como referencia de trabajo y reemplazarlo por el archivo original cuando esté disponible.

### 6.2 Opacidad y exportación

- El SVG no incluye un rectángulo de fondo: área exterior y separaciones interiores tienen **alfa 0**. Las zonas blancas están al **100 % de opacidad** en el archivo provisional.
- Eso no prueba que el diseñador original utilizara 100 % de opacidad. El resultado aplanado es una mezcla de color, fondo, suavizado y compresión; no hay una solución única que permita recuperar el alfa.
- Para usarlo, colocar el SVG en una capa independiente, mantener proporciones y ajustar su escala; probar primero al 100 %. Si visualmente queda demasiado marcado, ensayar una opacidad menor y registrar el cambio como decisión de diseño, no como dato de marca.
- Exportar PNG con canal alfa si se requiere una versión raster; verificarla sobre fondo oscuro, blanco y ajedrezado. No guardar el logo aislado como JPEG: ese formato no conserva transparencia.
- Evitar sombras, recontornos, recoloreos o deformaciones sin una referencia autorizada.

### 6.3 Reconstrucción de mayor fidelidad

1. Solicitar el logo maestro en SVG, AI, EPS o PDF vectorial y, si existe, sus versiones blanca y a color. Esta vía conserva geometría y proporciones originales.
2. Si no se dispone del maestro, elegir al menos dos publicaciones del mismo símbolo, nítidas y con mayor contraste. Confirmar que se trata de la misma variante.
3. Guardar la imagen de referencia y documentar fecha, URL, dimensiones y zona recortada. No usar logos de clínicas homónimas como sustitutos.
4. Crear una máscara inicial por color/luminancia solo como guía; revisar contorno del perfil, nariz, labios, mentón y las dos bandas curvilíneas. Eliminar puntos producidos por textura de piel.
5. Dibujar curvas Bézier manuales sobre la referencia a gran aumento. Mantener las tres regiones y huecos, suavizar nodos innecesarios y preservar el grosor relativo de los espacios.
6. Comparar el trazado superpuesto al recorte en varias escalas. Revisar contorno y separación de curvas; inspeccionar sobre fondos claros y oscuros.
7. Guardar un SVG con `viewBox` ajustado, fondo transparente y rutas vectoriales; crear un PNG de previsualización. Registrar «reconstrucción no oficial» hasta que la marca la confirme.
8. Validar con un archivo original antes de sustituir definitivamente la identidad gráfica oficial.

## 7. Construcción exacta del archivo de trabajo propuesto

### 7.1 Estructura

Crear un documento **1080 × 1350 px**, perfil de color sRGB y exportación RGB. Es una configuración recomendada para este flujo: no se afirma que todos los archivos examinados tengan esa dimensión exacta.

Capas, de abajo arriba:

1. `01_FOTO_ORIGINAL` — imagen a sangre, no destructiva, recortada a 4:5.
2. `02_AJUSTE_COLOR` — corrección sutil y reversible.
3. `03_CONTRASTE_TEXTO` — degradado o sombra si se necesita, editable.
4. `04_PRODUCTO` — solo para la plantilla de servicio/producto; recorte auténticamente transparente.
5. `05_TEXTO_CONTEXTO` — texto pequeño de apertura.
6. `06_TITULO_PRINCIPAL` — palabra o frase protagonista.
7. `07_SUBTITULO` — aclaración opcional.
8. `08_ISOTIPO` — SVG provisional u original aprobado.
9. `09_GUIAS` — guías, no exportables.

Crear margen de seguridad inicial de **80 px** en los cuatro lados como guía editable, no como una medida observada. El texto puede entrar en zonas más amplias si sigue siendo legible y la plantilla lo exige; revisar siempre el recorte de la vista de perfil. No utilizar el margen como marco visible.

### 7.2 Distribución inicial

- Foto: ocupa el 100 % del lienzo.
- Título y subtítulo: colocar juntos como un bloque visual, normalmente centrado o a la izquierda. Elegir un área que no oculte ojos, boca, lesión o producto si son esenciales.
- Ancho del símbolo en pieza de 1080 px: comenzar con **95 px** (8,8 %), a partir de la medición de la pieza de acné. Ajustar según la referencia específica. La posición puede ser inferior central, esquina baja o zona vacía adyacente al texto.
- Separación y espacios: equilibrar por percepción visual. No hay evidencia de una cuadrícula fija compartida por todos los posts.
- Sobre imágenes oscuras, símbolo y texto blancos; sobre imagen muy clara, moverlos o introducir un contraste controlado. No cambiar automáticamente el logo a otro color sin la versión aprobada.

### 7.3 Receta A — título centrado sobre fotografía

1. Elegir una foto que permita reservar una franja en el tercio superior o medio.
2. Insertar una línea introductoria breve en serif de peso medio.
3. Ubicar la palabra principal debajo, en mayúscula grande y peso fino; ajustar para que tenga espacio alrededor.
4. Añadir subtítulo únicamente si aporta información nueva.
5. Colocar isotipo pequeño en un área inferior despejada; comprobar que no se pierda.
6. Comparar con [la pieza de facial](https://www.instagram.com/p/DfhpukJOpCA/).

### 7.4 Receta B — texto editorial a la izquierda

1. Elegir una fotografía con rostro o tema destacado y espacio visual a la izquierda.
2. Componer una primera frase en serif fina y una frase fuerte en peso grueso, máximo una idea principal.
3. Ajustar interlínea y cortes de línea para que el bloque tenga ritmo. Alinear sus bordes; no cubrir la zona de interés.
4. Ubicar el isotipo cerca de un margen visual libre, sin necesidad de centrarlo.
5. Comparar con [la pieza de labios](https://www.instagram.com/p/DesJ9Lius5Z/) o [la de acné](https://www.instagram.com/p/Ddt6imAO_by/).

### 7.5 Receta C — clínica o comparación

1. Partir de una imagen de la zona real o una comparación coherente con el mensaje.
2. Si hace falta una lupa o trazo, usar líneas finas y una ampliación congruente, sin generar evidencia clínica falsa.
3. Titular el síntoma o pregunta; el detalle médico va en el pie.
4. Revisar contraste sobre texturas complejas.
5. Comparar con [telangiectasias](https://www.instagram.com/p/DdaMEkGOqiG/) o [azúcar y piel](https://www.instagram.com/p/DbnnJ7_OkPN/).

### 7.6 Receta D — producto o tratamiento

1. Elegir la fotografía que contextualice la zona tratada.
2. Usar una fotografía autorizada del producto real y quitar el fondo si se monta como elemento independiente; preservar etiqueta y proporción.
3. Colocar el producto en un tamaño subordinado a la foto o al titular, según la referencia.
4. Redactar una promesa prudente y comprobable; no garantizar resultados.
5. Comparar con [Radiesse](https://www.instagram.com/p/DfK_sMtOwcV/) y [Novuma](https://www.instagram.com/p/De-cwvMOxCP/).

## 8. Pie de foto y entrega para cada nuevo tema

El usuario entregará: **tema**, objetivo, audiencia, mensaje, tratamiento si aplica, fuentes médicas, fotografía y logo disponible. Generar:

1. Dos opciones de titular de portada, breves y específicas.
2. Un subtítulo opcional que complete la idea, no la repita.
3. Dirección fotográfica y una de las recetas A–D.
4. Copy original estructurado como gancho → situación → explicación accesible → criterio personalizado → llamada a la acción.
5. Entre cero y cinco hashtags relevantes, según necesidad; emojis moderados y coherentes.
6. Lista de afirmaciones que debe validar un profesional de salud.
7. Archivo editable con capas, exportación final PNG o JPG para la pieza y copy en texto separado.

### Plantilla de solicitud reutilizable

```text
TEMA: [tema dermatológico]
PÚBLICO: [personas a las que se dirige]
OBJETIVO: [educar / sensibilizar / explicar servicio / invitar a consulta]
MENSAJE CLAVE: [una sola idea]
TRATAMIENTO O PRODUCTO, SI APLICA: [nombre exacto y datos autorizados]
CTA: [agendar / escribir / reflexionar / comentar]
FUENTES MÉDICAS Y RESTRICCIONES: [indicar]
FOTOGRAFÍAS DISPONIBLES Y AUTORIZACIÓN: [adjuntar o describir]
LOGO OFICIAL: [adjuntar si se dispone]

Diseñar una pieza 1080 × 1350 px inspirada en el sistema gráfico NovaDerm.
Usar fotografía a sangre pertinente, textura natural, tonos de piel y neutros;
serif editorial blanca de alto contraste con una jerarquía clara;
el isotipo oficial si está disponible o la reconstrucción provisional etiquetada;
y contraste suficiente en teléfono. Seleccionar la receta de composición que
mejor corresponda al tema. No presentar una fuente o color como oficial si no
está verificado. Generar además un copy en español con gancho, explicación,
criterio de atención individualizada y CTA adecuado. Señalar afirmaciones que
necesitan validación dermatológica. Entregar pieza editable y texto separado.
```

## 9. Control de calidad y revisión de un segundo agente

La primera versión se revisa con un agente o revisor independiente que no invente datos de marca. Proporcionarle la referencia, brief y versión generada, y pedirle una tabla con **cumple / corregir / no verificable**, evidencia y cambio propuesto:

| Parámetro | Criterio de aceptación |
|---|---|
| Tema | Fotografía y titular describen la misma idea. |
| Foto | A sangre, zona relevante identificable, textura natural, derechos confirmados. |
| Composición | Titular legible en miniatura, orden claro y sujeto clínico no tapado. |
| Tipografía | Serif editorial y jerarquía comparables; nombre exacto marcado como no verificado si no hay fuente maestra. |
| Color | Texto y logo suficientemente contrastados; mediciones y propuestas no se llaman «colores oficiales». |
| Isotipo | Relación de aspecto preservada, fondo transparente, escala discreta; SVG marcado como provisional si no es el maestro. |
| Copy | El pie complementa la imagen, identifica su objetivo y evita afirmaciones absolutas. |
| Exactitud médica | Todas las afirmaciones clínicas están validadas por un profesional responsable. |
| Exportación | Dimensiones, legibilidad, ortografía y recorte revisados; archivo editable y final coinciden. |

**Auditoría independiente de este documento:** se revisaron los riesgos de atribuir fuente, HEX u opacidad oficiales a un JPEG, la necesidad de conservar huecos y curvas del símbolo y la obligación de etiquetar como aproximado el vector trazado. Se han incorporado esas observaciones en este documento. Ningún revisor puede convertir datos no disponibles en certezas; la verificación final requiere los activos de la marca.

### Resultado de la revisión independiente del SVG

El revisor contrastó el vector con el recorte original. Confirmó que conserva una silueta reconocible, dos separaciones curvas y transparencia en exterior y huecos. También detectó irregularidades visibles al ampliar: escalonamiento en el arco exterior y canales, un canal interior algo más ancho y pequeñas diferencias en nariz, labios, mentón y arranque del cabello. El blanco de la reconstrucción resulta más sólido que la impresión visual del JPEG; no se puede deducir la opacidad original. Por ello, el archivo sirve para **maquetación y comparación**, pero necesita un trazado Bézier refinado o el logo maestro para una reproducción definitiva.

