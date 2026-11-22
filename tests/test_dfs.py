
from config.environment_config import RANDOM_SEED
from environment.space_environment import SpaceEnvironment
from algorithms.dfs import depth_first_search


def test_dfs():

    environment = SpaceEnvironment(seed=RANDOM_SEED)
    result = depth_first_search(environment)

    assert result["success"] is True
    assert result["path"][0] == environment.start_state
    assert result["path"][-1] == environment.goal_state
    assert result["path_length"] == len(result["path"]) - 1

    for i in range(len(result["path"]) - 1):

        current_state = result["path"][i]
        next_state = result["path"][i + 1]

        successors = environment.get_successors(current_state)
        successor_states = [successor[0] for successor in successors]

        assert next_state in successor_states
