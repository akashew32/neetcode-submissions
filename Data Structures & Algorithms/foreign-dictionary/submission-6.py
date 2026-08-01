class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}
        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i-1]))):
                if words[i-1][j] not in adj:
                    adj[words[i-1][j]] = Node(words[i-1][j])
                    indegree[words[i-1][j]] = 0
                if words[i][j] not in adj:
                    adj[words[i][j]] = Node(words[i][j])
                    indegree[words[i][j]] = 0

                if words[i-1][j] == words[i][j]:
                    print(words[i][j])
                    if j == min(len(words[i])-1, len(words[i-1])-1) and len(words[i-1]) > len(words[i]):   
                        return ""

                    continue
                else:
                    adj[words[i-1][j]].children.append(words[i][j])
                    indegree[words[i][j]] += 1
                    break
            

        visited = set()
        order = []
        q = deque()
        print(indegree)
        
        for char in adj:
            if indegree[char] == 0:
                q.append(char)
        
        while q:
            print(q)
            curr = q.popleft()
            order.append(curr)
            visited.add(curr)
            for child in adj[curr].children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        if len(order) != len(adj):
            return ""
        for word in words:
            for char in word:
                if char not in visited:
                    visited.add(char)
                    order.append(char)
        return "".join(order)

    
class Node:
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.color = -1
