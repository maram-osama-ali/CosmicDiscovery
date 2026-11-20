
"""
Cosmic Discovery - Breadth-First Search (BFS)

BFS explores the environment level by level.

It uses:
- A queue to manage unexplored states.
- A visited set to avoid revisiting states.
- A parent dictionary to reconstruct the solution path.
- Metrics to evaluate algorithm performance.
"""

from collections import deque
import time


def breadth_first_search(environment):

    # ==========================================
    # 1. INITIALIZATION
    # ==========================================

    start_state = environment.start_state
    goal_state = environment.goal_state

    # Queue: stores states waiting to be explored.
    frontier = deque([start_state])

    # Visited: stores states that have already been discovered.
    visited = {start_state}

    # Parent: remembers how we reached each discovered state.
    # Each entry stores: previous state, action, movement cost.
    parent = {}

    # ==========================================
    # 2. INITIALIZE METRICS
    # ==========================================

    generated_nodes = 1  # Includes the starting state.
    expanded_nodes = 0
    max_frontier = 1

    start_time = time.perf_counter()

    # ==========================================
    # 3. BFS MAIN LOOP
    # ==========================================

    while frontier:

        # Remove the oldest state from the queue.
        current_state = frontier.popleft()

        # Check whether we reached the goal.
        if environment.is_goal(current_state):

            # Reconstruct the solution path.
            path = [current_state]
            actions = []
            path_cost = 0

            while current_state != start_state:

                previous_state, action, step_cost = parent[current_state]

                path.append(previous_state)
                actions.append(action)

                path_cost += step_cost

                current_state = previous_state

            # Reverse to get the path from start to goal.
            path.reverse()
            actions.reverse()

            end_time = time.perf_counter()

            return {
                "success": True,
                "path": path,
                "actions": actions,
                "path_cost": path_cost,
                "path_length": len(path) - 1,
                "generated_nodes": generated_nodes,
                "expanded_nodes": expanded_nodes,
                "max_frontier": max_frontier,
                "runtime": end_time - start_time
            }

        # The current state is not the goal, so expand it.
        expanded_nodes += 1

        # Generate all valid successors.
        successors = environment.get_successors(current_state)

        for next_state, action, step_cost in successors:

            # Only discover a state once.
            if next_state not in visited:

                visited.add(next_state)

                # Remember how we reached this state.
                parent[next_state] = (
                    current_state,
                    action,
                    step_cost
                )

                # Add the new state to the end of the queue.
                frontier.append(next_state)

                generated_nodes += 1

        # Record the largest queue size.
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    # ==========================================
    # 4. NO SOLUTION FOUND
    # ==========================================

    end_time = time.perf_counter()

    return {
        "success": False,
        "path": [],
        "actions": [],
        "path_cost": None,
        "path_length": None,
        "generated_nodes": generated_nodes,
        "expanded_nodes": expanded_nodes,
        "max_frontier": max_frontier,
        "runtime": end_time - start_time
    }
