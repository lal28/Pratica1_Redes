import socket

def conectarCliente(mensagem):
    server_adress = ('127.0.0.1', 5000)
    MSG = mensagem

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_adress)

    s.send(str.encode(MSG))
    data = s.recv(1024)

    print(data)
    s.close()

if __name__ == "__main__":
    conectarCliente()