class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #equation is (target - position) / speed and which ever is smallest
        #if arrive at the same time then grouped into 1
        #if arrive at different times then count as separate
        #now we need to use the distance and go from descending order 
        #if distance is lower but time is higher than it will form a fleet
        both = [] 
        res = []
        
        for i in range(len(position)):
            both.append((position[i], speed[i]))
  
        both.sort(reverse=True)
        
        for p, s in both:
            res.append((target - p) / s)
            if len(res) >= 2 and res[-1]<=res[-2]:
                res.pop()
        return len(res)
            



