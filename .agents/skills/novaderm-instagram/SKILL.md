---
name: novaderm-instagram
description: Automatizar posts estáticos de Instagram de Grupo Novaderm desde el tema y tres imágenes base a elección hasta diseño por capas, copy y carga en la cuenta del cliente, deteniéndose antes de Publicar. También iterar esas piezas; no programar ni producir videos.
---

# Posts de Grupo Novaderm hasta revisión en Instagram

Orquesta tres skills hermanas del proyecto: esta diseña y coordina; [novaderm-copy](../novaderm-copy/SKILL.md) trabaja en un agente paralelo; [novaderm-instagram-draft](../novaderm-instagram-draft/SKILL.md) guía al principal en el navegador. Cargar una skill de apoyo significa leer su SKILL.md, no invocar una API ficticia. Un único agente, el principal, controla Instagram para evitar carreras y duplicados.

## Alcance y reglas persistentes

- Al empezar pide **TEMA** si falta. Si ya está dado, úsalo. Recopila solo un dato esencial faltante que cambie la pieza: producto exacto, fuente clínica o CTA específico; no repetir un cuestionario ni pedir fecha de publicación.
- Empieza a comprobar acceso a Instagram mientras preparas las bases, sin cargar archivos aún. La cuenta de destino es **@grupo_novaderm**; visitar su perfil no prueba acceso a publicar como ella. Si el login requiere intervención, dejarlo al usuario y seguir las tareas independientes.
- Muestra **al menos tres imágenes base realmente distintas** y espera la elección explícita. Conserva esta pausa de revisión; no la elimines por optimizar. Solo fotos/fondos sin texto, logo, etiquetas ni gráfica de post. No generar el diseño completo con IA.
- Tras elegir, lanza al agente de copy al mismo tiempo que preparas composición, recorte y logo. No es necesario un nuevo turno de aprobación del texto si no se pidió: el principal lo evalúa, ajusta e integra.
- Entrega maestro SVG con capas y texto editable, PNG y copy separado; después carga PNG y pie en el compositor de Instagram, dentro de la cuenta confirmada. **No pulses Publicar/Compartir ni programes fecha**. El final es una previsualización verificada y abierta para que el usuario publique.
- Conserva derechos/consentimiento y controles clínicos. Sin validación necesaria, no digas «solo falta publicar»: informa el pendiente real. Una versión para revisión puede quedar preparada sin publicarse, si el usuario autorizó su carga y no contiene datos sensibles sin permiso.

## 1. Contexto mínimo y proyecto

Lee [sistema visual](references/sistema-visual.md) y [procedencia](references/procedencia.md) una vez por trabajo. Mira [contacto](references/visual/contacto.jpg) y dos portadas pertinentes; no recargues las doce ni los documentos extensos en cada reanudación. El archivo histórico se consulta solo para resolver dudas. Fuentes/colores oficiales no verificados y logos reconstruidos siguen siendo aproximaciones.

Lee [motor](references/motor.md) al preparar el entorno. Usa `paths` para resolver proyecto, runtime y skills hermanas; los recursos siempre parten de la raíz de skill, no de un directorio temporal. El proyecto de salidas es `Grupo Novaderm` dentro de este repositorio. Si se reubicó y no puede detectarse, identifica/pide la ruta persistente equivalente. No crees silenciosamente la ruta antigua de otro equipo.

Al arrancar, aplica la parte de sesión de [preparación de Instagram](../novaderm-instagram-draft/SKILL.md): abrir/reutilizar el navegador integrado y comprobar la cuenta activa. Si necesita intervención para iniciar sesión con el cliente, facilitarla mientras continúan las tareas independientes. No abrir aún un compositor vacío ni bloquear la preparación visual por una sesión pendiente. La carga se hace después de tener archivos finales.

Reutiliza el entorno Python de `Grupo Novaderm/.herramientas/novaderm-python` y sus dependencias. No reinstales navegador ni paquetes por post. `new --topic TEMA` crea un trabajo persistente `Publicaciones/tema_id/` sin fecha programada. Si hay trabajo abierto, reanuda desde `estado.json` y artefactos en vez de generar otro.

## 2. Bases y elección

Prepara tres rutas que varíen encuadre, gesto/sujeto o situación y distribución del espacio, conservando pertinencia. Usa prompts/recetas del sistema visual. Con generación disponible, usa su herramienta y skill específica para obtener tres archivos reales; un tríptico no cuenta. Guarda originales y prompts/procedencia.

Inspecciona texto accidental, logos, anatomía y naturalidad. Las portadas solo guían el estilo: no borrarles texto ni reutilizar sus fotografías como bases. No subir fotos de pacientes identificables a generadores sin autorización específica. Priorizar material clínico autorizado/revisado y no fabricar lesiones, procedimientos, resultados ni envases. Identificar bases sintéticas como ilustrativas, nunca evidencia o paciente real.

Sin generación, usa tres fotografías autorizadas existentes. Sin ninguna de esas vías, explica el bloqueo y solicita recursos; no llames imágenes a simples descripciones ni avances a diseñar. Registra las bases con `option`, muestra A/B/C visiblemente con una frase de enfoque cada una y pregunta cuál elige. **Detente esperando la elección.** Conserva `awaiting_base_choice` y el estado de sesión, sin crear un compositor vacío que luego pueda perderse.

Tras la elección real, ejecuta `select --choice ID --evidence CITA_REAL`. Una elección anterior solo cuenta si identifica inequívocamente esas bases. No simular consentimiento ni selección. Nuevas opciones conservan historial.

## 3. Copy paralelo y construcción visual

Lee [novaderm-copy](../novaderm-copy/SKILL.md) y pasa al agente solo tema, objetivo, público si es relevante, base elegida, CTA/datos autorizados y fuentes/pendientes clínicos. El agente carga su propia guía de voz; no necesita el manual completo, logos o motor. El principal puede continuar con recorte, zonas protegidas y estructura visual mientras llega el texto.

Si usas `collaboration.spawn_agent`, establece `fork_turns: "none"` y pon en el mensaje la ruta de `novaderm-copy/SKILL.md`, el brief mínimo y la carpeta de salida. Así no hereda todo el historial visual/navegador por defecto. No elijas otro modelo salvo instrucción del usuario o del entorno. Reutiliza el agente para ajustes mediante un mensaje breve.

Recibe storytelling, titular recomendado, secundario opcional y pie. Evalúa tono, afirmaciones, longitud, coherencia y repetición. Guarda decisión editorial y ajustes. `copy.md` y `caption.txt` contienen únicamente el pie final para pegar en Instagram, sin análisis, etiquetas «CTA», títulos de sección ni notas internas. Los claims y dudas viven aparte en `04_revision/afirmaciones.json`.

Sin agentes o ante un error real, informa la limitación y realiza dos pasadas secuenciales distintas. Registra `--mode sequential-unavailable` y causa auténtica; no simules agente ni revisión independiente. Con agentes disponibles usa el paralelo solicitado. Nunca delegues a dos agentes el control de la misma pestaña.

Compón con [motor SVG](references/motor.md): foto → tinte reversible opcional → contraste localizado opcional → producto recortado opcional → contexto → título → subtítulo opcional → isotipo vectorial → guías ocultas. No tapar ojos, lesión o información del tema. El generador solo crea la base; texto y logo se añaden después en capas reales.

Cormorant Garamond es sustituta, no fuente oficial. El isotipo blanco suministrado ya tiene alfa 0,82 interno; empieza con alfa de capa 1 y adapta posición/escala con criterio visual, no con un punto fijo. Preserva proporciones/huecos y documenta aproximaciones. Si montas un producto real, quita su fondo con transparencia auténtica y conserva etiqueta, diseño y detalles. No modificar logos originales.

## 4. Verificar y preparar Instagram

Ejecuta `copy`, `build`, `render` y `check`; abre PNG al 100 % y miniatura a 360 px. Compara las referencias pertinentes, revisa jerarquía, tildes, trazos, contraste, composición y logo. Usa [controles](references/copy-revision.md) sin cargar contexto editorial duplicado. No certificar visualmente lo que no se abrió ni exportaciones no producidas.

Documenta derechos y, si hay claims, fuentes primarias vigentes y revisión profesional real con responsable/fecha. No inventar aprobación; si no aplica, explicar por qué. El validador técnico no aprueba medicina.

Continúa con [novaderm-instagram-draft](../novaderm-instagram-draft/SKILL.md) usando los archivos finales exactos. El principal confirma cuenta, abre un único compositor, carga PNG, conserva el encuadre, pega `caption.txt` y verifica pantalla final. No agregar ubicaciones, etiquetas, colaboradores ni otro contenido no pedido. No programar.

Antes de afirmar «listo para publicar», registra con `handoff` la evidencia de cuenta correcta, imagen/caption actuales, previsualización y control final habilitado sin pulsarlo. Guarda captura y deja la pestaña accesible con la API disponible; no supongas que es un borrador permanente guardado por Instagram. El registro enlaza hashes: cualquier cambio posterior invalida el estado listo. Si la UI, acceso o validación impiden completar, entrega igualmente archivos y explica el punto exacto pendiente.

## 5. Cierre e iteración

Con éxito informa: «La imagen y el texto están cargados en @grupo_novaderm. La previsualización está abierta; falta que pulses Publicar». Incluye captura, enlace a la pestaña cuando exista, editable, PNG y copy. Solo usar esa frase si se observó el estado real. Sin éxito describe qué sí quedó listo y qué falta, sin afirmar carga ni aprobación.

No publiques ni crees automatizaciones/programaciones durante este flujo. Pide feedback solo sobre cambios concretos. Versiona correcciones; una base distinta vuelve a elección explícita. Cualquier cambio de imagen o copy obliga a actualizar también el compositor y repetir verificación. No recargar ni cerrar una previsualización abierta sin atender la posible pérdida de contenido.
