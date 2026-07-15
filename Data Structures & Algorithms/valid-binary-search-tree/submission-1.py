# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkInRange(root, -1001, 1001)
        

    def checkInRange(self, root: Optional[TreeNode], low, high) -> bool:
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self.checkInRange(root.left, low, root.val) and self.checkInRange(root.right, root.val, high)
