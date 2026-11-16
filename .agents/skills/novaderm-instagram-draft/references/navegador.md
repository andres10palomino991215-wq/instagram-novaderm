# Operación del navegador

Esta guía usa capacidades comprobadas en la sesión de creación, 16/11/2026. La interfaz de Instagram y las APIs disponibles pueden cambiar: leer la documentación actual de las herramientas al invocar, no fingir disponibilidad ni reutilizar índices viejos. No se probó una carga real a la cuenta del cliente al preparar esta skill.

## Navegador integrado y sesión

Usar `mcp__cua_repl` cuando esté disponible y respetar sus instrucciones de inicio. Para inventariar superficies la primera llamada es únicamente `await cua.getState()`. Para abrir el navegador integrado directamente, puede ser únicamente:

```javascript
var igTab = await cua.createBrowserTab('iab', 'https://www.instagram.com/', { visible: true });
```

No ejecutar a la vez varias APIs en esa primera llamada. Leer el resultado/documentación antes de continuar. Preferir reutilizar pestaña existente pertinente. El navegador integrado puede conservar una sesión distinta de la cuenta objetivo: comprobar la identidad activa, no solo el nombre del perfil visitado.

Con API DOM, usar snapshots y locators basados en controles observados. Tras interactuar, observar estado. No usar `evaluate` para mutar página, descubrir endpoints privados, extraer cookies o ejecutar publicaciones. El Playwright de Python del motor es para render local, **no para automatizar la cuenta de Instagram**. No crear otro perfil Chromium para intentar copiar la sesión.

La preparación del navegador puede solaparse con diseño/copy, pero solo un controlador actúa sobre la pestaña. Si el usuario necesita iniciar sesión, facilitar el handoff y continuar las tareas independientes; nunca solicitar contraseñas/OTP por chat. No acceder a mensajes ni a información personal ajena a la tarea.

## Carga de archivo

Antes de cargar leer la documentación `file-uploads` si el runtime la ofrece. En el runtime comprobado la carga se realiza con un **file chooser**, no `locator.setInputFiles`. El patrón es:

```javascript
// El locator y su nombre se obtienen de la UI observada en este momento.
const chooserPromise = igTab.playwright.waitForEvent('filechooser');
await observedUploadControl.click();
const chooser = await chooserPromise;
await chooser.setFiles(pngAbsolutePath);
await igTab.playwright.domSnapshot();
```

`observedUploadControl` y `pngAbsolutePath` se resuelven con controles actuales y el PNG final local, no son nombres globales garantizados. Preferir el input real o un botón visible que abra el selector. Ruta absoluta legible por ese navegador; si el navegador corre en otro equipo/entorno, usar el puente de archivos autorizado que ofrezca su documentación. No alojar el PNG públicamente para sortear un problema de carga.

Si el chooser no está soportado, usar el selector nativo solo después de leer la skill/documentación de Windows aplicable. No escribir archivos en un campo distinto por suposición. La petición de preparar este post para esa cuenta autoriza esa carga normal; no repetir permisos ya otorgados en la sesión salvo que cambie destino, datos o alcance.

## Texto y evidencia

Obtener el caption de UTF-8 a partir del archivo final del trabajo mediante una herramienta de archivos; transmitirlo a la UI con `fill`/`paste` del campo observado. Conservar saltos de línea. Verificar el contenido con lectura del campo/DOM actual; si la UI no permite lectura completa, inspeccionarlo y explicitar el límite en vez de registrar correspondencia no comprobada.

El estado final requiere botón de publicación visible sin accionarlo. Guardar captura con la API de screenshot y el mecanismo de archivos permitidos. Leer `screenshots` si el runtime lo exige. Antes de terminar, marcar la pestaña como entrega (`markDeliverable`) para que sobreviva al turno cuando esté soportado; usar handoff si requiere acción del usuario para completar sesión. No asegurar persistencia permanente del compositor.

Cuando las instrucciones de CUA exijan `completion_summary`, la siguiente llamada de herramienta tras observar el resultado final debe ser ese cierre, antes de ejecutar helpers de archivos o responder. Planificar la captura y marca de pestaña en la última interacción de CUA para cumplirlo. Después registrar evidencia local con el helper `handoff` del orquestador y responder con la captura embebida.

## Registro del trabajo

```powershell
& $py $tool handoff --job $job --status ready_for_user --account grupo_novaderm --tab-id $tabId --evidence 'Descripción concreta del estado observado' --screenshot $screenshotPath --content-verified
```

Ese comando **no carga ni publica**: registra lo que el principal ya observó. Exige PNG/caption actuales, control visual y revisión médica aprobada o no aplicable. No inventar valores para superar comprobaciones. `--content-verified` declara verificación real de imagen/pie en la UI; la herramienta no autentica la declaración.

Si hay revisiones pendientes, no usar `ready_for_user`; registrar `preparing` o `blocked` con la razón, aunque se haya dejado una versión en el compositor para revisar. Sin acceso de cliente, `awaiting_login` conserva los archivos listos para continuar. Ningún estado representa publicación ni fecha programada.
