
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

    start_state = environment.start_state
    goal_state = environment.goal_state

    frontier = deque([start_state])
    visited = {start_state}
    parent = {}
    generated_nodes = 1 
    expanded_nodes = 0
    max_frontier = 1

    start_time = time.perf_counter()

    while frontier:

        current_state = frontier.popleft()

        if environment.is_goal(current_state):

            path = [current_state]
            actions = []
            path_cost = 0

            while current_state != start_state:

                previous_state, action, step_cost = parent[current_state]
                path.append(previous_state)
                actions.append(action)
                path_cost += step_cost
                current_state = previous_state

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

        expanded_nodes += 1
        successors = environment.get_successors(current_state)

        for next_state, action, step_cost in successors:

            if next_state not in visited:

                visited.add(next_state)
                parent[next_state] = (current_state, action, step_cost)

                frontier.append(next_state)
                generated_nodes += 1

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)


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
