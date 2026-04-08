class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final = []
        while len(arr) > 1:
            greatest = 0
            for i in range(1,len(arr)):
                if arr[i] > greatest:
                    greatest = arr[i]
            del arr[0]
            final.append(greatest)
        final.append(-1)
        return final


            