"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        graphMap = {}
        visited = set()
        def dfs(node):
            visited.add(node)
            graphMap[node] = Node(node.val)
            for n in node.neighbors:
                if n not in visited:
                    dfs(n)
        dfs(node)

        visited = set()
        def dfs2(node):
            if node in visited:
                return
            visited.add(node)
            for n in node.neighbors:
                graphMap[node].neighbors.append(graphMap[n])
                dfs2(n)

        dfs2(node)
        return graphMap[node]
