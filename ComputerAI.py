class ComputerAI:
    def __init__(self, board, who_is_first, player_symbol, computer_symbol):
        """
        Initialises a ComputerAI object
        :param board: Relation to a TicTacToe Board object
        :param who_is_first: 'X' or 'O' sign for who is going first
        :param player_symbol: 'X' or 'O' sign for a player
        :param computer_symbol: 'X' or 'O' sign for a computer
        """
        self.board = board
        self.turn = who_is_first
        self.player = player_symbol
        self.computer = computer_symbol

    def computer_turn(self):
        """
        Computer move structure
        """
        self.board.make_a_move(player=self.computer, position=self.find_a_move())

    def find_a_move(self):
        """
        Tries to find a move for the computer, first tries to win in one move, then goes to minimax algorithm
        """
        possible_win, position = self.check_if_win_in_one(current_player=self.computer)
        if not possible_win:
            possible_win, position = self.check_if_win_in_one(current_player=self.player)
            if not possible_win:
                position = self.best_move()
        return position

    def check_if_win_in_one(self, current_player):
        """
        Checks if there is a possible win in one move
        """
        position = 0
        for i in range(1, 10):
            if self.board.board[str(i)] not in 'XO':
                self.board.make_a_move(player=current_player, position=str(i))
                if self.board.check_if_win():
                    position = i
                self.board.make_a_move(player=str(i), position=str(i))
        if position != 0:
            return True, str(position)
        return False, None

    def best_move(self):
        """
        Initialises a minimax algorithm
        """
        best_score = -9999999
        depth = 9
        for i in range(1, 10):
            if self.board.check_if_move_is_possible(position=str(i)):
                self.board.make_a_move(player=self.computer, position=str(i))
                score = self.minimax(False, depth)
                self.board.make_a_move(player=str(i), position=str(i))
                if score > best_score:
                    best_score = score
                    position = str(i)
        return position

    def minimax(self, is_maximizing, depth):
        """
        Recursion minimax algorithm
        :param is_maximizing: True for maximazing, False for minimazing
        :param depth: A coefficient to take into accound the depth of the algorithm
        """
        if self.board.check_if_win():
            if self.turn == self.player:
                return -1 * depth
            return 1 * depth
        for i in range(1, 10):
            if self.board.board[str(i)] not in 'XO':
                break
            if i == 9:
                return 0
        if is_maximizing:
            best_score = -9999999
            self.turn = self.computer
            for i in range(1, 10):
                if self.board.check_if_move_is_possible(position=str(i)):
                    self.board.make_a_move(player=self.computer, position=str(i))
                    score = self.minimax(is_maximizing=False, depth=depth + 1)
                    self.board.make_a_move(player=str(i), position=str(i))
                    best_score = max(score, best_score)
            self.turn = self.player
            return best_score
        else:
            best_score = 9999999
            self.turn = self.player
            for i in range(1, 10):
                if self.board.check_if_move_is_possible(position=str(i)):
                    self.board.make_a_move(player=self.player, position=str(i))
                    score = self.minimax(is_maximizing=True, depth=depth + 1)
                    self.board.make_a_move(player=str(i), position=str(i))
                    best_score = min(score, best_score)
            self.turn = self.computer
            return best_score
