class Solution:
    def trap(self, height):

        # water units trapped in each index of the array is calculated and added individually
        # water level at an index is determined by the lower of max_left and max_right for any bar i depends on min(left_max, right_max)
        # water trapped in index i = min(max_left, max_right) - height[i]
        # Therefore if max_left < max_right we fill the left index up to max_left and advance left pointer and vice versa
        # if max_left equals to max_right, moving either pointer would work

        # edge case
        if len(height) <= 2:
            return 0

        ans = 0

        # using two pointers i and j on indices 0 and n-1
        i = 1
        j = len(height) - 1

        # initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]

        while i <= j:
            # check the lmax and rmax for current i,j positions
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            # fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            # fill water upto rmax level for idex j and move j to the left
            else:
                ans += rmax - height[j]
                j -= 1
        return ans

# TIME : O(N) where n is length of the array
# Space : O(1) constant space and no extra space is required.


S = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(S.trap(height))
