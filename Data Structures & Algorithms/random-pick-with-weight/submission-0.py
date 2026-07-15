class Solution:

    def __init__(self, w: List[int]):
        self.lst = []
        for i in range(len(w)):
            for j in range(w[i]):
                self.lst.append(i)
        self.length = len(self.lst)
        

    def pickIndex(self) -> int:
        return self.lst[random.randint(0, self.length - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()