
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

        rng = random.Random(self.seed)
        protected_columns = {(START_POSITION[0], START_POSITION[1]),(GOAL_POSITION[0], GOAL_POSITION[1])}

        for z in range(self.depth - 1):

            for x in range(self.width):

                for y in range(self.height):

                    if (x, y) in protected_columns:
                        continue

                    if rng.random() < OBSTACLE_PROBABILITY:

                        self.obstacles.add(State(x, y, z))

        for z in range(self.depth):

            for x in range(self.width):

                for y in range(self.height):

                    state = State(x, y, z)

                    if state in self.obstacles:
                        continue

                    if rng.random() < NEBULA_PROBABILITY:

                        self.nebula_cells.add(state)


    def is_within_bounds(self, state):

        return (0 <= state.x < self.width and 0 <= state.y < self.height and 0 <= state.z < self.depth)


    def is_valid_state(self, state):

        return ( self.is_within_bounds(state) and state not in self.obstacles)


    def is_goal(self, state):

        return state == self.goal_state


    def get_successors(self, current_state):
        successors = []

        for action, (dx, dy, dz) in ACTIONS.items():

            next_state = State(
                current_state.x + dx,
                current_state.y + dy,
                current_state.z + dz)

            if self.is_valid_state(next_state):

                cost = self.get_step_cost(next_state)
                successors.append((next_state, action, cost))

        return successors

    def get_step_cost(self, destination_state):

        if destination_state in self.nebula_cells:
            return NEBULA_COST

        return NORMAL_COST

    def get_total_possible_states(self):

        return self.width * self.height * self.depth


    def get_traversable_states_count(self):

        return (self.get_total_possible_states() - len(self.obstacles))


    def get_environment_summary(self):

        return {
            "dimensions": (self.width, self.height, self.depth),

            "total_possible_states": self.get_total_possible_states(),

            "obstacle_count": len(self.obstacles),

            "traversable_states": self.get_traversable_states_count(),

            "nebula_count": len(self.nebula_cells),

            "start_state": self.start_state.to_tuple(),

            "goal_state": self.goal_state.to_tuple(),

            "random_seed": self.seed}
