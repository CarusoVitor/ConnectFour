from src.game_components.constants.ui_constants import *
import pygame


class HumanPlayer:

    @staticmethod
    def make_move():
        mouse_coordinates = pygame.mouse.get_pos()
        move = HumanPlayer.find_space_position(mouse_coordinates)
        return move

    @staticmethod
    def find_space_position(mouse_coordinates):
        """Find the position on the board that corresponds to the coordinates of the mouse click"""
        mouse_position_no_offset = (mouse_coordinates[0]-HORIZONTAL_OFFSET, mouse_coordinates[1]-VERTICAL_OFFSET)
        width, height = mouse_position_no_offset
        column = width//HORIZONTAL_DISTANCE_CIRCLES
        row = height//VERTICAL_DISTANCE_CIRCLES
        return row, column
