# Procedencia, derechos y portabilidad

Versión original preparada para revisión el 16/11/2026. Esta distribución conserva las tres skills de proyecto en `.agents/skills`. Recursos relativos a la raíz de skill; proyecto detectado/configurado en cada uso. El análisis y las reconstrucciones siguen teniendo los mismos límites.

## Fuentes locales

Origen: proyecto local Grupo Novaderm proporcionado por el usuario. Copias sin alterar bytes; logos originales intactos.

- [Manual](sources/Documentación/Manual_NovaDerm_20_semanas.md): análisis local aportado de 26 publicaciones de @grupo_novaderm, ventana de 20 semanas. Fechas/enlaces/observaciones proceden de ese análisis; este paquete no los volvió a auditar en Instagram.
- [Especificación](sources/Documentación/Especificacion_detallada_NovaDerm.md): mediciones y propuestas; conserva un enlace al SVG histórico en su árbol archivado, distinto del activo actual.
- [LEEME original](sources/LEEME.md): describe las reconstrucciones actuales; su listado enumera el proyecto de origen, no el contenido del paquete.
- `visual/01.jpg` a `12.jpg`: copias de portadas atribuidas a [@grupo_novaderm](https://www.instagram.com/grupo_novaderm/). Enlaces individuales, nombres originales y hashes en [resource-manifest.json](resource-manifest.json). `contacto.jpg` es una hoja derivada para inspección.
- `visual/logo-referencia.png`: captura del usuario; no convertir aro truncado ni controles de captura en identidad gráfica.
- `assets/logos/`: copias renombradas de `logo versión 2 blanco.svg`, `logo versión 2.svg`, `SVG logo principal.svg`. **Reconstrucciones, no maestros certificados**. El ~99 % de superposición del LEEME describe una prueba local previa, no una prueba nueva ni identidad geométrica demostrada.

Fotografías incluidas para contexto de revisión/estilo en el proyecto del usuario. Atribución y disponibilidad no equivalen a licencia, consentimiento ni autorización de republicación. No reutilizar como bases, borrar textos/logos o redistribuir fuera del entorno autorizado sin revisar derechos. Descripciones son paráfrasis del análisis; nuevo copy original.

## Fuente sustituta

Cormorant Garamond, Christian Thalmann; copyright The Cormorant Project Authors. Archivo variable normal 300–700 descargado de [Google Fonts](https://github.com/google/fonts/tree/main/ofl/cormorantgaramond) el 16/11/2026, sin modificar; [metadatos](../assets/fonts/METADATA.pb) y [SIL OFL 1.1](../assets/fonts/OFL.txt) incluidos. No identifica la fuente original de Novaderm. La licencia acompaña paquete y trabajos que reciben la fuente.

El manifiesto congela SHA-256 de los bytes incluidos; `verify-package` los comprueba aunque cambie el repositorio externo. El uso no descarga fotos/fuentes. Las dependencias de render sí pueden requerir instalación inicial con red.

## Trabajo persistente

`Publicaciones/tema_id/` queda dentro de Grupo Novaderm con brief, bases/procedencia, elección literal, copy/revisión, recursos, SVG y PNG. No usar descargas temporales ni URLs de sesión dentro del maestro. Bases/productos se copian al trabajo; SVG embebe imagen/fuente y anida rutas vectoriales del isotipo. `recursos/` conserva archivos separados y licencia para editores que ignoran fuentes embebidas.

No incluir credenciales o datos identificables de pacientes. Registrar una referencia al consentimiento, alcance y responsable, sin copiar autorizaciones privadas completas al paquete.
