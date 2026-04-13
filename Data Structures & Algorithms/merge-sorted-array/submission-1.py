class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = 0
        length = n + m -1
        while r < n:
            #loop through nums1 m times 
            if nums1[length] == 0:
                nums1[length] = nums2[r]
                length -= 1
                r +=1
        nums1.sort()
            #after m is done then go through the nums2
            #replace the nums1 with nums2 when going through n times 
