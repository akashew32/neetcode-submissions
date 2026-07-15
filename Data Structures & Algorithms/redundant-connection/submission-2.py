class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle = set()
        adj = {}
        visited = [False] * (len(edges) + 1)        
        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]] = []
            if edge[1] not in adj:
                adj[edge[1]] = []
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        start = -1
        def dfs(parent, node):
            nonlocal start
            if visited[node]:
                start = node
                return True
            visited[node] = True
            for child in adj[node]:
                if child == parent:
                    continue
                if dfs(node, child):
                    if start != -1:
                        cycle.add(node)
                    if node == start:
                        start = -1
                    return True
            return False
        dfs(-1, 1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]