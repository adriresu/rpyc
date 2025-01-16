import rpyc
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename="nodo3.log",
                    filemode="a")

class Nodo3:
    def __init__(self, host="localhost", port=18812):
        self.conn = rpyc.connect(host, port)
        logging.info("Nodo 3 conectado al servidor en %s:%s.", host, port)
        print("Nodo 3 conectado al servidor.")

if __name__ == "__main__":
    nodo3 = Nodo3()
    suma = 0
    flag = True
    while flag:
        try:
            for fila in range(8, 10):
                suma = nodo3.conn.root.sumar_fila(fila)
            flag = False
        except Exception as e:
            logging.error("Nodo 0 aún no ha creado la matriz.")
            time.sleep(1)

    nodo3.conn.root.get_suma_total(suma, 1)
    logging.info("Se sumaron las filas 7,8,9 por el nodo 3:")
    logging.info(suma)

    nodo3.conn.close()
