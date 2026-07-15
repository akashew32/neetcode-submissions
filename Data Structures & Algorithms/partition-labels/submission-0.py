class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        for i in range(len(s)):
            char = s[i]
            if char not in end:
                end[char] = 0
            end[char] = i
        res = []
        count = 1
        curr = 0
        for i in range(len(s)):
            num = s[i]
            curr = max(curr, end[num])
            if i == curr:
                res.append(count)
                count = 0
            count += 1
        return res
            

            