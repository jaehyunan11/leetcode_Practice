class Solution:
    def isPalindrome(self, x):
        """
        type x: int
        return type : bool

        """
        # if str(x) == str(x)[::-1]:
        #     return True

        # 1234
        # 1234 % x -> 4
        # 1234 // 10 -> 123
        # rev_num = rev_num * 10 + last digit
        # return orignal_num == rev_num

        # negative cannot be palindrome num since - sign
        if x < 0:
            return False

        original_num = x
        # reversed num
        rev_num = 0

        while x > 0:
            # get the last digit from x e.g. 121 % 10 return 1
            last_digit = x % 10
            # remove last digit from x e.g. 121 // 10 return 12
            x = x // 10
            # append last digit to right of rev_num e.g.
            rev_num = rev_num * 10 + last_digit
        return original_num == rev_num

# TIME : O(N) n is the number of digits in x
#      O(log(k)) k is the size of the number
# SPACE : O(1)
