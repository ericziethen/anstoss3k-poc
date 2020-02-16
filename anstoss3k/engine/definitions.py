
import enum


@enum.unique
class GameAction(enum.Enum):
    # pylint: disable=invalid-name
    FINISH_MOVE = 'Finish Move'


@enum.unique
class GameState(enum.Enum):
    # pylint: disable=invalid-name
    UNKNOWN = 'Unknown State'
    TEAM_SELECTION = 'Team Selection'
    PROGRESS_WEEK = 'Week Progress'
    MATCH_DAY_PREVIEW = 'Match Day Preview'
    MATCH_DAY_RESULTS = 'Match Day Results'
    MATCH_DAY_TABLES = 'Tables'
    SEASON_END = 'Season End'


class State():
    def __init__(self, data):
        self.data = data

    def handle_input(self, action):
        raise NotImplementedError

    def next_state(self, action):
        raise NotImplementedError
