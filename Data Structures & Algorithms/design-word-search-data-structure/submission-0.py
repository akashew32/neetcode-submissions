class WordDictionary:

    def __init__(self):
        self.children = {}
        self.EndOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = WordDictionary()
                curr = curr.children[char]
        curr.EndOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                if i == len(word) - 1:
                    for c in curr.children:
                        if curr.children[c].EndOfWord:
                            return True
                    return False
                for c in curr.children:
                    if curr.children[c].search(word[i+1:]):
                        return True
                return False
                
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return curr.EndOfWord
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False