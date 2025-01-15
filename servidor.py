import rpyc
import random
from rpyc.utils.server import ThreadedServer
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="server.log",
                    filemode="a")

class server_matriz(rpyc.Service):
    matriz = None  # Atributo compartido para almacenar la matriz

    def on_connect(self, conn):
        """ Se llama cuando un cliente se conecta """
        logging.info(f"Cliente conectado: {conn}")

    def on_disconnect(self, conn):
        """ Se llama cuando un cliente se desconecta """
        logging.info(f"Cliente desconectado: {conn}")

    def exposed_crear_matriz(self):
        logging.info("Creando matriz 10x10")
        self.matriz = [[0 for _ in range(10)] for _ in range(10)]  # Crear matriz y almacenarla
        return self.matriz

    def exposed_rellenar_matriz(self):
        logging.info("Rellenando matriz con números aleatorios")
        if self.matriz is None:
            raise ValueError("La matriz no ha sido creada.")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                self.matriz[i][j] = random.randint(1, 10)
        return self.matriz

    def exposed_sumar_fila(self, fila):
        if self.matriz is None:
            raise ValueError("La matriz no ha sido creada.")
        suma = sum(self.matriz[fila])
        logging.info(f"Sumando fila {fila}: resultado = {suma}")
        return suma

    def exposed_obtener_matriz(self):
        """ Permitir a otros nodos recuperar la matriz generada por Nodo 0 """
        if self.matriz is None:
            raise ValueError("La matriz no ha sido creada.")
        logging.info("Enviando la matriz a un cliente.")
        return self.matriz

if __name__ == "__main__":
    t = ThreadedServer(server_matriz, port=18812)
    t.start()
