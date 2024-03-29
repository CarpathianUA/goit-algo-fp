import heapq
import matplotlib.pyplot as plt


# max heap
def build_max_heap(nodes):
    max_heap = []
    for item in nodes:
        heapq.heappush(max_heap, -item)
    return [-i for i in max_heap]


# function to generate colors gradient
def generate_color(step, total_steps, start_color="#0000FF", end_color="#00FF00"):
    start_int = int(start_color[1:], 16)
    end_int = int(end_color[1:], 16)
    # Розбиваємо кольори на компоненти
    start_r = (start_int >> 16) & 255
    start_g = (start_int >> 8) & 255
    start_b = start_int & 255
    end_r = (end_int >> 16) & 255
    end_g = (end_int >> 8) & 255
    end_b = end_int & 255
    # Інтерполяція кольорів
    mix_r = int(start_r + (end_r - start_r) * (step / total_steps))
    mix_g = int(start_g + (end_g - start_g) * (step / total_steps))
    mix_b = int(start_b + (end_b - start_b) * (step / total_steps))
    # Формування нового кольору
    return f"#{mix_r:02x}{mix_g:02x}{mix_b:02x}"


def draw_node(ax, node, pos, color="skyblue"):
    circle = plt.Circle(pos, 0.5, color=color, ec="black", lw=1.5, zorder=4)
    ax.add_patch(circle)
    plt.text(*pos, str(node), ha="center", va="center", zorder=5, color="white")


def draw_edge(ax, pos1, pos2):
    line = plt.Line2D(
        [pos1[0], pos2[0]], [pos1[1], pos2[1]], color="gray", lw=1.5, zorder=3
    )
    ax.add_line(line)


# plot binary tree
def plot_binary_tree(
    heap, ax, visit_order, visit_colors, node_idx=0, pos=(0, 0), level=0, width=4
):
    if node_idx >= len(heap):
        return
    x_offset = width / 2 ** (level + 0.5)
    left_child_idx, right_child_idx = 2 * node_idx + 1, 2 * node_idx + 2
    color = (
        visit_colors[visit_order.index(node_idx)]
        if node_idx in visit_order
        else "skyblue"
    )
    draw_node(ax, heap[node_idx], pos, color=color)
    if left_child_idx < len(heap):
        left_pos = (pos[0] - x_offset, pos[1] - 2)
        draw_edge(ax, pos, left_pos)
        plot_binary_tree(
            heap,
            ax,
            visit_order,
            visit_colors,
            left_child_idx,
            left_pos,
            level + 1,
            width,
        )
    if right_child_idx < len(heap):
        right_pos = (pos[0] + x_offset, pos[1] - 2)
        draw_edge(ax, pos, right_pos)
        plot_binary_tree(
            heap,
            ax,
            visit_order,
            visit_colors,
            right_child_idx,
            right_pos,
            level + 1,
            width,
        )


# dfs traversal
def dfs(heap, node_idx=0, visit_order=None):
    if visit_order is None:
        visit_order = []
    if node_idx >= len(heap) or node_idx in visit_order:
        return
    visit_order.append(node_idx)
    left_child_idx = 2 * node_idx + 1
    right_child_idx = 2 * node_idx + 2
    if left_child_idx < len(heap):
        dfs(heap, left_child_idx, visit_order)
    if right_child_idx < len(heap):
        dfs(heap, right_child_idx, visit_order)
    return visit_order


# bfs traversal
def bfs(heap):
    visit_order = []
    queue = [0]
    while queue:
        node_idx = queue.pop(0)
        if node_idx < len(heap) and node_idx not in visit_order:
            visit_order.append(node_idx)
            left_child_idx = 2 * node_idx + 1
            right_child_idx = 2 * node_idx + 2
            if left_child_idx < len(heap):
                queue.append(left_child_idx)
            if right_child_idx < len(heap):
                queue.append(right_child_idx)
    return visit_order


if __name__ == "__main__":
    data = [20, 18, 15, 30, 10, 5, 7, 9, 8, 2, 1, 4, 6, 66]
    max_heap = build_max_heap(data)

    dfs_order = dfs(max_heap)
    dfs_colors = [generate_color(i, len(dfs_order)) for i in range(len(dfs_order))]

    _, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")
    plt.xlim(-10, 10)
    plt.ylim(-10, 2)
    plot_binary_tree(max_heap, ax, dfs_order, dfs_colors)
    plt.title("DFS Visualization")
    plt.show()

    bfs_order = bfs(max_heap)
    bfs_colors = [generate_color(i, len(bfs_order)) for i in range(len(bfs_order))]

    _, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")
    plt.xlim(-10, 10)
    plt.ylim(-10, 2)
    plot_binary_tree(max_heap, ax, bfs_order, bfs_colors)
    plt.title("BFS Visualization")
    plt.show()
