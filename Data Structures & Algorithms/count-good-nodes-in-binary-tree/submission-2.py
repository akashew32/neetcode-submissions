# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.checkNode(root, root.val)

    
    def checkNode(self, root: TreeNode, x: int) -> int:
        if not root:
            return 0
        if root.val < x:
            return self.checkNode(root.left, max(root.val, x)) + self.checkNode(root.right, max(root.val, x))
        else:
            return 1 + self.checkNode(root.left, max(root.val, x)) + self.checkNode(root.right, max(root.val, x))

            