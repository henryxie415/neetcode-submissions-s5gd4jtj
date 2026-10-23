class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        container = []
        result = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while container and temperature > container[-1][1]:
                stackI, stackT = container.pop()
                result[stackI] = index - stackI
            container.append([index,temperature])
        return result
            #use a dictionary to calculate the days with their index

            #three scenarios 
            #none is greater
            #next one is greater
            #couple more is greater 

            