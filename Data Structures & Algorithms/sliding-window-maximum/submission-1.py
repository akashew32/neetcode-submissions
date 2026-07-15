import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for i in range(len(nums)):

            # Remove smaller elements from back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Remove out-of-window indices
            if dq[0] <= i - k:
                dq.popleft()

            # Record answer once first window is complete
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res