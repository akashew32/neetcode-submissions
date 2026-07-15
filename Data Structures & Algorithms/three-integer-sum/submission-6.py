class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## This algorithm is not possible O(n) so we 
        nums.sort()
        returnList = []
        usedStart = set()

        

        for i in range(len(nums)-2):
            if nums[i] not in usedStart:
                usedStart.add(nums[i])
                pointer1 = i + 1
                pointer2 = len(nums) - 1
                while pointer1 < pointer2:
                    val = nums[i] + nums[pointer1] + nums[pointer2]
                    if val == 0:
                        returnList.append([nums[i], nums[pointer1], nums[pointer2]])
                        while pointer1 + 1< len(nums) and nums[pointer1 + 1] == nums[pointer1] and pointer1 != pointer2:
                            pointer1 += 1
                        pointer1 += 1
                    elif val < 0:
                        pointer1 += 1
                    else: 
                        pointer2 -= 1
        return returnList 


        

        