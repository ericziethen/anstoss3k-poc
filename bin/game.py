
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


class Game():
    def __init__(self, root_window, width, height):
        self.root_window = root_window

        game_data = setup_test_data()
        self.engine = GameEngine(game_data)
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
                print(self.engine.data)
                print(F'{"Name":<30}{"Goals +":<10}{"Goals -":<10}{"Goal Diff":<10}{"Points":<10}')
                print('--------------------------------------------------------------------------------------------')
                for team_dic in self.engine.data['teams'].values():
                    print(F'{team_dic["Name"]:<30}{team_dic["goals_for"]:<10}{team_dic["goals_against"]:<10}'
                          F'{team_dic["goals_for"]-team_dic["goals_against"]:<10}{team_dic["points"]:<10}')

                self.root_window.quit()
            else:
                self.engine.action(self.ui_actions[0])
                del self.ui_actions[:]
                self.play()

        # Always check for updated data
        self.root_window.after(500, self.check_ui_update)


def setup_test_data():
    team_dic = {
        1: {'Name': 'Bayern München'},
        2: {'Name': 'RB Leipzig'},
        3: {'Name': 'Borussia Dortmund'},
        4: {'Name': 'Bor. Mönchengladbach'},
    }
    for team in team_dic.values():
        team['points'] = 0
        team['goals_for'] = 0
        team['goals_against'] = 0

    match_days = {
        1: [{'home': 1, 'away': 2, 'home_score': None, 'away_score': None},
            {'home': 3, 'away': 4, 'home_score': None, 'away_score': None}],
        2: [{'home': 1, 'away': 3, 'home_score': None, 'away_score': None},
            {'home': 2, 'away': 4, 'home_score': None, 'away_score': None}],
        3: [{'home': 1, 'away': 4, 'home_score': None, 'away_score': None},
            {'home': 3, 'away': 2, 'home_score': None, 'away_score': None}],
        4: [{'home': 2, 'away': 1, 'home_score': None, 'away_score': None},
            {'home': 4, 'away': 3, 'home_score': None, 'away_score': None}],
        5: [{'home': 3, 'away': 1, 'home_score': None, 'away_score': None},
            {'home': 4, 'away': 2, 'home_score': None, 'away_score': None}],
        6: [{'home': 4, 'away': 1, 'home_score': None, 'away_score': None},
            {'home': 2, 'away': 3, 'home_score': None, 'away_score': None}],
    }

    game_data = {
        'teams': team_dic,
        'match_days': match_days,
    }

    return game_data


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
