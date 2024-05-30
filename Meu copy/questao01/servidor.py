import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("", 5000)
s.bind(server_address)
s.listen(1)

try:
    while True:

        #connection, address = s.accept() #original com erro-nomes da variavel 'connection' é usada como 'conn' nas linhas seguintes
        conn, address = s.accept()#feito alteração no nome da variável
        data = conn.recv(1024)
        print(f"Mensagem recebida do cliente-{data}")

        if not data:
            conn.sendall(data)
        MSG = data.decode().upper()
        conn.sendall(str.encode(MSG))

        conn.close()
        #s.close()#original com erro-servidor não pode fechar a conexão depois da primeira conexão com cliente
finally:
    s.close()#loop dentro do try e fechamento do servidor fora do loop
