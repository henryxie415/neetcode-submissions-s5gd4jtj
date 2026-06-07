class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #go through the array
        #calculate the currSum
        #have one pointer go through and add to the currSum to see if it meets the threshold
        #since currSum is going to be divided by k regardless
        #remove the first int of the window by subtracting from the currSum
        currSum = sum(arr[:k])
        print(currSum)
        res = 0

        for L in range(len(arr) - k + 1):

            if (currSum / k) >= threshold:
                res += 1
            if L < len(arr) - k:
                currSum += arr[L + k]
                currSum -= arr[L]
        return res

            
            