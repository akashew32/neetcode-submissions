class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0].copy()
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr.copy())
                curr = intervals[i].copy()
            else:
                curr[1] = max(curr[1], intervals[i][1])
        res.append(curr.copy())
        return res