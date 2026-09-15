class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use two pointers to go through 
        #use for loop and then an inner while loop 
        
        mp = {}
        res = 0

        for num in nums:
            if num not in mp:
                left = mp.get(num - 1, 0)
                right = mp.get(num + 1, 0)

                mp[num] = left + right + 1

                mp[num - left] = mp[num]
                mp[num + right] = mp[num]

                res = max(res, mp[num])

        return res