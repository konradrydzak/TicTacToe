class ComputerAlgorithm:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def find_a_move(self):
        # When Computer is starting, check if the board is empty, if so: start at position 1, 1 (saves a lot of time)
        for i in range(3):
            for j in range(3):
                if self.board.board[i][j] != '':
                    break
            # A smart way to break out of nested for loops: if there was no break it goes to continue else it breaks too
            else:
                continue
            break
        else:
            row = 1
            col = 1
            return row, col

        row, col = self.best_move()
        return row, col

    def best_move(self):
        best_score = -9999999
        depth = 9
        row = 0
        col = 0
        for i in range(3):
            for j in range(3):
                if self.board.check_if_move_is_possible(row=i, col=j):
                    self.board.make_a_move(symbol=self.game.computer_symbol, row=i, col=j)
                    score = self.minimax(is_maximizing=False, depth=depth)
                    self.board.make_a_move(symbol='', row=i, col=j)
                    if score > best_score:
                        best_score = score
                        row, col = i, j
        return row + 1, col + 1

    def minimax(self, is_maximizing, depth):
        if self.board.check_if_win(drawable=False):
            if self.game.current_player == self.game.player_symbol:
                return -1 * depth
            return 1 * depth
        if self.board.check_if_draw():
            return 0
        if is_maximizing:
            best_score = -9999999
            self.game.current_player = self.game.computer_symbol
            for i in range(3):
                for j in range(3):
                    if self.board.check_if_move_is_possible(row=i, col=j):
                        self.board.make_a_move(symbol=self.game.computer_symbol, row=i, col=j)
                        score = self.minimax(is_maximizing=False, depth=depth - 1)
                        self.board.make_a_move(symbol='', row=i, col=j)
                        best_score = max(score, best_score)
            self.game.current_player = self.game.player_symbol
            return best_score
        else:
            best_score = 9999999
            self.game.current_player = self.game.player_symbol
            for i in range(3):
                for j in range(3):
                    if self.board.check_if_move_is_possible(row=i, col=j):
                        self.board.make_a_move(symbol=self.game.player_symbol, row=i, col=j)
                        score = self.minimax(is_maximizing=True, depth=depth - 1)
                        self.board.make_a_move(symbol='', row=i, col=j)
                        best_score = min(score, best_score)
            self.game.current_player = self.game.computer_symbol
            return best_score
