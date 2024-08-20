import socket

# Instance of Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server(Socket) INFO
server_address = ('127.0.0.1', 8080)
print('Start up on {} port {}'.format(*server_address))

# Bind Socket info = socket instance + addr
server_socket.bind((server_address))

# Listen
server_socket.listen(1)

while True:
	print('accept wait')
    # 클라이언트 접속 대기
	client_socket, client_addr = server_socket.accept()
	
    # 이하 코드는 client가 accept되어야 실행 
	try:
		# 클라이언트가 보낸 데이터 수령(1024byte) + 문자열 복호화
		data = client_socket.recv(1024).decode()
		if(data == 'exit'):
			break
		print("Client: ",data)
		re = input('>> ')
		re = re.encode()
		server_socket.send(re)
	except Exception as err:
		# 클라이언트 소켓 연결 끊기
		client_socket.close()
	finally: # 모든 작업이 종료
		pass
		# client_socket.close()
		
client_socket.close()