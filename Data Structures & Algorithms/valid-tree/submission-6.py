class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## Check if connected and acyclic
        if len(edges) != n-1:
            return False
        ## Convert into adjacency map
        map = {}
        for edge in edges:
            if edge[0] not in map:
                map[edge[0]] = set()
            if edge[1] not in map:
                map[edge[1]] = set()
            map[edge[0]].add(edge[1])
            map[edge[1]].add(edge[0])
        
        visited = set()
        flag = True
        ## Perform DFS to check cycle

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            if node in map:
                for child in map[node]:
                    if parent == child:
                        continue
                    if not dfs(child, node):
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n
                




