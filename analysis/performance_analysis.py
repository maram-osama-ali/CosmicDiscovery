
import csv
from pathlib import Path
import matplotlib.pyplot as plt



PROJECT_ROOT = Path(__file__).resolve().parent.parent


RESULTS_FILE = PROJECT_ROOT / "experiments" / "results.csv"


OUTPUT_DIR = Path(__file__).resolve().parent / "plots"


def load_results():
    """Load algorithm results from the CSV file."""

    if not RESULTS_FILE.exists():
        raise FileNotFoundError(
            f"Results file not found: {RESULTS_FILE}\n"
            "Run the experiments first."
        )

    with open(RESULTS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        results = list(reader)

    if not results:
        raise ValueError("The results CSV file is empty.")

    return results


def print_comparison(results):
    """Print a comparison table of all algorithms."""

    print("\n" + "=" * 85)
    print("             SEARCH ALGORITHMS PERFORMANCE COMPARISON")
    print("=" * 85)

    headers = [
        "Algorithm", "Path Cost", "Path Length",
        "Generated", "Expanded", "Max Frontier", "Runtime (s)"
    ]

    print(
        f"{headers[0]:<12}{headers[1]:<12}{headers[2]:<14}"
        f"{headers[3]:<13}{headers[4]:<12}{headers[5]:<15}{headers[6]:<12}"
    )
    print("-" * 85)

    for result in results:
        print(
            f"{result['algorithm']:<12}"
            f"{result['path_cost']:<12}"
            f"{result['path_length']:<14}"
            f"{result['generated_nodes']:<13}"
            f"{result['expanded_nodes']:<12}"
            f"{result['max_frontier']:<15}"
            f"{float(result['runtime']):<12.4f}"
        )

    print("=" * 85)


def create_graphs(results):
    """Create and save performance comparison graphs."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    algorithms = [r["algorithm"] for r in results]

    metrics = [
        ("runtime", "Runtime Comparison", "Runtime (seconds)",
         "runtime_comparison.png"),
        ("generated_nodes", "Generated Nodes Comparison",
         "Number of Generated Nodes", "generated_nodes.png"),
        ("expanded_nodes", "Expanded Nodes Comparison",
         "Number of Expanded Nodes", "expanded_nodes.png"),
        ("max_frontier", "Maximum Frontier Comparison",
         "Maximum Frontier Size", "max_frontier.png"),
    ]

    for metric, title, ylabel, filename in metrics:
        values = [float(r[metric]) for r in results]

        plt.figure(figsize=(9, 5))
        bars = plt.bar(algorithms, values)

        plt.title(title)
        plt.xlabel("Search Algorithm")
        plt.ylabel(ylabel)
        plt.grid(axis="y", linestyle="--", alpha=0.4)

        for bar, value in zip(bars, values):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{value:.3f}" if metric == "runtime" else f"{int(value)}",
                ha="center",
                va="bottom"
            )

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / filename, dpi=300)
        plt.close()

  
    path_costs = [float(r["path_cost"]) for r in results]
    path_lengths = [int(r["path_length"]) for r in results]

    plt.figure(figsize=(9, 5))
    x = range(len(algorithms))
    width = 0.35

    plt.bar(
        [i - width / 2 for i in x],
        path_costs,
        width,
        label="Path Cost"
    )

    plt.bar(
        [i + width / 2 for i in x],
        path_lengths,
        width,
        label="Path Length"
    )

    plt.xticks(list(x), algorithms)
    plt.title("Path Cost vs Path Length")
    plt.xlabel("Search Algorithm")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "path_comparison.png", dpi=300)
    plt.close()

    print(f"\nGraphs saved successfully in: {OUTPUT_DIR}")


def print_analysis(results):
    """Print basic observations from the experiment results."""

    successful = [r for r in results if r["success"].lower() == "true"]

    if not successful:
        print("\nNo algorithm successfully found the goal.")
        return

    fastest = min(successful, key=lambda r: float(r["runtime"]))
    cheapest = min(successful, key=lambda r: float(r["path_cost"]))
    shortest = min(successful, key=lambda r: int(r["path_length"]))
    fewest_expansions = min(
        successful, key=lambda r: int(r["expanded_nodes"])
    )

    print("\nPERFORMANCE ANALYSIS")
    print("-" * 40)
    print(f"Fastest algorithm: {fastest['algorithm']}")
    print(f"Lowest path cost: {cheapest['algorithm']}")
    print(f"Shortest path: {shortest['algorithm']}")
    print(f"Fewest expanded nodes: {fewest_expansions['algorithm']}")

    print("\nObservations:")

    print(
        "- BFS finds a shortest path in number of steps, "
        "but not necessarily the lowest-cost path."
    )
    print(
        "- UCS considers step costs and finds the lowest-cost path "
        "when step costs are positive."
    )
    print(
        "- DFS may find a longer path because it explores "
        "one branch deeply before backtracking."
    )
    print(
        "- IDS repeats depth-limited searches, which can increase "
        "the number of generated and expanded nodes."
    )
    print(
        "- Runtime and memory-related measurements depend on "
        "the environment and the particular experiment."
    )


def main():
    results = load_results()

    print_comparison(results)
    create_graphs(results)
    print_analysis(results)


if __name__ == "__main__":
    main()
