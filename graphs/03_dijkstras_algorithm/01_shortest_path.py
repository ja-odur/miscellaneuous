import heapq


class Node:
    def __init__(self, vertex, parent=None):
        self.vertex = vertex
        self.parent = parent
        # Distance from source
        self.distance = float('inf')
        self.explored = False

    def __repr__(self):
        return f"Node(vertex={self.vertex}, parent={self.parent}, distance={self.distance})"


def dijkstra_shortest_path_table(graph, start):

    path_table = {}

    for node in graph:

        path_table[node] = Node(node)

    path_table[start].distance = 0

    queue = [(0, start)]

    while queue:
        distance, node = heapq.heappop(queue)

        if path_table[node].explored:
            continue

        path_table[node].explored = True

        for neighbor, neighbor_distance in graph[node]:
            if path_table[neighbor].explored:
                continue

            new_distance = distance + neighbor_distance

            if new_distance < path_table[neighbor].distance:
                path_table[neighbor].distance = new_distance
                path_table[neighbor].parent = node
                heapq.heappush(queue, (new_distance, neighbor))

    return path_table


def dijkstra_shortest_path_func_generator(graph, start):
    path_table = dijkstra_shortest_path_table(graph, start)

    def _shortest_path(end):
        path = []
        while True:
            try:
                node = path_table[end]
                path.append(node)
                if node.vertex == start:
                    break

                end = node.parent
            except Exception as exc:
                print(exc)
                return None

        return path

    return _shortest_path

# Explanation - https://www.youtube.com/watch?v=bZkzH5x0SKU


if __name__ == '__main__':
    graph = {
        "A": [("B", 2), ("D", 8)],
        "B": [("A", 2), ("D", 5), ("E", 6)],
        "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
        "E": [("B", 6), ("D", 3), ("F", 1), ("C", 9)],
        "F": [("D", 2), ("E", 1), ("C", 3)],
        "C": [("E", 9), ("F", 3)],
    }

    shortest_path = dijkstra_shortest_path_func_generator(graph, "A")

    print(shortest_path("C"))
    print(shortest_path("D"))

