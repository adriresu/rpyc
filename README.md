# Proyecto: Suma distribuida de una matriz con RPyC

## Autores
- Daniel Andres Moreno Rey.
- Adrián Resua Vidal.
- Rodrigo Rojas.
- Arturo Lopez.

## Descripción del Proyecto
Este proyecto utiliza **RPyC** para gestionar la suma de una matriz cuyos cálculos se distribuyen entre múltiples nodos (nodo0, nodo1, nodo2 y nodo3) y un servidor central que actúa como punto de coordinación y almacenamiento de la matriz compartida.

---

## Funcionamiento
1. **Servidor**:
   - Se inicia un servidor que conecta los diversos nodos para realizar la suma de las filas de la matriz.

2. **Nodos**:
   - **Nodo 0**: 
     - Crea la matriz inicial y la rellena con valores.
     - Calcula la suma de la fila 0 de la matriz.
   - **Nodo 1**: 
     - Calcula la suma de las filas 1, 2 y 3 de la matriz.
   - **Nodo 2**: 
     - Calcula la suma de las filas 4, 5 y 6 de la matriz.
   - **Nodo 3**: 
     - Calcula la suma de las filas 7, 8 y 9 de la matriz.

---

## Requisitos
1. **Python** (asegúrate de tenerlo instalado en tu sistema).
2. Biblioteca **RPyC**:
   - Instalar con `pip install rpyc`.

---

## Instrucciones de Uso
1. **Crear el entorno virtual**:
   - Si no tienes un entorno virtual creado, ejecútalo con:
     ```bash
     python -m venv venv
     ```
2. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     ./venv/Scripts/activate
     ```
   - En Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
3. **Instalar las dependencias**:
   - Asegúrate de instalar RPyC dentro del entorno virtual:
     ```bash
     pip install rpyc
     ```
4. **Iniciar el servidor**:
   - Ejecuta el siguiente comando:
     ```bash
     python servidor.py
     ```
5. **Iniciar los nodos**:
   - Ejecuta el comando para cada nodo, reemplazando `X` por el número del nodo (0, 1, 2 o 3):
     ```bash
     python nodoX.py
     ```

