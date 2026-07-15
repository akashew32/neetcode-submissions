# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        total = 0
        exp = 0
        while curr1 or curr2:
            if curr1:
                total += curr1.val * (10 ** exp)
                curr1 = curr1.next
            if curr2: 
                total += curr2.val * (10 ** exp)
                curr2 = curr2.next 
            exp += 1
        stringTotal = str(total)
        stringTotal = ("".join(reversed(stringTotal)))
        print(stringTotal)
        returnList = ListNode()
        curr = returnList
        for s in stringTotal:
            curr.next = ListNode(s)
            curr = curr.next
        return returnList.next


        