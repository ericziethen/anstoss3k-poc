
import tkinter as tk

from anstoss3k.engine.engine import GameEngine, GameState
from anstoss3k.ui.states import (
    team_selection,
    week_progress,
    matchday_preview
)

GAME_DATA = {
    'teams': ['Team 1', 'Team 2']
}


class Game():
    def __init__(self, root_window, width, height):
        self.root_window = root_window
        self.engine = GameEngine(GAME_DATA)
        self.ui_actions = []
        self.screens = {}
        self.current_canvas = None
        self.dims = (width, height)
        self.setup_screens()

    def setup_screens(self):
        # Can this done in a loop
        self.screens[GameState.TEAM_SELECTION] = team_selection.TeamSelectionStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)
        self.screens[GameState.PROGRESS_WEEK] = week_progress.ProgressWeekStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)
        self.screens[GameState.MATCH_DAY_PREVIEW] = matchday_preview.MatchDayPreviewStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)

    def play(self):
        # TODO - Start the initial screen
        print(F'DRAW SCREEN: {str(self.engine.state)}')

        #if self.current_canvas:
        #    self.current_canvas.destroy()

        self.screens[self.engine.state].draw()
        self.current_canvas = self.screens[self.engine.state].canvas

    def check_ui_update(self):
        # Todo - Find a more defined way to treat the action
        if self.ui_actions:
            self.engine.action(self.ui_actions[0])
            del self.ui_actions[:]
            self.play()

        # Always check for updated data
        self.root_window.after(500, self.check_ui_update)


def main():
    root = tk.Tk()
    width = 640
    height = 480
    root.geometry(F'{width}x{height}')

    game = Game(root, width, height)
    game.play()

    # To check if need to go to the engine
    # https://stackoverflow.com/questions/25753632/tkinter-how-to-use-after-method/25753719#25753719
    root.after(500, game.check_ui_update)

    root.mainloop()


if __name__ == '__main__':
    main()
