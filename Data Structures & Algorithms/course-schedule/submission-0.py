class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        inDegree = [0] * numCourses
        for edge in prerequisites:
            inDegree[edge[1]] += 1
            if edge[0] not in adj:
                adj[edge[0]] = []
            adj[edge[0]].append(edge[1])
        
        q = deque()
        sorting = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            sorting.append(curr)
            if curr in adj:
                for out in adj[curr]:
                    inDegree[out] -= 1
                    if inDegree[out] == 0:
                        q.append(out)
        
        if len(sorting) != numCourses:
            return False
        return True