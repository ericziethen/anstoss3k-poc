
from anstoss3k.engine.definitions import GameAction, GameState, State


class MatchDayResultsState(State):
    def handle_input(self, action):
        pass

    def next_state(self, action):
        if action == GameAction.FINISH_MOVE:
            return GameState.MATCH_DAY_TABLES

        return GameState.UNKNOWN
