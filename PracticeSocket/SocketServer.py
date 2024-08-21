import socket

# Instance of Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Server(Socket) INFO
server_address = ('127.0.0.1', 8080)
print('Start up on {} port {}'.format(*server_address))

# Bind Socket info = socket instance + addr
server_socket.bind(server_address)

# Listen
server_socket.listen(1)

print('accept wait')
# 클라이언트 접속 대기
client_socket, client_addr = server_socket.accept()

print("Connected!")
try:
    while True:
        try:
            print("Waiting for Client message...")
            # 클라이언트가 보낸 데이터 수령(1024byte) + 문자열 복호화
            data = client_socket.recv(1024).decode()
            if not data:
                print("클라이언트가 연결을 종료했습니다.")
                break
            if data == 'exit':
                print("Client has disconnected.")
                break
            print("Client: ", data)

            response = input('>> ')
            response = response.encode()
            client_socket.sendall(response)
        except ConnectionResetError:
            print("클라이언트와의 연결이 끊어졌습니다.")
            break
        except BrokenPipeError:
            print("데이터 전송 중 오류가 발생했습니다. 클라이언트가 연결을 종료했을 수 있습니다.")
            break
finally:
    client_socket.close()
    server_socket.close()
