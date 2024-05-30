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
        MSG=data.decode('utf-8')
        #Verificar se a mensagem é um número
        if MSG.isdigit():
            print(f"A mensagem recebida e um numero:{MSG}")
            MSG=int(MSG)*2 #Fazer a multiplicação
            MSG=str(f"A multiplicacao por 2= {MSG}")
            conn.send(str.encode(MSG))
        else:
            MSG=data.decode('utf-8').upper()    
            conn.send(str.encode(MSG))

        conn.close()
        
finally:
    s.close()
