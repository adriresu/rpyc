import rpyc
import random
from rpyc.utils.server import ThreadedServer
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='server.log',
                    filemode='a')

class server_matriz(rpyc.Service):
    def on_connect(self, conn):
        """ Se llama cuando un cliente se conecta """
        logging.info(f"Cliente conectado: {conn}")

    def on_disconnect(self, conn):
        """ Se llama cuando un cliente se desconecta """
        logging.info(f"Cliente desconectado: {conn}")

    def exposed_crear_matriz(self):
        logging.info("Creando matriz 10x10")
        return [[0 for _ in range(10)] for _ in range(10)]

    def exposed_rellenar_matriz(self, matriz):
        logging.info("Rellenando matriz con números aleatorios")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = random.randint(1, 10)
        return matriz

    def exposed_sumar_fila(self, matriz, fila):
        suma = 0
        for i in range(len(matriz[fila])):
            suma += matriz[fila][i]
        logging.info(f"Sumando fila {fila}: resultado = {suma}")
        return suma

if __name__ == "__main__":
    t = ThreadedServer(server_matriz, port=18812)
    t.start()
