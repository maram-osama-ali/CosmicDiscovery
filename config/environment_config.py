"""
Cosmic Discovery - Environment Configuration

Central configuration for the Phase I and Phase II
deep-space search environment.
"""

# Grid dimensions
GRID_WIDTH = 20
GRID_HEIGHT = 20
GRID_DEPTH = 5

# Initial and goal positions
START_POSITION = (0, 0, 0)
# The minimum possible number of movements is 38
GOAL_POSITION = (19, 19, 0)

# Reproducibility
RANDOM_SEED = 42

# Environment generation
OBSTACLE_PROBABILITY = 0.18
NEBULA_PROBABILITY = 0.12

# Movement costs
NORMAL_COST = 1
NEBULA_COST = 4

# Movement actions
ACTIONS = {
    "RIGHT": (1, 0, 0), "LEFT": (-1, 0, 0),
    "FORWARD": (0, 1, 0), "BACKWARD": (0, -1, 0),
    "UP": (0, 0, 1), "DOWN": (0, 0, -1),}
