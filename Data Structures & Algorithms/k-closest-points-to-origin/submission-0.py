class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        
        for point in points:
            dist = -(point[0] ** 2 + point[1] ** 2)
            temp = (dist, point)
            heapq.heappush(out, temp)
            if len(out) > k:
                heapq.heappop(out)
        
        res = []
        for p in out:
            res.append(p[1])
        return res

        
        