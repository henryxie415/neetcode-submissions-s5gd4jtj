class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #start the first pointer to the first instance of the list
        l = 0 
        r = 1
        #the second pointer goes through to see if there are any duplicates 
        while r < (len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            else:
                r += 1

        print (list(set(nums)))
        return len(list(set(nums)))

        #after reaching the end of the list pop the remaining (nums - first pointer index)\


