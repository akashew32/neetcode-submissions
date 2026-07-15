"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashMap = {}
        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        dummy = Node(0)
        curr1 = dummy
        while curr:
            if curr.next:
                hashMap[curr].next = hashMap[curr.next]
            if curr.random:
                hashMap[curr].random = hashMap[curr.random]
            curr1.next = hashMap[curr]
            curr1 = curr1.next
            curr = curr.next
        return dummy.next
