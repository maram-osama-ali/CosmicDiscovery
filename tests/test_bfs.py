
"""
Test Breadth-First Search for Cosmic Discovery.
"""

from config.environment_config import RANDOM_SEED
from environment.space_environment import SpaceEnvironment
from algorithms.bfs import breadth_first_search


def test_bfs():

    print("\n========== BFS TEST ==========")

    # Generate the environment.
    environment = SpaceEnvironment(seed=RANDOM_SEED)

    # Run BFS.
    result = breadth_first_search(environment)

    # Check whether a solution was found.
    assert result["success"] is True

    # Check the starting and ending positions.
    assert result["path"][0] == environment.start_state
    assert result["path"][-1] == environment.goal_state

    # Check the path length.
    assert result["path_length"] == len(result["path"]) - 1

    # Check that every movement is valid.
    for i in range(len(result["path"]) - 1):

        current_state = result["path"][i]
        next_state = result["path"][i + 1]

        successors = environment.get_successors(current_state)

        successor_states = [
            successor[0] for successor in successors
        ]

        assert next_state in successor_states

    # Display results.
    print("BFS found a solution!")
    print("Path length:", result["path_length"])
    print("Path cost:", result["path_cost"])
    print("Generated nodes:", result["generated_nodes"])
    print("Expanded nodes:", result["expanded_nodes"])
    print("Maximum frontier:", result["max_frontier"])
    print("Runtime:", result["runtime"], "seconds")

    print("\nBFS test passed successfully!")


if __name__ == "__main__":
    test_bfs()
