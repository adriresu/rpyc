import rpyc
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="nodo2.log",
                    filemode="a")

class Nodo2:
    def __init__(self, host="localhost", port=18812):
        self.conn = rpyc.connect(host, port)
        logging.info("Nodo 2 conectado al servidor en %s:%s.", host, port)
        print("Nodo 2 conectado al servidor.")

if __name__ == "__main__":
    nodo2 = Nodo2()
    suma = 0
    flag = True
    while flag:
        try:
            for fila in range(4, 7):
                suma = nodo2.conn.root.sumar_fila(fila)
            flag = False
        except Exception as e:
            logging.error("Nodo 0 aún no ha creado la matriz.")
            time.sleep(1)

    nodo2.conn.root.get_suma_total(suma, 1)
    logging.info("Se sumaron las filas 4,5,6 por el nodo 2:")
    logging.info(suma)

    nodo2.conn.close()
