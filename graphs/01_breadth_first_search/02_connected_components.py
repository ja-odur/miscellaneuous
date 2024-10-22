from collections import deque


def connected_components(graph):
    seen = set()
    components = []

    for vertex in graph:
        if vertex in seen:
            continue

        connected = []
        queue = deque()

        queue.append(vertex)
        seen.add(vertex)
        connected.append(vertex)


        while queue:
            current_vertex = queue.popleft()

            for neighbor in graph[current_vertex]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
                    connected.append(neighbor)

        components.append(connected)

    return components


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

    components = connected_components(graph)
    print(components)

    graph = {
        '1': ['3', '5'],
        '3': ['1', '5'],
        '5': ['1', '3', '7', '9'],
        '7': ['5'],
        '9': ['5'],
        '2': ['4'],
        '4': ['2'],
        '6': ['8', '10'],
        '8': ['6'],
        '10': ['6'],
    }

    components = connected_components(graph)
    print(components)
