class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qmap = {}
        for q in queries:
            qmap[q] = -1
        heap = []
        nums = sorted(queries)
        intervals.sort()
        i = 0
        for q in nums:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                qmap[q] = heap[0][0]
        res = []
        for q in queries:
            res.append(qmap[q])
        return res



