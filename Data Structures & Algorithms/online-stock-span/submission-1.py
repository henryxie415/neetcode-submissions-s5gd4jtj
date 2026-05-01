class StockSpanner:

    def __init__(self):
        self.algo = [] 

    def next(self, price: int) -> int:
        span = 1
        while self.algo and self.algo[-1][0] <= price:
            span += self.algo[-1][1]
            self.algo.pop()
        self.algo.append((price, span))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)