from collections import deque


def dfs(graph, node):
    stack = deque()  # Use a deque to not lose efficiency with pop(0)

    stack.append(node)
    visited = {}

    while stack:
        current_node = stack.pop()
        print("processing node - ", current_node)

        if not visited.get(current_node):
            visited[current_node] = True

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def dfs_recursive(graph, node):
    visited = {}

    def _dfs(_graph, _node):
        print("processing node - ", _node)
        visited[_node] = True
        for neighbor in _graph[_node]:
            if neighbor not in visited:
                _dfs(_graph, neighbor)

    return _dfs(graph, node)



if __name__ == "__main__":
    graph = {
        "5": ["3", "7"],
        "3": ["2", "4"],
        "7": ["8"],
        "2": [],
        "4": ["8"],
        "8": []
    }

    dfs(graph, "5")
    dfs_recursive(graph, "5")
