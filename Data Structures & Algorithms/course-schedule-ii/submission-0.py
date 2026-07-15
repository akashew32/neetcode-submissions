class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        inDegree = [0] * numCourses
        for edge in prerequisites:
            inDegree[edge[0]] += 1
            if edge[1] not in adj:
                adj[edge[1]] = []
            adj[edge[1]].append(edge[0])
        
        q = deque()
        topo = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            topo.append(curr)
            if curr in adj:
                for node in adj[curr]:
                    inDegree[node] -= 1
                    if inDegree[node] == 0:
                        q.append(node)
        if len(topo) == numCourses:
            return topo
        return []