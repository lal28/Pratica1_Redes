import socket
import multiprocessing #importar multiprocessing

#Função Cliente
#por conta do funcionamento do multiprocesso, a mensagem digitada vai ser passada como parâmetro da função
def conectarCliente(mensagem):#Encapsular em uma função
    IP=socket.gethostbyname(socket.gethostname())
    server_address = (IP, 5000)
    MSG=mensagem
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_address)
    s.sendall(str.encode(MSG))
    data = s.recv(1024)
    print(f"Mensagem recebida do servidor-{data}")
    s.close()

#Função Servidor
def iniciarServer():
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

#Multiprocessos        
if __name__=='__main__':
    mensagem=input("Qual mensagem deseja enviar?")
    processoServidor=multiprocessing.Process(target=iniciarServer)
    processoCliente=multiprocessing.Process(target=conectarCliente, args=(mensagem,))

    processoServidor.start()
    processoCliente.start()

    processoCliente.join()
    processoServidor.terminate()
