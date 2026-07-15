# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and self.compareHeight(root)
        
    def findHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))
    
    def compareHeight(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.findHeight(root.left) - self.findHeight(root.right)) > 1:
            return False
        return True

