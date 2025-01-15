import rpyc
import random
from rpyc.utils.server import ThreadedServer
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="server.log",
                    filemode="a")

class server_matriz(rpyc.Service):
    matriz = None  # Variable estática compartida entre todas las conexiones

    def on_connect(self, conn):
        """ Se llama cuando un cliente se conecta """
        logging.info(f"Cliente conectado: {conn}")

    def on_disconnect(self, conn):
        """ Se llama cuando un cliente se desconecta """
        logging.info(f"Cliente desconectado: {conn}")

    def exposed_crear_matriz(self):
        logging.info("Creando matriz 10x10")
        server_matriz.matriz = [[0 for _ in range(10)] for _ in range(10)]  # Crear matriz y almacenarla
        logging.info(f"Matriz creada: {server_matriz.matriz}")
        return server_matriz.matriz

    def exposed_rellenar_matriz(self):
        logging.info("Rellenando matriz con números aleatorios")
        if server_matriz.matriz is None:
            raise ValueError("La matriz no ha sido creada.")
        for i in range(len(server_matriz.matriz)):
            for j in range(len(server_matriz.matriz[i])):
                server_matriz.matriz[i][j] = random.randint(1, 10)
        logging.info(f"Matriz rellenada: {server_matriz.matriz}")
        return server_matriz.matriz

    def exposed_sumar_fila(self, fila):
        if server_matriz.matriz is None:
            raise ValueError("La matriz no ha sido creada.")
        suma = sum(server_matriz.matriz[fila])
        logging.info(f"Sumando fila {fila}: resultado = {suma}")
        return suma

    def exposed_obtener_matriz(self):
        """ Permitir a otros nodos recuperar la matriz generada por Nodo 0 """
        if server_matriz.matriz is None:
            logging.warning("La matriz no está disponible en el servidor.")
            raise ValueError("La matriz no ha sido creada.")
        logging.info(f"Enviando la matriz al cliente: {server_matriz.matriz}")
        return server_matriz.matriz

if __name__ == "__main__":
    t = ThreadedServer(server_matriz, port=18812)
    t.start()
