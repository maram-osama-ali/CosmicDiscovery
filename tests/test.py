"""
Tests for Cosmic Discovery Environment.

This file tests:
1. Environment configuration.
2. State representation.
3. Space environment generation.
4. Boundaries.
5. Successors.
6. Movement costs.
7. Reproducibility.
8. Starting vertical column.
9. Guaranteed path.
"""

from config import environment_config
from environment.state import State
from environment.space_environment import SpaceEnvironment


def test_configuration():

    print("\nTEST 1: CONFIGURATION")

    assert environment_config.GRID_WIDTH == 20
    assert environment_config.GRID_HEIGHT == 20
    assert environment_config.GRID_DEPTH == 5
    assert environment_config.START_POSITION == (0, 0, 0)
    assert environment_config.GOAL_POSITION == (19, 19, 0)
    assert environment_config.NORMAL_COST == 1
    assert environment_config.NEBULA_COST == 4

    total_positions = (environment_config.GRID_WIDTH * environment_config.GRID_HEIGHT * environment_config.GRID_DEPTH)
    assert total_positions == 2000

    print("Configuration is correct.")
    print("Total possible positions:", total_positions)


def test_state():

    print("\n TEST 2: STATE")

    position = State(5, 7, 2)
    assert position.to_tuple() == (5, 7, 2)
    print("State representation is correct.")
    print("Position:", position.to_tuple())



def test_environment_generation():

    print("\n TEST 3: ENVIRONMENT GENERATION")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)
    assert environment.is_valid_state(State(0, 0, 0))
    assert environment.is_valid_state(State(19, 19, 0))

    print("Environment generated successfully.")
    print("Start position is valid.")
    print("Goal position is valid.")



def test_boundaries():

    print("\nTEST 4: BOUNDARIES")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)

    assert environment.is_within_bounds(State(0, 0, 0))
    assert environment.is_within_bounds(State(19, 19, 4))
    assert not environment.is_within_bounds(State(-1, 0, 0))
    assert not environment.is_within_bounds(State(20, 0, 0))
    assert not environment.is_within_bounds(State(0, 20, 0))
    assert not environment.is_within_bounds(State(0, 0, 5))

    print("All boundary tests passed.")


def test_successors():

    print("\nTEST 5: SUCCESSORS")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)
    current_position = State(0, 0, 0)
    successors = environment.get_successors(current_position)

    assert len(successors) > 0

    for next_state, action, cost in successors:

        assert environment.is_valid_state(next_state)
        assert action in environment_config.ACTIONS
        assert cost in [environment_config.NORMAL_COST, environment_config.NEBULA_COST]

    print("Successor generation is correct.")
    print("Number of successors:", len(successors))


def test_movement_costs():

    print("\nTEST 6: MOVEMENT COSTS")

    environment = SpaceEnvironment(seed=42)
    for position in environment.nebula_cells:

        cost = environment.get_step_cost(position)
        assert cost == environment_config.NEBULA_COST

    for z in range(environment.depth):
        for x in range(environment.width):
            for y in range(environment.height):

                position = State(x, y, z)

                if (environment.is_valid_state(position) and position not in environment.nebula_cells):

                    cost = environment.get_step_cost(position)
                    assert cost == environment_config.NORMAL_COST

    for position in environment.obstacles:
        assert not environment.is_valid_state(position)

    print("All movement cost tests passed.")
    print("Nebula cost:", environment_config.NEBULA_COST)
    print("Normal cost:", environment_config.NORMAL_COST)
    print("Obstacle validation is correct.")


def test_reproducibility():

    print("\nTEST 7: REPRODUCIBILITY")

    environment1 = SpaceEnvironment(seed=42)
    environment2 = SpaceEnvironment(seed=42)

    assert environment1.obstacles == environment2.obstacles
    assert environment1.nebula_cells == environment2.nebula_cells

    print("Same seed generates the same environment.")
    print("Reproducibility test passed.")



def test_starting_vertical_column():

    print("\nTEST 8: STARTING VERTICAL COLUMN")

    environment = SpaceEnvironment(seed=42)
    start_x = environment.start_state.x
    start_y = environment.start_state.y

    for z in range(environment.depth):

        position = State(start_x, start_y, z)
        assert environment.is_valid_state(position), (f"Starting vertical column contains an obstacle at {position}")

    print("Starting vertical column is completely free.")
    print("Positions checked:", environment.depth)



def test_guaranteed_path():

    print("\nTEST 9: GUARANTEED PATH")

    environment = SpaceEnvironment(seed=42)
    path = []

    for z in range(environment.depth):
        path.append(State(0, 0, z))

    for x in range(1, environment.width):
        path.append(State(x, 0, environment.depth - 1))

    for y in range(1, environment.height):
        path.append(State(environment.width - 1, y, environment.depth - 1))


    for z in range(environment.depth - 2, -1, -1):

        path.append(State(environment.width - 1, environment.height - 1,z))

    assert path[0] == environment.start_state
    assert path[-1] == environment.goal_state


    for position in path:
        assert environment.is_valid_state(position), (f"Invalid position found in path: {position}")

    for i in range(len(path) - 1):

        current_state = path[i]
        next_state = path[i + 1]
        successors = environment.get_successors(current_state)
        successor_states = [successor[0] for successor in successors]
        assert next_state in successor_states, (f"Invalid movement: {current_state} -> {next_state}")

    print("A complete valid path exists!")
    print("Start:", path[0].to_tuple())
    print("Goal:", path[-1].to_tuple())
    print("Number of positions:", len(path))
    print("Number of movements:", len(path) - 1)


if __name__ == "__main__":

    test_configuration()
    test_state()
    test_environment_generation()
    test_boundaries()
    test_successors()
    test_movement_costs()
    test_reproducibility()
    test_starting_vertical_column()
    test_guaranteed_path()
    print("ALL TESTS PASSED SUCCESSFULLY!")
