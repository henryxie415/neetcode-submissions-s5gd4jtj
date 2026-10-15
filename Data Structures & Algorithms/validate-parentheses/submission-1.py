class Solution:
    def isValid(self, s: str) -> bool:
        #use a dictionary 
        container = {"}":"{", ")":"(", "]":"["}
        #stack is the result 
        result = []


        for i in range(len(s)):
            if s[i] in container:
                if result and result[-1] == container[s[i]]:
                    result.pop()
                else:
                    return False 
            else:
                result.append(s[i])
        return True if not result else False


