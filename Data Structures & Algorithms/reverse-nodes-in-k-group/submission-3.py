# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        curr1 = dummy
        while curr:
            start = curr
            for i in range(k):
                if not curr:
                    curr1.next = start
                    return dummy.next
                prev = curr
                curr = curr.next
            prev.next = None
            ## Reverse from start to prev

            prev = None
            while start:
                next_node = start.next
                start.next = prev
                prev = start
                start = next_node
            curr1.next = prev
            while curr1.next:
                curr1 = curr1.next
        
        return dummy.next
            