import rpyc
import random
import logging
from rpyc.utils.server import ThreadedServer
import threading

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="server.log",
                    filemode="a")

class server_matriz(rpyc.Service):
    def __init__(self):
        self.matriz_compartida = None
        self.matriz_disponible = False
        self.client_connections = 0
        self.suma_total = 0
        self.lock = threading.Lock()

    def on_connect(self, conn):
        """ Se llama cuando un cliente se conecta """
        logging.info(f"Cliente conectado: {conn}")

    def on_disconnect(self, conn):
        """ Se llama cuando un cliente se desconecta """
        logging.info(f"Cliente desconectado: {conn}")

    def exposed_crear_matriz(self):
        with self.lock:
            logging.info("Creando matriz 10x10")
            matriz = [[0 for _ in range(10)] for _ in range(10)]
            self.suma_total = 0
            self.client_connections = 0
            self.matriz_compartida = matriz
            self.matriz_disponible = False
            return matriz

    def exposed_rellenar_matriz(self):
        with self.lock:
            logging.info("Rellenando matriz con números aleatorios")
            for i in range(len(self.matriz_compartida)):
                for j in range(len(self.matriz_compartida[i])):
                    self.matriz_compartida[i][j] = random.randint(1, 10)
            self.matriz_disponible = True
            return self.matriz_compartida

    def exposed_sumar_fila(self, fila):
        with self.lock:
            suma = 0
            for i in range(len(self.matriz_compartida[fila])):
                suma += self.matriz_compartida[fila][i]
            logging.info(f"Sumando fila {fila}: resultado = {suma}")
            return suma

    def exposed_obtener_matriz(self):
        with self.lock:
            if not self.matriz_disponible:
                raise ValueError("La matriz no está disponible.")
            logging.info("Matriz enviada a un cliente")
            return self.matriz_compartida

    def exposed_get_suma_total(self, suma, entidad):
        with self.lock:
            if entidad == 0:
                if self.client_connections != 3:
                    return False
                else:
                    self.suma_total += suma
                    logging.info("La suma total de la matriz: \n%s\n%s", self.matriz_compartida, self.suma_total)
                    return self.suma_total
            elif entidad == 1:
                self.suma_total += suma
                self.client_connections += 1
                return

if __name__ == "__main__":
    service_instance = server_matriz()
    t = ThreadedServer(
        service=service_instance,
        port=18812,
        protocol_config={"allow_all_attrs": True}
    )
    t.start()
