from multiprocessing import Process
import servidor
import cliente

def run_server():
    servidor.iniciarServer()

def run_client(mensagem):
    cliente.conectarCliente(mensagem)

if __name__ == "__main__":

    mensagem=input("Qual a mensagem?")
    server_process = Process(target=run_server)
    client_process = Process(target=run_client, args=(mensagem,))

    server_process.start()
    client_process.start()

    client_process.join()  # Aguarda o cliente terminar
    server_process.terminate()  # Termina o servidor