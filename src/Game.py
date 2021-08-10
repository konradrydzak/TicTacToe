import pygame
from pygame.locals import *

import Board
import ComputerAlgorithm
import Window

# RGB colors codes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game:
    def __init__(self):
        self.who_is_starting = None
        self.player_symbol = None
        self.computer_symbol = None
        self.current_player = None
        self.game_ended = None
        self.board = None
        self.computer_algorithm = None
        self.window = None

    def start_game(self):
        self.game_ended = False
        self.window = Window.Window(game=self)
        self.window.prepare_game_start()
        if self.who_is_starting:
            self.current_player = self.player_symbol
        else:
            self.current_player = self.computer_symbol
        self.board = Board.Board(window=self.window)
        self.computer_algorithm = ComputerAlgorithm.ComputerAlgorithm(board=self.board, game=self)
        self.game()

    def endgame_checks(self):
        # Prepare window for text in endgame conditions
        font = pygame.font.SysFont(name=None, size=150)
        if self.board.check_if_win(drawable=True):
            self.game_ended = True
            if self.current_player == self.player_symbol:
                variable_text = 'You win!'
                text = font.render(variable_text, True, GREEN)
            else:
                variable_text = 'You lose!'
                text = font.render(variable_text, True, RED)
            textRect = text.get_rect()
            textRect.center = (self.window.width // 2, self.window.height // 2)
            self.window.surface.blit(text, textRect)
            pygame.display.update()

        if self.board.check_if_draw():
            self.game_ended = True
            variable_text = "It's a draw!"
            text = font.render(variable_text, True, BLUE)
            textRect = text.get_rect()
            textRect.center = (self.window.width // 2, self.window.height // 2)
            self.window.surface.blit(text, textRect)
            pygame.display.update()

    def game(self):
        while True:
            if self.game_ended:
                self.window.game_restart_question()
            else:
                if self.current_player == self.computer_symbol:
                    row, col = self.computer_algorithm.find_a_move()
                    self.board.make_a_move(symbol=self.current_player, row=row - 1, col=col - 1)

                    if self.current_player == 'X':
                        self.window.draw_cross(row, col)
                    else:
                        self.window.draw_cirle(row, col)
                    pygame.display.update()

                    self.endgame_checks()

                    if self.current_player == self.player_symbol:
                        self.current_player = self.computer_symbol
                    else:
                        self.current_player = self.player_symbol

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if self.current_player == self.player_symbol:
                            row, col = self.window.user_click()
                            if self.board.check_if_move_is_possible(row - 1, col - 1):
                                self.board.make_a_move(symbol=self.current_player, row=row - 1, col=col - 1)

                                if self.current_player == 'X':
                                    self.window.draw_cross(row, col)
                                else:
                                    self.window.draw_cirle(row, col)
                                pygame.display.update()

                                self.endgame_checks()

                                if self.current_player == self.player_symbol:
                                    self.current_player = self.computer_symbol
                                else:
                                    self.current_player = self.player_symbol
