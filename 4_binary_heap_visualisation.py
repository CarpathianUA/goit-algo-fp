import heapq
import matplotlib.pyplot as plt


def build_max_heap(nodes):
    max_heap = []
    for item in nodes:
        heapq.heappush(max_heap, -item)
    return [-i for i in max_heap]


def draw_node(ax, node, pos, node_radius=0.5):
    circle = plt.Circle(pos, node_radius, color="skyblue", ec="black", lw=1.5, zorder=4)
    ax.add_patch(circle)
    plt.text(*pos, int(node), ha="center", va="center", zorder=5)


def draw_line(ax, pos1, pos2):
    line = plt.Line2D(
        [pos1[0], pos2[0]], [pos1[1], pos2[1]], color="gray", lw=1.5, zorder=3
    )
    ax.add_line(line)


def plot_binary_tree(heap, ax, node_idx=0, pos=(0, 0), level=0, width=4):
    if node_idx >= len(heap):
        return

    # calculate horizontal position to keep tree balanced
    x_offset = width / 2 ** (level + 0.5)
    left_child_idx = 2 * node_idx + 1
    right_child_idx = 2 * node_idx + 2

    draw_node(ax, heap[node_idx], pos)

    if left_child_idx < len(heap):
        left_pos = (pos[0] - x_offset, pos[1] - 2)  # go down and to the left
        draw_line(ax, pos, left_pos)
        plot_binary_tree(heap, ax, left_child_idx, left_pos, level + 1, width)

    if right_child_idx < len(heap):
        right_pos = (pos[0] + x_offset, pos[1] - 2)  # go down and to the right
        draw_line(ax, pos, right_pos)
        plot_binary_tree(heap, ax, right_child_idx, right_pos, level + 1, width)


if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")
    plt.xlim(-10, 10)
    plt.ylim(-10, 2)

    data = [20, 18, 15, 30, 10, 5, 7, 9, 8, 2, 1, 4, 6, 66]
    max_heap = build_max_heap(data)
    plot_binary_tree(max_heap, ax)
    plt.show()
