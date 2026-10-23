class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #equation is (target - position) / speed and which ever is smallest
        #reverse the and sort the positions to start from the target
        #if times are the same then they form the same carFleet
        #the position are different but time is greater than, they could form the same fleet 
        new = sorted(zip(position, speed))
        stack = []
        for p, s in reversed(new):
            time = (target - p) / s
            #if stack is true and time is greater than stack[-1]    
            if stack and time > stack[-1]:
                stack.append(time)

            #add the time to the stack
            elif not stack:
                stack.append(time)
            #return the len of stack
        return len(stack)
            



