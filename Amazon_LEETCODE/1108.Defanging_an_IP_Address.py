class Solution:
    def defangIpaddr(self, address):

        # return address.replace('.', "[.]")
        # O(N) TIME, O(1) SPACE

        # return "[.]".join(address.split('.'))
        # O(N) TIME, O(1) SPACE

        output = []
        for ch in address:
            if ch.isdigit():
                output.append(ch)
            else:
                output.append("[.]")
        return ''.join(output)
        # O(N) TIME, O(N) SPACE


S = Solution()
address = "1.1.1.1"
print(S.defangIpaddr(address))
