class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        result = []
        numbers.sort()


        for i in range(len(numbers) - 2):
            if numbers[i] > 0:
                break
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            l = i + 1
            r = len(numbers) - 1
            while l < r:
                total_sum = numbers[i] + numbers[l] + numbers[r]
                if total_sum > 0:
                    r -= 1
                elif total_sum < 0:
                    l += 1
                else:
                    result.append([numbers[i], numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1
        return result