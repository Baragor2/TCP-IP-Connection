import socket

HOST = "localhost"
PORT = 65432



def send_file(file_name: str, host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        client.send(bytes(file_name, encoding='utf-8'))

        with open(file_name, 'rb') as file:
            client.sendfile(file)


def main() -> None:
    file_name = input()
    send_file(file_name, HOST, PORT)


if __name__ == '__main__':
    main()