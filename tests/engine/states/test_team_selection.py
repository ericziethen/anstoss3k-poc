
from anstoss3k.engine.definitions import GameAction, GameState, State
from anstoss3k.engine.states.team_selection import TeamSelectionState

def test_next_state_complete_action():
    state = TeamSelectionState('data')
    assert state.next_state(GameAction.FINISH_MOVE) == GameState.PROGRESS_WEEK
