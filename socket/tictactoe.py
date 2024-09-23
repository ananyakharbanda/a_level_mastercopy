

class TicTacToe():
    def __init__(self):
        self.game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.players = ['O', 'X']

    def render_row(self, row_index):
        print('{} | {} | {}'.format(self.game[row_index][0], self.game[row_index][1], self.game[row_index][2]))
        print('-'*10)

    def render_board(self):
        for i in range(3):
            self.render_row(i)

    def cell2rowandcolumn(self, cell_index):
        if cell_index == 1:
            return (0,0)
        if cell_index == 2:
            return (0,1)
        if cell_index == 3:
            return (0,2)
        if cell_index == 4:
            return (1,0)
        if cell_index == 5:
            return (1,1)
        if cell_index == 6:
            return (1,2)
        if cell_index == 7:
            return (2,0)
        if cell_index == 8:
            return (2,1)
        if cell_index == 9:
            return (2,2)
        
    def make_move(self, player_index, cell_index):
        if not self.is_valid_move(cell_index):
            print('invalid move!')
            return 
        else:
            row, column = self.cell2rowandcolumn(cell_index)
            self.game[row][column] = self.players[player_index]


    def is_valid_move(self, cell_index):
        row, column = self.cell2rowandcolumn(cell_index)
        if self.game[row][column] in ['O', 'X']:
            return False
        return True
        
    def is_full(self):
        for row in self.game:
            for slot in row:
                if slot not in ['O', 'X']:
                    return False
        return True

    def get_winner(self):
        winner = ''
        for row in self.game:
            first_slot = row[0]
            count = 0
            for slot in row:
                if slot == first_slot:
                    count += 1
            if count == 3:
                winner = first_slot
        if winner != '':
            return winner

        columns = [[], [], []]
        for row in self.game:
            for i in range(3):
                columns[i].append(row[i])
        for column in columns:
            first_slot = column[0]
            count = 0
            for slot in column:
                if slot == first_slot:
                    count += 1
            if count == 3:
                winner = first_slot
        if winner != '':
            return winner
        
        diagonals = [[self.game[0][0], self.game[1][1], self.game[2][2]], [self.game[0][2], self.game[1][1], self.game[2][0]]]
        for diagonal in diagonals:
            first_slot = diagonal[0]
            count = 0
            for slot in diagonal:
                if slot == first_slot:
                    count += 1
            if count == 3:
                winner = first_slot
        if winner != '':
            return winner
        print('no winner!')
        return None 

# ttt = TicTacToe()
# ttt.render_board()

# while True:
#     user_inp_player = int(input('Enter your player_index here: '))
#     user_inp_cell = int(input('Enter your cell index here: '))
#     ttt.make_move(user_inp_player, user_inp_cell)
#     x = ttt.get_winner()
#     if x != '':
#         break
#     ttt.render_board()
