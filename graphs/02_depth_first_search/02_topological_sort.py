def topological_sort(graph):
    visited = {}
    result = []

    def dfs(node):
        if visited.get(node):
            return

        visited[node] = True

        for neighbor in graph[node]:
            dfs(neighbor)

        result.append(node)

    for node in graph:
        dfs(node)

    return result[::-1]


if __name__ == "__main__":
    graph = {
        "5": ["3", "7"],
        "3": ["2", "4"],
        "7": ["8"],
        "2": [],
        "4": ["8"],
        "8": []
    }

    t_sort = topological_sort(graph)
    print(t_sort)
