class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        #map the frequencies to a map
        for num in nums:
            map[num] = map.get(num,0) + 1
        
        #create an array of the num and count 
        arr = []
        for num, cnt in map.items():
            #contain the num and count in the array
            arr.append([cnt,num])
            #sort the array 
        arr.sort()
        #while k is less than 0 use a min heap to pop off 
        arr2 = []
        while len(arr2) < k:
            arr2.append(arr.pop()[1])
        return arr2
        #place the popped off values in an empty array and return that 

