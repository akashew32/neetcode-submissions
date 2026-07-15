class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Define a hashmap that I will use to store 
        ## freq array as key and list of elements as value
        hashMap = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            if tuple(count) in hashMap:
                hashMap[tuple(count)].append(string)
            else:
                hashMap[tuple(count)] = [string]
        return list(hashMap.values())


