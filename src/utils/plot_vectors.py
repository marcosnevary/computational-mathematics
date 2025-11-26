import matplotlib.pyplot as plt
import numpy as np


def plot_vectors(
    titles: list[str],
    vectors_list: list[np.ndarray],
    *,
    comparison: bool,
    determinant: bool,
) -> None:
    def plot_graph(vectors: np.ndarray, ax: plt.Axes, title: str, colors: np.ndarray) -> None:
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)
        ax.set_xticks(range(-8, 9))
        ax.set_yticks(range(-8, 9))
        ax.grid(visible=True)

        for i, (x, y) in enumerate(vectors):
            ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=colors[i], zorder=3)
            pos_x = x + 0.1
            pos_y = y + 0.1 if y >= 0 else y - 0.4
            ax.text(pos_x, pos_y, f'({x}, {y})', fontsize=12, color=colors[i])

        if determinant:
            parallelogram = np.array([[0, 0], vectors[0], vectors[0] + vectors[1], vectors[1]])
            ax.fill(parallelogram[:, 0], parallelogram[:, 1], alpha=0.2, zorder=2)

            first_sum = 0
            second_sum = 0
            for i in range(4):
                x1, y1 = parallelogram[i]
                x2, y2 = parallelogram[(i + 1) % 4]
                first_sum += x1 * y2
                second_sum += y1 * x2
            area = abs(first_sum - second_sum) / 2

            det = np.linalg.det(vectors)

            ax.text(
                -7,
                6,
                f'Det = {det:.2f}\nÁrea = {area:.2f}',
                fontsize=9,
                bbox={'facecolor': 'white', 'edgecolor': 'black', 'boxstyle': 'round'},
            )

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(title)

    colors = plt.cm.tab10(range(len(vectors_list[0])))

    if not comparison:
        _, ax = plt.subplots(figsize=(6, 6))
        plot_graph(vectors_list[0], ax, titles[0], colors)

    else:
        _, axes = plt.subplots(1, len(vectors_list), figsize=(6 * len(vectors_list), 6))
        for i, vectors in enumerate(vectors_list):
            plot_graph(vectors, axes[i], titles[i], colors)

    plt.show()
