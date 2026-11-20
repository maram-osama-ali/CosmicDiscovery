# Cosmic Discovery – Deep Space Exploration

## Project Overview

**Cosmic Discovery** is an Artificial Intelligence search project that simulates a spacecraft navigating through a three-dimensional space environment to reach a destination.

The environment contains asteroid obstacles and nebula regions with different movement costs. The spacecraft must find a valid path from its starting position to its goal.

The project implements and compares different AI search algorithms to study their performance in terms of path quality, computational time, and memory usage.

## Environment Design

The environment is represented as a 3D grid with the following dimensions:

- Width: 20
- Height: 20
- Depth: 5
- Total possible states: 2,000

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
| Normal Space | A free cell without a special effect | 1 |
| Nebula | A region that makes movement more expensive | 4 |
| Asteroid | An obstacle that cannot be crossed | Not allowed |

The environment uses the following probabilities:

- **Asteroid probability:** 18% in the four lower layers.
- **Nebula probability:** 12% in free cells.

The upper layer (`z = 4`) is obstacle-free. Protected vertical passages at the starting and goal positions ensure that a valid route between them exists.

### Reproducibility

The environment uses a fixed random seed (`42`) by default. This ensures that the same obstacles and nebula regions are generated when the same seed is used.

## Project Structure

```text
CosmicDiscovery/
│
├── algorithms/
│   ├── __init__.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── ucs.py
│   └── ids.py
│
├── analysis/
│   ├── __init__.py
│   └── performance_analysis.py
│
├── config/
│   ├── __init__.py
│   └── environment_config.py
│
├── environment/
│   ├── __init__.py
│   ├── state.py
│   ├── space_environment.py
│   └── visualization.py
│
├── experiments/
│   ├── __init__.py
│   ├── run_experiments.py
│   ├── collect_metrics.py
│   └── results/
│
├── tests/
│   ├── __init__.py
│   ├── test.py
│   └── test_bfs.py
│
├── report/
│   ├── phase1_report.md
│   └── contribution_statement.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Implemented Components

### 1. Environment Configuration

Created `config/environment_config.py` to define the grid dimensions, starting and goal positions, random seed, obstacle and nebula probabilities, movement costs, and available actions.

### 2. State Representation

Created `environment/state.py` to represent each spacecraft position using three coordinates: `x`, `y`, and `z`.

The State class also supports coordinate comparison, hashing, and readable representations.

### 3. Space Environment

Created `environment/space_environment.py` with the `SpaceEnvironment` class.

Its responsibilities include:

- Generating the 3D space environment.
- Creating asteroid obstacles and nebula regions.
- Checking whether positions are within grid boundaries.
- Validating spacecraft positions.
- Generating valid successor states.
- Calculating movement costs.
- Providing environment statistics.

### 4. Environment Testing

Created `tests/test.py` to verify the environment.

The tests cover:

- Grid dimensions and total number of possible states.
- State representation.
- Environment generation.
- Starting and goal position validity.
- Boundary checking.
- Successor generation.
- Movement cost calculation.
- Reproducibility using the same random seed.
- Protected starting and goal passages.
- Existence of a valid path through the upper layer.

All nine environment tests passed successfully.

### 5. Breadth-First Search (BFS)

Implemented Breadth-First Search in `algorithms/bfs.py`.

The algorithm uses:

- A FIFO queue to explore states level by level.
- A visited set to prevent revisiting states.
- A parent dictionary to reconstruct the solution path.
- Performance metrics to evaluate the search.

The implementation returns:

- Search success status.
- Solution path.
- Actions taken.
- Path cost.
- Path length.
- Generated nodes.
- Expanded nodes.
- Maximum frontier size.
- Runtime.

Created `tests/test_bfs.py` to verify the BFS solution and its movements.

**BFS test result:**

| Metric | Result |
|---|---:|
| Solution found | Yes |
| Path length | 38 |
| Path cost | 50 |
| Generated nodes | 1,714 |
| Expanded nodes | 1,706 |
| Maximum frontier | 96 |
| Runtime | Approximately 0.034 seconds |

*Runtime may vary depending on the machine and execution conditions.*

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

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Run Environment Tests

```bash
python -m tests.test
```

### 5. Run BFS Tests

```bash
python -m tests.test_bfs
```

## Current Development Status

- [x] Project structure and Git setup
- [x] Environment configuration
- [x] State representation
- [x] 3D space environment generation
- [x] Obstacle and nebula generation
- [x] Successor generation and movement costs
- [x] Environment testing
- [x] Breadth-First Search implementation
- [x] BFS testing
- [ ] Depth-First Search (DFS)
- [ ] Uniform-Cost Search (UCS)
- [ ] Iterative Deepening Search (IDS)
- [ ] Additional search algorithms for Phase II
- [ ] Performance comparison and visualizations
- [ ] Final project report

## Technologies Used

- **Python:** Main programming language.
- **Git and GitHub:** Version control and project collaboration.

## Project Repository

[Cosmic Discovery – GitHub](https://github.com/maram-osama-ali/CosmicDiscovery)

---