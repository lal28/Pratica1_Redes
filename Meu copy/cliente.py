import socket



def conectarCliente(mensagem):

    #variável onde armazenaremos uma tupla contendo o endereço IP do
    #servidor e o socket no qual ele estará aguardando o recebimento da mensagem
    #IP='192.168.18.4'
    IP=socket.gethostbyname(socket.gethostname())
    server_adress=(IP,5000)
    #mensagem que será enviada para o servidor
    #MSG="Primeira mensagem em rede"
    MSG=mensagem

    #novo socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #iniciar a conexão
    s.connect(server_adress) 

    #enviar a mensagem
    s.send(str.encode(MSG))
    
    #aguardamos a resposta do servidor
    data=s.recv(1024).decode('utf-8')

    #imprimir a mensagem do servidor
    print(data)

    #Feche a conexão
    s.close()
