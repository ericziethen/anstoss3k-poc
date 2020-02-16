
from anstoss3k.engine.definitions import GameAction, GameState, State
from anstoss3k.engine.states.match_day_results import MatchDayResultsState

def test_next_state_complete_action():
    state = MatchDayResultsState('data')
    assert state.next_state(GameAction.FINISH_MOVE) == GameState.MATCH_DAY_TABLES
