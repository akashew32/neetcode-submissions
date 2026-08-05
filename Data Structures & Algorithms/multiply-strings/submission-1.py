class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = list(reversed(list(num1)))
        l2 = list(reversed(list(num2)))

        sum = 0
        for i in range(len(l1)):
            ## Index i represents ith number * 10 ^ i
            curr = 0
            for j in range(len(l2)):
                curr += ((ord(l2[j]) - 48) * 10 ** j) * (ord(l1[i]) - 48)
            curr = curr * 10 ** i
            sum += curr
        if not sum:
            return str(sum)
        ret = []
        while sum != 0:
            ret.append(chr(sum % 10 + 48))
            sum = sum // 10
        return "".join(list(reversed(ret)))

