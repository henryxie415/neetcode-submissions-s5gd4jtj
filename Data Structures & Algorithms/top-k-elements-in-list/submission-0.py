class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hash map with the key being the frequency and the value being numeber
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in map.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        
        #use the k to return the entries from the sorted hash map