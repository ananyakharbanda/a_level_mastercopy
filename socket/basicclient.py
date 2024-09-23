
import socket

client_socket = socket.socket()
client_socket.connect(('192.168.1.6', 12345))

data = b''
while b'\n' not in data:
    data = data + client_socket.recv(5)
    print(len(data))
    print('received 5 bytes')
print(len(data))
print(data)

