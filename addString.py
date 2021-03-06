class Solution:
    def addStrings(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)
        carry, res = 0, ""
        while num1 or num2 or carry:
            if num1:
                carry += int(num1.pop())
            if num2:
                carry += int(num2.pop())
            res = + str(carry % 10)
            carry = carry // 10
        return res[::-1]
