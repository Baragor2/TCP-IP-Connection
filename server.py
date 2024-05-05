import socket

HOST = 'localhost'
PORT = 65432
BUFFER_SIZE = 2048


def make_connection(host: str, port: int) -> socket:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    return server


def communicate_with_client(host: str) -> None:
    print(host)
    print('waiting...')


def get_client(server: socket) -> tuple[socket, socket]:
    client_socket, client_address = server.accept()
    print(f'{client_address} connected')
    return client_socket, client_address


def get_file_name(client_socket: socket, buffer: int) -> str:
    file_name = 'server_' + client_socket.recv(buffer).decode()
    return file_name


def download_file(file_name: str, client_socket: socket, buffer: int) -> None:
    with open(file_name, mode="wb") as file:
        data = client_socket.recv(buffer)
        while data:
            file.write(data)
            data = client_socket.recv(buffer)


def main():
    server = make_connection(HOST, PORT)
    communicate_with_client(HOST)
    client_socket, client_address = get_client(server)
    file_name = get_file_name(client_socket, BUFFER_SIZE)
    download_file(file_name, client_socket, BUFFER_SIZE)


if __name__ == '__main__':
    main()
