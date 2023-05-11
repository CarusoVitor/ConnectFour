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
        self.board_surface_img = pygame.image.load("../imgs/Connect4Board.png")

    def play(self, player_types: Tuple[str, str] = None, delay=0):
        if player_types is None:
            player_types = ("Human", "RandomBot")

        board = Board()
        player_turn = PLAYER_ONE
        player_turn_type = player_types[player_turn]
        move = (0, 0)

        board_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        board_surface.fill("White")

        info_surface = pygame.rect.Rect(0, SCREEN_HEIGHT-INFO_HEIGTH, INFO_WIDTH, INFO_HEIGTH)
        pygame.draw.rect(board_surface, LIGHT_BLUE, info_surface)

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
                if mouse_press and board_surface.get_at(pygame.mouse.get_pos()) == WHITE:
                    move = HumanPlayer.make_move()
                    move_status = board.add_to_board(move, player_turn)
            else:
                move = RandomBotPlayer.make_move(board)
                move_status = board.add_to_board(move, player_turn)

            if move_status:
                rect = self.get_rect_from_position(move)
                pygame.draw.rect(board_surface, COLOR_PLAYERS[player_turn], rect)
                if board.check_win(move, player_turn):
                    break
                player_turn ^= 1
                player_turn_type = player_types[player_turn]
                sleep(delay)

            board_surface.blit(self.board_surface_img, (0, 0))
            pygame.display.update()
            clock.tick(60)

        if board.check_win(move, player_turn):
            if player_turn == PLAYER_ONE:
                winner_str = f"O jogador vermelho foi vencedor!"
            else:
                winner_str = f"O jogador amarelo foi vencedor!"

            font = pygame.font.SysFont(FONT, FONT_SIZE)
            winner_surface = font.render(winner_str, False, COLOR_PLAYERS[player_turn])

            board_surface.blit(self.board_surface_img, (0, 0))
            board_surface.blit(winner_surface, DISPLAY_WINNER_TEXT_COORDS)

            pygame.display.update()
            sleep(3)
        else:
            print("Empate!")

    def get_rect_from_position(self, position):
        """Gets the rectangle that will be used to paint the circle corresponding to the position of the board"""
        pos_row, pos_column = position
        top_left_rect_coordinates = (
            HORIZONTAL_OFFSET + HORIZONTAL_DISTANCE_CIRCLES * pos_column,
            VERTICAL_OFFSET + VERTICAL_DISTANCE_CIRCLES * pos_row
        )
        width_rect = CIRCLE_DIAMATER + 1
        height_rect = CIRCLE_DIAMATER + 1
        rect = pygame.rect.Rect(
            top_left_rect_coordinates[0],
            top_left_rect_coordinates[1],
            width_rect,
            height_rect
        )
        return rect


