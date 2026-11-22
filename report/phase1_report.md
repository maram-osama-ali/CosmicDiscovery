\# Cosmic Discovery – Phase I Report

\## Search Algorithms Applied to a 3D Space Exploration Problem



\### 1. Introduction



Cosmic Discovery is an Artificial Intelligence project that simulates a spacecraft navigating through a three-dimensional space environment to reach a predefined destination.



The environment contains asteroid obstacles that cannot be crossed and nebula regions that increase movement costs. The spacecraft must find a valid path from its initial position to the goal while navigating these conditions.



The main objective of Phase I is to model this problem as a state-space search problem, implement four uninformed search algorithms, and evaluate their performance in terms of solution quality, computational effort, runtime, and frontier size.



The implemented algorithms are:



\- Breadth-First Search (BFS)

\- Depth-First Search (DFS)

\- Uniform-Cost Search (UCS)

\- Iterative Deepening Search (IDS)



\### 2. Problem Modeling



\#### 2.1 State Representation



Each spacecraft position is represented by a state containing three coordinates:



`State(x, y, z)`



The environment is a three-dimensional grid with the following dimensions:



| Parameter | Value |

|---|---:|

| Width | 20 |

| Height | 20 |

| Depth | 5 |

| Total possible states | 2,000 |



The total number of possible states is calculated as:



`20 × 20 × 5 = 2,000 states`



\#### 2.2 Initial and Goal States



\- Initial state: `(0, 0, 0)`

\- Goal state: `(19, 19, 0)`



The minimum possible number of movements between these positions is 38, assuming movement along the X and Y axes without obstacles requiring a detour.



\#### 2.3 Actions



The spacecraft can perform six possible actions:



| Action | Coordinate Change |

|---|---|

| RIGHT | (+1, 0, 0) |

| LEFT | (-1, 0, 0) |

| FORWARD | (0, +1, 0) |

| BACKWARD | (0, -1, 0) |

| UP | (0, 0, +1) |

| DOWN | (0, 0, -1) |



Each action moves the spacecraft by one cell along a single axis.



\#### 2.4 Transition Model



A transition occurs when the spacecraft applies a valid action to its current state.



A successor state is valid if:



1\. Its coordinates remain within the grid boundaries.

2\. It is not occupied by an asteroid obstacle.



The environment generates valid successor states and associates each transition with its corresponding action and movement cost.



\#### 2.5 Path Cost



Movement costs depend on the destination cell:



| Cell Type | Movement Cost |

|---|---:|

| Normal space | 1 |

| Nebula | 4 |

| Asteroid | Not traversable |



The total path cost is the sum of the costs of all transitions along the solution path.



\#### 2.6 Environment Generation and Assumptions



The environment is generated using a fixed random seed of 42 to ensure reproducibility.



The generation parameters are:



\- Obstacle probability: 0.18 (18%).

\- Nebula probability: 0.12 (12%).

\- Normal movement cost: 1.

\- Nebula movement cost: 4.



Additional assumptions and design decisions:



\- Asteroid obstacles are generated only in the four lower layers.

\- The upper layer (`z = 4`) is obstacle-free.

\- The vertical columns at the starting and goal X-Y coordinates are protected from asteroid generation.

\- Nebula cells may appear in any layer, provided that the cell is not an obstacle.

\- The spacecraft moves only between adjacent cells along one axis.

\- All movement costs are positive.



These design decisions ensure that the environment contains obstacles and variable movement costs while maintaining a valid route between the starting and goal positions.



\### 3. Search Algorithm Implementations



Four uninformed search algorithms were implemented to solve the spacecraft navigation problem.



\#### 3.1 Breadth-First Search (BFS)



BFS explores the search space level by level, visiting states according to their depth from the initial state.



Implementation details:

\- Uses a FIFO queue.

\- Uses a visited set to avoid revisiting states.

\- Stores parent information to reconstruct the solution path.

\- Finds a path with the minimum number of movements when all transitions are treated equally.



Since this environment has different movement costs, BFS does not guarantee the minimum-cost solution.



\#### 3.2 Depth-First Search (DFS)



DFS explores one branch as deeply as possible before backtracking.



Implementation details:

\- Uses a stack-based search strategy.

\- Tracks visited states to avoid unnecessary repeated exploration.

\- Stores parent information for path reconstruction.



DFS can find a valid solution, but it does not guarantee the shortest path or the lowest-cost path.



\#### 3.3 Uniform-Cost Search (UCS)



UCS expands the state with the lowest accumulated path cost.



Implementation details:

\- Uses a priority queue.

\- Prioritizes states according to their accumulated path cost.

\- Updates paths when a cheaper route to a state is found.

\- Skips outdated priority queue entries.



Because all movement costs are positive, UCS guarantees an optimal minimum-cost solution.



\#### 3.4 Iterative Deepening Search (IDS)



IDS combines the depth-first search strategy with repeated depth limits.



Implementation details:

\- Performs depth-limited search repeatedly.

\- Increases the depth limit after each iteration.

\- Uses a best-depth record within each iteration.

\- Accumulates performance metrics across iterations.



IDS can find a shallow solution, but repeated searches may increase computational effort.



In this environment, IDS finds a solution with the minimum number of movements, but it does not guarantee the minimum path cost because movement costs are not uniform.



\### 4. Experimental Setup



All four algorithms were evaluated using the same environment configuration and random seed (42).



The experiments recorded the following performance metrics:



| Metric | Description |

|---|---|

| Success | Whether the algorithm reached the goal |

| Path Cost | Total cost of the returned path |

| Path Length | Number of movements in the path |

| Generated Nodes | Number of nodes generated during search |

| Expanded Nodes | Number of nodes expanded during search |

| Maximum Frontier | Largest number of nodes stored in the frontier |

| Runtime | Time taken to execute the algorithm |



The experiment results were saved in `experiments/results.csv` to support reproducibility and comparison.



\### 5. Experimental Results



The following table presents the measured results for the four algorithms using the fixed environment configuration.



| Metric | BFS | DFS | UCS | IDS |

|---|---:|---:|---:|---:|

| Success | Yes | Yes | Yes | Yes |

| Path Cost | 50 | 572 | 43 | 59 |

| Path Length | 38 | 428 | 40 | 38 |

| Generated Nodes | 1,714 | 1,632 | 1,724 | 165,635 |

| Expanded Nodes | 1,706 | 944 | 1,723 | 150,985 |

| Maximum Frontier | 96 | 879 | 118 | 66 |

| Runtime (seconds) | 0.0289 | 0.0149 | 0.1178 | 3.0783 |



These values represent one experiment run with seed 42. Runtime measurements may vary depending on the machine and execution conditions.



\### 6. Performance Analysis and Discussion



The experimental results reveal important differences between the four search algorithms.



\#### 6.1 Path Quality



\- \*\*BFS\*\* found a path of 38 movements with a total cost of 50.

\- \*\*DFS\*\* found a much longer path of 428 movements with a total cost of 572.

\- \*\*UCS\*\* achieved the lowest path cost of 43, although its path contained 40 movements.

\- \*\*IDS\*\* found a path of 38 movements with a total cost of 59.



These results demonstrate the difference between minimizing the number of movements and minimizing the total path cost.



BFS and IDS found paths with the minimum possible number of movements in this experiment. However, UCS found the cheapest path because it considers the different movement costs of normal and nebula cells.



\#### 6.2 Runtime Comparison



DFS was the fastest algorithm in this experiment, taking approximately 0.0149 seconds.



BFS required approximately 0.0289 seconds, while UCS required approximately 0.1178 seconds.



IDS had the longest runtime at approximately 3.0783 seconds because it repeats depth-limited searches with increasing depth limits.



\#### 6.3 Search Effort



DFS expanded the fewest nodes (944), while IDS expanded the largest number (150,985).



IDS also generated 165,635 nodes, significantly more than the other algorithms, due to repeated search iterations.



BFS and UCS expanded a similar number of nodes: 1,706 and 1,723, respectively.



\#### 6.4 Frontier Size



The maximum frontier size indicates the largest number of stored nodes during the search.



DFS had the largest maximum frontier (879), followed by UCS (118), BFS (96), and IDS (66).



A smaller maximum frontier can indicate lower frontier storage requirements, but it does not represent the complete memory usage of an algorithm.



\### 7. Theoretical Complexity Analysis



Let:

\- `b` represent the branching factor (maximum number of successors per state).

\- `d` represent the depth of the shallowest solution.

\- `m` represent the maximum search depth.



For this environment, the maximum branching factor is 6 because the spacecraft has six possible movement actions.



| Algorithm | Time Complexity | Space Complexity | Complete? | Optimal? |

|---|---|---|---|---|

| BFS | O(b^d) | O(b^d) | Yes | Yes, for equal step costs |

| DFS | O(b^m) | O(bm) | Yes, with finite graph and visited-state handling | No |

| UCS | Exponential in the worst case | Exponential in the worst case | Yes, with positive step costs | Yes |

| IDS | O(b^d) | O(bd) | Yes | Yes, for equal step costs |



The theoretical properties depend on the search implementation and problem assumptions.



In particular:

\- BFS and IDS are optimal in terms of the number of movements when all step costs are equal.

\- UCS is optimal for the minimum total path cost when all step costs are positive.

\- DFS does not guarantee an optimal solution.

\- The implemented environment is finite, and the search algorithms use visited-state or depth-handling mechanisms to avoid unbounded repeated exploration.



\### 8. Limitations



The experiment has several limitations:



1\. Results are based on one fixed random seed and one environment configuration.

2\. Runtime measurements can vary across machines and execution conditions.

3\. A single experiment does not establish general performance superiority.

4\. The maximum frontier size is used as a memory-related metric, but it does not measure total memory consumption.

5\. The algorithms are evaluated on one fixed grid size of 2,000 possible states.



Further experiments with different random seeds and environment sizes could provide a more comprehensive evaluation.



\### 9. Search Visualization



To better understand the behavior of each search algorithm, 3D visualizations were generated using Matplotlib.



Each visualization displays:



\- \*\*Obstacles:\*\* Asteroid cells that cannot be traversed.

\- \*\*Nebula cells:\*\* Regions with higher movement costs.

\- \*\*Explored states:\*\* States visited during the search.

\- \*\*Final path:\*\* The path returned by the search algorithm.

\- \*\*Start state:\*\* The initial spacecraft position.

\- \*\*Goal state:\*\* The destination.



Four separate visualizations were generated:



| Algorithm | Visualization File |

|---|---|

| BFS | `visualizations/bfs\_visualization.png` |

| DFS | `visualizations/dfs\_visualization.png` |

| UCS | `visualizations/ucs\_visualization.png` |

| IDS | `visualizations/ids\_visualization.png` |



The visualizations help compare the exploration patterns and solution paths produced by the algorithms.



They also demonstrate how different search strategies behave in the same three-dimensional environment.



\### 10. Conclusion



This project modeled a spacecraft navigation problem as a state-space search problem in a three-dimensional grid.



Four uninformed search algorithms were implemented and evaluated: BFS, DFS, UCS, and IDS.



The experimental results showed that:



\- BFS and IDS found paths with the minimum number of movements in the tested environment.

\- UCS found the lowest-cost solution because it considers the different movement costs.

\- DFS achieved the shortest runtime in this particular experiment, but returned a much longer and more expensive path.

\- IDS required significantly more computational effort because it repeated depth-limited searches.



The project demonstrates that no single search algorithm is best for every performance criterion. The appropriate algorithm depends on whether the main objective is minimizing path length, minimizing total cost, reducing runtime, or controlling memory usage.



Overall, Phase I provided a practical comparison of uninformed search strategies and demonstrated how theoretical search properties relate to measured performance in a 3D navigation environment.



\*\*Implementation-Specific Complexity Note:\*\*



The classical IDS space complexity is O(bd), assuming depth-limited search uses depth-first tree search without storing all previously visited states.



Our implementation uses additional graph-search bookkeeping structures, including a `best\_depth` dictionary, a `parent` dictionary, and an accumulated `explored\_states` list across iterations. Therefore, its actual memory consumption is higher than the classical O(bd) bound and depends on the number of stored states and exploration records.



\*\*DFS Implementation-Specific Complexity Note:\*\*



The classical DFS space complexity is O(bm), assuming that only the current search path and frontier are stored.



Our implementation uses additional data structures, including a `visited` set to prevent revisiting states and a `parent` dictionary to reconstruct the solution path. It also stores an `explored\_states` list for performance analysis and visualization. Therefore, its actual memory consumption can be higher than the classical O(bm) bound and depends on the number of visited and explored states.



\*\*BFS Implementation-Specific Complexity Note:\*\*



The classical BFS space complexity is O(b^d), where b is the branching factor and d is the depth of the shallowest solution.



Our implementation uses additional data structures, including a `visited` set, a `parent` dictionary, and an `explored\_states` list. These structures store information about discovered and explored states. Therefore, the actual memory consumption depends on the number of discovered and explored states, in addition to the frontier size.



\*\*UCS Implementation-Specific Complexity Note:\*\*



Our UCS implementation uses a priority queue, a `best\_cost` dictionary, a `parent` dictionary, and an `explored\_states` list.



The priority queue may contain multiple entries for the same state when a better path is discovered. Outdated entries are skipped when removed from the queue. Therefore, the actual memory consumption depends on the number of queue entries and stored states.



The algorithm guarantees an optimal solution when all step costs are positive, as in our environment.





\### 11. Reproducibility



To reproduce the experiment results, activate the project's virtual environment, install the required dependencies, and run:



```bash

python -m experiments.run\_experiments

```



To generate the 3D search visualizations, run:



```bash

python -m experiments.run\_visualizations

```



To generate the performance comparison tables and graphs, run:



```bash

python -m analysis.performance\_analysis

```



To execute the complete test suite, run:



```bash

python -m pytest -v tests/test.py tests/test\_bfs.py tests/test\_dfs.py tests/test\_ucs.py tests/test\_ids.py



```

