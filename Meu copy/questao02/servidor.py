import socket
'''
UDP (User Datagram Protocol) é sem conexão e não garante entrega, 
ordem ou verificação de erros. Ele é mais rápido, 
mas menos confiável em comparação ao TCP

*Foram mantidas as alterações do código da primeira questão
Já que os erros impediam o funcionamento do código
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# Alteração para UDP
server_address = ("", 5000)
s.bind(server_address)
#Não há um processo de estabelecimento de conexão (como o handshake de três vias em TCP)
#s.listen(1)# UDP não usa listen()

try:
    while True:

        #conn, address = s.accept() #UDP não usa accept()
        #No UDP, utiliza-se recvfrom para receber dados, que também retorna o endereço do remetente
        data, address = s.recvfrom(1024) # Alteração para recvfrom em vez de recv
        print(f"Mensagem recebida do cliente-{data}")

        if data:
            #conn.sendall(data)# UDP não checa se os dados foram enviados
            MSG = data.decode().upper()
            #No UDP, utiliza-se sendto para enviar dados para um endereço específico.
            s.sendto(str.encode(MSG), address)# Alteração para sendto em vez de sendall

        #conn.close() UDP é um protocolo sem conexão
        
finally:
    # Fecha o socket
    s.close()
    
