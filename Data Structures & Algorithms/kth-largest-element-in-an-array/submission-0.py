class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums) - k
        return select(nums, n)
        



        ## Median of Medians to find nth largest
def select(arr: List[int], k: int) -> int:
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sub)[len(sub)//2] for sub in sublists]

    pivot = select(medians, len(medians) // 2)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(low):
        return select(low, k)
    elif k < len(low) + len(pivots):
        return pivots[0]
    else:
        return select(high, k - len(low) - len(pivots))

    