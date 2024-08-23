import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_server_addr = ('127.0.0.1', 8080) # destination ip

class Client:
    def __init__(self, ip) -> None:
        print("CLIENT <", ip,">")
        self._ip = ip
    
    # to Proxy
    def sendMess(self, dest_ip, message):
        pass

    