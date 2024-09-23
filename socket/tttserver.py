
import socket
from tictactoe import TicTacToe

server_socket = socket.socket()
server_socket.bind(('192.168.1.6', 12346))
server_socket.listen()

client_socket, client_addr = server_socket.accept()

game = TicTacToe()
while True:
    cell_index = int(input('Enter cell index here: '))
    if not game.is_valid_move(cell_index):
        continue
    game.make_move(0, cell_index)   
    client_socket.sendall(str(cell_index).encode() + b'\n')
    game.render_board()
    if game.is_full():
        if game.get_winner() not in ['O', 'X']:
            print('no winner!')
            break
    elif game.get_winner() in ['O', 'X']:
        print('winner is {}'.format(game.get_winner()))
    data = ''
    while '\n' not in data:
        data = data + client_socket.recv(1024).decode()
    client_cell_index = int(data.strip('\n'))
    game.make_move(1, client_cell_index)
    game.render_board()
    if game.is_full():
        if game.get_winner() not in ['O', 'X']:
            print('no winner!')
            break
    elif game.get_winner() in ['O', 'X']:
        print('winner is {}'.format(game.get_winner()))
