''' The Main Engine to play the game. '''

from anstoss3k.engine.definitions import GameState
from anstoss3k.engine.states import (
    team_selection, progress_week, match_day_preview, match_day_results, match_day_tables
)


class GameEngine():
    def __init__(self, data):
        self.state = GameState.TEAM_SELECTION
        self.states = {}
        self.data = data

        # Initialize the Data
        self.init_season()

        # Initialize the States
        self.init_states()

    def init_states(self):
        self.states[GameState.TEAM_SELECTION] = team_selection.TeamSelectionState(self.data)
        self.states[GameState.PROGRESS_WEEK] = progress_week.ProgressWeekState(self.data)
        self.states[GameState.MATCH_DAY_PREVIEW] = match_day_preview.MatchDayPreviewState(self.data)
        self.states[GameState.MATCH_DAY_RESULTS] = match_day_results.MatchDayResultsState(self.data)
        self.states[GameState.MATCH_DAY_RESULTS] = match_day_tables.MatchDayTablesState(self.data)

    def action(self, action):
        state_class = self.states[self.state]
        state_class.handle_input(action)
        self.state = state_class.next_state(action)

    def init_season(self):
        self.data['match_days'] = []
        self.init_matchdays()
        self.data['current_match_day'] = 1

    def init_matchdays(self):
        team_count = len(self.data['teams'])
        match_day_count = (team_count - 1) * 2
        for day in range(1, match_day_count + 1):
            self.data['match_days'].append(day)



