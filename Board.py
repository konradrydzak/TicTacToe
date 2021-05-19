class Board:
    def __init__(self):
        self.board = {'7': '7', '8': '8', '9': '9', '4': '4', '5': '5', '6': '6', '1': '1', '2': '2', '3': '3'}

    def print_board(self):
        print()
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'] + '\n')

    def check_if_move_is_possible(self, position):
        if len(position) == 1:
            if position in '123456789':
                if self.board[position] not in 'XO':
                    return True
        return False

    def make_a_move(self, player, position):
        self.board[position] = player

    def check_if_win(self):
        if ((self.board['1'] == self.board['2'] and self.board['1'] == self.board['3'])
                or (self.board['4'] == self.board['5'] and self.board['4'] == self.board['6'])
                or (self.board['7'] == self.board['8'] and self.board['7'] == self.board['9'])
                or (self.board['1'] == self.board['4'] and self.board['1'] == self.board['7'])
                or (self.board['2'] == self.board['5'] and self.board['2'] == self.board['8'])
                or (self.board['3'] == self.board['6'] and self.board['3'] == self.board['9'])
                or (self.board['1'] == self.board['5'] and self.board['1'] == self.board['9'])
                or (self.board['3'] == self.board['5'] and self.board['3'] == self.board['7'])):
            return True
