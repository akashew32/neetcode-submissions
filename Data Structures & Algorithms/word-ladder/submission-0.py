class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        adj = self.buildLadder(wordList)
        count = 0
        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)

        while q:
            count += 1
            for i in range(len(q)):
                curr = q.popleft()
                for word in adj[curr]:
                    if word not in visited:
                        q.append(word)
                        visited.add(word)
                if curr == endWord:
                    return count
            
        return 0

    
    def buildLadder(self, wordList: List[str]) -> Dict[str, List[str]]:
        adj = {word: [] for word in wordList}
        words = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                temp = list(word)
                for j in range(26):
                    temp[i] = chr(97 + j)
                    curr = "".join(temp)
                    if curr in words and curr != word:
                        adj[word].append(curr)
        return adj

