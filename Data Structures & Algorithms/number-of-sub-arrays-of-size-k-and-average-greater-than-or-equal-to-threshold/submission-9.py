class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        currSum = sum(arr[:k])
        res = 0 

        for i in range(len(arr)):
            if (currSum / k) >= threshold:
                res += 1
                print(res)
            if i + k < len(arr):
                currSum += arr[i + k]
                currSum -= arr[i]
                print(currSum/k)
            else:
                break
        return res
            

            
            