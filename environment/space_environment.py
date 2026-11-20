
"""
Cosmic Discovery - 3D Space Environment

Responsible for:
- Generating the 3D grid.
- Generating asteroid obstacles.
- Generating nebula regions.
- Validating spacecraft positions.
- Generating successor states.
- Calculating movement costs.
"""

import random
from environment.state import State
from config.environment_config import (
    GRID_WIDTH,
    GRID_HEIGHT,
    GRID_DEPTH,
    START_POSITION,
    GOAL_POSITION,
    RANDOM_SEED,
    OBSTACLE_PROBABILITY,
    NEBULA_PROBABILITY,
    NORMAL_COST,
    NEBULA_COST,
    ACTIONS,)


class SpaceEnvironment:

    def __init__(self, seed=RANDOM_SEED):

        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.depth = GRID_DEPTH

        self.start_state = State(*START_POSITION)
        self.goal_state = State(*GOAL_POSITION)

        self.seed = seed

        self.obstacles = set()
        self.nebula_cells = set()

        self._generate_environment()

    def _generate_environment(self):
        """
        Generate a reproducible space environment.

        The upper layer (z = 4) is obstacle-free.

        The four lower layers contain randomly generated
        obstacles, except for two protected vertical passages.
        """

        rng = random.Random(self.seed)

        # Protected passages:
        # One at the starting position.
        # One at the destination position.
        protected_columns = {
            (START_POSITION[0], START_POSITION[1]),
            (GOAL_POSITION[0], GOAL_POSITION[1]),
        }

        # Generate obstacles in the lower four layers.
        for z in range(self.depth - 1):

            for x in range(self.width):

                for y in range(self.height):

                    if (x, y) in protected_columns:
                        continue

                    if rng.random() < OBSTACLE_PROBABILITY:

                        self.obstacles.add(State(x, y, z))

        # Generate nebula regions in free cells.
        for z in range(self.depth):

            for x in range(self.width):

                for y in range(self.height):

                    state = State(x, y, z)

                    if state in self.obstacles:
                        continue

                    if rng.random() < NEBULA_PROBABILITY:

                        self.nebula_cells.add(state)

    def is_within_bounds(self, state):
        """Check whether a state belongs to the grid."""

        return (
            0 <= state.x < self.width
            and 0 <= state.y < self.height
            and 0 <= state.z < self.depth)

    def is_valid_state(self, state):
        """
        A valid state must:
        1. Be inside the grid.
        2. Not contain an asteroid.
        """

        return (
            self.is_within_bounds(state)
            and state not in self.obstacles)

    def is_goal(self, state):
        """Check whether the spacecraft reached its destination."""

        return state == self.goal_state

    def get_successors(self, current_state):
        """
        Generate all valid successor states.

        Returns:
            A list of (next_state, action, step_cost).
        """

        successors = []

        for action, (dx, dy, dz) in ACTIONS.items():

            next_state = State(
                current_state.x + dx,
                current_state.y + dy,
                current_state.z + dz
            )

            if self.is_valid_state(next_state):

                cost = self.get_step_cost(next_state)

                successors.append(
                    (next_state, action, cost)
                )

        return successors

    def get_step_cost(self, destination_state):
        """
        Calculate the cost of entering a destination cell.

        Normal space: 1
        Nebula region: 4
        """

        if destination_state in self.nebula_cells:
            return NEBULA_COST

        return NORMAL_COST

    def get_total_possible_states(self):
        """Return the theoretical number of grid positions."""

        return self.width * self.height * self.depth

    def get_traversable_states_count(self):
        """Return the number of positions without obstacles."""

        return (
            self.get_total_possible_states()
            - len(self.obstacles)
        )

    def get_environment_summary(self):
        """Return important environment statistics."""

        return {
            "dimensions": (
                self.width,
                self.height,
                self.depth
            ),
            "total_possible_states":
                self.get_total_possible_states(),

            "obstacle_count":
                len(self.obstacles),

            "traversable_states":
                self.get_traversable_states_count(),

            "nebula_count":
                len(self.nebula_cells),

            "start_state":
                self.start_state.to_tuple(),

            "goal_state":
                self.goal_state.to_tuple(),

            "random_seed":
                self.seed
        }
