import rpyc
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='master.log', filemode='a')

class MasterService(rpyc.Service):
    def on_connect(self, conn):
        """ Se llama cuando un cliente se conecta """
        logging.info(f"Cliente conectado: {conn}")

    def exposed_initialize_and_delegate(self):
        # Crear y rellenar la matriz
        conn_local = rpyc.connect("localhost", 18812)  # Conectar al servidor que tiene las funciones
        matriz = conn_local.root.exposed_crear_matriz()
        matriz = conn_local.root.exposed_rellenar_matriz(matriz)
        conn_local.close()

        results = []
        
        # Distribuir la suma de cada fila a los nodos trabajadores
        for i in range(10):
            worker_port = 20000 + i  # Puertos de los trabajadores del 20000 al 20009
            conn = rpyc.connect("localhost", worker_port)
            sum_fila = conn.root.exposed_sumar_fila(matriz, i)
            results.append(sum_fila)
            conn.close()

        total_sum = sum(results)
        logging.info(f"Suma total de todas las filas: {total_sum}")
        return results, total_sum

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MasterService, port=18811)  # El puerto del maestro debe ser diferente
    t.start()
