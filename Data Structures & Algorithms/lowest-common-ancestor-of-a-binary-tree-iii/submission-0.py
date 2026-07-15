"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        vals = set()
        vals.add(p.val)
        vals.add(q.val)
        curr1 = p
        curr2 = q
        while curr1.parent or curr2.parent:
            if curr1.parent:
                if curr1.parent.val in vals:
                    return curr1.parent
                vals.add(curr1.parent.val)
                curr1 = curr1.parent
            if curr2.parent:
                if curr2.parent.val in vals:
                    return curr2.parent
                vals.add(curr2.parent.val)
                curr2 = curr2.parent