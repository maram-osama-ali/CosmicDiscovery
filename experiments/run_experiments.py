
from config.environment_config import RANDOM_SEED
from environment.space_environment import SpaceEnvironment

from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search
from algorithms.ucs import uniform_cost_search
from algorithms.ids import iterative_deepening_search

from experiments.collect_metrics import collect_metrics


def run_experiments():

    algorithms = {
        "BFS": breadth_first_search,
        "DFS": depth_first_search,
        "UCS": uniform_cost_search,
        "IDS": iterative_deepening_search
    }

    results = []

    print("Starting Search Algorithms Experiments...")
    print("=" * 50)

    
    for name, algorithm in algorithms.items():

        print(f"\nRunning {name}...")

        environment = SpaceEnvironment(seed=RANDOM_SEED)

        result = algorithm(environment)

        result["algorithm"] = name

        results.append(result)

        print(f"{name} completed!")
        print(f"Success: {result['success']}")

   
    collect_metrics(results)

    return results


if __name__ == "__main__":
    run_experiments()
