import rpyc
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="nodo1.log",
                    filemode="a")

class Nodo1:
    def __init__(self, host="localhost", port=18812):
        self.conn = rpyc.connect(host, port)
        logging.info("Nodo 1 conectado al servidor en %s:%s.", host, port)
        print("Nodo 1 conectado al servidor.")

if __name__ == "__main__":
    nodo1 = Nodo1()
    suma = 0
    flag = True
    while flag:
        try:
            for fila in range(1, 3):
                suma = nodo1.conn.root.sumar_fila(fila)
            flag = False
        except Exception as e:
            logging.error("Nodo 0 aún no ha creado la matriz.")
            time.sleep(1)

    nodo1.conn.root.get_suma_total(suma, 1)
    logging.info("Se sumaron las filas 1,2,3 por el nodo 1:")
    logging.info(suma)

    nodo1.conn.close()
