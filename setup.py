#!/usr/bin/env python3
"""Prepara únicamente el entorno local de las skills de este proyecto."""
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "Grupo Novaderm"
ENV = PROJECT / ".herramientas" / "novaderm-python"
REQUIREMENTS = ROOT / ".agents" / "skills" / "novaderm-instagram" / "scripts" / "requirements.txt"


def main():
    if sys.version_info < (3, 11):
        raise SystemExit("Se necesita Python 3.11 o superior. Instálalo y vuelve a ejecutar este comando.")
    exe = ENV / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    if not exe.is_file():
        print("Creando entorno local de Python…", flush=True)
        venv.create(ENV, with_pip=True)
    print("Instalando dependencias del proyecto…", flush=True)
    subprocess.run([str(exe), "-m", "pip", "install", "-r", str(REQUIREMENTS)], check=True)
    print("Instalando el navegador de renderizado de Playwright…", flush=True)
    subprocess.run([str(exe), "-m", "playwright", "install", "chromium"], check=True)
    tool = ROOT / ".agents" / "skills" / "novaderm-instagram" / "scripts" / "novaderm.py"
    subprocess.run([str(exe), str(tool), "verify-package"], check=True)
    subprocess.run([str(exe), str(tool), "paths"], check=True)
    print("Entorno preparado. Abre esta carpeta como proyecto de Codex.", flush=True)


if __name__ == "__main__":
    main()
