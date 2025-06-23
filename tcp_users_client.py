import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 12345)
client_socket.connect(server_address)

message = "Привет, сервер!"
client_socket.send(message.encode())

response = client_socket.recv(1024)
print(response.decode())

client_socket.close()
