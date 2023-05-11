from src.game_components.ui.game_ui_pygame import GameUI

if __name__ == "__main__":
    game_ui = GameUI()
    players = ("Human", "Human")
    game_ui.play(players, delay=0)
