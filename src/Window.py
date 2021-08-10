import pygame
from pygame.locals import *

# RGB colors codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
ORANGE = (255, 150, 50)


class Window:
    def __init__(self, game):
        self.width = 600
        self.height = 600

        pygame.init()

        self.surface = pygame.display.set_mode(size=(self.width, self.height))
        pygame.display.set_caption('TicTacToe')

        self.surface.fill(color=WHITE)

        self.game = game

    def prepare_game_start(self):
        font = pygame.font.SysFont(name=None, size=75)
        variable_text = "Do you want to start?"
        text = font.render(variable_text, True, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.width // 2, 2 * self.height // 5)
        self.surface.blit(text, textRect)

        font = pygame.font.SysFont(name=None, size=125)
        variable_text = "Yes"
        text = font.render(variable_text, True, GREEN)
        yes_text_rect = text.get_rect()
        yes_text_rect.center = (self.width // 3, 3 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=DARK_GREEN, rect=yes_text_rect)
        self.surface.blit(text, yes_text_rect)

        variable_text = "No"
        text = font.render(variable_text, True, RED)
        no_text_rect = text.get_rect()
        no_text_rect.center = (2 * self.width // 3, 3 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=DARK_RED, rect=no_text_rect)
        self.surface.blit(text, no_text_rect)

        pygame.display.update()

        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if yes_text_rect.collidepoint(x, y):
                        self.game.who_is_starting = True
                        intro = False
                    if no_text_rect.collidepoint(x, y):
                        self.game.who_is_starting = False
                        intro = False

        self.surface.fill(color=WHITE)

        font = pygame.font.SysFont(name=None, size=60)
        variable_text = "Do you want to be O or X?"
        text = font.render(variable_text, True, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.width // 2, 2 * self.height // 5)
        self.surface.blit(text, textRect)

        font = pygame.font.SysFont(name=None, size=125)
        variable_text = "O"
        text = font.render(variable_text, True, WHITE)
        o_text_rect = text.get_rect()
        o_text_rect.center = (self.width // 3, 3 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=BLACK, rect=o_text_rect)
        self.surface.blit(text, o_text_rect)

        variable_text = "X"
        text = font.render(variable_text, True, WHITE)
        x_text_rect = text.get_rect()
        x_text_rect.center = (2 * self.width // 3, 3 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=BLACK, rect=x_text_rect)
        self.surface.blit(text, x_text_rect)

        pygame.display.update()

        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if o_text_rect.collidepoint(x, y):
                        self.game.player_symbol = '0'
                        self.game.computer_symbol = 'X'
                        intro = False
                    if x_text_rect.collidepoint(x, y):
                        self.game.player_symbol = 'X'
                        self.game.computer_symbol = '0'
                        intro = False

        self.surface.fill(color=WHITE)

        # Draw TicTacToe grid
        pygame.draw.line(surface=self.surface, color=BLACK, start_pos=(self.width / 3, 0),
                         end_pos=(self.width / 3, self.height), width=5)
        pygame.draw.line(surface=self.surface, color=BLACK, start_pos=(2 * self.width / 3, 0),
                         end_pos=(2 * self.width / 3, self.height), width=5)
        pygame.draw.line(surface=self.surface, color=BLACK, start_pos=(0, self.height / 3),
                         end_pos=(self.width, self.height / 3), width=5)
        pygame.draw.line(surface=self.surface, color=BLACK, start_pos=(0, 2 * self.height / 3),
                         end_pos=(self.width, 2 * self.height / 3), width=5)

        pygame.display.update()

    def game_restart_question(self):
        font = pygame.font.SysFont(name=None, size=55)
        variable_text = "Do you want to play again?"
        text = font.render(variable_text, True, ORANGE)
        textRect = text.get_rect()
        textRect.center = (self.width // 2, 4 * self.height // 5)
        self.surface.blit(text, textRect)

        font = pygame.font.SysFont(name=None, size=75)
        variable_text = "Yes"
        text = font.render(variable_text, True, GREEN)
        yes_text_rect = text.get_rect()
        yes_text_rect.center = (self.width // 3, 4.5 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=DARK_GREEN, rect=yes_text_rect)
        self.surface.blit(text, yes_text_rect)

        variable_text = "No"
        text = font.render(variable_text, True, RED)
        no_text_rect = text.get_rect()
        no_text_rect.center = (2 * self.width // 3, 4.5 * self.height // 5)
        pygame.draw.rect(surface=self.surface, color=DARK_RED, rect=no_text_rect)
        self.surface.blit(text, no_text_rect)

        pygame.display.update()

        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if yes_text_rect.collidepoint(x, y):
                        intro = False
                        self.game.start_game()
                    if no_text_rect.collidepoint(x, y):
                        pygame.quit()
                        exit()

    def user_click(self):
        x, y = pygame.mouse.get_pos()

        row = 0
        col = 0

        if x < self.width / 3:
            col = 1
        elif x < self.width / 3 * 2:
            col = 2
        elif x < self.width:
            col = 3

        if y < self.height / 3:
            row = 1
        elif y < self.height / 3 * 2:
            row = 2
        elif y < self.height:
            row = 3

        return row, col

    def draw_cirle(self, row, col):
        pygame.draw.circle(surface=self.surface, color=BLACK, center=((col - 1) * 200 + 100, (row - 1) * 200 + 100),
                           radius=80, width=3)

    def draw_cross(self, row, col):
        pygame.draw.line(surface=self.surface, color=BLACK,
                         start_pos=((col - 1) * 200 + 25, (row - 1) * 200 + 25),
                         end_pos=((col - 1) * 200 + 175, row * 200 - 25), width=4)
        pygame.draw.line(surface=self.surface, color=BLACK,
                         start_pos=((col - 1) * 200 + 25, row * 200 - 25),
                         end_pos=((col - 1) * 200 + 175, (row - 1) * 200 + 25), width=4)
