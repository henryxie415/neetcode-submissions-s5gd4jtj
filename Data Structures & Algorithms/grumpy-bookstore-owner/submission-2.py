class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #First step is to calculate the number of satisfied customers
        base = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                base += customers[i]
        print(base)

        #calulate the consecutive minutes as the window setup
        extra = 0 
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        
        best = extra
        #sliding window 

        for i in range(minutes, len(grumpy)):
            if grumpy[i] == 1:
                extra += customers[i]
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]
            best = max(best, extra)
        return best + base 



        