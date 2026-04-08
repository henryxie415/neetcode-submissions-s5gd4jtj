class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap with the frequencies

        map = {}
 
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        #use an array to keep track of number and frequencies 
        finals = []
        for num, cnt in map.items():
            finals.append([cnt, num])
        finals.sort()

        arr = []
        while len(arr) < k:
            arr.append(finals.pop()[1])
        return arr
        

        #use k to append to the new list 



            #return the max number of frequencies