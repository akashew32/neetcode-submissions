# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        height = self.getHeight(root)
        vals = []
        q = deque()
        q.append(root)
        for i in range(height):
            for j in range(len(q)):
                curr = q.popleft()
                if curr:
                    vals.append(str(curr.val))
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    vals.append("NULL")
        result = ",".join(vals)
        print(result)
        return result 
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i < len(vals):
            curr = q.popleft()
            if i < len(vals) and vals[i] != "NULL":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if i < len(vals) and vals[i] != "NULL":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i += 1
            


        return root

    def getHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
