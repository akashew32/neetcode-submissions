class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(j):
            if memo[j] != -1:
                return memo[j]
            LIS = 1
            for i in range(j + 1, len(nums)):
                if nums[i] > nums[j]:
                    LIS = max(LIS, 1 + dfs(i))
            memo[j] = LIS
            return LIS
        for j in range(len(nums)):
            dfs(j)
        return max(memo)