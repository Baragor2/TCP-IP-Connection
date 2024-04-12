import socket

HOST = '192.168.1.55'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(HOST)
print('waiting...')

client_socket, client_address = server.accept()

print(f'{client_address} connected')

with open('image_server.jpg', mode="wb") as file:
    data = client_socket.recv(2048)
    while data:
        file.write(data)
        data = client_socket.recv(2048)
server.close()
