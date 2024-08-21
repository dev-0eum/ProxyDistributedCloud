import socket

server_addr = ('127.0.0.1', 8080)

class Client:
    def __init__(self, name:str) -> None:
        print("CLIENT <", name,">")
        self._name = name
    

    