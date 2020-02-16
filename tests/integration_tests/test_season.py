
from anstoss3k.engine.engine import GameEngine
from anstoss3k.engine.definitions import GameAction, GameState


def test_season_states_2_teams():
    game_data = {
            'teams': ['Team 1', 'Team 2']
        }
    engine = GameEngine(game_data)

    assert engine.state == GameState.TEAM_SELECTION
    assert engine.data['current_match_day'] == 1

    # Match day 1
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.PROGRESS_WEEK
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_PREVIEW
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_RESULTS
    engine.action(GameAction.FINISH_MOVE)
    assert engine.state == GameState.MATCH_DAY_TABLES
    engine.action(GameAction.FINISH_MOVE)

    assert engine.state == GameState.TEAM_SELECTION
    assert engine.data['current_match_day'] == 2

    # Match Day 2
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
