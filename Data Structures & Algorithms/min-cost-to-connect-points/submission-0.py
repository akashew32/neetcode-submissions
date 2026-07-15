class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        weights = {}
        mst = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (dist, (i, j)))
                weights[(i, j)] = dist
        dsu = UnionFind(len(points))
        while edges and len(mst) < len(points):
            dist, (i, j) = heapq.heappop(edges)
            if dsu.connected(i, j):
                continue
            mst.append((i, j))
            dsu.union(i, j)
        res = 0
        for edge in mst:
            res += weights[edge]
        return res 


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        # Path compression: point node directly to its root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in the same set
        
        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
            
        