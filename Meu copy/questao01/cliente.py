import socket

server_address = ('127.0.0.1', 5000)
MSG='Primeira mensagemem rede'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
s.sendall(str.encode(MSG))
data = s.recv(1024)
print(f"Mensagem recebida do servidor-{data}")
s.close()