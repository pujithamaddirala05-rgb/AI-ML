from collections import deque

# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}

# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None

# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            if node == goal:
                return path

            # Reverse alphabetical order so alphabetical node is explored first
            for neighbour in sorted(graph[node], reverse=True):
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)

    return None

# Main
source = "Alice"
goal = "Bob"

print("BFS Path:")
print(" -> ".join(bfs(graph, source, goal)))

print()

print("DFS Path:")
print(" -> ".join(dfs(graph, source, goal)))