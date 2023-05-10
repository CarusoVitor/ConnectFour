import unittest
from src.constants import *
from src.board import Board

class BoardTestCase(unittest.TestCase):

    def test_get_first_row_legal_moves(self):
        legal_moves = [(ROWS-1, column) for column in range(COLUMNS)]
        board = Board(None, None)
        self.assertEqual(legal_moves, board.get_legal_moves())

    def test_get_legal_moves(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        legal_moves_state = [(3, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 5), (1, 6)]
        board = Board(None, None, board_state)
        legal_moves_board = board.get_legal_moves()
        self.assertEqual(sorted(legal_moves_board, key=lambda move: move[1]), legal_moves_state)


if __name__ == "__main__":
    unittest.main()