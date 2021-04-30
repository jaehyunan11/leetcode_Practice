class Solution:
    def arrangeWords(self, text):
        # Get all the words
        words = text.split()
        # Make lowercase for first word
        words[0] = words[0].lower()
        # sorted by length
        words.sort(key=len)
        # First word and its first char to make upper
        words[0] = words[0][0].upper() + words[0][1:]
        return " ".join(words)

# TIME : O(nlogn) since we sorted the words that take nLogn time
# Space : O(n) the array is same space as text.


S = Solution()
text = "Leetcode is cool"
print(S.arrangeWords(text))
