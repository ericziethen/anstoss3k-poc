
import tkinter as tk

from anstoss3k.engine.engine import GameEngine, GameState
from anstoss3k.ui.states import (
    team_selection,
    week_progress,
    matchday_preview,
    matchday_result,
    matchday_tables,
    season_end
)








# GAME DATA WE NEED
    # 4 Teams
    # Random Match Days
    # Randomize Result Generation and calculation

TEAM_DIC = {
    1: {'Name': 'Bayern München'},
    2: {'Name': 'RB Leipzig'},
    3: {'Name': 'Borussia Dortmund'},
    4: {'Name': 'Bor. Mönchengladbach'},
}

GAME_DATA = {
    'teams': TEAM_DIC
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
        self.screens[GameState.MATCH_DAY_RESULTS] = matchday_result.MatchDayResultStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)
        self.screens[GameState.MATCH_DAY_TABLES] = matchday_tables.MatchDayTablesStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)
        self.screens[GameState.SEASON_END] = season_end.SeasonEndStateScreen(
            self.root_window, self.dims[0], self.dims[1], ui_actions=self.ui_actions)

    def play(self):
        self.screens[self.engine.state].draw()
        self.current_canvas = self.screens[self.engine.state].canvas

    def check_ui_update(self):
        if self.ui_actions:
            if self.engine.state == GameState.SEASON_END:
                self.root_window.quit()
            else:
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
