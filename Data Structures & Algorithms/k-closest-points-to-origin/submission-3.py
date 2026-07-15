class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heap = []
        for x, y in points:
            d = (x * x) + (y * y)
            heapq.heappush(heap, (d, [x, y]))
        for i in range(k):
            d, p = heapq.heappop(heap)
            dist.append(p)
        return dist