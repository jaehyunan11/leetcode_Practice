# Two Pointer, Greedy
class Solution:
    def partionLabels(self, S):
        """
              0 1 2 3 4 5 6 7 8 
              a b a b c b a c a 
        i     i i i i i i i i i
        start s               
        end             e   e e
        output                8
        """
        # iterlate last index and charcater.
        # 'a':8, 'b':5, 'c': 7
        last = {c: i for i, c in enumerate(S)}

        print(last)
        start = end = 0
        output = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            print(f"end:{end}")
            if i == end:
                output.append(end-start+1)
                start = i+1
        return output

# TIME COMPLEXITY : O(N) Length of S
# SPACE COMPLEXITY : O(1) Keep data structure last of not more than 26 characters


s = Solution()
S = "ababcbacadefegdehijhklij"
print(s.partionLabels(S))
