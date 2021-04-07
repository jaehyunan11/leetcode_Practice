class Solution:
    def average(self, salary):
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

# TIME and Space : O(1)
