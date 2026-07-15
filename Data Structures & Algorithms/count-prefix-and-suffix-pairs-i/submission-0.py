class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        
        def isPrefixAndSuffix(s1, s2) -> bool:
            return s2.startswith(s1) and s2.endswith(s1)


        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count