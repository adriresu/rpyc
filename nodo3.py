import rpyc
import logging
import time

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="nodo3.log",
    filemode="a"
)

class NodoCliente:
    def __init__(self, host="localhost", port=18812, filas=None):
        self.conn = rpyc.connect(host, port)
        self.filas = filas
        logging.info(f"Nodo Cliente conectado al servidor en {host}:{port}.")
        print("Nodo Cliente conectado al servidor.")

    def obtener_matriz(self):
        logging.info("Nodo Cliente solicita la matriz al servidor.")
        intentos = 10  # Máximo número de intentos
        for _ in range(intentos):
            try:
                matriz = self.conn.root.obtener_matriz()
                logging.info("Matriz recibida por Nodo Cliente:")
                for fila in matriz:
                    logging.info(fila)
                return matriz
            except ValueError:
                logging.warning("Matriz no disponible. Reintentando en 1 segundo...")
                time.sleep(1)
        raise RuntimeError("No se pudo obtener la matriz después de varios intentos.")

    def sumar_filas_asignadas(self, matriz):
        resultados = {}
        for fila in self.filas:
            suma = self.conn.root.sumar_fila(fila)
            resultados[fila] = suma
            logging.info(f"Suma de la fila {fila} por Nodo Cliente: {suma}")
            print(f"Suma de la fila {fila}: {suma}")
        return resultados

    def cerrar_conexion(self):
        self.conn.close()
        logging.info("Conexión cerrada por Nodo Cliente.")
        print("Conexión cerrada.")

if __name__ == "__main__":
    # Nodo 3 suma las filas 7, 8 y 9
    nodo3 = NodoCliente(filas=[7, 8, 9])
    matriz = nodo3.obtener_matriz()
    nodo3.sumar_filas_asignadas(matriz)
    nodo3.cerrar_conexion()
