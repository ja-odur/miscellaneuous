from collections import deque, defaultdict


def reverse_graph(graph):
    _reversed = defaultdict(list)

    for node, neighbours in graph.items():
        for neighbour in neighbours:
            _reversed[neighbour].append(node)

    return _reversed

def dfs(_graph, _node, visited, stack):
    print("processing node - ", _node)
    if _node not in visited:
        visited[_node] = True

        for neighbor in _graph[_node]:
            if neighbor not in visited:
                visited, stack = dfs(_graph, neighbor, visited, stack)
        stack.append(_node)

    return visited, stack

def fill_stack(graph):
    visited = {}
    stack = deque()

    for node in graph:
        visited, stack = dfs(graph, node, visited, stack)

    return stack

def kosaraju_scc(graph):
    reversed_graph = reverse_graph(graph)
    stack = fill_stack(reversed_graph)
    visited = {}
    scc = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited, component = dfs(graph, node, visited, [])
            scc.append(component)

    return scc


# Other SCC components
# Tarjan's - https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# Path-based - https://en.wikipedia.org/wiki/Path-based_strong_component_algorithm
# Stackoverflow - https://stackoverflow.com/questions/70491133/implementing-kosarajus-algorithm-for-scc s


if __name__ == '__main__':
    graph = {
        "1": ["3"],
        "3": ["5", "11"],
        "5": ["1", "7", "9"],
        "11": ["6", "8"],
        "6": ["10"],
        "8": ["6"],
        "10": ["8"],
        "7": ["9"],
        "9": ["2", "4", "8"],
        "2": ["4", "10"],
        "4": ["7"],
    }
    print(kosaraju_scc(graph))
