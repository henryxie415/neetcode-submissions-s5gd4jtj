class Solution:
    def isValid(self, s: str) -> bool:
        container = {'}':'{', ']':'[', ')':'('}
        stack = []
        #goes through the string 
        for i in range(len(s)):
            if s[i] in container:
                if stack and stack[-1] == container[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False


