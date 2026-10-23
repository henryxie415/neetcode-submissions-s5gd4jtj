class Solution:
    def isValid(self, s: str) -> bool:
        container = {']':'[', '}':'{', ')':'('}
        stack = []
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
        #stack should hold the first half of the string 
        #second half is counting backwards
        #if the object is in the container and if the stack is full and if the current object is the same as the key in the container 
        #if not in append into the stack 