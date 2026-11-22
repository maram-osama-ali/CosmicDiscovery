
import matplotlib.pyplot as plt


def visualize_search(environment, result, algorithm_name):

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    
    if environment.obstacles:
        obstacles = list(environment.obstacles)

        ax.scatter(
            [s.x for s in obstacles],
            [s.y for s in obstacles],
            [s.z for s in obstacles],
            color="gray",
            marker="s",
            label="Obstacles",
            alpha=0.4,
            s=15
        )

    
    if environment.nebula_cells:
        nebula = list(environment.nebula_cells)

        ax.scatter(
            [s.x for s in nebula],
            [s.y for s in nebula],
            [s.z for s in nebula],
            color="purple",
            marker="o",
            label="Nebula",
            alpha=0.5,
            s=15
        )

   
    explored = set(result["explored_states"])

    if explored:
        ax.scatter(
            [s.x for s in explored],
            [s.y for s in explored],
            [s.z for s in explored],
            color="blue",
            marker=".",
            label="Explored States",
            alpha=0.4,
            s=12
        )

    
    path = result["path"]

    if path:
        ax.plot(
            [s.x for s in path],
            [s.y for s in path],
            [s.z for s in path],
            color="red",
            linewidth=2.5,
            marker="o",
            markersize=3,
            label="Final Path"
        )

    
    start = environment.start_state

    ax.scatter(
        start.x, start.y, start.z,
        color="green",
        marker="^",
        s=120,
        label="Start"
    )

   
    goal = environment.goal_state

    ax.scatter(
        goal.x, goal.y, goal.z,
        color="gold",
        marker="*",
        s=180,
        label="Goal"
    )

    ax.set_title(f"{algorithm_name} - Cosmic Discovery")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(0, environment.width - 1)
    ax.set_ylim(0, environment.height - 1)
    ax.set_zlim(0, environment.depth - 1)

    ax.legend()
    plt.tight_layout()

    return fig
