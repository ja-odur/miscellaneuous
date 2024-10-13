from collections import deque


def shortest_path(graph, node, target):
    # These lists should not be global. At each call of BFS, they should reset
    visited = {}  # Use a dict so you can store where the visit came from
    queue = deque()  # Use a deque to not lose efficiency with pop(0)

    visited[node] = None
    queue.append(node)

    while queue:
        current_node = queue.popleft()
        print("processing node - ", current_node)

        if current_node == target:  # Bingo!
            # Extract path from visited info
            path = []
            while current_node:
                path.append(current_node)
                current_node = visited[current_node] # Walk back

            return path[::-1] # Reverse path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited[neighbor] = current_node  # Remember where we came from
                queue.append(neighbor)



if __name__ == '__main__':
    graph = {
        'S': ['A', 'B', 'C'],
        'A': ['D'],
        'B': ['E'],
        'C': ['F', 'J'],
        'D': ['G'],
        'E': ['I', 'J'],
        'F': ['S'],
        'G': ['H'],
        'I': [],
        'J': [],
        'H': ['D']
    }

    path = shortest_path(graph, 'S', 'J')
    print(path)