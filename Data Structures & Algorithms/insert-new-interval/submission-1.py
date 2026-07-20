class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = newInterval
        for start, end in intervals:
            if start > newInterval[1]:
                if curr:
                    res.append(curr.copy())
                    curr = []
                res.append([start, end])
            elif end < newInterval[0]:
                res.append([start, end])
            elif curr:
                curr[0] = min(curr[0], start)
                curr[1] = max(curr[1], end)
        if curr:
            res.append(curr.copy())
        return res