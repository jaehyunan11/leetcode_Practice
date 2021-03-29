from collections import defaultdict


class Solution:
    def countComponents(self, n, edges):
        # Create our undirected graph.
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        print(graph)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                count += 1
        return count

        if count == 1 and len(edges) < n:
            return True
        else:
            return False


S = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(S.countComponents(n, edges))

print(-3 % 4)
