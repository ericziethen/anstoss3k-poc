
import enum


@enum.unique
class GameState(enum.Enum):
    # pylint: disable=invalid-name
    TEAM_SELECTION = 'Team Selection'
    MATCH_DAY_PREVIEW = 'Match Day Preview'
    MATCH_DAY_RESULS = 'Match Day Results'
    TABLES = 'Tables'
    SEASON_END = 'Season End'


class State():
    def __init__(self, data):
        self.data = data

    def validate_input(self, input):
        pass

    def handle_input(self, input):
        pass

    def update_state(self):
        pass
