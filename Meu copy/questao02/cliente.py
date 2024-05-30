import socket

server_address = ('127.0.0.1', 5000)
MSG='Primeira mensagemem rede'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# Alteração para UDP
#s.connect(server_address) UDP sem connect()
s.sendto(MSG.encode(), server_address)  # Alteração para sendto em vez de sendall
#No UDP, utiliza-se recvfrom para receber dados, que também retorna o endereço do remetente
data, server = s.recvfrom(1024)  # Alteração para recvfrom em vez de recv
print(f"Mensagem recebida do servidor-{data}")
s.close()