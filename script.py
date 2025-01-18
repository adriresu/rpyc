import subprocess
import time
import os

# Ruta del ejecutable de Python en el entorno virtual
venv_python = os.path.join(os.getcwd(), "../.venv", "Scripts", "python.exe")

# Ejecutar el servidor en segundo plano
server_process = subprocess.Popen([venv_python, "servidor.py"])

# Esperar 2 segundos antes de ejecutar los nodos
time.sleep(2)

# Ejecutar los nodos en paralelo dentro del entorno virtual
nodo_scripts = ["nodo0.py", "nodo1.py", "nodo2.py", "nodo3.py"]
nodo_processes = [subprocess.Popen([venv_python, nodo]) for nodo in nodo_scripts]

# Esperar a que todos los procesos terminen
server_process.wait()
for process in nodo_processes:
    process.wait()
