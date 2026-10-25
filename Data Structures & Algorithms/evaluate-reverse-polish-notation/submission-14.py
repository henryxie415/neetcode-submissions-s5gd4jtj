class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        container = []

        for token in tokens:
            if token == '+':
                var1 = container.pop()
                var2 = container.pop()
                new = var1 + var2
                container.append(new)
            elif token == '-':
                var1 = container.pop()
                var2 = container.pop()
                new = var2 - var1
                container.append(new)
            elif token == '*':
                var1 = container.pop()
                var2 = container.pop()
                new = var1 * var2
                container.append(new)
            elif token == '/':
                var1 = container.pop()
                var2 = container.pop()
                new = int(float(var2)/var1)
                container.append(new)
            else:
                container.append(int(token))
        return container[-1]