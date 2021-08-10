import pygame

# RGB colors codes
BLACK = (0, 0, 0)


class Board:
    def __init__(self, window):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.window = window

    def make_a_move(self, symbol, row, col):
        self.board[row][col] = symbol

    def check_if_move_is_possible(self, row, col):
        if self.board[row][col] == '':
            return True
        return False

    def check_if_win(self, drawable):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '':
                if drawable:
                    pygame.draw.line(surface=self.window.surface, color=BLACK, start_pos=(10, i * 200 + 100),
                                     end_pos=(600 - 10, i * 200 + 100), width=15)
                    pygame.display.update()
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != '':
                if drawable:
                    pygame.draw.line(surface=self.window.surface, color=BLACK, start_pos=(j * 200 + 100, 10),
                                     end_pos=(j * 200 + 100, 600 - 10), width=15)
                    pygame.display.update()
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            if drawable:
                pygame.draw.line(surface=self.window.surface, color=BLACK, start_pos=(25, 25),
                                 end_pos=(600 - 25, 600 - 25), width=20)
                pygame.display.update()
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            if drawable:
                pygame.draw.line(surface=self.window.surface, color=BLACK, start_pos=(600 - 25, 25),
                                 end_pos=(25, 600 - 25), width=20)
                pygame.display.update()
            return True

    def check_if_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True
