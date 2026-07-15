# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr = head
        if length - n == 0:
            return head.next
        
        for i in range(length - 1 - n):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return head