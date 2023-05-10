from src.constants import ROWS, COLUMNS


class Board:
    def __init__(self, player_one, player_two, board_state=None):
        self.board = []
        if board_state is None:
            self._init_board()
        else:
            self.board = board_state
        self.player_one = player_one
        self.player_two = player_two

    def _init_board(self):
        for row_index in range(ROWS):
            row = []
            for column_index in range(COLUMNS):
                row.append(".")
            self.board.append(row)

    # TODO: make more efficient not checking the next row if there are no legal moves on the current one
    def get_legal_moves(self):
        legal_moves = []
        for row_index in range(ROWS):
            for column_index in range(COLUMNS):
                move = (row_index, column_index)
                if self._legal_move(move):
                    legal_moves.append(move)
        return legal_moves

    def _legal_move(self, move):
        piece_row, piece_column = move
        if piece_row < ROWS-1:
            return self.board[piece_row+1][piece_column] != "." and self.board[piece_row][piece_column] == "."
        else:
            return self.board[piece_row][piece_column] == "."

    def __str__(self):
        str = ""
        for row_index in range(ROWS):
            for column_index in range(COLUMNS):
                str += self.board[row_index][column_index]
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
    board = Board(None, None, board_state)
    print(board)