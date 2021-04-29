class Solution:
    def isValid(self, s):
        # stack, pchar = [], {"(": ")", "{": "}", "[": "]"}

        # for parentheses in s:
        #     if parentheses in pchar:
        #         stack.append(parentheses)
        #     elif len(stack) == 0 or pchar[stack.pop()] != parentheses:
        #         return False
        # return len(stack) == 0

        # Iterate through the input string, and for each char, append it to the stack if:

        # stack is empty, or
        # if the last item in stack is not a matching half of the current char, e.g. char == '(', but stack[-1] == '{'
        # Note: ' ) ' and ' ( ' are not considered matching if ' ) ' comes first in the iteration.

        stack = []
        for parentheses in s:
            if len(stack) == 0:
                stack.append(parentheses)
            elif stack[-1] == '{' and parentheses == '}':
                stack.pop()
            elif stack[-1] == '[' and parentheses == ']':
                stack.pop()
            elif stack[-1] == '(' and parentheses == ')':
                stack.pop()
            else:
                stack.append(parentheses)
        return False if stack else True


S = Solution()
s = "()"
print(S.isValid(s))
