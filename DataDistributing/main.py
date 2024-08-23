import client as cp
import server as sp

info = ("127.0.0.1",80)

client1 = cp.Client("16.64.1.1")
client2 = cp.Client("16.64.1.2")
client3 = cp.Client("16.64.1.3")
client4 = cp.Client("16.64.1.4")

proxy_server = sp.Proxy(info[0],info[1])

server1 = sp.Server("127.0.0.2",8080)
server2 = sp.Server("127.0.0.3",8080)
server3 = sp.Server("127.0.0.4",8080)
server4 = sp.Server("127.0.0.5",8080)

# Clients send messages to proxy server
## proxy bind, listen, accept
## client connect, send
### proxy recv
### server bind,listen, accept
print(proxy_server.getPort())
# Proxy Server transfer data to Server