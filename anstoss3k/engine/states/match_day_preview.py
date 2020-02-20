
import random

from anstoss3k.engine.definitions import GameAction, GameState, State


class MatchDayPreviewState(State):
    def handle_input(self, action):
        # Calculate the Results for the current match day

        for match in self.data['match_days'][self.data['current_match_day']]:
            match['home_score'] = random.randint(0, 3)
            match['away_score'] = random.randint(0, 3)

    def next_state(self, action):
        if action == GameAction.FINISH_MOVE:
            return GameState.MATCH_DAY_RESULTS

        return GameState.UNKNOWN
