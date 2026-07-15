# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = []
        output = []
        stack.append(root)
        while stack:
            temp = self.traverseLevel(stack)
            output.append(temp[0])
            stack = temp[1]
        return output


        
    def traverseLevel(self, stack: [Optional[TreeNode]]) -> List[[List[int]], List[Optional[TreeNode]]]:
        output = []
        traversal = []
        for root in stack:
            if root.left:
                output.append(root.left)
            if root.right:
                output.append(root.right)
            
            print("i'm gay")
        
            traversal.append(root.val)
        return [traversal, output]
