class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False        
        map = {}
        heap = []

        for num in hand:
            if num not in map:
                map[num] = 0
                heapq.heappush(heap, num)
            map[num] += 1
        
        while map:
            while heap[0] not in map:
                heapq.heappop(heap)
            start = heap[0]
            for i in range(groupSize):
                if start + i not in map:
                    return False
                map[start + i] -= 1
                if map[start + i] <= 0:
                    map.pop(start + i)
        return True
        