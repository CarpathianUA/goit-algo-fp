import matplotlib.pyplot as plt
import numpy as np


def draw_branch(ax, origin, angle, length, depth):
    if depth == 0:
        return None

    # calculate the end point of the branch
    end = (
        origin[0] + length * np.cos(np.radians(angle)),
        origin[1] + length * np.sin(np.radians(angle)),
    )

    ax.plot([origin[0], end[0]], [origin[1], end[1]], "k-", lw=2)

    new_length = length * 0.8

    # recursive calls for the two new branches
    draw_branch(ax, end, angle - 45, new_length, depth - 1)
    draw_branch(ax, end, angle + 45, new_length, depth - 1)


def pythagoras_tree(depth=5):
    _, ax = plt.subplots()

    # set the aspect of the plot to equal to ensure the angles are correct
    ax.set_aspect("equal")
    ax.axis("off")
    origin = (0.0, 0.0)  # starting point of the tree

    # initial angle
    angle = 90

    # initial branch length
    length = 40
    draw_branch(ax, origin, angle, length, depth)

    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 150)

    plt.show()


if __name__ == "__main__":
    depth = int(input("Enter the recursion depth: "))
    pythagoras_tree(depth)
