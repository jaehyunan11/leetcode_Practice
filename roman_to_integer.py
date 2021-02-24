class Solution:
    def romanToInt(self, s: str) -> int:

        res = 0
        max_add = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # 0) Edge Case (if str is either empty or length of str is 0)
        if s == "" or len(s) == 0:
            return 0
        # 1) Check from right to left to check char in S
        for c in s[::-1]:
            if d[c] < max_add:
                res -= d[c]
            else:
                res += d[c]
                max_add = d[c]
        return res


res = Solution()
s = "MCMXCIV"
print(res.romanToInt(s))
