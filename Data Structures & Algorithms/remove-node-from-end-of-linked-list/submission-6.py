# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pRight = dummy.next
        pLeft = dummy
        for i in range(n):
            pRight = pRight.next
        
        while pRight:
            pRight = pRight.next
            pLeft = pLeft.next
        
        pLeft.next = pLeft.next.next
        return dummy.next