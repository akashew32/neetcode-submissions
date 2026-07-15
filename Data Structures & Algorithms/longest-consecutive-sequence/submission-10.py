class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Base case empty list returns 0
        if nums == []:
            return 0
        
        ## Create a hashset
        numSet = set(nums)
        
        ## Create a list of potential starts
        ## Number cannot be in middle of sequence to be start
        potentialStarts = []
        for num in nums:
            if (num - 1) not in numSet:
                potentialStarts.append(num)

        ## Create a counter to count the length of the sequence
        ## Set current longest as 1
        counter = 1
        curr = 1
        for start in potentialStarts:
            val = start

            ## Start counting conseq sequence starting with start
            while val + 1 in numSet:
                counter += 1
                val += 1

            ## Replace current longest if prev sequence longer
            if counter > curr:
                curr = counter
                
            ## Reset counter for next start sequence
            counter = 1

        return curr
            
        