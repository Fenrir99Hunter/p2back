# P2back
pruebas back end Jacome
____________________________________________________________________________________________________________________________________
WINDOWS


1. Instalar Git
Descarga Git desde: https://git-scm.com/download/win.

Ejecuta el instalador y deja las opciones por defecto (asegúrate de que se agregue al PATH).

Verifica la instalación:

bash
git --version
2. Crear carpeta de trabajo en el escritorio
En el Explorador de Windows, crea una carpeta llamada pruebajacome en el Escritorio.

Abre Visual Studio Code.

En VS Code, selecciona Archivo → Abrir carpeta y elige pruebajacome.

3. Clonar el repositorio desde GitHub
En la terminal integrada de VS Code (PowerShell o Git Bash):

bash
cd ~/Desktop/pruebajacome
git clone https://github.com/Fenrir99Hunter/p2back.git
Esto creará una subcarpeta p2back dentro de pruebajacome.

4. Instalar Python 3.13.7
Descarga desde python.org/downloads la versión 3.13.7.

Durante la instalación, marca la casilla “Add python.exe to PATH”.

Verifica:

bash
python --version
5. Crear y activar entorno virtual
Dentro de la carpeta del proyecto:

bash
cd p2back
python -m venv .venv
.\.venv\Scripts\activate
6. Si falla la activación del entorno virtual
Opción A: Seleccionar intérprete en VS Code

Ctrl+Shift+P → “Python: Seleccionar intérprete” → elige .venv\Scripts\python.exe.

Opción B: Habilitar ejecución de scripts en PowerShell

Abre PowerShell como administrador y ejecuta:

powershell
Set-ExecutionPolicy RemoteSigned
Acepta con S o Y. Reinicia VS Code y vuelve a activar el entorno.

7. Instalar dependencias y correr el servidor
Instala Django:

bash
pip install django
Entra a la carpeta del proyecto:

bash
cd p2back/mysite
Ejecuta el servidor:

bash
python manage.py runserver
__________________________________________________________________________________________________________________
en linux: teorico, no pude probar la VM, nclave olvidada

1. Instalar dependencias básicas
Asegúrate de tener lo necesario:

bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-venv python3-pip -y
2. Clonar el repositorio desde GitHub
bash
cd ~/Escritorio
git clone https://github.com/Fenrir99Hunter/P2back.git pruebajacome
cd pruebajacome


3. Abrir en Visual Studio Code
Si aún no tienes VS Code:

bash
sudo snap install code --classic
Abrir la carpeta:

bash
code ~/Escritorio/pruebajacome
4. Crear y activar entorno virtual
En la terminal integrada de VS Code:

bash
python3 -m venv .venv
source .venv/bin/activate


5. Seleccionar intérprete en VS Code
Ctrl+Shift+P

Escribe Python: Select Interpreter

Elige el que está en .venv/bin/python

6. Instalar Django
Con el entorno virtual activado:

bash
pip install django
7. Ejecutar el proyecto
Según la estructura del repo, entra en la carpeta del proyecto:

bash
cd p2back/mysite
python manage.py runserver
