class Solution:
    def myAtoi(self, s):
        # Step 1: Strip off leading and training spaces
        # Step 2: check for a - or + as the first character in the input and set the flag accoringly, also remove the character, as we will bring it back before returning
        # Step 3: iterate through the string to convert any digit into integer and break if the character is not a digit
        # Step 4: check if the result(num multiplied by the flag) is in the integer range and return the upper/lower interger value accoringly
        # Step 5: If the value is in the integer range, return

        # MAX and MIN
        MAX = 2**31 - 1
        MIN = -(2**31)

        # edge case
        if s == "":
            return 0

        s = s.strip()
        flag = 1

        if s and s[0] == '-':
            flag = -1
            s = s[1:]
        elif s and s[0] == '+':
            flag = 1
            s = s[1:]

        # STEP3
        num = 0
        for c in s:
            if c.isdigit():
                num = (num*10) + int(c)
            else:
                break

        res = (num*flag)
        if res > MAX:
            return MAX
        elif res < MIN:
            return MIN
        return res


"""
    Time complexity: O(n)
    Space complexity: O(1)
"""
S = Solution()
s = "42"
print(S.myAtoi(s))
