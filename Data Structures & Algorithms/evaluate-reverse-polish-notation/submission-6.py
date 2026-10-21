class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #after an operation sign add the parenesis 
        container = []
        for token in tokens:

            if token == '*':
                val2 = container.pop()
                val1 = container.pop()
                new = val1 * val2
                container.append(new)
            elif token == '+':
                val2 = container.pop()
                val1 = container.pop()
                new = val1 + val2
                container.append(new)
            elif token == '-':
                val2 = container.pop()
                val1 = container.pop()
                new = val1 - val2
                container.append(new)
            elif token == '/':
                val2 = container.pop()
                val1 = container.pop()
                new = (int(float(val1) / val2))
                container.append(new)
            else:
                container.append(int(token))
        return container[0]