# Sistema visual operativo

## Evidencia y límites

Origen: análisis local de 26 publicaciones de @grupo_novaderm (23 imágenes, tres portadas de reels) de julio a noviembre de 2026. Las doce copias locales se inspeccionaron para este paquete; no se analizaron movimiento/audio.

| Estado | Qué sabemos |
|---|---|
| Observado en copias | Fotografía a sangre; piel y primeros planos; serif de alto contraste; texto corto blanco; isotipo discreto y posición variable. |
| Medido en archivos | Dos copias 1088×1344 y 1350×1688; símbolo histórico ~8,8 % de ancho visible en una pieza. SVG blanco actual fill-opacity=0.82; grises 0.70/0.76/0.82. |
| Propuesta de producción | 1080×1350, margen inicial 80 px, escala tipográfica y fuente sustituta; ubicación/contraste ajustables. |
| No verificado | Fuente/pesos originales, colores oficiales, alfa original, geometría maestra, plantilla fija y derechos de las fotos para nuevos usos. |

La documentación describe un isotipo anterior opaco y versiones nuevas. El activo por defecto es la reconstrucción cuadrada **versión 2 blanca**; no confundir sus valores con el recurso histórico ni con originales de la cuenta.

## Dirección fotográfica

La base comunica piel, preocupación o cuidado en una mirada. Primer plano íntimo/detalle, luz suave lateral/difusa, profundidad natural, piel, crema, arena, marrón y gris. Conservar poros, arrugas y variaciones. No imponer un filtro cálido a una foto clínica que precise fidelidad cromática. Evitar piel plástica, glamour agresivo, dramatización de lesiones y una plantilla azul corporativa universal.

| Tema | Ruta y referencias locales | Reserva |
|---|---|---|
| Cuidado/facial | Cenital, manos y textil; [01](visual/01.jpg) | Superior tranquila; rostro/manos completos. |
| Cambio de piel | Perfil cálido; [02](visual/02.jpg) | Bloque central si despeja lo esencial. |
| Servicio/producto | Cuello/rostro y producto real; [03](visual/03.jpg), [04](visual/04.jpg) | Producto en capa; título inferior, logo puede ir arriba. |
| Labios/criterio | Macro boca/mejilla; [06](visual/06.jpg) | Texto izquierda baja; preservar labios. |
| Rutina inclusiva | Gesto cotidiano/espejo; [07](visual/07.jpg) | Revisar anatomía/reflejo. |
| Condición/empatía | Zona clínica autorizada; [05](visual/05.jpg), [08](visual/08.jpg), [09](visual/09.jpg), [11](visual/11.jpg), [12](visual/12.jpg) | No tapar lesión ni manipular evidencia. |
| Explicación de vasos | Macro y ampliación coherente; [10](visual/10.jpg) | Lupa como capa posterior, no obligatoria. |

Tres rutas posibles: A macro/perfil; B gesto de cuidado/retrato de otro encuadre; C manos/objeto/entorno pertinente. No cambiar tema para obtener diversidad. Una condición puede requerir tres encuadres autorizados del mismo material sin alterar lesiones.

Prompt adaptable por ruta (resolver variables antes de enviarlo):

> Fotografía editorial realista para dermatología sobre {tema}, {sujeto y gesto}, {encuadre distinto}, luz suave {dirección}, textura cutánea natural, color respetuoso de la piel, fondo {neutro/entorno pertinente}, composición vertical 4:5 con espacio tranquilo en {zona}. Solo fotografía base. Sin letras, palabras, logotipos, marcas de agua, tipografía, marcos, recuadros, iconos ni diseño de publicación. No simular resultados de tratamiento. {Restricciones anatómicas y privacidad}.

Si hay una marca, no inventar envase con IA: fondo sin empaque y montaje con recorte real autorizado. Objetos genéricos sin etiqueta son admisibles si no sugieren un producto concreto falso.

## Composición y tipografía

Foto a sangre, sin marco. Una idea en 2–4 líneas; una palabra/frase dominante. Alternar tamaño/peso, no imponer mayúsculas. Una familia con pesos 400/600 suele bastar. No deformar el ancho. Cormorant Garamond se incluye como sustituta; Bodoni Moda queda como alternativa de comparación, no incluida.

| Nivel | Inicio a 1080 px | Uso |
|---|---|---|
| Protagonista | 105–180 px | Interlínea 0,85–1,0; ajuste óptico. |
| Frase | 68–110 px | 0,95–1,08; dos a cuatro líneas. |
| Contexto/subtítulo | 30–48 px | 1,05–1,2; ampliar/eliminar si falla en móvil. |
| Microtexto | Evitar menos de 28 px | Pasar al pie si no es esencial. |

Son propuestas. El motor admite tamaño, línea base, peso 300–700 y anclaje por línea. Preferir centro o izquierda. No encoger automáticamente para llenar cajas.

Texto `#FFFFFF` o cálido `#F7F3EF`: puntos de partida. Piel/arena/marrón surgen de la foto; no son paleta oficial. `#AF7A52` en la documentación es un píxel de piel. Turquesas de la reconstrucción principal (`#75DEE2`, `#01CBD5`, `#02B9C9`) se muestrearon de una captura, tampoco son oficiales.

Contraste: buscar primero foto y ubicación adecuadas; luego degradado negro localizado editable si hace falta. No ocultar lesión ni falsear comparación. La corrección de color del motor es tinte reversible opcional, no revelado fotográfico profesional.

## Isotipo, tamaño y transparencia

Usar [blanco](../assets/logos/isotipo-blanco.svg) sobre fondo oscuro; [gris](../assets/logos/isotipo-gris.svg) solo si referencia/contraste lo justifican; [color](../assets/logos/isotipo-color.svg) para variante acordada. No agregar aro, disco, sombra o contorno.

`viewBox="78 98 600 600"` es lienzo cuadrado con margen transparente. Tres trazos forman el símbolo con huecos alfa 0. Blanco ya a 0,82 por trazo; capa externa empieza en 1. Capa 0,8 produciría alfa efectivo 0,656. La apariencia translúcida de las portadas no demuestra esos valores originales.

La referencia histórica ~95 px en 1080 corresponde a **ancho visible**, no al cuadrado actual. La geometría ocupa ~87 % del viewBox: viewport inicial ~109 px deja ~95 px visibles. Es aproximación; verificar contorno renderizado. No es tamaño ni área de protección oficial.

Posiciones: inferior central, esquinas bajas, arriba o cerca del texto si despeja el tema; observar 03 y 09. Proporción intacta, escala discreta. Empezar en ~8–10 % de ancho visible y adaptar en miniatura. Margen inicial 80 px como guía, nunca para forzar una posición que tape información. Documentar archivo, escala visible, posición, alfa interna y adicional.

Logo oficial nuevo: preservar original y comprobar transparencia/viewBox/procedencia. No llamarlo oficial solo por ser SVG ni reconstruir otra variante silenciosamente.
