import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8080)
print("server info served...")

client_socket.connect(server_addr)
print("connected to server")

try:
    while True:
        data = input(">> ")
        if data == 'exit':
            break
        data = data.encode()
        client_socket.sendall(data)

        print("Waiting for Server Response...")

        try:
            response = client_socket.recv(1024).decode()
            print("Server: ", response)
        except ConnectionResetError:
            print("서버와의 연결이 끊어졌습니다.")
            break
finally:
    client_socket.close()
