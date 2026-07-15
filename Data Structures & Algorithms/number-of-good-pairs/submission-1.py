class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        pairs = 0
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                pairs += count[num]
                count[num] += 1
        return pairs