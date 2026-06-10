class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        base = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                base += customers[i]
        
        extra = 0 

        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        best = extra

        for i in range(minutes, len(grumpy)):
            if grumpy[i] == 1:
                extra += customers[i]
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]
            best = max(best, extra)

        return base + best