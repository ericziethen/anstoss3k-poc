
from anstoss3k.engine.definitions import GameAction, GameState, State
from anstoss3k.engine.states.match_day_tables import MatchDayTablesState


def test_next_state_complete_action_more_games():
    data = {'current_match_day': 1, 'match_days': [1, 2, 3, 4]}
    state = MatchDayTablesState(data)
    assert state.next_state(GameAction.FINISH_MOVE) == GameState.TEAM_SELECTION



def test_next_state_complete_action_no_more_games():
    data = {'current_match_day': 4, 'match_days': [1, 2, 3, 4]}
    state = MatchDayTablesState(data)
    assert state.next_state(GameAction.FINISH_MOVE) == GameState.SEASON_END
