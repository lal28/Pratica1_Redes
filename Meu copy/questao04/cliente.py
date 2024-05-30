import socket

IP=socket.gethostbyname(socket.gethostname())
server_address = (IP, 5000)
MSG=input("Digite a mensagem a ser enviada para o servidor: ")#trocar para input
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
s.sendall(str.encode(MSG))
data = s.recv(1024)
print(f"Mensagem recebida do servidor-{data}")
s.close()