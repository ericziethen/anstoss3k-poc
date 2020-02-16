
from anstoss3k.engine.definitions import GameAction, GameState
from anstoss3k.engine import engine


def test_initial_game_state():
    game_engine = engine.GameEngine()
    assert game_engine.state == GameState.TEAM_SELECTION


def test_team_selection_complete():
    game_engine = engine.GameEngine()
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.PROGRESS_WEEK


def test_week_progress_complete():
    game_engine = engine.GameEngine()
    game_engine.state = GameState.PROGRESS_WEEK
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.MATCH_DAY_PREVIEW
