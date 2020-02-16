
from anstoss3k.engine.definitions import GameAction, GameState, State


class MatchDayTablesState(State):
    def handle_input(self, action):
        pass

    def next_state(self, action):
        if action == GameAction.FINISH_MOVE:
            if self.data['current_match_day'] < len(self.data['match_days']):
                return GameState.TEAM_SELECTION

            return GameState.SEASON_END

        return GameState.UNKNOWN
