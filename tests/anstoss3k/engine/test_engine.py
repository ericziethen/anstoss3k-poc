
from anstoss3k.engine.definitions import GameState
from anstoss3k.engine import engine

def test_initial_game_state():
    game_engine = engine.GameEngine()
    assert game_engine.state == GameState.TEAM_SELECTION

