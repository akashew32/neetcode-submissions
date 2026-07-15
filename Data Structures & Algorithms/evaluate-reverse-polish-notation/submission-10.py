class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["/", "+", "*", "-"])
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                print([token, num1, num2])
                combined = 0
                if token == "/":
                    combined = num2 // num1
                    if num2 % num1 != 0 and combined < 0:
                        combined += 1
                elif token == "+":
                    combined = num2 + num1
                elif token == "*":
                    combined = num2 * num1
                else:
                    combined = num2 - num1
                stack.append(combined)
        print(stack)
        return stack[0]
                