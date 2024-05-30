import socket

HOST = '127.0.0.1'
PORT=5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)

while True:
    connection, address = server.accept()
    print(f"Conecyado ao endereço{address}")
    message = connection.recv(1024).decode('utf-8')
    print(f"Mensagem do cliente é:{message}")
    connection.send(f"recebi sua mensagem".encode('utf-8'))
    connection.close()
    print(f"Conexão com {address} foi fechada")