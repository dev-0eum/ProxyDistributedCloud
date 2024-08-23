import socket

# Instance of Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

class Server:
    #Encapsulation
    def __init__(self, ip, port) -> None:
        self._ip = ip
        self._port = port
        if(ip == "127.0.0.1"):
            print("Proxy Server Open")
        else:
            print("Server <",ip,":",port,"> Opened")
    
    def getIP(self):
        return self._ip;

    def getPort(self):
        return self._port;

    def bind(self):
        server_socket.bind(self._ip, self._port)

    # from Proxy
    def getMess():
        pass
    

# Proxy needs to send message to each Server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inherit Class
class Proxy(Server):
    def __init__ (self,ip, port):
        super().__init__(ip,port)
        
    def setting():
        client_socket.connect()