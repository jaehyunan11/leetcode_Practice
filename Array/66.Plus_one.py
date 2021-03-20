class Solution:
    def plusOne(self, digits):
        n = len(digits)
        # move along the input array starting from the end
        for i in range(n):
            # rightmost integer
            idx = n - 1 - i
            # set all the nines at the end of array to zero
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits


S = Solution()
digits = [1, 2, 3]
print(S.plusOne(digits))
