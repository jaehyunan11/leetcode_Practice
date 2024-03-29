class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        max_dur = releaseTimes[0]
        longestKey = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            # Find Diff Duration
            dur = releaseTimes[i] - releaseTimes[i-1]
            # Check current max duration vs duration.
            if dur > max_dur:
                max_dur = dur
                longestKey = keysPressed[i]
            # If current max duration and duration equals then find max of longestKey.
            elif dur == max_dur:
                longestKey = max(keysPressed[i], longestKey)
        return longestKey


S = Solution()
releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
print(S.slowestKey(releaseTimes, keysPressed))

# Time Complexity : O(N)
# Space Complexity : O(N)
