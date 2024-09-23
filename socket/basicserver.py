

import socket

server_socket = socket.socket()
server_socket.bind(('192.168.1.6', 12345))
server_socket.listen()
print('before blocking listen call')

while True:
    client_socket, client_address = server_socket.accept()
    print('after blocking call' + ' ' + str(client_address))
    client_socket.sendall(b'hello from server!' + b'\n')
    client_socket.close()

server_socket.close()