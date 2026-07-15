# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        if not head.next:
            return
        slow = head
        fast = head.next

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        ## Slow is now mid point
        prev = slow.next
        slow.next = None
        curr = head

        ## Reverse second half
        second = None
        while prev:
            nextNode = prev.next
            prev.next = second
            second = prev
            prev = nextNode
    

        while curr and second:
            temp1 = curr.next 
            temp2 = second.next
            curr.next = second
            curr.next.next = temp1
            second = temp2
            curr = curr.next.next
        
        return

