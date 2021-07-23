import Board
import ComputerAI

import pygame
from pygame.locals import *

# TODO Add visual representation of the state of the game

width = 550
height = 550


def initializing_window():
    pygame.init()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('TicTacToe')

    # White background
    window.fill((255, 255, 255))

    # Draw TicTacToe grid
    pygame.draw.line(window, (0, 0, 0), (width / 3, 0), (width / 3, height), 5)
    pygame.draw.line(window, (0, 0, 0), (2 * width / 3, 0), (2 * width / 3, height), 5)
    pygame.draw.line(window, (0, 0, 0), (0, height / 3), (width, height / 3), 5)
    pygame.draw.line(window, (0, 0, 0), (0, 2 * height / 3), (width, 2 * height / 3), 5)

    pygame.display.update()


def user_click():
    # get coordinates of mouse click
    x, y = pygame.mouse.get_pos()

    # get column of mouse click (1-3)
    if x < width / 3:
        col = 1
    elif x < width / 3 * 2:
        col = 2
    elif x < width:
        col = 3

    # get row of mouse click (1-3)
    if y < height / 3:
        row = 3
    elif y < height / 3 * 2:
        row = 2
    elif y < height:
        row = 1

    position = col + (row - 1) * 3
    return position


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
        initializing_window()
        while True:
            run = True
            if self.turn == self.computer:
                self.computer_AI.computer_turn()
                self.board.print_board()
                self.endgame_check()
                self.change_turn()
            else:
                self.board.print_board()

            while run:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        pygame.quit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if self.turn == self.player:
                            position = str(user_click())
                            if self.board.check_if_move_is_possible(position=position):
                                self.player_turn(position)
                                self.board.print_board()
                                self.endgame_check()
                                self.change_turn()
                                self.computer_AI.computer_turn()
                                self.board.print_board()
                                self.endgame_check()
                                self.change_turn()

    def player_turn(self, position):
        """
        A player making a turn
        """
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
