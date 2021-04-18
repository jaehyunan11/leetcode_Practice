class Solution:
    def romanToInt(self, s):
        # total, i = 0, 0
        # Loop the s.length
        # If i+1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
        # Subtract large to small
        # total += roman_dict[s[i+1]] - roman_dict[s[i]]
        # i += 2 (check forward 2 places)
        # else:
        # add the curr string to total
        # return total

        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000, }

        # total and i pointer
        total, i = 0, 0

        while i < len(s):
            # i+1 -> check two roman_num
            if i+1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                # subtract from large to small and add to total
                total += roman_dict[s[i+1]] - roman_dict[s[i]]
                i += 2
            else:
                total += roman_dict[s[i]]
                i += 1
        return total

# TIME : O(1) As there is a finite set of roman numerals,
# the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX.
# SPACE : O(1) Because only a constant number of single-value variables are used,
# the space complexity is O(1).


S = Solution()
s = "III"
print(S.romanToInt(s))
