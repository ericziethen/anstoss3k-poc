
from anstoss3k.engine.definitions import GameAction, GameState
from anstoss3k.engine import engine

GAME_DATA = {
        'teams': ['Team 1', 'Team 2']
    }

def test_initial_game_state():
    game_engine = engine.GameEngine(GAME_DATA)
    assert game_engine.state == GameState.TEAM_SELECTION


def test_game_action_next_state():
    game_engine = engine.GameEngine(GAME_DATA)
    game_engine.action(GameAction.FINISH_MOVE)

    assert game_engine.state == GameState.PROGRESS_WEEK

def test_setup_matchdays():
    game_engine = engine.GameEngine(GAME_DATA)
    assert len(game_engine.data['match_days']) == 2
    assert 1 in game_engine.data['match_days']
    assert 2 in game_engine.data['match_days']
