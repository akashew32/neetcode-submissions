class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        ## Create a hashset
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        ## Create a list of potential starts
        ## Number cannot be in middle of sequence to be start
        potentialStarts = []
        for num in nums:
            if (num - 1) not in numSet:
                potentialStarts.append(num)

        ## Create a counter to count the length of the sequence
        ## Set 
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
            
        