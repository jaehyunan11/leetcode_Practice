# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def maxLevelSum(self, root: TreeNode) -> int:
#         if root is None:
#             return 0

from collections import deque

queue = deque(['name', 'age', 'DOB'])
print(queue)

de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
# printing modified deque
print("The deque after appending at right is : ")
print(de)
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
# printing modified deque
print("The deque after appending at left is : ")
print(de)
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
# printing modified deque
print("The deque after deleting from right is : ")
print(de)
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
# printing modified deque
print("The deque after deleting from left is : ")
print(de)
