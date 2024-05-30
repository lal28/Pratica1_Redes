import socket
import cliente
import multiprocessing
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#endereço e porta que o servido vai escutar
#"" significa que vai escutar de todas as interfaces
#IP='192.168.18.4'
IP=socket.gethostbyname(socket.gethostname())
s_adress=(IP, 5000)


def iniciarServer():
    #servidor esperar por conexões
    s.bind(s_adress)
    #escutar as conexões, o parametro especifica a quantidade de conexões aceitas
    s.listen(1)

    try:
        while True:
            
            connection, address= s.accept()
            print(f"Conectado ao cliente {address}")
            #receber a mensagem do cliente, parametro é quantidade de bytes da mensagem
            data=connection.recv(1024)
            print(f"Mensagem recebida do CLiente:{data}")
            
       

            if not data:
                connection.sendall(data)
            MSG=data.decode('utf-8')
            if MSG.isdigit():
                print(f"A mensagem recebida é um número!:{MSG}")
                MSG=int(MSG)*2
                MSG=str(f"A mensagem recebida é um número,a multiplicação por 2= {MSG}")
                connection.send(str.encode(MSG))
            else:
                MSG=data.decode('utf-8').upper()    
                connection.send(str.encode(MSG))
                


            

            connection.close()
            print("conexão encerrada")
    finally:
        s.close()
        print("Servidor encerrado")

if __name__=='__main__':
    mensagem=input("Qual mensagem deseja enviar?")
    processoServidor=multiprocessing.Process(target=iniciarServer)
    processoCliente=multiprocessing.Process(target=cliente.conectarCliente, args=(mensagem,))

    processoServidor.start()
    processoCliente.start()

    processoCliente.join()
    processoServidor.terminate()