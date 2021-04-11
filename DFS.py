
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        # all node that we visited
        visited = set()
        stack = []
        stack.append(startNode)

        while(len(stack)):
            # set last element from stack
            curr = stack[-1]
            # remove the last element from the stack
            stack.pop()

            # curr node is not visited
            # Then add the curr node to the visited
            if curr not in visited:
                print(curr, end=" ")
                visited.add(curr)
            # loop the neighbor of the vertex
            # if the vertex is not visited
            # then add the vertex in the stack and iternate
            for vertex in self.graph[curr]:
                if vertex not in visited:
                    stack.append(vertex)


g = Graph()
g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.DFS(2)


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


# def dfs(start):
#     # Add to stack
#     stack.append(start)
#     # Loop stack
#     while len(stack) > 0:
#         # Move stack to current
#         cur = stack.pop()
#         for neighbor in adj_list[cur]:
#             if not neighbor in visited:
#                 stack.append(neighbor)
#         visited.append(cur)


# dfs(1)
# print(visited)
