# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        array = self.getArray(root)

        return array[k-1]

        
    def getArray(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        return self.getArray(root.left) + [root.val] + self.getArray(root.right)

        
