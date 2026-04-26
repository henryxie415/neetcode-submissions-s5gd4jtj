class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        

        for i in range(len(temperatures)):
            j = i + 1
            counter = 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                counter += 1
            if j == len(temperatures):
                counter = 0
            res.append(counter)
        return res
