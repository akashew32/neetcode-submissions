# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -1000
        ## Calculate the maximum path sum at every node and update global max accordingly
        def traverse(tree) -> int:
            nonlocal maxSum
            if not tree:
                return 0
            leftVal = traverse(tree.left)
            rightVal = traverse(tree.right)
            currPath = tree.val
            if rightVal > 0:
                currPath += rightVal
            if leftVal > 0:
                currPath += leftVal
            maxSum = max(maxSum, currPath)

            return max(tree.val, tree.val + rightVal, tree.val + leftVal)
        
        traverse(root)
        return maxSum




    
    def copyTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tree = TreeNode(root.val)
        tree.left = self.copyTree(root.left)
        tree.right = self.copyTree(root.right)
        return tree
    
   



