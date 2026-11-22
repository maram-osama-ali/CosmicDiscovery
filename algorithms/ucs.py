
import heapq
import time
from itertools import count


def uniform_cost_search(environment):

    start_state = environment.start_state
    goal_state = environment.goal_state

    counter = count()

    frontier = [(0, next(counter), start_state)]

    best_cost = {start_state: 0}
    parent = {}

    generated_nodes = 1
    expanded_nodes = 0
    max_frontier = 1

    start_time = time.perf_counter()

    while frontier:

        current_cost, _, current_state = heapq.heappop(frontier)

        # Ignore outdated entries
        if current_cost != best_cost[current_state]:
            continue

        if environment.is_goal(current_state):

            path = [current_state]
            actions = []
            path_cost = current_cost

            while current_state != start_state:

                previous_state, action, step_cost = parent[current_state]

                path.append(previous_state)
                actions.append(action)

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

            new_cost = current_cost + step_cost

            if new_cost < best_cost.get(next_state, float("inf")):

                best_cost[next_state] = new_cost

                parent[next_state] = (
                    current_state,
                    action,
                    step_cost
                )

                heapq.heappush(
                    frontier,
                    (new_cost, next(counter), next_state)
                )

                generated_nodes += 1

        max_frontier = max(max_frontier, len(frontier))

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
