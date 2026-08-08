class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        tickets.reverse()
        adj = {}
        for ticket in tickets:
            if ticket[0] not in adj:
                adj[ticket[0]] = []
            if ticket[1] not in adj:
                adj[ticket[1]] = []
            adj[ticket[0]].append(ticket[1])
        
        path = []
        
        def dfs(start) -> bool:
            while adj[start]:
                child = adj[start].pop()
                dfs(child)
            path.append(start)

        dfs("JFK")
        path.reverse()
        return path
            
            

        