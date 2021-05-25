import Board
import ComputerAI


class Game:
    def __init__(self, who_is_first='X', player_symbol='O', computer_symbol='X'):
        """
        Initialises a Game object
        :param who_is_first: 'X' or 'O' sign for who is going first
        :param player_symbol: 'X' or 'O' sign for a player
        :param computer_symbol: 'X' or 'O' sign for a computer
        """
        self.turn = who_is_first
        self.player = player_symbol
        self.computer = computer_symbol
        self.board = Board.Board()
        self.computer_AI = ComputerAI.ComputerAI(board=self.board, who_is_first=self.turn, player_symbol=self.player,
                                                 computer_symbol=self.computer)

    def start_game(self):
        """
        Starts the game and sets up the object attributes
        """
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
        self.computer_AI = ComputerAI.ComputerAI(board=self.board, who_is_first=self.turn, player_symbol=self.player,
                                                 computer_symbol=self.computer)
        self.turn_structure()

    def turn_structure(self):
        """
        Structures the game
        """
        while True:
            if self.turn == self.player:
                self.board.print_board()
                self.player_turn()
            else:
                self.computer_AI.computer_turn()
            self.endgame_check()
            self.change_turn()

    def player_turn(self):
        """
        A player turn structure
        """
        while True:
            position = str(input('Select a place to make a move: '))
            if self.board.check_if_move_is_possible(position=position):
                break
        self.board.make_a_move(player=self.player, position=position)

    def change_turn(self):
        """
        Change turn structure
        """
        if self.turn == self.player:
            self.turn = self.computer
        else:
            self.turn = self.player

    def endgame_check(self):
        """
        Engame possibilities checks
        """
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
        """
        Play again question structure
        """
        play_again = str.lower(input('\nDo you want to play again? (yes/no - default) '))
        if play_again == 'yes':
            self.board.board = {'7': '7', '8': '8', '9': '9', '4': '4', '5': '5', '6': '6', '1': '1', '2': '2',
                                '3': '3'}
            print()
            self.start_game()
        else:
            exit(0)
