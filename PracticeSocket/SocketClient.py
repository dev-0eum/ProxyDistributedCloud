import socket

print("hello")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("world")
server_addr = ('127.0.0.1', 8080)
print("server info served...")

client_socket.connect((server_addr))
print("connected to server")

while True:
    try:
        data = input(">> ")
        if data == 'exit':
            break
        data = data.encode()
        client_socket.send(data)

        re = client_socket.recv(1024).decode()
        print("Server: ",re)
    finally:
        pass

client_socket.close()



def recv_message():
	message = client_socket.recv(1024).decode()
    