# Instagram de Grupo Novaderm

Proyecto de Codex para crear publicaciones estáticas de Instagram, con tres imágenes base a elección, diseño editable por capas, copy en la voz de Novaderm y preparación de la publicación en Instagram. El usuario revisa y pulsa **Publicar**; el proyecto no programa publicaciones.

## Preparación para el cliente

1. Accede a este repositorio con una cuenta de GitHub autorizada. Si el repositorio es privado, el propietario debe concederte acceso antes de que puedas clonarlo.
2. Clónalo o pídele a Codex que lo clone. Abre la carpeta del repositorio como proyecto en Codex.
3. Pide a Codex: «Prepara este proyecto para mi equipo siguiendo el README y verifica sus dependencias». Alternativamente, ejecuta desde la raíz:

   ```powershell
   python setup.py
   ```

   En macOS o Linux usa `python3 setup.py`. Necesitas Python 3.11 o superior y conexión a Internet para instalar paquetes y Chromium. En Linux, si Playwright indica bibliotecas del sistema faltantes, instala los requisitos que te indique en su documentación oficial.
4. Inicia un chat de Codex en esta carpeta y escribe: `Usa $novaderm-instagram. Tema: [tu tema]`.

Las skills están en `.agents/skills/` y Codex las descubre al abrir esta carpeta como proyecto. Si no aparecen, inicia un nuevo chat o reinicia Codex. La instalación crea un entorno Python local en `Grupo Novaderm/.herramientas/` y puede instalar Chromium en la caché de Playwright del usuario; no instala las skills globalmente ni guarda contraseñas.

## Qué sucede al usarlo

El asistente comprueba la cuenta activa en el navegador integrado. Si hace falta, el usuario inicia sesión en Instagram directamente. Se generan tres imágenes base y se espera una elección; a partir de ella, un agente trabaja el copy en paralelo con el diseño. Se entregan SVG editable, PNG y texto. Con acceso y validaciones necesarias, se carga la imagen y el pie en el compositor de `@grupo_novaderm`, y se deja la previsualización abierta para que el usuario pulse Publicar. La disponibilidad de generación de imágenes, subagentes y navegador depende de la sesión de Codex; no se puede prometer que estén habilitados en todos los equipos.

Los trabajos y dependencias locales se guardan en `Grupo Novaderm/Publicaciones/` y `Grupo Novaderm/.herramientas/`, excluidos de Git. No incluyas contraseñas, cookies, información privada de pacientes ni sesiones de navegador en el repositorio.

## Estructura

- `.agents/skills/novaderm-instagram/`: orquestador, recursos visuales y motor SVG/PNG.
- `.agents/skills/novaderm-copy/`: voz editorial y copy.
- `.agents/skills/novaderm-instagram-draft/`: preparación en Instagram mediante navegador.
- `Grupo Novaderm/Documentación/` y `Logos/`: documentación y copias de los recursos suministrados.
- `setup.py`: preparación reproducible del entorno del proyecto.

Las fotografías incluidas son referencias de estilo, no autorización de reutilización. Los logos son reconstrucciones; la tipografía incluida es una sustituta y los colores oficiales no están verificados. Los claims médicos necesitan respaldo y revisión profesional cuando corresponda. La primera carga real en la cuenta del cliente debe verificarse en su navegador.

El código y los materiales de marca se comparten en este repositorio para el proyecto del cliente; la inclusión de recursos no supone cesión de derechos ni autorización para usos fuera de este encargo. La fuente Cormorant Garamond conserva su licencia OFL en `.agents/skills/novaderm-instagram/assets/fonts/OFL.txt`.
