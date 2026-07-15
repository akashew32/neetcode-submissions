class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSum = [1]
        rightSum = [1]
        output = []
        total = 1
        for i in range(1, len(nums)):
            total *= nums[i-1]
            leftSum.append(total)
        total = 1
        numsReversed = nums
        numsReversed.reverse()
        print(numsReversed)
        for i in range(0, len(nums) - 1):
            total *=  numsReversed[i]
            rightSum.append(total)
        rightSum.reverse()
        
        for i in range(len(nums)):
            output.append(rightSum[i] * leftSum[i])
        return output