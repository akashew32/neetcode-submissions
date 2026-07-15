# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        dummy = lists[0]
        for i in range(1, len(lists)):
            ## Merge the curr and previous
            curr1 = lists[i-1]
            curr2 = lists[i]
            dummy = ListNode()
            curr = dummy
            while curr1 or curr2:
                if curr1 and curr2:
                    if curr1.val < curr2.val:
                        curr.next = curr1
                        curr1 = curr1.next
                    else:
                        curr.next = curr2
                        curr2 = curr2.next
                    curr = curr.next
                elif curr1:
                    curr.next = curr1
                    curr1 = curr1.next
                    curr = curr.next
                elif curr2:
                    curr.next = curr2
                    curr2 = curr2.next
                    curr = curr.next
            lists[i] = dummy.next



        return lists[-1]