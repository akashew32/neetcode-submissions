class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        adj = {}
        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]] = []
            if edge[1] not in adj:
                adj[edge[1]] = []
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node in adj:
                for n in adj[node]:
                    dfs(n)

        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i)
                count += 1
        
        return count
        
        