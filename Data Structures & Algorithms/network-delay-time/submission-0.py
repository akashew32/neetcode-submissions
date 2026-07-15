class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [10000000] * n
        dist[k-1] = 0
        q = []
        heapq.heappush(q, (0, k - 1))
        adj = {}
        for i in range(len(times)):
            edge = (times[i][0] - 1, times[i][1] - 1, times[i][2])
            if edge[0] not in adj:
                adj[edge[0]] = []
            adj[edge[0]].append((edge[1], edge[2]))
        
        while q:
            d, node = heapq.heappop(q)
            if d > dist[node]:
                continue
            if node in adj:
                for v, w in adj[node]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(q, (dist[v], v))
        return max(dist) if max(dist) < 1000000 else -1
            
