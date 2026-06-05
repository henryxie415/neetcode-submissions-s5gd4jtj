class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        #have the window be the size of k
        #move the window throughout the whole string
        #and keep count the number of W
        #use the min function to find the lowest number of Ws
        #return that counter 
        current_whites = 0

        for i in range(k):
            if blocks[i] == "W":
                current_whites += 1

        res = current_whites

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                current_whites -= 1
            if blocks[i] == "W":
                current_whites += 1
            res = min(res, current_whites)
        return res
            
            
            
            


