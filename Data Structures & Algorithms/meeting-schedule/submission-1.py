"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []
        for interval in intervals:
            heapq.heappush(heap, (interval.start, interval.end))
        
        b = - (2 ** 31)
        while heap:
            curr = heapq.heappop(heap)
            if curr[0] < b:
                return False
            b = curr[1]
        return True