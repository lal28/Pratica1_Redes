import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("", 5000)
s.bind(server_address)
s.listen(1)

try:
    while True:

        conn, address = s.accept()
        data = conn.recv(1024)
        print(f"Mensagem recebida do cliente-{data}")

        if not data:
            conn.sendall(data)
        MSG = data.decode().upper()
        conn.sendall(str.encode(MSG))

        conn.close()
        
finally:
    s.close()
