class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0        
        min_buy = prices[0]     

        for price in prices:
            # update the best profit based on current smallest price
            max_profit = max(max_profit, price - min_buy)   

            # update if smaller price is found
            min_buy = min(min_buy, price)               
        
        return max_profit
        