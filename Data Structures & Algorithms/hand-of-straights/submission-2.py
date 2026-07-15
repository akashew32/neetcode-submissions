class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        map = {}

        for num in hand:
            if num not in map:
                map[num] = 0
            map[num] += 1
        
        while map:
            start = min(map)
            for i in range(groupSize):
                if start + i not in map:
                    return False
                map[start + i] -= 1
                if map[start + i] <= 0:
                    map.pop(start + i)
        return True
        