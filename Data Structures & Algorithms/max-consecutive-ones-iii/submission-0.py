class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = 0
        longest = 0
        map = {}
        map[0] = 0
        map[1] = 0
        l = 0 
        for r in range(len(nums)):
            map[nums[r]] += 1
            while map[0] > k:
                map[nums[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest