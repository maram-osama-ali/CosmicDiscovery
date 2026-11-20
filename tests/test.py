
"""
Tests for Cosmic Discovery Environment.

This file tests:
1. Environment configuration.
2. State representation.
3. Space environment generation.
4. Valid positions and movement.
5. Movement costs.
6. Reproducibility.
"""

from config import environment_config
from environment.state import State
from environment.space_environment import SpaceEnvironment


# ==========================================
# TEST 1: ENVIRONMENT CONFIGURATION
# ==========================================

def test_configuration():

    print("\n========== TEST 1: CONFIGURATION ==========")

    assert environment_config.GRID_WIDTH == 20
    assert environment_config.GRID_HEIGHT == 20
    assert environment_config.GRID_DEPTH == 5

    assert environment_config.START_POSITION == (0, 0, 0)
    assert environment_config.GOAL_POSITION == (19, 19, 0)

    assert environment_config.NORMAL_COST == 1
    assert environment_config.NEBULA_COST == 4

    total_positions = (
        environment_config.GRID_WIDTH
        * environment_config.GRID_HEIGHT
        * environment_config.GRID_DEPTH
    )

    assert total_positions == 2000

    print("Configuration is correct.")
    print("Total possible positions:", total_positions)


# ==========================================
# TEST 2: STATE REPRESENTATION
# ==========================================

def test_state():

    print("\n========== TEST 2: STATE ==========")

    position = State(5, 7, 2)

    assert position.to_tuple() == (5, 7, 2)

    print("State representation is correct.")
    print("Position:", position.to_tuple())


# ==========================================
# TEST 3: ENVIRONMENT GENERATION
# ==========================================

def test_environment_generation():

    print("\n========== TEST 3: ENVIRONMENT GENERATION ==========")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)

    assert environment.is_valid_state(State(0, 0, 0))
    assert environment.is_valid_state(State(19, 19, 0))

    print("Environment generated successfully.")
    print("Start position is valid.")
    print("Goal position is valid.")


# ==========================================
# TEST 4: BOUNDARIES
# ==========================================

def test_boundaries():

    print("\n========== TEST 4: BOUNDARIES ==========")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)

    assert environment.is_within_bounds(State(0, 0, 0))
    assert environment.is_within_bounds(State(19, 19, 4))

    assert not environment.is_within_bounds(State(-1, 0, 0))
    assert not environment.is_within_bounds(State(20, 0, 0))
    assert not environment.is_within_bounds(State(0, 20, 0))
    assert not environment.is_within_bounds(State(0, 0, 5))

    print("All boundary tests passed.")


# ==========================================
# TEST 5: SUCCESSORS
# ==========================================

def test_successors():

    print("\n========== TEST 5: SUCCESSORS ==========")

    environment = SpaceEnvironment(seed=environment_config.RANDOM_SEED)

    current_position = State(0, 0, 0)

    successors = environment.get_successors(current_position)

    assert len(successors) > 0

    for next_state, action, cost in successors:

        assert environment.is_valid_state(next_state)
        assert action in environment_config.ACTIONS
        assert cost in [
            environment_config.NORMAL_COST,
            environment_config.NEBULA_COST
        ]

    print("Successor generation is correct.")
    print("Number of successors:", len(successors))


# ==========================================
# TEST 6: MOVEMENT COSTS
# ==========================================


# ==========================================
# TEST 6: MOVEMENT COSTS
# ==========================================

def test_movement_costs():

    print("\n========== TEST 6: MOVEMENT COSTS ==========")

    environment = SpaceEnvironment(seed=42)

    # Check that every nebula cell has movement cost 4.
    for position in environment.nebula_cells:

        cost = environment.get_step_cost(position)

        assert cost == environment_config.NEBULA_COST

    # Check that every normal free cell has movement cost 1.
    for z in range(environment.depth):
        for x in range(environment.width):
            for y in range(environment.height):

                position = State(x, y, z)

                if (
                    environment.is_valid_state(position)
                    and position not in environment.nebula_cells
                ):

                    cost = environment.get_step_cost(position)

                    assert cost == environment_config.NORMAL_COST

    # Check that obstacle cells are invalid.
    for position in environment.obstacles:

        assert not environment.is_valid_state(position)

    print("All movement cost tests passed.")
    print("Nebula cost:", environment_config.NEBULA_COST)
    print("Normal cost:", environment_config.NORMAL_COST)
    print("Obstacle validation is correct.")



# ==========================================
# TEST 7: REPRODUCIBILITY
# ==========================================


# ==========================================
# TEST 7: REPRODUCIBILITY
# ==========================================

def test_reproducibility():

    print("\n========== TEST 7: REPRODUCIBILITY ==========")

    environment1 = SpaceEnvironment(seed=42)
    environment2 = SpaceEnvironment(seed=42)

    assert environment1.obstacles == environment2.obstacles

    assert environment1.nebula_cells == environment2.nebula_cells

    print("Same seed generates the same environment.")
    print("Reproducibility test passed.")




# ==========================================
# TEST 8: STARTING VERTICAL COLUMN
# ==========================================

def test_starting_vertical_column():

    print("\n========== TEST 8: STARTING VERTICAL COLUMN ==========")

    environment = SpaceEnvironment(seed=42)

    start_x = environment.start_state.x
    start_y = environment.start_state.y

    # Check every position from the starting layer to the upper layer.
    for z in range(environment.depth):

        position = State(start_x, start_y, z)

        assert environment.is_valid_state(position), (
            f"Starting vertical column contains an obstacle at {position}"
        )

    print("Starting vertical column is completely free.")
    print("Positions checked:", environment.depth)




# ==========================================
# TEST 9: GUARANTEED PATH THROUGH UPPER LAYER
# ==========================================

def test_guaranteed_path():

    print("\n========== TEST 9: GUARANTEED PATH ==========")

    environment = SpaceEnvironment(seed=42)

    path = []

    # 1. Move vertically from the start to the upper layer.
    for z in range(environment.depth):

        path.append(State(0, 0, z))

    # 2. Move horizontally along the X-axis.
    for x in range(1, environment.width):

        path.append(State(x, 0, environment.depth - 1))

    # 3. Move horizontally along the Y-axis.
    for y in range(1, environment.height):

        path.append(State(environment.width - 1, y, environment.depth - 1))

    # 4. Move vertically down to the goal.
    for z in range(environment.depth - 2, -1, -1):

        path.append(State(
            environment.width - 1,
            environment.height - 1,
            z
        ))

    # Check that the path starts at the correct position.
    assert path[0] == environment.start_state

    # Check that the path ends at the correct position.
    assert path[-1] == environment.goal_state

    # Check that every position is valid.
    for position in path:

        assert environment.is_valid_state(position), (
            f"Invalid position found in path: {position}"
        )

    # Check that every consecutive pair is a valid movement.
    for i in range(len(path) - 1):

        current_state = path[i]
        next_state = path[i + 1]

        successors = environment.get_successors(current_state)

        successor_states = [
            successor[0] for successor in successors
        ]

        assert next_state in successor_states, (
            f"Invalid movement: {current_state} -> {next_state}"
        )

    print("A complete valid path exists!")
    print("Start:", path[0].to_tuple())
    print("Goal:", path[-1].to_tuple())
    print("Number of positions:", len(path))
    print("Number of movements:", len(path) - 1)




# ==========================================
# RUN ALL TESTS
# ==========================================

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

    print("\n========================================")
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("========================================")
