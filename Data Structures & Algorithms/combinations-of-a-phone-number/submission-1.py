class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        path = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))
                return

            temp = digitToChar[digits[i]]
            for char in temp:
                path.append(char)
                backtrack(i+1)
                path.pop()
        if not digits:
            return []
        backtrack(0)
        return res
            
