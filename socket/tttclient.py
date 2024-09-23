
import socket
from tictactoe import TicTacToe

client_socket = socket.socket()
client_socket.connect(('192.168.1.6', 12346))
game = TicTacToe()

while True:
    data = ''
    while '\n' not in data:
        data = data + client_socket.recv(1024).decode()
    server_cell_index = int(data.strip('\n'))
    game.make_move(0, server_cell_index)
    game.render_board()
    if game.is_full():
        if game.get_winner() not in ['O', 'X']:
            print('no winner!')
            break
    elif game.get_winner() in ['O', 'X']:
        print('winner is {}'.format(game.get_winner()))
    client_move = int(input('Enter your move here: '))
    if not game.is_valid_move(client_move):
        continue
    game.make_move(1, client_move)  
    game.render_board()
    client_socket.sendall(str(client_move).encode() + b'\n')
    if game.is_full():
        if game.get_winner() not in ['O', 'X']:
            print('no winner!')
            break
    elif game.get_winner() in ['O', 'X']:
        print('winner is {}'.format(game.get_winner()))