class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(val) -> int:
            curr = 0
            for char in list(str(val)):
                curr += int(char) ** 2
            return curr
        
        curr1 = n
        curr2 = getNext(n)
        while curr1 != curr2:
            curr1 = getNext(curr1)
            curr2 = getNext(getNext(curr2))
        print(curr1)
        return curr1 == 1