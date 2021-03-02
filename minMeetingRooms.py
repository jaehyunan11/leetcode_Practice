class Solution:
    def minMeetingRooms(self, intervals):
        # If no meeting time intervals, then return 0
        if not intervals:
            return 0
        # process each metting in increasing start times for intervals
        intervals.sort(key=lambda x: x[0])
        # room heap to keep track O(nlogN) runtime where n is
        room = [intervals[0][1]]
        used = 0
        start_time = sorted([i[0] for i in intervals])
        end_time = sorted([i[i] for i in intervals])


s = Solution()
intervals = [[0, 30], [5, 10], [15, 20]]
