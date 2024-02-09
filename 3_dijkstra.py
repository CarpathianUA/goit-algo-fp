import heapq


def dijkstra(graph: dict, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # distance, vertex

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4, "F": 2},
        "F": {"E": 2},
    }

    print(dijkstra(graph, "A"))
