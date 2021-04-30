class Solution:
    def letterCominbations(self, digits):
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = []
        stack = [("", digits)]
        while stack:
            string, digit = stack.pop()
            if not digit:
                result.append(string)
                continue
            for i in phone[digit[0]]:
                stack.append((string+i, digit[1:]))
        return result


S = Solution()
digits = "23"
print(S.letterCominbations(digits))
