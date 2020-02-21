
import random

from anstoss3k.engine.definitions import GameAction, GameState, State


class MatchDayPreviewState(State):
    def handle_input(self, action):
        # Calculate the Results for the current match day
        for match in self.data['match_days'][self.data['current_match_day']]:
            match['home_score'] = random.randint(0, 3)  # nosec
            match['away_score'] = random.randint(0, 3)  # nosec

            # Add Points and goals to the team
            if match['home_score'] > match['away_score']:
                self.data['teams'][match['home']]['points'] += 3
            elif match['home_score'] < match['away_score']:
                self.data['teams'][match['away']]['points'] += 3
            else:
                self.data['teams'][match['home']]['points'] += 1
                self.data['teams'][match['away']]['points'] += 1

            self.data['teams'][match['home']]['goals_for'] += match['home_score']
            self.data['teams'][match['home']]['goals_against'] += match['away_score']
            self.data['teams'][match['away']]['goals_for'] += match['away_score']
            self.data['teams'][match['away']]['goals_against'] += match['home_score']

    def next_state(self, action):
        if action == GameAction.FINISH_MOVE:
            return GameState.MATCH_DAY_RESULTS

        return GameState.UNKNOWN
