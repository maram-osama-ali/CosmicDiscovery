
import time


def depth_limited_search(environment, limit):

    start_state = environment.start_state

    frontier = [(start_state, 0)]

   
    best_depth = {start_state: 0}

    parent = {}

    generated_nodes = 1
    expanded_nodes = 0
    max_frontier = 1
    explored_states = []
    while frontier:

        current_state, depth = frontier.pop()

        if depth != best_depth[current_state]:
            continue
        explored_states.append(current_state)

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

            return {
                "success": True,
                "path": path,
                "actions": actions,
                "path_cost": path_cost,
                "path_length": len(path) - 1,
                "generated_nodes": generated_nodes,
                "expanded_nodes": expanded_nodes,
                "max_frontier": max_frontier,
                "explored_states": explored_states
            }

        if depth < limit:

            expanded_nodes += 1

            for next_state, action, step_cost in environment.get_successors(current_state):

                new_depth = depth + 1

                if new_depth < best_depth.get(next_state, float("inf")):

                    best_depth[next_state] = new_depth

                    parent[next_state] = (
                        current_state,
                        action,
                        step_cost
                    )

                    frontier.append((next_state, new_depth))
                    generated_nodes += 1

            max_frontier = max(max_frontier, len(frontier))

    return {
        "success": False,
        "path": [],
        "actions": [],
        "path_cost": None,
        "path_length": None,
        "generated_nodes": generated_nodes,
        "expanded_nodes": expanded_nodes,
        "max_frontier": max_frontier,
        "explored_states": explored_states
    }


def iterative_deepening_search(environment):

    start_time = time.perf_counter()

    max_depth = (
        environment.width *
        environment.height *
        environment.depth
    ) - 1

    total_generated = 0
    total_expanded = 0
    max_frontier = 0
    all_explored_states = []
    for limit in range(max_depth + 1):

        result = depth_limited_search(environment, limit)
        all_explored_states.extend(result["explored_states"])
        total_generated += result["generated_nodes"]
        total_expanded += result["expanded_nodes"]

        max_frontier = max(
            max_frontier,
            result["max_frontier"]
        )

        if result["success"]:

            result["generated_nodes"] = total_generated
            result["expanded_nodes"] = total_expanded
            result["max_frontier"] = max_frontier
            result["explored_states"] = all_explored_states
            result["runtime"] = time.perf_counter() - start_time

            return result

    return {
        "success": False,
        "path": [],
        "actions": [],
        "path_cost": None,
        "path_length": None,
        "generated_nodes": total_generated,
        "expanded_nodes": total_expanded,
        "max_frontier": max_frontier,
        "explored_states": all_explored_states,

        "runtime": time.perf_counter() - start_time
    }
