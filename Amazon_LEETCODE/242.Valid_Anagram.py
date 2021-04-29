class Solution:
    def isAnagram(self, s, t):
        # Counter Dictionary
        # iterate s string and update the number of each char
        # iterate t string
        # if t string in Counter dictionary
        # subtract the Counter[char]
        # else return False
        # Iterate Counter.value
        # if value is not 0 then return False
        # else Return True
        Counter = {}

        for char in s:
            if char in Counter:
                Counter[char] += 1
            else:
                Counter[char] = 1

        for char in t:
            if char in Counter:
                Counter[char] -= 1
            else:
                return False

        for val in Counter.values():
            if val != 0:
                return False
        return True

# TIME : O(N) since we iterate 3N  accessing the counter table
# O(1) Although we use extra space, the space complexity is O(1)
# because table size stay's constant (max 26 characters) no mater how large n is


S = Solution()
s = "anagram"
t = "nagaram"
print(S.isAnagram(s, t))
