class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            
            newStone = -1 * abs(stone1 - stone2)
            heapq.heappush(stones, newStone)

        
        if not stones:
            return 0
        else:
            return -stones[0]