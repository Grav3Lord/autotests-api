import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Используем 127.0.0.1 вместо localhost, чтобы избежать проблем с резолвингом:
    # 'localhost' может резолвиться в IPv6-адресс ::1, а сокет создан как IPv4 aka AF_INET.
    server_address = ("127.0.0.1", 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)

    # Список для хранения сообщений
    messages = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        messages.append(data)

        response = "\n".join(messages)
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    server()
