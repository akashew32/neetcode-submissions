# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## Dfs with a stack
        if not root and not subRoot:
            return True
        if not subRoot or not root:
            return False
        target = subRoot.val

        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if self.isSameTree(curr, subRoot):
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return False
        



    def isSameTree(self, root1: optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root2 and not root1:
            print("pinky pie")
            return True
        elif root1 and root2:
            return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        else:
            return False