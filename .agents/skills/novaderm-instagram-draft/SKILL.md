---
name: novaderm-instagram-draft
description: Cargar un post final de un trabajo de novaderm-instagram en el navegador integrado, verificar la previsualización y dejar al usuario la acción de Publicar. Usar como apoyo de esa skill; no crea imágenes, no publica ni programa.
---

# Preparar el post en Instagram

Skill de apoyo de [novaderm-instagram](../novaderm-instagram/SKILL.md). Su resultado es un **compositor verificado y abierto**, no un post publicado ni necesariamente un borrador persistido en los servidores de Instagram. El principal es el único dueño de la pestaña; el agente de [copy](../novaderm-copy/SKILL.md) entrega archivos y no controla el navegador.

## Entrada mínima

- Trabajo persistente de `novaderm-instagram` con autorización para cargar sus archivos a `@grupo_novaderm`. Si se invoca directamente, resolver la ruta del trabajo existente; no exigir de nuevo tema ni imagen elegida. Archivos externos sin ese registro requieren preparar/importar su revisión antes de usar este flujo, no simular que ya existe un trabajo del motor.
- Cuando viene del orquestador: `05_entrega/post.png`, `caption.txt`, revisión visual y médica/derechos. Reutilizar datos conocidos; no volver a pedir tema ni elegir foto.
- Cuenta de destino: `grupo_novaderm`. Visitar su perfil como espectador **no demuestra** sesión con permisos para publicar en ella. Otra cuenta es un encargo diferente que requiere adaptar el destino; el helper de este paquete rechaza cuentas distintas.

## Flujo

1. Leer [operación del navegador](references/navegador.md). Descubrir herramientas actuales y usar el navegador integrado solicitado. Abrir o reutilizar una única pestaña de Instagram. La comprobación de sesión puede hacerse mientras avanza el diseño; no abrir un compositor vacío prematuramente.
2. Verificar la cuenta **activa para publicar** con la UI de perfil/cambio de cuenta. Si está desconectada o es otra cuenta, permitir al usuario iniciar sesión/cambiar a la del cliente en el navegador. Nunca pedir contraseña/OTP por chat ni guardar cookies o secretos. No usar la sesión personal para publicar contenido del cliente. Un CAPTCHA o permiso inesperado requiere seguir la política real del entorno, no eludirla.
3. Con PNG/caption finales y cuenta confirmada, abrir «Crear»/«Nueva publicación» usando controles observados, sin coordenadas o selectores históricos. Si ya hay un compositor del mismo trabajo, inspeccionarlo y continuar, sin duplicarlo. No descartar contenido ajeno para empezar.
4. Cargar el PNG mediante el mecanismo de archivos documentado en la sesión. Inspeccionar vista de recorte; mantener proporción y composición final. No añadir filtros o retoques de Instagram que modifiquen el diseño aprobado. Avanzar únicamente por controles intermedios observados.
5. Pegar el contenido exacto de `caption.txt` en el campo de descripción, sin encabezados del informe ni notas del agente. Si Instagram obliga a cargar imagen antes de mostrar ese campo, esperar al PNG: no intentar forzar un orden incompatible con la UI. Verificar párrafos, acentos, emojis y texto completo. No añadir ubicación, colaboradores, tags ni música salvo que se pidieron.
6. Revisar cuenta, miniatura/recorte, pie y el botón final «Compartir»/«Publicar». **No pulsarlo.** No enviar formularios finales, programar, usar endpoints de publicación ni atajos equivalentes. Las flechas de avance solo se usan tras confirmar que no son la acción final.
7. Capturar evidencia real de esa previsualización, conservar la pestaña como entrega/handoff según la API disponible y hacer el cierre de CUA requerido antes de cambiar a otras herramientas. Registrar `handoff` con cuenta observada, pestaña y hashes de archivos actuales; banderas de correspondencia solo si se verificaron. No registrar credenciales ni mensajes privados.
8. Avisar por chat: «El post está cargado en @grupo_novaderm con su texto y la previsualización revisada. Solo falta que pulses Publicar». Mostrar captura y archivos. Usar esa frase solo si se cumplieron cuenta, contenido y revisiones; si falta algo, indicar el bloqueo concreto. Dejar la pestaña abierta. No asegurar que sobrevivirá cerrar sesión, recargar o cerrar el navegador: conservar siempre PNG/caption locales.

## Reanudación y fallos

Consultar `estado.json` y la UI actual. Un ID de pestaña guardado puede haber caducado: volver a descubrirla, no afirmar que el borrador sigue ahí. Si PNG o caption cambian, actualizar el compositor y repetir revisión; el registro anterior deja de ser válido.

Si no hay acceso al navegador integrado, solicitar conexión/handoff y seguir produciendo los archivos independientes. No cambiar a otro navegador sin que sea compatible con la petición del usuario. Sin capacidad de subir archivos, probar el selector nativo documentado o pedir al usuario esa operación puntual; no declarar la carga completada. Tras un error, observar primero el estado; no repetir cargas a ciegas. Un segundo intento solo tras resolver la causa; si persiste, conservar archivos y comunicar la limitación.

La publicación final queda siempre en manos del usuario en este flujo, aun cuando una herramienta permita automatizarla. Una petición futura de publicar es un encargo distinto que debe tratarse explícitamente.
