import socket

HOST = '127.0.0.1'
PORT = 5000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("TESTE!!!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))