
from anstoss3k.engine.engine import GameEngine
from anstoss3k.engine.definitions import GameAction, GameState

from bin.game import GAME_DATA

def test_season_states_2_teams():
    engine = GameEngine(GAME_DATA)

    # Match day 1
    assert engine.state == GameState.TEAM_SELECTION
    assert engine.data['current_match_day'] == 1

    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.PROGRESS_WEEK
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_PREVIEW
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_RESULTS
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_TABLES
    engine.action(GameAction.FINISH_MOVE)

    # Match Day 2
    assert engine.state == GameState.TEAM_SELECTION
    assert engine.data['current_match_day'] == 2

    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.PROGRESS_WEEK
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_PREVIEW
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_RESULTS
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_TABLES
    engine.action(GameAction.FINISH_MOVE)

    # Matchday 3 to 6
    for day in range(3, 7):
        assert engine.state == GameState.TEAM_SELECTION
        assert engine.data['current_match_day'] == day

        engine.action(GameAction.FINISH_MOVE)
        assert engine.state == GameState.PROGRESS_WEEK
        engine.action(GameAction.FINISH_MOVE)
        assert engine.state == GameState.MATCH_DAY_PREVIEW
        engine.action(GameAction.FINISH_MOVE)
        assert engine.state == GameState.MATCH_DAY_RESULTS
        engine.action(GameAction.FINISH_MOVE)
        assert engine.state == GameState.MATCH_DAY_TABLES
        engine.action(GameAction.FINISH_MOVE)


    # End of Season
    assert engine.state == GameState.SEASON_END
