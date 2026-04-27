class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(temperatures)):
            j = i + 1
            counter = 1
            while j < len(temperatures):
                if temperatures[i] >= temperatures[j]:
                    counter += 1
                    j += 1
                else:
                    stack.append(counter)
                    break
            #if there is nothing greater than then counter is zero 
            if j == len(temperatures):
                counter = 0
                stack.append(counter)
                print(counter)
            print(stack)
        return stack
