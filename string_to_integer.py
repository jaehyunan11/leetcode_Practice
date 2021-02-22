import re


class Solution:
    def myAtoi(self, string):
        # 1) Remove all the whitespace in the given string
        string = string.strip()
        # 2) Find digits including +, - in the given string and remove the characters
        string = re.findall('^[+\-]*\d+', string)
        # 3) Set Max/Min int
        MAX = 2**31 - 1
        MIN = -(2**31)
        # 4)
        try:
            res = int("".join(string))
            if res > MAX:
                res = MAX
            elif res < MIN:
                res = MIN
            return res
            # return max(min(res, MAX), MIN)
        except:
            return 0

        # ^ (Check if a string starts with a certain character)
        # ? (matches zero or one occurrence of the pattern left to it) "OR" concept e.g. [+\-]? matches an optional "+","-", or empty string
        # [] (specifies a set of characters you wish to match)
        # + (one or more occurrence of the pattern left to it)
        # \d (digit) [0-9]


s = Solution2()
string = "   -32 string"
print(s.myAtoi(string))
