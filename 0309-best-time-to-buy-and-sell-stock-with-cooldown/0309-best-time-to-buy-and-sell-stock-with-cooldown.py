class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def helper(i: int, sell: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, sell) in dp:
                return dp[(i, sell)]

            cooldown = helper(i + 1, sell)
            if sell:
                buy = helper(i + 1, not sell) - prices[i]
                dp[(i, sell)] =max(buy, cooldown)
            else:
                ss =helper(i + 2, not sell) + prices[i]
                dp[(i, sell)] = max(ss,cooldown)
      
            return dp[(i, sell)]

        return helper(0, True)