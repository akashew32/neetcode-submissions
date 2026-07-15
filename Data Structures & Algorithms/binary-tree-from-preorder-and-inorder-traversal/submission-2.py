# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        
        if len(preorder) == 2:
            if inorder[0] != preorder[0]:
                return TreeNode(preorder[0], TreeNode(preorder[1]), None)
            else:
                return TreeNode(preorder[0], None, TreeNode(preorder[1]))
        
        rootval = preorder[0]
        tree = TreeNode(preorder[0])

        leftpre = []
        rightpre = []
        leftin = []
        rightin = []

        switch = False
        for i in range(len(inorder)):
            if inorder[i] == rootval:
                switch = True
            elif not switch:
                leftin.append(inorder[i])
            else:
                rightin.append(inorder[i])
        
        ptr = 1
        for i in range(len(leftin)):
            leftpre.append(preorder[ptr])
            ptr += 1
        
        for i in range(len(rightin)):
            rightpre.append(preorder[ptr])
            ptr += 1
        
        tree.left = self.buildTree(leftpre, leftin)
        tree.right = self.buildTree(rightpre, rightin)
        return tree





        
        
        
