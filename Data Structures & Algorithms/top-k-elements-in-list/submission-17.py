class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
        heap = []
        for key in map:
            heapq.heappush(heap, (map[key] * -1, key))
        res = []
        for i in range(k):
            if heap:
                res.append(heapq.heappop(heap)[1])
        return res
