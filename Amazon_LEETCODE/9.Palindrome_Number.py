class Solution:
    def isPalindrome(self, x):
        # if str(x) == str(x)[::-1]:
        #     return True
        # 1234
        # 1234 % x -> 4 (get the last digit)
        # 1234 // 10 -> 123 (separate the last digit)
        # rev_num = rev_num * 10 + last digit
        # return orignal_num == rev_num

        # negative cannot be palindrome num since - sign
        if x < 0:
            return False

        original_num = x
        # rev_num
        rev_num = 0

        while x > 0:
            # get the last digit from x
            last_digit = x % 10
            # remove last digit from x by integer division
            x = x // 10
            # append last digit to right of rev_num
            rev_num = rev_num * 10 + last_digit
        return original_num == rev_num

# TIME : O(log(n)) k is the size of the number (divide the input by 10 for every iteration)
# SPACE : O(1)


S = Solution()
x = 1234
print(S.isPalindrome(x))
