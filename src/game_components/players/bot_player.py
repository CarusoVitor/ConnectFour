from random import randint


class RandomBotPlayer:
    @staticmethod
    def make_move(board):
        legal_moves = board.get_legal_moves()
        choice = randint(0, len(legal_moves)-1)
        return legal_moves[choice]
