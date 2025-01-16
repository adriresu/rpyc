import rpyc
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="nodo0.log",
                    filemode="a")

class Nodo0:
    def __init__(self, host="localhost", port=18812):
        self.conn = rpyc.connect(host, port)
        logging.info("Nodo 0 conectado al servidor en %s:%s.", host, port)

if __name__ == "__main__":
    nodo0 = Nodo0()
    matriz = nodo0.conn.root.crear_matriz()
    matriz = nodo0.conn.root.rellenar_matriz()
    logging.info("Matriz generada por Nodo 0:")
    for fila in matriz:
        logging.info("Fila 1: %s", fila)

    suma_fila_1 = nodo0.conn.root.sumar_fila(0)

    while True:
        suma_total = nodo0.conn.root.get_suma_total(suma_fila_1, 0)
        if suma_total:
            logging.info("La suma total de la matriz es: %s", suma_total)
            nodo0.conn.close()
            break
        else:
            logging.info("Esperando que la suma de las filas de las matrices se realice...")
            time.sleep(1)
