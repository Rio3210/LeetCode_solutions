class StockSpanner:

    def __init__(self):
        self.lst = [(0, inf)]                  

    def next(self, price: int) -> int:          
        date = self.lst[0][0] + 1               
        while self.lst[0][1] <= price:          
            self.lst.pop(0)                  
        self.lst.insert(0, (date, price))       
        return self.lst[0][0] - self.lst[1][0]
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)