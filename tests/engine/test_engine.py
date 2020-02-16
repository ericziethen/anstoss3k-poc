
from anstoss3k.engine.definitions import GameAction, GameState
from anstoss3k.engine import engine


def test_initial_game_state():
    game_engine = engine.GameEngine()
    assert game_engine.state == GameState.TEAM_SELECTION


def test_game_action_next_state():
    game_engine = engine.GameEngine()
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.PROGRESS_WEEK
