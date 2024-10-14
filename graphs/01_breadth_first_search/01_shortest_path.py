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


# Dungeon Problem Statement
# You are trapped in a 2D dungeon and need to find the quickest way out! The dungeon is composed of unit
# cubes which may or may not be filled with rock. It takes one minute to move one unit north, south,
# east, west. You cannot move diagonally and the maze is surrounded by solid rock on all sides.
# Is an escape possible? If yes, how long will it take?
def shortest_path_dungeon(grid, r_start, c_start, r_end, c_end, rock="#"):
    row_count = len(grid)
    col_count = len(grid[0])

    def key(row, col):
        return f"({row}, {col})"

    def get_neighbors(row, col):
        dr = [-1, +1, 0, 0]
        dc = [0, 0, +1, -1]
        neighbors = []

        for i in range(4):
            rr = row + dr[i]
            cc = col + dc[i]

            if rr < 0 or cc < 0: continue;
            if rr >= row_count or cc >= col_count: continue;

            if grid[rr][cc] == rock: continue;

            neighbors.append((rr, cc))

        return neighbors

    visited = {}
    r_queue = deque()
    c_queue = deque()

    visited[key(r_start, c_start)] = None

    r_queue.append(r_start)
    c_queue.append(c_start)

    while r_queue:
        current_row = r_queue.popleft()
        current_col = c_queue.popleft()
        print("processing node - ", current_row, current_col)

        if current_row == r_end and current_col == c_end:
            path = []
            current_node = key(current_row, current_col)

            while current_node:
                path.append(current_node)
                current_node = visited[current_node]

            return path[::-1]

        for r, c in get_neighbors(current_row, current_col):
            if key(r, c) not in visited:
                visited[key(r, c)] = key(current_row, current_col)
                r_queue.append(r)
                c_queue.append(c)

def get_grid_coordinates(grid, target):
    for row, value in enumerate(grid):
        for col, col_value in enumerate(value):
            if col_value == target:
                return row, col
    return None, None


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

    grid = [
        "S..#...",
        ".#...#.",
        ".#.....",
        "..##...",
        "#.#E.#."
    ]

    r_start, c_start = get_grid_coordinates(grid, 'S')
    r_end, c_end = get_grid_coordinates(grid, 'E')

    path = shortest_path_dungeon(grid, r_start, c_start, r_end, c_end)
    print(path)