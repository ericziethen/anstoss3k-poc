
import tkinter as tk

from anstoss3k.engine.engine import GameEngine, GameState
from anstoss3k.ui.states.team_selection import (
    TeamSelectionStateScreen
)

GAME_DATA = {
    'teams': ['Team 1', 'Team 2']
}


class Game():
    def __init__(self, root_window):
        self.root_window = root_window
        self.engine = GameEngine(GAME_DATA)
        self.screens = {}
        self.dims = (640, 480)

        self.setup_screens()

    def setup_screens(self):
        self.screens[GameState.TEAM_SELECTION] = TeamSelectionStateScreen(self.root_window, self.dims[0], self.dims[1])

    def play(self):
        # TODO - Start the initial screen
        self.screens[self.engine.state].draw()


def main():
    root = tk.Tk()

    game = Game(root)
    game.play()

    # TODO - How to run the game and get data

    root.mainloop()


if __name__ == '__main__':
    main()
