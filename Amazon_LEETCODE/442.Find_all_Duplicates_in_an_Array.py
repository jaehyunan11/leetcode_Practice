class Solution:
    def findDuplicates(self, nums):
        #         # First make each nums to absolute value
        #         # Find nums - 1 index.
        #         # Make it as negative values
        #         # Iterate nums
        #         # if num[i] > 0 then make it to negative value
        #         # else (num[i] < 0) then append to res array (it means it already visited)

        #         # [4,3,2,7,8,2,3,1]
        #         # 4-> 4-1 = 3 index
        #         # 3-> 3-1 = 2 index
        #         # 2-> 2-1 = 1 index
        #         # 7-> 7-1 = 6 index
        #         # 8-> 8-1 = 7 index
        #         # 2-> 2-1 = 1 index

        res = []
        for i in nums:
            i = abs(i)
            if nums[i-1] > 0:
                nums[i-1] *= -1
            else:
                res.append(i)
        return res
# TIME COMPLEXITY : O(N) ## Iterate each nums to compare whether visited or not. First time visited makes negative value otherwise append to duplicated_nums
# SPACE COMPLEXITY : O(1) No extra space is required, other than space for the output list. We re-use the input array to store visited status


S = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(S.findDuplicates(nums))


# from collections import Counter


# class Solution2:
#     def findDuplicates(self, nums):
#         return [x for x, y in Counter(nums).items() if y > 1]

# TIME : O(N)
# SPACE : O(1)


# class Solution3:
#     def findDuplicates(self, nums):
#         count, res = {}, []
#         for i in nums:
#             if i not in count:
#                 count[i] = 1
#             else:
#                 count[i] += 1
#         for i, j in count.items():
#             if j > 1:
#                 res.append(i)
#         return res

# TIME O(N)
# SAPCE : O(N)
