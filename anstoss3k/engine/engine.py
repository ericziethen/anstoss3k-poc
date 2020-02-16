''' The Main Engine to play the game. '''

from anstoss3k.engine.definitions import GameState
from anstoss3k.engine.states import (
    team_selection
)

class GameEngine():
    def __init__(self):
        self.state = GameState.TEAM_SELECTION
        self.states = {}
        self.data = {}

        self.init_states()

    def init_states(self):
        self.states[GameState.TEAM_SELECTION] = team_selection.TeamSelectionState(self.data)

    def action(self, action):
        state_class = self.states[self.state]
        state_class.handle_input(action)
        self.state = state_class.next_state(action)
