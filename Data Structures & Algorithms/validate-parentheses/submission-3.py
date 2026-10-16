class Solution:
    def isValid(self, s: str) -> bool:
        container = {')':'(', '}':'{', ']':'['}
        result = []

        for i in range(len(s)):
            #add into the stack the first half
            if s[i] in container:
                if result and result[-1] == container[s[i]]:
                    result.pop()
                else:
                    return False
            else:
                result.append(s[i])
            
            #pop if the num is in container and is equal to s[-1]
            #return False if the number is not equal 
            #return False if not in container 
            #return True if stack is empty 
        if not result:
            return True 
        else:
            return False