class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        container = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while container and t > container[-1][0]:
                #if no next largest; counter is zero 
                stackT, stackI = container.pop()
                #if next down is largest; counter += 1
                #if next number is largest; terminate
                result[stackI] = i - stackI
            container.append((t, i))
        return result