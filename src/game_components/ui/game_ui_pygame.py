import pygame
from sys import exit
from src.game_components.constants.ui_constants import *
from src.game_components.board import Board
from src.game_components.constants.game_constants import PLAYER_ONE
from src.game_components.players.bot_player import RandomBotPlayer
from src.game_components.players.human_player import HumanPlayer
from time import sleep
from typing import Tuple


class GameUI:
    def __init__(self):
        pygame.init()
        self.screen_img = pygame.image.load("../imgs/Connect4Board.png")
        self.screen = None

    def play(self, player_types: Tuple[str, str] = None, delay=0):
        if player_types is None:
            player_types = ("Human", "RandomBot")

        board = Board()
        player_turn = PLAYER_ONE
        player_turn_type = player_types[player_turn]
        move = (0, 0)

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("White")
        screen.blit(self.screen_img, (0, 0))

        info_surface = pygame.rect.Rect(0, SCREEN_HEIGHT-INFO_HEIGHT, INFO_WIDTH, INFO_HEIGHT)
        pygame.draw.rect(screen, LIGHT_BLUE, info_surface)
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        turn_text = font.render("Turno", False, "Black")

        screen.blit(turn_text, TURN_TEXT_COORDS)
        pygame.draw.circle(screen, COLOR_PLAYERS[player_turn], PLAYER_TURN_COIN_COORDS, CIRCLE_RADIUS + 2)

        pygame.display.set_caption("Connect 4")
        clock = pygame.time.Clock()
        mouse_press = False

        while board.have_empty_spaces():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = True
                else:
                    mouse_press = False

            move_status = False

            if player_turn_type == "Human":
                if mouse_press and screen.get_at(pygame.mouse.get_pos()) == WHITE:
                    move = HumanPlayer.make_move()
                    move_status = board.add_to_board(move, player_turn)
            else:
                move = RandomBotPlayer.make_move(board)
                move_status = board.add_to_board(move, player_turn)

            if move_status:
                center = self.get_circle_center_from_position(move)
                pygame.draw.circle(screen, COLOR_PLAYERS[player_turn], center, CIRCLE_RADIUS+2)
                if board.check_win(move, player_turn):
                    break
                player_turn ^= 1
                player_turn_type = player_types[player_turn]
                sleep(delay)
                pygame.draw.circle(screen, COLOR_PLAYERS[player_turn], PLAYER_TURN_COIN_COORDS, CIRCLE_RADIUS + 2)

            screen.blit(self.screen_img, (0, 0))
            pygame.display.update()
            clock.tick(FPS)

        if board.check_win(move, player_turn):
            if player_turn == PLAYER_ONE:
                final_str = f"O jogador vermelho foi vencedor!"

            else:
                final_str = f"O jogador amarelo foi vencedor!"
            final_color = COLOR_PLAYERS[player_turn]

        else:
            final_str = "Empate!"
            final_color = "Black"

        winner_text = font.render(final_str, False, final_color)

        screen.blit(self.screen_img, (0, 0))
        screen.blit(winner_text, WINNER_TEXT_COORDS)

        pygame.display.update()
        sleep(3)

    def get_circle_center_from_position(self, position):
        """Gets the center coordinates of the circle corresponding to the position clicked"""
        pos_row, pos_column = position

        starting_center_x, starting_center_y = FIRST_CIRCLE_CENTER

        center = (starting_center_x + HORIZONTAL_DISTANCE_CIRCLES * pos_column,
                  starting_center_y + VERTICAL_DISTANCE_CIRCLES * pos_row)

        return center
