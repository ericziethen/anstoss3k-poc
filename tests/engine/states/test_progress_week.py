
from anstoss3k.engine.definitions import GameAction, GameState, State
from anstoss3k.engine.states.progress_week import ProgressWeekState


def test_next_state_complete_action():
    state = ProgressWeekState('data')
    assert state.next_state(GameAction.FINISH_MOVE) == GameState.MATCH_DAY_PREVIEW
