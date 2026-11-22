
from config.environment_config import RANDOM_SEED
from environment.space_environment import SpaceEnvironment
from algorithms.ucs import uniform_cost_search


def test_ucs():

    environment = SpaceEnvironment(seed=RANDOM_SEED)
    result = uniform_cost_search(environment)

    assert result["success"] is True
    assert result["path"][0] == environment.start_state
    assert result["path"][-1] == environment.goal_state
    assert result["path_length"] == len(result["path"]) - 1

    total_cost = 0

    for i in range(len(result["path"]) - 1):

        current_state = result["path"][i]
        next_state = result["path"][i + 1]

        successors = environment.get_successors(current_state)

        valid_successors = {
            state: cost for state, action, cost in successors
        }

        assert next_state in valid_successors

        total_cost += valid_successors[next_state]

    assert result["path_cost"] == total_cost
