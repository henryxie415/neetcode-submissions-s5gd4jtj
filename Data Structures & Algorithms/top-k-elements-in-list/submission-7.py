class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to count the frequencies 
        counter = {}
        res = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        #use k to go through the hashmap to find the max value and delete it from the hashmap 
        while k != 0:
            largest = max(counter, key=counter.get)
            res.append(largest)
            del counter[largest]
            k -= 1
        return res
        #do this number of k times 