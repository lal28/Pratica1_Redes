import socket

#Trocar para o ip local com o próprio método do socket
IP=socket.gethostbyname(socket.gethostname())
#IP='192.168.18.4' #De forma alternativa, pode ser olhado no sistema e escrito manualmente
server_address = (IP, 5000)
MSG='Primeira mensagemem rede'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
s.sendall(str.encode(MSG))
data = s.recv(1024)
print(f"Mensagem recebida do servidor-{data}")
s.close()