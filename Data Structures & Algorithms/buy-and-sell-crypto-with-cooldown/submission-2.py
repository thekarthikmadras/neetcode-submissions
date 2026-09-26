from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize states
        buy = -prices[0]   # Bought on first day
        sell = 0           # No profit yet
        cool = 0           # Cooldown state
        
        for i in range(1, n):
            prev_buy = buy
            prev_sell = sell
            prev_cool = cool
            
            buy = max(prev_buy, prev_cool - prices[i])
            sell = prev_buy + prices[i]
            cool = max(prev_cool, prev_sell)
        
        return max(sell, cool)
