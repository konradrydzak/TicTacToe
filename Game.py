import Board
import ComputerAI


class Game:
    def __init__(self, who_is_first='X', player_symbol='O', computer_symbol='X'):
        self.turn = who_is_first
        self.player = player_symbol
        self.computer = computer_symbol
        self.board = Board.Board()
        self.computer_AI = ComputerAI.ComputerAI(self.board, self.turn, self.player, self.computer)

    def start_game(self):
        is_starting = str.lower(input('Do you want to start? (yes/no - default) '))
        player_symbol = str.upper(input('Do you want to be X or O? (X/O - default) '))
        if player_symbol == 'X':
            self.player = 'X'
            self.computer = 'O'
        else:
            self.player = 'O'
            self.computer = 'X'
        if is_starting == 'yes':
            self.turn = self.player
        else:
            self.turn = self.computer
        self.computer_AI = ComputerAI.ComputerAI(self.board, self.turn, self.player, self.computer)
        self.turn_structure()

    def turn_structure(self):
        while True:
            if self.turn == self.player:
                self.board.print_board()
                self.player_turn()
            else:
                self.computer_AI.computer_turn()
            self.endgame_check()
            self.change_turn()

    def player_turn(self):
        while True:
            position = str(input('Select a place to make a move: '))
            if self.board.check_if_move_is_possible(position):
                break
        self.board.make_a_move(self.player, position)

    def change_turn(self):
        if self.turn == self.player:
            self.turn = self.computer
        else:
            self.turn = self.player

    def endgame_check(self):
        if self.board.check_if_win():
            self.board.print_board()
            if self.turn == self.player:
                print('Congrats! You win!')
            else:
                print('Unfortunately, computer won.')
            self.play_again()
        else:
            for i in range(1, 10):
                if self.board.board[str(i)] not in 'XO':
                    break
                if i == 9:
                    self.board.print_board()
                    print('It\'s a draw')
                    self.play_again()

    def play_again(self):
        play_again = str.lower(input('\nDo you want to play again? (yes/no - default) '))
        if play_again == 'yes':
            self.board.board = {'7': '7', '8': '8', '9': '9', '4': '4', '5': '5', '6': '6', '1': '1', '2': '2',
                                '3': '3'}
            print()
            self.start_game()
        else:
            exit(0)
