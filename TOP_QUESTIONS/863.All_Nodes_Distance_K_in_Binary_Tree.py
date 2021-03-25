# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def convert_into_graph(self, node, parent, graph):
        """
        3: [5, 1],
        5: [6, 2, 3],
        6: [5],
        2: [7, 4, 5],
        7: [2],
        4: [2],
        1: [0, 8, 3],
        0: [1], 8: [1]
        }
        """

        if not node:
            return
        if parent:
            graph[node].append(parent)
        if node.right:
            graph[node].append(node.right)
            self.convert_into_graph(node.right, node, graph)
        if node.left:
            graph[node].append(node.left)
            self.convert_into_graph(node.left, node, graph)

    def distanceK(self, root, target, K):
        graph = defaultdict(list)
        visit, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        self.convert_into_graph(root, None, graph)

        graph.append((target, 0))

        while q:
            node, dist = q.popleft()
            visit.add(node)

            if dist == K:
                res.append(node.val)

            # adjacency list traversal
            for nei in graph[node]:
                if nei not in visit:
                    q.append((nei, dist+1))
        return res


S = Solution()
root = [3, 5, 1, 6, 2, 0, 8, 0, 0, 7, 4]
print(S.convert_into_graph(root, None, graph))

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/448707/python-solution-convert-tree-to-graph-then-run-bfs-memory-beats-100


# # To convert into graph we need to know who is the parent
# def convert_into_graph(self, node, parent, g):
#     if not node:
#         return
#     if parent:
#         g[node].append(parent)
#     if node.right:
#         g[node].append(node.right)
#         self.convert_into_graph(node.right, node, g)
#     if node.left:
#         g[node].append(node.left)
#         self.convert_into_graph(node.left, node, g)

# def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

#     g = defaultdict(list)
#     visit, q, res = set(), deque(), []
#     # We have a graph, now we can use simply BFS to calculate K distance from node.
#     self.convert_into_graph(root, None, g)

#     q.append((target, 0))

#     while q:
#         n, d = q.popleft()
#         visit.add(n)

#         if d == K:
#             res.append(n.val)

#         # adjacency list traversal
#         for nei in g[n]:
#             if nei not in visit:
#                 q.append((nei, d+1))
#     return res

# Use BFS and return all the values K distance from target
# Tree cannot traverse backwards since tree is acyclic graph

# If we can convert to undirect graph we could simply run BFS on the adjacency list of each node

# To convert into graph we need to know who is the parent
