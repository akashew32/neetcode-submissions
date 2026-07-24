class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if not carry:
                break
            nextCarry = (carry + digits[i]) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = nextCarry
        return [carry] + digits if carry else digits