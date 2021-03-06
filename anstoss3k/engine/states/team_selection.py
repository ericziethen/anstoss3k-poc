
from anstoss3k.engine.definitions import GameAction, GameState, State


class TeamSelectionState(State):
    def handle_input(self, action):
        pass

    def next_state(self, action):
        if action == GameAction.FINISH_MOVE:
            return GameState.PROGRESS_WEEK

        return GameState.UNKNOWN
