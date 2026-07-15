class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        length = len(nums)
        returnList = []
        if len(nums) == 1:
            return nums
        count = 0
        nums.sort()
        for i in range(length):
            count += 1
            if i + 1 == length:
                if count in hashMap:
                    hashMap[count] += [nums[i]]
                else: 
                    hashMap[count] = [nums[i]]
            else: 
                if nums[i] != nums[i+1]:
                    if count in hashMap:
                        hashMap[count] += [nums[i]]
                    else: 
                        hashMap[count] = [nums[i]]
                    count = 0

        for i in range(length, -1, -1):
            if i in hashMap:
                returnList += hashMap[i]
        print (hashMap)
        return returnList[0:k]
                
