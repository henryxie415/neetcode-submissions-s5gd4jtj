class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        container = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while container and temp > container[-1][1]:
                stackI, stackT = container.pop()
                result[stackI] = index - stackI
            container.append([index, temp])
        return result
                