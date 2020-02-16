''' States and Sub-States for the Team selection '''

from anstoss3k.engine.definitions import GameAction, GameState, State


class TeamSelectionState(State):
    def handle_input(self, action):
        self.action = action

    def next_state(self):
        if self.action == GameAction.FINISH_MOVE:
            return GameState.PROGRESS_WEEK
