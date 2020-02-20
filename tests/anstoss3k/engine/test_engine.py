
from anstoss3k.engine.definitions import GameAction, GameState
from anstoss3k.engine import engine

from bin.game import GAME_DATA


def test_initial_game_state():
    game_engine = engine.GameEngine(GAME_DATA)
    assert game_engine.state == GameState.TEAM_SELECTION


def test_game_action_next_state():
    game_engine = engine.GameEngine(GAME_DATA)
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.PROGRESS_WEEK

def test_setup_matchdays():
    game_engine = engine.GameEngine(GAME_DATA)
    assert len(game_engine.data['match_days']) == 6
