class Solution:
    def findSumTillSingleDigit(self, num):
        sum = 0
        while num > 0 or sum > 9:
            if (num == 0):
                num = sum
                sum = 0
            sum += num % 10
            num //= 10
        return sum


class Solution2:
    def findSumTillSingleDigit(self, num):
        # if a number is divisible by 9 then
        # the sum of its digit until sum ceomes sigle digit is always 9
        # n = 2880
        # 2+8+8 = 18 , 1+ 8 = 9
        # so number can be either 9x or 9x+K
        # first case always 9 second case is K
        if (num == 0):
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
# TIME and SPACE : O(1)


S = Solution()
S2 = Solution2()
num = 1234
print(S.findSumTillSingleDigit(num))
print(S2.findSumTillSingleDigit(num))
