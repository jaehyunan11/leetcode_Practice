"""
     4
    / \
   1   5
  / \   \
 2   3   9
"""

vertice = [4, 1, 5, 2, 3, 9]
adj_list = {}
adj_list[4] = [1, 5]
adj_list[1] = [2, 3]
adj_list[5] = [9]
adj_list[2] = []
adj_list[3] = []
adj_list[9] = []

stack = []
visited = []


def bfs(start):
    stack.append(start)

    while len(stack) > 0:
        cur = stack.pop()
        for neighbor in adj_list[cur]:
            if not neighbor in visited:
                stack.insert(0, neighbor)
        visited.append(cur)


bfs(4)

print(visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


bfs(visited, graph, 'A')
dfs(visited, graph, 'A')
