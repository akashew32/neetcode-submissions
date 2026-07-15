

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        ret = set()
        visited = set()

        
        trie = PrefixTrie()
        for word in words:
            trie.insert(word)

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r,c) in visited:
                return

            if board[r][c] not in node.children:
                return

            visited.add((r,c))

            node = node.children[board[r][c]]
            
            if node.endOfWord:
                ret.add(node.word)

            dfs(r-1, c, node)
            dfs(r+1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            visited.remove((r,c)) 

        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root)


        return list(ret)
                    
                

        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.word = None

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.endOfWord = True
        curr.word = word

    def search(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.isEndOfWord
    
    
            

        