import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
Existem várias maneiras de visualizar o endereço IP 
local da rede em diferentes sistemas operacionais. 
Alguns métodos comuns:
Windows -'ipconfig', usando as configurações de rede do sistema
MAC - 'ifconfig', usando as preferências de sistema
Linux - 'ifconfig', 'ip addr show', preferências do sistema(depende da interface)

É possível também implementar no próprio códico uma forma de obter o endereço de ip usando o método
socket.gethostbyname(socket.gethostname())
'''

server_address = ('', 5000)
s.bind(server_address)
s.listen(1)

try:
    while True:

        conn, address = s.accept()
        data = conn.recv(1024)
        print(f"Mensagem recebida do cliente {address}-{data}")

        if not data:
            conn.sendall(data)
        MSG = data.decode().upper()
        conn.sendall(str.encode(MSG))

        conn.close()
        
finally:
    s.close()
