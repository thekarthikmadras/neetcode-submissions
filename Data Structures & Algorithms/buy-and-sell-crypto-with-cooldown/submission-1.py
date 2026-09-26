from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize DP states
        first_buy = 0      # Max profit if we can buy (first transaction)
        first_sell = 0     # Max profit if we can sell (first transaction)
        second_buy = 0     # Max profit if we can buy (second transaction)
        
        for i in range(n - 1, -1, -1):
            # Calculate new states
            new_first_buy = max(first_sell - prices[i], first_buy)
            new_first_sell = max(second_buy + prices[i], first_sell)
            
            # Update second_buy BEFORE updating first_buy
            second_buy = first_buy
            first_buy, first_sell = new_first_buy, new_first_sell
        
        return first_buy
