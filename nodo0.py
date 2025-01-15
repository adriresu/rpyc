import rpyc
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="nodo0.log",
    filemode="a"
)

class Nodo0:
    def __init__(self, host="localhost", port=18812):
        self.conn = rpyc.connect(host, port)
        logging.info("Nodo 0 conectado al servidor en %s:%s.", host, port)
        print("Nodo 0 conectado al servidor.")

    def crear_y_rellenar_matriz(self):
        logging.info("Nodo 0 solicita creación de matriz.")
        print("Creando matriz en el servidor...")
        self.conn.root.crear_matriz()
        logging.info("Nodo 0 solicita rellenar la matriz con números aleatorios.")
        print("Rellenando matriz en el servidor...")
        matriz = self.conn.root.rellenar_matriz()
        logging.info("Matriz generada por Nodo 0:")
        for fila in matriz:
            logging.info(fila)
        return matriz

    def sumar_fila_0(self):
        suma = self.conn.root.sumar_fila(0)
        logging.info(f"Suma de la fila 0 por Nodo 0: {suma}")
        print(f"Suma de la fila 0: {suma}")
        return suma

    def cerrar_conexion(self):
        self.conn.close()
        logging.info("Conexión cerrada por Nodo 0.")
        print("Conexión cerrada.")

if __name__ == "__main__":
    nodo0 = Nodo0()
    matriz = nodo0.crear_y_rellenar_matriz()
    nodo0.sumar_fila_0()
    nodo0.cerrar_conexion()
