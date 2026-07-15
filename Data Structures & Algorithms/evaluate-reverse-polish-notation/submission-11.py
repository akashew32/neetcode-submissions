class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ## Create a set to identify if token 
        ## is an operation in constant time
        operations = set(["/", "+", "*", "-"])
        
        ## Empty stack to store values
        stack = []

        for token in tokens:
            ## Add numbers to the stack as we iterate
            ## if not an operation
            if token not in operations:
                stack.append(int(token))

            ## If an operation
            else:
                ## Collect the right most values as operands
                num1 = stack.pop()
                num2 = stack.pop()
                combined = 0

                ## Check for all four operations
                if token == "/":
                    combined = num2 // num1

                    ## If negative automatically truncates up but we 
                    ## want to truncate towards 0
                    if num2 % num1 != 0 and combined < 0:
                        combined += 1
                elif token == "+":
                    combined = num2 + num1
                elif token == "*":
                    combined = num2 * num1
                else:
                    combined = num2 - num1
                stack.append(combined)
        
        return stack[0]
                