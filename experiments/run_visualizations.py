
import os
import matplotlib.pyplot as plt

from environment.space_environment import SpaceEnvironment
from environment.visualization import visualize_search

from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search
from algorithms.ucs import uniform_cost_search
from algorithms.ids import iterative_deepening_search


def main():

    
    environment = SpaceEnvironment(seed=42)

    algorithms = {
        "BFS": breadth_first_search,
        "DFS": depth_first_search,
        "UCS": uniform_cost_search,
        "IDS": iterative_deepening_search
    }

    
    output_dir = "visualizations"
    os.makedirs(output_dir, exist_ok=True)

    for name, algorithm in algorithms.items():

        print(f"Running {name}...")

        result = algorithm(environment)

        if result["success"]:

            fig = visualize_search(
                environment,
                result,
                name
            )

            file_path = os.path.join(
                output_dir,
                f"{name.lower()}_visualization.png"
            )

            fig.savefig(file_path, dpi=300)
            plt.close(fig)

            print(f"{name} visualization saved: {file_path}")

        else:
            print(f"{name} failed to find a path.")


if __name__ == "__main__":
    main()
