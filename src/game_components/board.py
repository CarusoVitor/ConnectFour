from src.game_components.constants.game_constants import *


class Board:
    def __init__(self, board_state=None):
        self.board = []
        self.coins_num = {}
        self._init_board(board_state)

    def add_to_board(self, move, player):
        if self._is_legal_move(move):
            coin_row, coin_column = move
            self.board[coin_row][coin_column] = player
            self.coins_num[player] += 1
            self.coins_num[EMPTY_SPACE] -= 1
            return True
        else:
            return False

    def get_position(self, position):
        row, column = position
        return self.board[row][column]

    def check_win(self, move, player):
        return self._check_horizontal_win(move, player) or \
               self._check_vertical_win(move, player) or \
               self._check_diagonal_win(move, player)

    def have_empty_spaces(self):
        return self.coins_num[EMPTY_SPACE] > 0

    # TODO: make more efficient not checking the next row if there are no legal moves on the current one
    def get_legal_moves(self):
        legal_moves = []
        for row_index in range(ROWS):
            for column_index in range(COLUMNS):
                move = (row_index, column_index)
                if self._is_legal_move(move):
                    legal_moves.append(move)
        return legal_moves

    def _init_board(self, board_state=None):
        if board_state is None:
            self.coins_num[EMPTY_SPACE] = TOTAL_SPACES
        else:
            self.coins_num[EMPTY_SPACE] = 0

        self.coins_num[PLAYER_ONE] = 0
        self.coins_num[PLAYER_TWO] = 0

        for row_index in range(ROWS):
            row = []
            for column_index in range(COLUMNS):
                if board_state is None:
                    row.append(EMPTY_SPACE)
                else:
                    coin = STR_TO_COINS[board_state[row_index][column_index]]
                    self.coins_num[coin] += 1
                    row.append(coin)
            self.board.append(row)

    def _is_legal_move(self, move):
        coin_row, coin_column = move
        if self._on_board_limits(move):
            if coin_row < ROWS-1:
                return self.board[coin_row+1][coin_column] != EMPTY_SPACE and self.board[coin_row][coin_column] == EMPTY_SPACE
            else:
                return self.board[coin_row][coin_column] == EMPTY_SPACE
        else:
            return False

    def _on_board_limits(self, move):
        coin_row, coin_column = move
        return coin_row < ROWS and coin_column < COLUMNS

    def _check_horizontal_win(self, move, player):
        coin_row, coin_column = move
        coin_count = 0
        for column in range(COLUMNS):
            if self.get_position((coin_row, column)) == player:
                coin_count += 1
                if coin_count == 4:
                    return True
            else:
                coin_count = 0
        return False

    def _check_vertical_win(self, move, player):
        coin_row, coin_column = move
        if coin_row > 2:
            return False
        for row in range(coin_row, coin_row+4):
            if self.get_position((row, coin_column)) != player:
                return False
        return True

    def _check_diagonal_win(self, move, player):
        return self._check_diagonal_win_up_down(move, player) or \
               self._check_diagonal_win_down_up(move, player)

    def _check_diagonal_win_up_down(self, move, player):
        coin_row, coin_column = move

        start_row = max(coin_row - coin_column, 0)
        start_column = max(coin_column - coin_row, 0)

        if start_row > 2 or start_column > 3:
            return False

        if start_row >= start_column:
            end_row = ROWS
            end_column = ROWS-start_row
        else:
            end_row = COLUMNS-start_column
            end_column = COLUMNS

        row = start_row
        column = start_column
        coin_count = 0

        while row < end_row and column < end_column:
            if self.get_position((row, column)) == player:
                coin_count += 1
                if coin_count == 4:
                    return True
            else:
                coin_count = 0
            row += 1
            column += 1
        return False

    def _check_diagonal_win_down_up(self, move, player):
        coin_row, coin_column = move

        start_column = max(coin_row + coin_column - (ROWS - 1), 0)
        start_row = coin_row + coin_column - start_column

        if start_row < 3 or start_column > 3:
            return False

        end_row = min(coin_row + coin_column - ROWS, 0) - 1
        end_column = min(coin_row + coin_column+1, COLUMNS)

        row = start_row
        column = start_column
        coin_count = 0

        while row > end_row and column < end_column:
            if self.get_position((row, column)) == player:
                coin_count += 1
                if coin_count == 4:
                    return True
            else:
                coin_count = 0
            row -= 1
            column += 1
        return False

    def __str__(self):
        str_output = ""
        for row_index in range(ROWS+1):
            if row_index > 0:
                str_output += str(row_index-1)
            str_output += " "
            for column_index in range(COLUMNS):
                if row_index == 0:
                    if column_index == 0:
                        str_output += " "
                    str_output += str(column_index)
                    str_output += " "
                else:
                    str_output += COINS_TO_STR[self.board[row_index-1][column_index]]
                    str_output += " "
            str_output += "\n"
        return str_output
