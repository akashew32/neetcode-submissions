"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        map = {}
        endmap = {}
        vals = set()
        for interval in intervals:
            start, end = interval.start, interval.end
            if start not in map:
                map[start] = 0
                endmap[start] = 0
                vals.add(start)
            if end not in map:
                map[end] = 0
                endmap[end] = 0
                vals.add(end)
            map[start] += 1
            endmap[end] += 1

        count = 0
        curr = 0
        for time in sorted(list(vals)):
            curr += map[time]
            curr -= endmap[time]
            count = max(count, curr)
        return count
        