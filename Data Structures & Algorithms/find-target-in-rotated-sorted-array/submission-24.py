class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid
        
        
        if l == 0 or nums[0] > target:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0
        
        
        ## perform binary search
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        else:
            return -1

