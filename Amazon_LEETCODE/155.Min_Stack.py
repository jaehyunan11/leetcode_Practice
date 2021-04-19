class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        # stack : 12 6 10 6 8
        # min_stack : 12 6 6

    def push(self, x):
        self.stack.append(x)
        # not self.min_stack value x <=self.min_stack[-1]:
        # then add x to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # if right most minstack and right most stack are equal
        # pop minstack
        # and pop stack
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        # right most stack is top
        return self.stack[-1]

    def getMin(self):
        # right most min stack is getMIN
        return self.min_stack[-1]

    # def __init__(self):
    #     self.stack = []

    # def push(self, x):
    #     # if the stack is empty, then the min value
    #     # must just be the first value we add
    #     if not self.stack:
    #         self.stack.append((x, x))
    #         return
    #     current_min = self.stack[-1][1]
    #     self.stack.append((x, min(x, current_min)))

    # def pop(self):
    #     self.stack.pop()

    # def top(self):
    #     # Looking at the top of a Stack is an O(1) operation.
    #     self.stack[-1][0]

    # def getMin(self):
    #     self.stack[-1][1]

# TIME : O(1)
# Space : O(N) Worst case is that all the operations are push. In this case, there will be O(2n) space used.
