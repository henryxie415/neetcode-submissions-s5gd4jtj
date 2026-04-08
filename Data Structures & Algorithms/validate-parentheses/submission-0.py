
class Solution:
    def isValid(self, s: str) -> bool:
        #initialize the stack 
        stack = []
        #create a hashmap for close to open brackets 
        closeToOpen = {'}':'{', ']':'[', ')':'('}
        #append the open brackets to the stack
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        #pop the bracket from the stack if the corresponding bracket shows up
        #if stack is empty then True
        #otherwise False 