class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty list"
        encoded = ""
        for i in range(len(strs)):
            string = strs[i]
            for j in range(len(string)):
                char = string[j]
                encoded += str(ord(char))
                if j != len(string) - 1:
                    encoded += " "
            if i != len(strs) - 1:
                encoded += ","
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "empty list":
            return []
        lst = s.split(",")
        for i in range(len(lst)):
            lst[i] = lst[i].split(" ")
        
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if " " in lst[i][j]:
                    lst[i][j] = lst[i][j].strip()
                if lst[i][j] != "":
                    lst[i][j] = chr(int(lst[i][j]))
            lst[i] = "".join(lst[i])
        return lst
