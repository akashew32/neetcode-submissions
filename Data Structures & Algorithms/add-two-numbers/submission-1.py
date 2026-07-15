# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while curr1 or curr2:
            temp = carry
            if curr1:
                temp+=curr1.val
                curr1 = curr1.next
            if curr2:
                temp += curr2.val
                curr2 = curr2.next

            curr.next = ListNode(temp % 10)
            curr = curr.next
            carry = temp // 10
        if carry:
            curr.next = ListNode(carry)
        return dummy.next


        