class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #after an operation sign add the parenesis 
        
        stack = []
        for token in tokens:
            #use pops and push 
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return int(stack[0])