# Cosmic Discovery – Deep Space Exploration

## Project Overview

**Cosmic Discovery** is an Artificial Intelligence search project that simulates a spacecraft navigating through a three-dimensional space environment to reach a predefined destination.

The environment contains asteroid obstacles that cannot be crossed and nebula regions that increase movement costs.

The project implements and compares four uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Iterative Deepening Search (IDS)

The algorithms are evaluated based on solution quality, computational effort, runtime, and frontier size. The project also includes 3D search visualizations and performance comparison graphs.

## Environment Design

The environment is represented as a 3D grid with the following dimensions:

| Parameter | Value |
|---|---:|
| Width | 20 |
| Height | 20 |
| Depth | 5 |
| Total possible states | 2,000 |

### Starting and Goal Positions

- **Start:** `(0, 0, 0)`
- **Goal:** `(19, 19, 0)`

### Movement Actions

The spacecraft can move in six directions:

- RIGHT and LEFT
- FORWARD and BACKWARD
- UP and DOWN

Each action moves the spacecraft by one cell along one axis.

### Environment Elements

| Element | Description | Movement Cost |
|---|---|---:|
| Normal Space | A free cell | 1 |
| Nebula | A region with higher movement cost | 4 |
| Asteroid | An obstacle that cannot be crossed | Not allowed |

The environment uses a fixed random seed of 42 by default to ensure reproducibility.

- Obstacle probability: 18%.
- Nebula probability: 12%.
- Asteroids are generated only in the four lower layers.
- The upper layer (`z = 4`) is obstacle-free.
- Protected vertical passages at the start and goal positions ensure a valid route.

## Implemented Search Algorithms

### 1. Breadth-First Search (BFS)

BFS explores states level by level using a FIFO queue.

It uses a visited set to avoid revisiting states and a parent dictionary to reconstruct the solution path.

BFS finds a path with the minimum number of movements, but it does not guarantee the minimum total cost when movement costs differ.

### 2. Depth-First Search (DFS)

DFS explores one branch as deeply as possible before backtracking.

It uses a stack, a visited set, and a parent dictionary to manage the search and reconstruct the solution.

DFS can find a valid path but does not guarantee the shortest or cheapest path.

### 3. Uniform-Cost Search (UCS)

UCS expands the state with the lowest accumulated path cost.

It uses a priority queue and a best-cost dictionary to track the cheapest known route to each state.

Since all movement costs are positive, UCS guarantees an optimal minimum-cost solution.

### 4. Iterative Deepening Search (IDS)

IDS repeatedly performs depth-limited search while increasing the depth limit.

It combines depth-first exploration with repeated iterations to find a shallow solution.

The implementation records the best known depth of each state within each iteration and accumulates performance metrics across iterations.

## Performance Metrics

The project records the following metrics for each algorithm:

| Metric | Description |
|---|---|
| Success | Whether the goal was reached |
| Path Cost | Total cost of the returned path |
| Path Length | Number of movements |
| Generated Nodes | Number of generated nodes |
| Expanded Nodes | Number of expanded nodes |
| Maximum Frontier | Largest frontier size |
| Runtime | Execution time in seconds |

Experimental results are saved in `experiments/results.csv`.

## Project Structure

```text
CosmicDiscovery/
|
|-- algorithms/
|   |-- __init__.py
|   |-- bfs.py
|   |-- dfs.py
|   |-- ucs.py
|   |-- ids.py
|
|-- analysis/
|   |-- __init__.py
|   |-- performance_analysis.py
|   |-- plots/
|
|-- config/
|   |-- __init__.py
|   |-- environment_config.py
|
|-- environment/
|   |-- __init__.py
|   |-- state.py
|   |-- space_environment.py
|   |-- visualization.py
|
|-- experiments/
|   |-- __init__.py
|   |-- run_experiments.py
|   |-- collect_metrics.py
|   |-- run_visualizations.py
|   |-- results.csv
|
|-- tests/
|   |-- __init__.py
|   |-- test.py
|   |-- test_bfs.py
|   |-- test_dfs.py
|   |-- test_ucs.py
|   |-- test_ids.py
|
|-- visualizations/
|   |-- bfs_visualization.png
|   |-- dfs_visualization.png
|   |-- ucs_visualization.png
|   |-- ids_visualization.png
|
|-- report/
|   |-- phase1_report.md
|   |-- contribution_statement.md
|
|-- README.md
|-- requirements.txt
|-- .gitignore
```

## 3D Search Visualizations

The project generates a separate 3D visualization for each search algorithm using Matplotlib.

The visualizations display:

- Asteroid obstacles.
- Nebula regions.
- Explored states.
- The final solution path.
- Start and goal positions.

Generated images are saved in the `visualizations/` directory.

## Performance Analysis

The performance analysis script reads the experimental results and generates comparison graphs.

The generated plots include:

- Runtime comparison.
- Generated nodes comparison.
- Expanded nodes comparison.
- Maximum frontier comparison.
- Path cost and path length comparison.

The graphs are saved in `analysis/plots/`.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/maram-osama-ali/CosmicDiscovery.git
cd CosmicDiscovery
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Experiments

```bash
python -m experiments.run_experiments
```

This runs the four search algorithms and saves their performance metrics in `experiments/results.csv`.

### 6. Generate 3D Visualizations

```bash
python -m experiments.run_visualizations
```

### 7. Generate Performance Analysis

```bash
python -m analysis.performance_analysis
```

### 8. Run the Complete Test Suite

```bash
python -m pytest -v tests/test.py tests/test_bfs.py tests/test_dfs.py tests/test_ucs.py tests/test_ids.py
```

**Latest test result:** 13 tests passed.

## Technologies Used

- **Python:** Main programming language.
- **NumPy:** Numerical and array operations, where required by the project.
- **Matplotlib:** 3D visualizations and performance graphs.
- **Pytest:** Automated testing.
- **Git and GitHub:** Version control and collaboration.

## Development Status

- [x] Project structure and Git setup
- [x] Environment configuration
- [x] State representation
- [x] 3D space environment generation
- [x] Obstacle and nebula generation
- [x] Successor generation and movement costs
- [x] Environment testing
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform-Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Search algorithm testing
- [x] Performance metrics collection
- [x] Performance comparison and analysis
- [x] 3D search visualizations
- [x] Phase I report

## Project Repository

[Cosmic Discovery – GitHub](https://github.com/maram-osama-ali/CosmicDiscovery)