
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
        self.ui_actions = []
        self.screens = {}
        self.dims = (640, 480)
        self.setup_screens()

    def setup_screens(self):
        self.screens[GameState.TEAM_SELECTION] = TeamSelectionStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)

    def play(self):
        # TODO - Start the initial screen
        self.screens[self.engine.state].draw()

    def check_ui_update(self):
        # Todo - Find a more defined way to treat the action
        if self.ui_actions:
            self.engine.action(self.ui_actions[0])
            del self.ui_actions[:]
            self.play()
        '''
            if the ui got back to us
                send the command back to the engine
                call play again
        '''

        # ALways check for updated data
        self.root_window.after(500, self.check_ui_update)


def main():
    root = tk.Tk()

    game = Game(root)
    game.play()

    # To check if need to go to the engine
    # https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method/25753719#25753719
    root.after(500, game.check_ui_update)

    root.mainloop()


if __name__ == '__main__':
    main()
