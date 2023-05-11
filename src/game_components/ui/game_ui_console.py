from src.game_components.board import Board
from src.game_components.constants.game_constants import PLAYER_ONE, PLAYER_TWO
from src.game_components.players.bot_player import RandomBotPlayer
from src.game_components.players.human_player import HumanPlayer


class Game:
    def play(self, player_one_type="Human", player_two_type="Human"):
        board = Board()

        if player_one_type == "Human":
            player_one = HumanPlayer()
        else:
            player_one = RandomBotPlayer()

        if player_two_type == "Human":
            player_two = HumanPlayer()
        else:
            player_two = RandomBotPlayer()

        player_turn = PLAYER_ONE
        move = (0, 0)

        while board.have_empty_spaces():
            print(board)
            print(f"Faça sua jogada jogador {player_turn+1}: ")
            # sleep(1)

            if player_turn == PLAYER_ONE:
                move = player_one.make_move(board)
                move_status = board.add_to_board(move, player_turn)
                while not move_status:
                    move = player_one.make_move(board)
                    move_status = board.add_to_board(move, player_turn)

            elif player_turn == PLAYER_TWO:
                move = player_two.make_move(board)
                move_status = board.add_to_board(move, player_turn)
                while not move_status:
                    move = player_two.make_move(board)
                    move_status = board.add_to_board(move, player_turn)

            if board.check_win(move, player_turn):
                break

            player_turn ^= 1

        print(board)
        if board.check_win(move, player_turn):
            if player_turn == PLAYER_ONE:
                print("O jogador 1 foi vencedor!")
            elif player_turn == PLAYER_TWO:
                print("O jogador 2 foi vencedor!")
        else:
            print("Empate!")