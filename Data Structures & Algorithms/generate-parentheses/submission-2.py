class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = 0
        right = 0
        res = []
        path = []

        def backtrack(l, r, path):
            if l > n:
                return
            if l == n:
                for i in range(n-r):
                    path.append(")")
                res.append(path.copy())
                for i in range(n-r):
                    path.pop()
                
                return
            if r < l:
                path.append("(")
                backtrack(l + 1, r, path)
                path.pop()
                path.append(")")
                backtrack(l, r+1, path)
                path.pop()
            if r == l:
                path.append("(")
                backtrack(l + 1, r, path)
                path.pop()
            
        
        backtrack(left, right, path)
        ret = []
        for p in res:
            ret.append("".join(p))
        return ret


            
            