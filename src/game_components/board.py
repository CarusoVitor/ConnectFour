from src.game_components.constants import *


class Board:
    def __init__(self, board_state=None):
        self.board = []
        self._init_board(board_state)

    def add_to_board(self, move, player):
        if self._is_legal_move(move):
            coin_row, coin_column = move
            self.board[coin_row][coin_column] = player
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
        for row_index in range(ROWS):
            row = []
            for column_index in range(COLUMNS):
                if board_state is None:
                    row.append(EMPTY_SPACE)
                else:
                    row.append(STR_TO_COINS[board_state[row_index][column_index]])
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
        return False

    def __str__(self):
        str = ""
        for row_index in range(ROWS):
            for column_index in range(COLUMNS):
                str += COINS_TO_STR[self.board[row_index][column_index]]
                str += " "
            str += "\n"
        return str


if __name__ == "__main__":
    board_state = [
        [".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", "o", ],
        [".", ".", ".", ".", ".", ".", "x", ],
        ["x", ".", ".", ".", ".", "o", "x", ],
        ["x", "o", "o", "x", "o", "o", "x", ],
    ]
    board = Board(board_state)
    print(board)