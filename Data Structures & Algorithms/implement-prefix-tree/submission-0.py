class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = PrefixTree()
                curr = curr.children[char]
        curr.isEndOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]    
        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]  
        
        return True
        
        