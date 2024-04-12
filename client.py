import socket

HOST = "192.168.1.55"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    with open('cat.jpg', mode="rb") as file:
        data = file.read(2048)
        while data:
            client.send(data)
            data = file.read(2048)