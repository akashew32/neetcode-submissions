class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        a, b = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < b:
                count += 1
                b = min(b, end)
            else:
                b = end
        return count

