import unittest
from src.game_components.constants import *
from src.game_components.board import Board


class BoardTestCase(unittest.TestCase):
    def test_get_first_row_legal_moves(self):
        board = Board()
        legal_moves = [(ROWS-1, column) for column in range(COLUMNS)]
        self.assertEqual(board.get_legal_moves(), legal_moves)

    def test_get_legal_moves(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        legal_moves_state = [(3, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 5), (1, 6)]
        legal_moves_board = board.get_legal_moves()
        self.assertEqual(sorted(legal_moves_board, key=lambda move: move[1]), legal_moves_state)

    def test_add_to_board_player_one_first_row(self):
        board = Board()
        move = (5, 0)
        board.add_to_board(move, PLAYER_ONE)
        self.assertEqual(board.get_position(move), PLAYER_ONE)

    def test_add_to_board_player_two(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (3, 0)
        board.add_to_board(move, PLAYER_TWO)
        self.assertEqual(board.get_position(move), PLAYER_TWO)

    def test_add_to_board_invalid_move_no_piece_below(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (0, 0)
        board.add_to_board(move, PLAYER_TWO)
        self.assertEqual(board.get_position(move), EMPTY_SPACE)

    def test_add_to_board_invalid_move_occupied_position(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (5, 0)
        self.assertFalse(board.add_to_board(move, PLAYER_TWO))

    def test_add_to_board_off_limits_move(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            [".", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (8, 8)
        self.assertFalse(board.add_to_board(move, PLAYER_TWO))

    def test_winner_vertical_1(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", "o", ],
            ["x", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (2, 0)
        board.add_to_board(move, PLAYER_ONE)
        self.assertTrue(board.check_win(move, PLAYER_ONE))

    def test_winner_vertical_2(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (0, 0)
        board.add_to_board(move, PLAYER_TWO)
        self.assertTrue(board.check_win(move, PLAYER_TWO))

    def test_not_winner_vertical(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "o", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (0, 0)
        board.add_to_board(move, PLAYER_ONE)
        self.assertFalse(board.check_win(move, PLAYER_TWO))

    def test_winner_horizontal_1(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", "x", ".", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (5, 2)
        board.add_to_board(move, PLAYER_ONE)
        self.assertTrue(board.check_win(move, PLAYER_ONE))

    def test_winner_horizontal_2(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", "o", "o", "o", ".", "x", "x", ],
            ["x", "x", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (4, 4)
        board.add_to_board(move, PLAYER_TWO)
        self.assertTrue(board.check_win(move, PLAYER_TWO))

    def test_winner_horizontal_3(self):
        board_state = [
            [".", "x", "x", "x", ".", ".", ".", ],
            ["o", "x", "o", "x", ".", ".", ".", ],
            ["o", "o", "x", "o", ".", ".", "o", ],
            ["o", "x", "o", "x", ".", ".", "x", ],
            ["x", "o", "x", "o", ".", "o", "x", ],
            ["x", "x", "o", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (0, 0)
        board.add_to_board(move, PLAYER_ONE)
        self.assertTrue(board.check_win(move, PLAYER_ONE))

    def test_winner_horizontal_4(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", ".", "x", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (5, 1)
        board.add_to_board(move, PLAYER_ONE)
        self.assertTrue(board.check_win(move, PLAYER_ONE))

    def test_not_winner_horizontal(self):
        board_state = [
            [".", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", ".", ],
            ["o", ".", ".", ".", ".", ".", "o", ],
            ["o", ".", ".", ".", ".", ".", "x", ],
            ["x", ".", ".", ".", ".", "o", "x", ],
            ["x", ".", "x", "x", "o", "o", "x", ],
        ]
        board = Board(board_state)
        move = (4, 2)
        board.add_to_board(move, PLAYER_ONE)
        self.assertFalse(board.check_win(move, PLAYER_ONE))


if __name__ == "__main__":
    unittest.main()