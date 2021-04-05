class Solution:
    def maxiumAverageSubtree(self, root):
        self.maxAvg = 0
        # find out valueSum (node.left + node.right + node)
        # find out valueCount (node.left + node.right + node)
        # Avg : valueSum / valueSize
        # leafNode
        #valueSum = node.val
        #valuesize = 1
        self.traverse(root)
        return self.maxAvg

    def traverse(self, root):
        if not root:
            return [0, 0]
        lsum, lcount = self.traverse(root.left)
        rsum, rcount = self.traverse(root.right)

        sum_ = lsum + rsum + root.val
        count = lcount + rcount + 1
        avg = sum_ / count

        self.maxAvg = max(self.maxAvg, avg)
        return [lsum+rsum+root.val, lcount+rcount+1]

# TIME : O(N) where N is the number of node in the tree. This is because we visit each and every node only onc

# Space : O(N), because we will create N states for each of the nodes in the tree.
