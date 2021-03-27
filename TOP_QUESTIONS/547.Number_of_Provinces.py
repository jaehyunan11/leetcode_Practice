class Solution:
    def findCircleNum(self, isConnected):
        # N = len(isConnected)
        # visited = set()
        # result = 0
        # print(N)
        # for i in range(N):
        #     if i in visited:
        #         continue
        #     visited.add(i)
        #     print(visited)
        #     result += 1
        #     stack = [i]
        #     while stack:
        #         curr = stack.pop()
        #         # find neighbor
        #         for nei in range(i+1, N):
        #             if nei not in visited and isConnected[curr][nei]:
        #                 visited.add(nei)
        #                 stack.append(nei)
        # return result


S = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(S.findCircleNum(isConnected))
