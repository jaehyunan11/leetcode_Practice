from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def setEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = set()

        queue = []
        queue.append(s)

        # set s as visited
        visited.add(s)

        while queue:
            u = queue.pop(0)
            print(u, end=" ")

            # u => [v1, v2, v3]
            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)


g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.BFS(2)

# TIME COMPLEXITY : O(V+E)
# SPACE COMPLEXITY : O(V) we use queue which required to have extra space to enqueue and deque the nodes
# V => Vertices (nodes)
# E => Edges

# Initialize a Queue
# enqueue initial node to the queue
# Mark enqueued node as visited
# Begin a loop that will go on as long as the queue is not a empty
# Dequeue the node front of the queue and save it to a variable, let's call it V
# loop over all ne4ighbors of V that are not visited
# Enqueue current neighbor to the queue
# Mark current neighbor to the visited

# """
#      4
#     / \
#    1   5
#   / \   \
#  2   3   9
# """

# vertice = [4, 1, 5, 2, 3, 9]
# adj_list = {}
# adj_list[4] = [1, 5]
# adj_list[1] = [2, 3]
# adj_list[5] = [9]
# adj_list[2] = []
# adj_list[3] = []
# adj_list[9] = []

# stack = []
# visited = []

# def bfs(start):
#     stack.append(start)

#     while len(stack) > 0:
#         cur = stack.pop()
#         for neighbor in adj_list[cur]:
#             if not neighbor in visited:
#                 stack.insert(0, neighbor)
#         visited.append(cur)

# bfs(4)

# print(visited)

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# visited = []  # List to keep track of visited nodes.
# queue = []  # Initialize a queue

# def bfs(visited, graph, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         s = queue.pop(0)
#         print(s, end=" ")

#         for neighbor in graph[s]:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)

# # visited = set()  # Set to keep track of visited nodes.

# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# bfs(visited, graph, 'A')
# dfs(visited, graph, 'A')
