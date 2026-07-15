class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        ## Create a hashset
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        potentialStarts = []
        for num in nums:
            if (num - 1) not in numSet:
                potentialStarts.append(num)

        counter = 1
        curr = 1
        for start in potentialStarts:
            val = start
            while val + 1 in numSet:
                counter += 1
                val += 1
            if counter > curr:
                curr = counter
            counter = 1

        return curr
            
        