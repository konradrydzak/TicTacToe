class ComputerAI:
    def __init__(self, board, who_is_first, player_symbol, computer_symbol):
        self.board = board
        self.turn = who_is_first
        self.player = player_symbol
        self.computer = computer_symbol

    def computer_turn(self):
        self.board.make_a_move(self.computer, self.find_a_move())

    def find_a_move(self):
        possible_win, position = self.check_if_win_in_one(self.computer)
        if not possible_win:
            possible_win, position = self.check_if_win_in_one(self.player)
            if not possible_win:
                position = self.best_move()
        return position

    def check_if_win_in_one(self, current_player):
        position = 0
        for i in range(1, 10):
            if self.board.board[str(i)] not in 'XO':
                self.board.make_a_move(current_player, str(i))
                if self.board.check_if_win():
                    position = i
                self.board.make_a_move(str(i), str(i))
        if position != 0:
            return True, str(position)
        else:
            return False, None

    def best_move(self):
        best_score = -9999999
        depth = 9
        for i in range(1, 10):
            if self.board.check_if_move_is_possible(str(i)):
                self.board.make_a_move(self.computer, str(i))
                score = self.minimax(False, depth)
                self.board.make_a_move(str(i), str(i))
                if score > best_score:
                    best_score = score
                    position = str(i)
        return position

    def minimax(self, is_maximizing, depth):
        if self.board.check_if_win():
            if self.turn == self.player:
                return -1 * depth
            else:
                return 1 * depth
        else:
            for i in range(1, 10):
                if self.board.board[str(i)] not in 'XO':
                    break
                if i == 9:
                    return 0
        if is_maximizing:
            best_score = -9999999
            self.turn = self.computer
            for i in range(1, 10):
                if self.board.check_if_move_is_possible(str(i)):
                    self.board.make_a_move(self.computer, str(i))
                    score = self.minimax(False, depth + 1)
                    self.board.make_a_move(str(i), str(i))
                    best_score = max(score, best_score)
            self.turn = self.player
            return best_score
        else:
            best_score = 9999999
            self.turn = self.player
            for i in range(1, 10):
                if self.board.check_if_move_is_possible(str(i)):
                    self.board.make_a_move(self.player, str(i))
                    score = self.minimax(True, depth + 1)
                    self.board.make_a_move(str(i), str(i))
                    best_score = min(score, best_score)
            self.turn = self.computer
            return best_score
