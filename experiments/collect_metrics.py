
import csv
import os


def collect_metrics(results, output_file="experiments/results.csv"):

    columns = [
        "algorithm",
        "success",
        "path_cost",
        "path_length",
        "generated_nodes",
        "expanded_nodes",
        "max_frontier",
        "runtime"
    ]

    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)


    with open(output_file, "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=columns)

        writer.writeheader()

        for result in results:
            writer.writerow({
                column: result.get(column)
                for column in columns
            })

    print(f"\nResults saved successfully to: {output_file}")

    
    print("\nSearch Algorithms Performance Comparison")
    print("-" * 100)

    for result in results:

        print(f"\nAlgorithm: {result['algorithm']}")

        for column in columns[1:]:

            value = result.get(column)

            if column == "runtime" and value is not None:
                value = f"{value:.6f} seconds"

            print(f"{column}: {value}")

    return output_file
