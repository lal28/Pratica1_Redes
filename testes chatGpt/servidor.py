import socket

def iniciarServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_adress = ('127.0.0.1', 5000)

    s.bind(s_adress)
    s.listen(1)

    try:
        while True:
            connection, address = s.accept()
            print(f"Conectado a {address}")
            data = connection.recv(1024)
            print(f"Mensagem recebida: {data}")

            if not data:
                connection.sendall(data)
            MSG = data.decode().upper()

            connection.send(str.encode(MSG))
            connection.close()
            print("conexão encerrada")
    finally:
        s.close()
        print("Servidor encerrado")

if __name__ == "__main__":
    iniciarServer()