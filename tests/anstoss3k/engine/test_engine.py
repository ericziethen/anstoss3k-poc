
from anstoss3k.engine.definitions import GameAction, GameState
from anstoss3k.engine import engine

from bin.game import setup_test_data


def test_initial_game_state():
    game_engine = engine.GameEngine(setup_test_data())
    assert game_engine.state == GameState.TEAM_SELECTION


def test_game_action_next_state():
    game_engine = engine.GameEngine(setup_test_data())
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.PROGRESS_WEEK

def test_setup_matchdays():
    game_engine = engine.GameEngine(setup_test_data())
    assert len(game_engine.data['match_days']) == 6
